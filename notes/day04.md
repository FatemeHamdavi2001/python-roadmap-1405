# Day 04 — Control Flow + Git History + Linux Navigation

- **Persian Date:** 14 Shahrivar 1405
- **Gregorian Date:** September 5, 2026

---

## Topics

- **Python:** ساختارهای شرطی (`if/elif/else`)، حلقه‌های تکرار (`for`)، تابع `range()`، پیمایش رشته‌ها و بررسی متدهای `startswith()` و `endswith()`.
- **Git:** مشاهده تاریخچه Commitها با دستورات `git log` ،`git log --oneline` ،`git log --stat` و `git log -p`.
- **Linux:** ناوبری فایل‌سیستم، درک عمیق `pwd` ،`ls` ،`cd` و تفاوت Absolute Path با Relative Path (`.` ،`..` ،`~` ،`/`).
- **Integration:** اجرای برنامه‌های پایتون در ترمینال لینوکس و مدیریت نسخه با گیت.

---

## What I Learned

- **1. Control Flow (`if / elif / else`)**
  - **Persian:** نحوه ساخت منطق‌های شرطی پیچیده‌تر، ترتیب بررسی شرط‌ها و شرط‌های تو‌در‌تو.
  - **English:** Building complex conditional logic, understanding order of condition evaluation, and nested conditions.

- **2. Iteration with `for` Loop & `range()`**
  - **Persian:** پیمایش روی کاراکترهای رشته و استفاده از `range(start, stop, step)` برای تولید دنباله‌ای از اعداد (با این نکته که `stop` در بازه محاسبه نمی‌شود).
  - **English:** Iterating through string characters and using `range(start, stop, step)` to generate number sequences (noting that `stop` is excluded).

- **3. Documentation Usage**
  - **Persian:** خواندن مستندات رسمی برای `str.startswith()` ،`str.endswith()` و `range()` و نحوه اعمال آن‌ها در کدهای عملی.
  - **English:** Reading official documentation for `str.startswith()`, `str.endswith()`, and `range()`, and applying them practically.

- **4. Git Commit History**
  - **Persian:** استفاده از `git log --oneline` برای دیدن خلاصه سابقه و `git log -p` برای بررسی تغییرات دقیق فایل‌ها (Diff).
  - **English:** Using `git log --oneline` for concise commit history and `git log -p` to inspect detailed file changes (diffs).

- **5. Linux File System Paths**
  - **Persian:** تفاوت مسیر مطلق (از ریشه `/`) و مسیر نسبی (از دایرکتوری فعلی `.`).
  - **English:** Difference between absolute paths (starting from root `/`) and relative paths (starting from current directory `.`).

---

## Exercises

- **Exercise 01 (Access Level Checker):**
  - **Persian:** بررسی سن و تشخیص حساب کاربری Admin با استفاده از متد `startswith("admin")`.
  - **English:** Age categorization and checking for Admin accounts using `startswith("admin")`.

- **Exercise 02 (Number Pattern Analyzer):**
  - **Persian:** پیمایش اعداد از ۱ تا n و مشخص کردن زوج/فرد بودن و مضرب ۳ بودن بدون استفاده از List یا Function.
  - **English:** Iterating from 1 to n to check for even/odd and multiples of 3 without lists or functions.

- **Exercise 03 (Character Position Scanner):**
  - **Persian:** پیمایش رشته با حلقه `for` و تشخیص نوع کاراکتر (حرف، عدد، فاصله یا سایر) همراه با موقعیت ایندکس آن.
  - **English:** Traversing a string using `for` loop to inspect character types (letter, number, space, other) along with index positions.

- **Mental Challenge:**
  - **Persian:** تحلیل و حدس دقیق خروجی حلقه‌های `range()` روی کاغذ قبل از اجرا.
  - **English:** Analyzing and predicting `range()` loop outputs on paper prior to execution.

---

## Mini Project

- **Account Risk Analyzer**
  - **Persian:** برنامه جامع تحلیل ریسک حساب کاربری. ورودی‌ها (نام، سن و پسورد) را دریافت کرده، با حلقه `for` ویژگی‌های پسورد را آنالیز می‌کند و سطح ریسک را بر اساس شرایط مشخص می‌سازد.
  - **English:** A comprehensive user risk analysis script that accepts credentials, analyzes password properties via a `for` loop, and outputs a calculated risk rating.

```python
# Password logic used for risk assessment:
if len(password) >= 8 and digit >= 1 and alpha >= 1:
    pwd_strength = "High"
    risk_level = "Safe"
elif len(password) >= 8 and (digit >= 1 or alpha >= 1):
    pwd_strength = "Medium"
    risk_level = "Review Required"
else:
    pwd_strength = "Low"
    risk_level = "Action Required"

```

---

## Errors & Debugging

