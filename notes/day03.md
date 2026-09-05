# Day 03 — Python Foundations

- **Persian Date:** 5 Shahrivar 1405
- **Gregorian Date:** August 27, 2026

---

## Topics

- **Persian:** ایندکس‌گذاری مثبت و منفی رشته‌ها، اسلایسینگ (Slicing)، مفهوم تغییرناپذیری (Immutability)، فرمت‌دهی رشته‌ها با `f-string`، بررسی مستندات پایتون (`len()` و `str.replace()`) و تفاوت تابع (Function) با متد (Method).
- **English:** String indexing (positive & negative), string slicing, string immutability concept, string formatting using `f-strings`, documentation practice (`len()` & `str.replace()`), and understanding the difference between functions and methods.

---

## What I Learned

- **1. String Indexing (Positive & Negative)**
  - **Persian:** هر کاراکتر در رشته یک موقعیتعددی (Index) دارد که از ۰ شروع می‌شود. همچنین با ایندکس منفی می‌توان از انتهای رشته به کاراکترها دسترسی داشت (`1-` یعنی آخرین کاراکتر).
  - **English:** Every character in a string has a numerical position (Index) starting from 0. Negative indexing allows accessing characters from the end (`-1` is the last character).

- **2. String Slicing (`string[start:end]`)**
  - **Persian:** جداسازی بخشی از رشته با مشخص کردن شروع و پایان. نکته مهم این است که مقدار `end` در خروجی شامل نمی‌شود.
  - **English:** Extracting a part of a string by specifying start and end index. Note that the `end` index is excluded.

- **3. String Immutability**
  - **Persian:** رشته‌ها در پایتون غیرقابل تغییر مستقیم هستند و نمی‌توان یک کاراکتر را مستقیماً جایگزین کرد.
  - **English:** Strings in Python are immutable; individual characters cannot be changed directly.

- **4. Function vs. Method (`len()` vs. `str.replace()`)**
  - **Persian:** تابع یک ورودی می‌گیرد و خروجی می‌دهد (مثل `len(text)`)، اما متد روی یک شیء خاص اجرا می‌شود و تغییراتی روی آن اعمال می‌کند (مثل `text.replace()`).
  - **English:** A function takes an argument and returns a value (e.g., `len(text)`), while a method is called on a specific object to perform actions (e.g., `text.replace()`).

- **5. String Formatting with f-strings**
  - **Persian:** استفاده از فرمت `f"{variable}"` برای جای‌گذاری راحت‌تر متغیرها داخل رشته‌ها.
  - **English:** Using `f"{variable}"` syntax to easily insert variables inside strings.

---

## Exercises

- **Persian:**
  - **Exercise 1 (Character Inspector):** گرفتن کلمه و نمایش اولین کاراکتر، آخرین کاراکتر و طول رشته بدون AI.
  - **Exercise 2 (Username Cleaner):** حذف فواصل اضافی با `strip()` و کوچک‌کردن حروف با `lower()`.
  - **Exercise 3 (Email Inspector):** پیدا کردن موقعیت `@` با متد `find()` و جدا کردن یوزرنیم و دامنه با Slicing.
  - **Exercise 4 (Password Masker):** دریافت پسورد، نمایش طول، اولین و آخرین کاراکتر بدون چاپ خود پسورد.
  - **Exercise 5 (Text Analyzer):** تحلیل کامل متن (حذف فاصله، lowercase، طول، اولین و آخرین کاراکتر).
  - **Mental Challenge:** حدس خروجی‌های Slicing و Indexing روی کاغذ قبل از اجرای کد.
- **English:**
  - **Exercise 1 (Character Inspector):** Taking a word and printing first/last characters and total length without AI.
  - **Exercise 2 (Username Cleaner):** Removing whitespaces with `strip()` and converting to lowercase with `lower()`.
  - **Exercise 3 (Email Inspector):** Finding `@` position using `find()` and splitting username/domain with slicing.
  - **Exercise 4 (Password Masker):** Getting password, showing length, first and last character without printing the actual password.
  - **Exercise 5 (Text Analyzer):** Full text analysis (cleaning whitespace, lowercasing, length, first/last character).
  - **Mental Challenge:** Guessing indexing and slicing outputs on paper before code execution.

---

## Mini Project

