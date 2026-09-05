# Day 01 — Python, Git & Linux Basics

- **Persian Date:** 31 Mordad 1405
- **Gregorian Date:** August 22, 2026

---

## Topics

- **Persian:** مفاهیم اولیه متغیرها و تابع `input()` در پایتون، اصول کار با کنترل نسخه Git و GitHub، و دستورات کاربردی ترمینال لینوکس.
- **English:** Basic Python variables and `input()` function, fundamental Git & GitHub version control concepts, and essential Linux terminal commands.

---

## Python

- **1. Variable**
  - **Persian:** ظرفی در حافظه که داده‌ها و مقادیر را در خودش نگه‌داری می‌کند.
  - **English:** A variable is a container in memory that stores data or values.

- **2. input()**
  - **Persian:** تابعی که ورودی یا متن را از کاربر دریافت می‌کند.
  - **English:** This function gets an input or text from the user.

- **3. What is the data type of input() output?**
  - **Persian:** خروجی آن همیشه یک رشته متنی (String) است.
  - **English:** Its output is always a string text (String).

- **4. How do we convert a String to an Integer?**
  - **Persian:** از تابع `int()` استفاده می‌کنیم؛ مانند `int(input())`.
  - **English:** We use the `int()` function, like `int(input())`.

- **5. What is the difference between = and ==?**
  - **Persian:** علامت `=` برای مقداردهی (قرار دادن مقدار در متغیر) است، اما `==` برای مقایسه دو مقدار استفاده می‌شود.
  - **English:** The `=` operator is used for assignment, while `==` is used to compare two values.

- **6. What Error did you see today and why did it happen?**
  - **Persian:** خطای `TypeError` رخ داد، چون سعی کردم ورودی `input()` را بدون تبدیل به عدد، مستقیم با یک عدد جمع کنم.
  - **English:** A `TypeError` occurred because I tried to add the `input()` string directly to a number without converting it first.

---

## Git & GitHub

- **1. What is Git?**
  - **Persian:** گیت ابزاری برای کنترل نسخه است که تغییرات فایل‌ها و کدها را در طول زمان ثبت می‌کند.
  - **English:** Git is a version control tool that tracks changes in your files and code over time.

- **2. What is GitHub?**
  - **Persian:** گیت‌هاب یک وب‌سایت برای ذخیره و مدیریت پروژه‌های گیت آنلاین است.
  - **English:** GitHub is a website to host and manage Git projects online.

- **3. What is a Repository?**
  - **Persian:** ریپازیتوری (پوشه پروژه) جایی است که تمام فایل‌ها و تاریخچه تغییرات برنامه در آن ذخیره می‌شود.
  - **English:** A repository is the main project folder where all files and version history are stored.

- **4. What is the difference between Working Directory and Staging Area?**
  - **Persian:** در Working Directory روی فایل‌ها کار می‌کنید، اما Staging Area محیطی است که فایل‌ها را برای ثبت نهایی انتخاب و آماده می‌کنید.
  - **English:** Working Directory is where you edit files, while Staging Area is where you prepare chosen files before saving them.

- **5. What does git add do?**
  - **Persian:** فایل‌های تغییریافته را از Working Directory به Staging Area منتقل می‌کند.
  - **English:** It moves changed files from the Working Directory to the Staging Area.

- **6. What does git commit do?**
  - **Persian:** تغییرات آماده‌شده در Staging Area را همراه با یک پیام به‌طور دائمی ثبت می‌کند.
  - **English:** It permanently saves the staged changes with a descriptive message.

- **7. What does git push do?**
  - **Persian:** کدهای ثبت‌شده روی سیستم را به سرور آنلاین مثل گیت‌هاب می‌فرستد.
  - **English:** It sends saved commits from your computer to an online server like GitHub.

- **8. What information does git status give you?**
  - **Persian:** وضعیت فایل‌ها را نشان می‌دهد؛ مانند اینکه کدام فایل تغییر کرده، اضافه شده یا آماده ثبت است.
  - **English:** It shows file statuses, such as which files are changed, added, or ready to commit.

- **9. Why should we check git diff before commit?**
  - **Persian:** تا تغییرات دقیق خط‌به‌خط را مرور کنیم و از درست بودن کدها قبل از ثبت مطمئن شویم.
  - **English:** To review exact line-by-line changes and make sure the code is correct before saving.

---

## Linux

- **1. What is Linux?**
  - **Persian:** لینوکس یک سیستم‌عامل قدرتمند و متن‌باز (Open-Source) است.
  - **English:** Linux is a powerful and open-source operating system.

- **2. What is Terminal?**
  - **Persian:** ترمینال یک محیط متنی است که از طریق آن با نوشتن دستورات به سیستم‌عامل فرمان می‌دهیم.
  - **English:** Terminal is a text interface where we give commands to the operating system.

- **3. What does pwd do?**
  - **Persian:** مسیر کامل پوشه‌ای که الان در آن هستید را نشان می‌دهد.
  - **English:** It shows the current folder path where you are.

- **4. What does ls do?**
  - **Persian:** لیست فایل‌ها و پوشه‌های داخل مسیر فعلی را نشان می‌دهد.
  - **English:** It lists all files and folders in the current directory.

- **5. What does cd do?**
  - **Persian:** برای جابه‌جایی و تغییر پوشه‌ها استفاده می‌شود.
  - **English:** It is used to change or move between folders.

- **6. What does mkdir do?**
  - **Persian:** یک پوشه (Directory) جدید می‌سازد.
  - **English:** It creates a new folder (directory).

- **7. What does touch do?**
  - **Persian:** یک فایل جدید و خالی می‌سازد.
  - **English:** It creates a new empty file.

---

## New Vocabulary

| English | Persian |
|---|---|
| variable | متغیر |
| repository | مخزن / پوشه پروژه |
| commit | ثبت تغییرات |
| directory | پوشه |
| command | دستور |
| terminal | ترمینال |
| file | فایل |
| error | خطا |

---

## Reflection

1. **What was the hardest part today?**
- **Persian:** سخت‌ترین قسمت لینوکس بود و سخت‌ترین کار این بود که امروز کل روزم را به برنامه‌نویسی اختصاص دادم و کارهای دیگرم را نتوانستم انجام دهم.
- **English:** The hardest part was Linux, and the most difficult thing was that I spent my whole day programming and couldn't do my other tasks.

2. **Which concept is still confusing to me?**
- **Persian:** مباحث مربوط به لینوکس و گیت.
- **English:** Concepts related to Linux and Git.

3. **What did I do without AI today?**
- **Persian:** نوشتن کدهای تمرینی که ۸ تا تمرین بود، همه را بدون AI انجام دادم.
- **English:** Writing the practice code—there were 8 exercises, and I did all of them without AI.

4. **What should I improve tomorrow?**
- **Persian:** باید بتوانم زمانم را مدیریت کنم که همه کارهایم را بتوانم انجام دهم.
- **English:** I need to manage my time better so I can complete all my tasks.