* **Logical Errors in Exercises 2 & 3:**
* **Persian:** برنامه بدون خطا اجرا می‌شد اما خروجی آن با منطق مورد انتظار مطابقت نداشت (خطای منطقی). با بررسی خط‌به‌خط کد، الگوریتم اصلاح شد.
* **English:** The program executed without raising runtime exceptions, but yielded incorrect logical outputs (Logical Error). Fixed by step-by-step trace and algorithm review.



---

## Documentation I Read

* **1. `range()**`
* **Syntax:** `range(stop)` or `range(start, stop[, step])`
* **Type:** Built-in Type
* **What does it do?:** Generates an immutable sequence of numbers from `start` up to (but not including) `stop`.
* **Return value:** `range` object


* **2. `str.startswith()**`
* **Syntax:** `str.startswith(prefix[, start[, end]])`
* **Type:** String Method
* **What does it do?:** Checks if a string starts with the specified prefix.
* **Return value:** `bool` (`True` / `False`)


* **3. `str.endswith()**`
* **Syntax:** `str.endswith(suffix[, start[, end]])`
* **Type:** String Method
* **What does it do?:** Checks if a string ends with the specified suffix.
* **Return value:** `bool` (`True` / `False`)



---

## Git & Linux Practices

* **Git Log Commands:**
* `git log --oneline`: نمایش هر commit در یک خط کوتاه.
* `git log -p`: نمایش تمام تغییرات داخل کد (Diffs) برای هر commit.


* **Linux Navigation Challenge (`python.txt` in `/home/nazanin/day04`):**
* **Absolute Path:** `cat /home/nazanin/day04/python.txt`
* **Relative Path:** `cat ./python.txt`



---

## New Vocabulary

| English | Persian |
| --- | --- |
| Iteration | تکرار / پیمایش |
| Loop Variable | متغیر حلقه |
| Absolute Path | مسیر مطلق |
| Relative Path | مسیر نسبی |
| Logical Error | خطای منطقی |
| Sequence | دنباله |

---

## Problems I Faced

* **Persian:** درک الگوریتم و پیاده‌سازی منطق بدون استفاده از توابع آماده پایتون در تمرین‌های ۲ و ۳.
* **English:** Understanding the algorithm and implementing loop logic without using high-level built-in functions in Exercises 2 and 3.

---

## What I Solved Without AI

* **Persian:** کدنویسی کامل تمرین‌ها و مینی‌پروژه، اجرای دستورات لینوکس، بررسی Git Log و برطرف کردن خطاهای منطقی برنامه‌ها.
* **English:** Writing code for exercises and the mini-project, Linux CLI execution, Git Log inspection, and fixing logical code bugs.

---

## Review

* **Persian:** مرور و تمرین بیشتر روی تفکر الگوریتمی و نحوه طراحی مراحل منطقی حل مسئله قبل از کدنویسی.
* **English:** Further review and practice on algorithmic thinking and step-by-step problem-solving prior to coding.

---

## Reflection

1. **Which part was harder today?**

* **Persian:** تمرین دوم و سوم سخت‌تر بودند و مجبور شدم برای درک منطق برنامه و الگوریتم پیاده‌سازی از AI کمک بگیرم.
* **English:** Exercises 2 and 3 were harder, and I had to get assistance from AI to understand the program logic and algorithm implementation.

2. **How did you design the Risk Level logic in the Mini Project?**

* **Persian:** با بررسی طول پسورد و وجود حداقل یک حرف و یک عدد، سطح قدرت پسورد و سطح ریسک را مشخص کردم (کد آن را خودم نوشتم اما درک منطق اولیه با راهنمایی بود).
* **English:** By checking password length and presence of characters/digits, I defined strength and risk levels (wrote code independently after understanding the core logic).

3. **What were your Linux Absolute and Relative paths?**

* **Persian:** مسیر مطلق: `cat /home/nazanin/day04/python.txt` / مسیر نسبی: `cat ./python.txt`
* **English:** Absolute path: `cat /home/nazanin/day04/python.txt` / Relative path: `cat ./python.txt`

4. **What stood out to you in Git Log?**

* **Persian:** دستورات `--oneline` برای فشرده دیدن تاریخچه و `-p` برای دیدن تغییرات دقیق کد برام خیلی جالب بودند.
* **English:** The `--oneline` command for compact history and `-p` for inspecting detailed code diffs were particularly interesting.

5. **Did you encounter any specific errors?**

* **Persian:** بله، در تمرین دوم و سوم کدم اجرا می‌شد اما خطای منطقی داشت و خروجی درست نمی‌داد که خودم برطرفشان کردم.
* **English:** Yes, Exercises 2 and 3 executed without crashes but had logical bugs and incorrect outputs, which I debugged and resolved myself.

6. **How was your overall experience integrating Python, Linux, and Git?**

* **Persian:** تجربه خیلی خوبی بود، فقط باید تفکر الگوریتمی و منطقیم رو بهتر کنم تا بتونم راحت‌تر تصمیم بگیرم و کدهای پیچیده‌تر رو پیاده‌سازی کنم.
* **English:** It was a great experience; I just need to strengthen my algorithmic and logical thinking to make decisions easier and implement complex logic.

```

```