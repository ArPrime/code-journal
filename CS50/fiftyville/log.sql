-- Keep a log of any SQL queries you execute as you solve the mystery.

-- 'the theft took place on July 28, 2024 and that it took place on Humphrey Street', go for the rime_scene_reports
SELECT description
FROM crime_scene_reports
WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- | Littering took place at 16:36. No known witnesses.

-- Ask witnesses
SELECT name, transcript
FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28
AND transcript LIKE '%bakery%';
-- | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- Find cars that left bakery between 10:15 and 10:25
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2024 AND month = 7 AND day = 28
AND activity = 'exit'
AND hour = 10 AND minute >= 15 AND minute <= 25;


-- Find people who withdrew from Leggett Street ATM on July 28
SELECT DISTINCT people.id, people.name, people.phone_number, people.passport_number, people.license_plate
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2024 AND atm_transactions.month = 7 AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.transaction_type = 'withdraw';

-- Using IN with Subquery
SELECT DISTINCT people.id, people.name, people.phone_number, people.passport_number, people.license_plate
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE people.license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2024 AND month = 7 AND day = 28
    AND activity = 'exit'
    AND hour = 10 AND minute >= 15 AND minute <= 25
)
AND atm_transactions.year = 2024 AND atm_transactions.month = 7 AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.transaction_type = 'withdraw';

-- Find calls made on July 28 with duration < 60 seconds
SELECT caller, receiver, duration
FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60;
-- Bruce or Diana


-- Find earliest flight from Fiftyville on July 29
SELECT flights.id, flights.hour, flights.minute, airports.city
FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE flights.year = 2024 AND flights.month = 7 AND flights.day = 29
AND flights.origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
ORDER BY flights.hour, flights.minute
LIMIT 1;
-- | 36 | 8    | 20     | New York City |

-- Check passengers on the earliest flight
SELECT people.name, passengers.seat, passengers.passport_number
FROM passengers
JOIN people ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36
AND people.passport_number IN (3592750733, 3391710505);
-- | Bruce


-- the thief is Bruce
SELECT name, passport_number
FROM people
WHERE phone_number = '(375) 555-8161';
-- | Robin |