- **Secure Username Analyzer**
  - **Persian:** دریافت نام، نام خانوادگی و سال تولد؛ تمیزکاری ورودی‌ها، ساخت یوزرنیم ترکیب‌شده، محاسبه طول، نمایش اولین و آخرین کاراکتر و بررسی طول یوزرنیم با شرط `if/else` (بزرگتر از ۱۵ کاراکتر: Long / در غیر این صورت: OK).
  - **English:** Takes first name, last name, and birth year; cleans inputs, creates a combined username, calculates length, displays first/last character, and checks username length with an `if/else` condition (Long if > 15 chars, otherwise OK).

---

## Errors

- **`IndexError: string index out of range` (Debugging Lab)**
  - **Persian:** این خطا زمانی رخ داد که خواستم به ایندکس ۲۰ یک رشته کوتاه (مثل `"Ali"`) دسترسی پیدا کنم، در حالی که این ایندکس در حافظه وجود ندارد.
  - **English:** This error occurred when trying to access index 20 of a short string (like `"Ali"`), which exceeds the available string indices.

---

## Documentation I Read

- **1. `len()` (Built-in Function)**
  - **Name:** `len()`
  - **Type:** Built-in Function
  - **What does it do?:** Returns the number of items/characters in an object.
  - **Example:** `len("Python")` -> `6`
  - **Return value:** `int`

- **2. `str.replace()` (String Method)**
  - **Name:** `replace()`
  - **Type:** String Method
  - **What does it do?:** Returns a copy of the string with all occurrences of substring `old` replaced by `new`.
  - **Example:** `"I like Python".replace("Python", "Security")` -> `"I like Security"`
  - **Return value:** `str` (New String)

---

## New Vocabulary

| English | Persian |
|---|---|
| indexing | ایندکس‌گذاری / دسترسی به موقعیت |
| slicing | اسلایسینگ / برش دادن رشته |
| immutability | تغییرناپذیری |
| parameter | پارامتر (ورودی تابع) |
| return value | مقدار بازگشتی |
| string method | متد رشته |
| out of range | خارج از محدوده مجاز |
| find | پیدا کردن موقعیت کاراکتر |

---

## Problems I Faced

- **Persian:** درک دقیق بازه Slicing (عدم محاسبه خود `end`) و پیدا کردن راهی برای جدا کردن ایمیل بدون استفاده از تابع `split()`.
- **English:** Understanding the exact slicing range (excluding the `end` index) and finding a way to split email parts without using the `split()` function.

---

## What I Solved Without AI

- **Persian:** تمرین‌های ۱، ۲، ۴، ۵، چالش ذهنی و پیدا کردن و برطرف‌کردن خطای `IndexError` در Debugging Lab کاملاً مستقلاً انجام شد.
- **English:** Exercises 1, 2, 4, 5, the mental challenge, and finding/fixing the `IndexError` in the Debugging Lab were completed entirely independently.

---

## Review

- **Persian:** مرور و تمرین بیشتر روی تکنیک‌های Slicing، متد `find()` و کار با `f-strings`.
- **English:** Further review and practice on slicing techniques, the `find()` method, and working with `f-strings`.

---

## Reflection

1. **Which part was harder today?**
- **Persian:** امروز یکم مینی پروژه برام سخت بود و البته استفاده از f-string، البته تقریبا یادش گرفتم.
- **English:** The mini-project was a bit hard for me today, as well as using f-strings, but I almost learned it.

2. **Which was harder for you, Indexing or Slicing?**
- **Persian:** اسلایسینگ سخت‌تر بود برام.
- **English:** Slicing was harder for me.

3. **Did you manage to solve Email Inspector without AI?**
- **Persian:** نه یک مقداری رو از AI کمک گرفتم؛ اون قسمتی که باید از تابع find استفاده می‌کردم برای `@`. فقط ازش پرسیدم از چه راهی میشه یک رشته رو از یک کاراکتر خاص جدا کرد.
- **English:** No, I got some help from AI for the part where I needed to use the `find()` function for `@`. I only asked how to separate a string by a specific character.

4. **Did you find the Index Error yourself?**
- **Persian:** آره خودم پیداش کردم و حلش کردم.
- **English:** Yes, I found it and fixed it myself.

5. **What is still the difference between Function and Method for you?**
- **Persian:** خب تابع یک ورودی می‌گیره و یک خروجی میده، اما متد یک تغییراتی رو روی اون رشته اعمال می‌کنه.
- **English:** A function takes an input and gives an output, while a method applies changes directly to that specific string/object.

6. **What improved in your problem-solving compared to Day 02?**
- **Persian:** احساس می‌کنم یک مقدار تفکر الگوریتمی رو دارم یاد می‌گیرم.
- **English:** I feel like I am starting to learn algorithmic thinking a bit more.