// 新增知识：JavaScript 代码可以放在单独的 .js 文件中
// 这样可以让代码更整洁，也可以在多个页面中重复使用

// 新增知识：DOMContentLoaded 事件
// 什么是 DOM？Document Object Model（文档对象模型）= 整个网页
// DOMContentLoaded 的意思是："当整个网页加载完成后，再执行代码"
// 这样可以确保所有的 HTML 元素都已经存在了

document.addEventListener('DOMContentLoaded', function() {
    // 这里面的代码会在网页加载完成后才执行
    console.log("网页加载完成！");
    // console.log() 会在浏览器的控制台输出信息，用来调试代码
});

// 定义一个函数（function）
// 函数是一段可以重复使用的代码
function sayHello() {
    // alert() 会弹出一个提示框
    alert("你好！欢迎来到我的网站！👋");
}
