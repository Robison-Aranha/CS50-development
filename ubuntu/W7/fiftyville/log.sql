-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT name FROM people WHERE phone_number IN ("(130) 555-0289", "(499) 555-9472", "(367) 555-5533", "(499) 555-9472", "(286) 555-6063", "(770) 555-1861", "(031) 555-6622", "(826) 555-1652", "(338) 555-6650")
IN

SELECT transcript FROM interviews WHERE day = 28 AND month = 7; 

SELECT id FROM flights WHERE origin_airport_id IN (SELECT origin_airport_id FROM airports WHERE city = "Fiftyville");

SELECT destination_airport_id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND day = 29 AND month = 7;

SELECT hour, minute FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND day = 29 AND month = 7 ORDER BY hour, minute;

SELECT city FROM airports WHERE id IN (6, 11, 4, 1, 9);

SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND day = 29 AND month = 7 AND hour = 8 AND minute = 20);

SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND destination_airport_id IN (SELECT id FROM airports WHERE city = "London") AND day = 29 AND month = 7 AND hour = 8 AND minute = 20));

SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28 AND month = 7;

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE duration <= 60 AND day = 28 AND month = 7);

SELECT license_plate FROM courthouse_security_logs WHERE day = 28 AND month = 7 AND activity = "exit" hour = 10 AND minute = 25;

SELECT name FROM people WHERE license_plate IN ("322W7JE", "0NTHK55", "1106N58");
INTERSECT
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND day = 29 AND month = 7 AND hour = 8 AND minute = 20));

SELECT name FROM people WHERE phone_number IN ("(996) 555-8899", "(892) 555-8872", "(375) 555-8161", "(717) 555-1342", "(676) 555-6554", "(725) 555-3243", "(910) 555-3251", "(066) 555-9701", "(704) 555-2131");

SELECT account_number FROM atm_transactions WHERE atm_location = "Fifer Street" AND day = 28 AND month = 7;

SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE atm_location = "Fifer Street" AND day = 28 AND month = 7 AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND day = 29 AND month = 7 AND hour = 8 AND minute = 20));

SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Ernest") AND day = 28 AND month = 7 AND duration < 60);