import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get user's stocks
    stocks = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    # Get user's cash
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = rows[0]["cash"]

    # Initialize grand total
    grand_total = cash

    # Get current price for each stock
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = usd(quote["price"])
        stock["total"] = usd(quote["price"] * stock["total_shares"])
        stock["shares"] = stock["total_shares"]
        grand_total += quote["price"] * stock["total_shares"]

    return render_template("index.html",
                         stocks=stocks,
                         cash=usd(cash),
                         grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Ensure shares was submitted
        if not shares:
            return apology("must provide shares", 400)

        # Ensure shares is a positive integer
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("shares must be positive", 400)
        except ValueError:
            return apology("shares must be an integer", 400)

        # Look up the stock quote
        stock = lookup(symbol)

        # Ensure symbol is valid
        if stock is None:
            return apology("invalid symbol", 400)

        # Calculate total cost
        total_cost = stock["price"] * shares

        # Get user's cash balance
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]

        # Ensure user can afford the purchase
        if cash < total_cost:
            return apology("can't afford", 400)

        # Update user's cash
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?",
                  total_cost, session["user_id"])

        # Record the transaction
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                  session["user_id"], stock["symbol"], shares, stock["price"])

        # Redirect to home page
        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # 获取所有交易记录
    transactions = db.execute(
        "SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC",
        session["user_id"]
    )

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Ensure symbol was submitted
        if not symbol:
            return apology("must provide symbol", 400)

        # Look up the stock quote
        stock = lookup(symbol)

        # Ensure symbol is valid
        if stock is None:
            return apology("invalid symbol", 400)

        # Display the quote
        return render_template("quoted.html",
                             name=stock["name"],
                             symbol=stock["symbol"],
                             price=usd(stock["price"]))

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        if not password:
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        if not confirmation:
            return apology("must confirm password", 400)

        # Ensure passwords match
        if password != confirmation:
            return apology("passwords do not match", 400)

        # Hash the password
        hash_password = generate_password_hash(password)

        # Try to insert new user into database
        try:
            result = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                              username, hash_password)
        except ValueError:
            # Username already exists
            return apology("username already exists", 400)

        # Log the user in automatically after registration
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # 验证输入
        if not symbol:
            return apology("must provide symbol", 400)

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("must provide positive number of shares", 400)

        shares = int(shares)

        # 查询用户拥有的股票数量
        rows = db.execute(
            "SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
            session["user_id"], symbol.upper()
        )

        if not rows or rows[0]["total_shares"] < shares:
            return apology("you don't own enough shares", 400)

        # 获取当前股价
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 400)

        # 计算收益
        sale_value = shares * stock["price"]

        # 更新数据库
        # 1. 记录交易（负数表示卖出）
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
            session["user_id"], stock["symbol"], -shares, stock["price"]
        )

        # 2. 更新用户现金
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            sale_value, session["user_id"]
        )

        flash(f"Sold {shares} shares of {stock['symbol']} for {usd(sale_value)}!")
        return redirect("/")

    else:
        # GET 请求：显示卖出表单
        # 获取用户拥有的股票
        stocks = db.execute(
            "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0",
            session["user_id"]
        )

        return render_template("sell.html", stocks=stocks)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to account"""

    if request.method == "POST":
        amount = request.form.get("amount")

        # Ensure amount was submitted
        if not amount:
            return apology("must provide amount", 400)

        # Ensure amount is a positive number
        try:
            amount = float(amount)
            if amount <= 0:
                return apology("amount must be positive", 400)
        except ValueError:
            return apology("invalid amount", 400)

        # Update user's cash
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",
                  amount, session["user_id"])

        # Redirect to home page
        flash(f"Successfully added {usd(amount)}!")
        return redirect("/")

    else:
        return render_template("add_cash.html")
