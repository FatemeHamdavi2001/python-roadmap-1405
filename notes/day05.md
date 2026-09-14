فایل کامل و یکپارچه **Day 05** با فرمت استاندارد قبلی، شامل تمام نکات، کدها، اصلاحات مفهومی (مثل تفاوت `for` و `range`) و بخش Reflection آماده کپی در `notes/day05.md`:

```markdown
# Day 05 — Advanced Control Flow (For, Range, Match) & Algorithm Design

- **Persian Date:** 23 Shahrivar 1405
- **Gregorian Date:** September 14, 2026

---

## Topics

- **Python:** حلقه‌های `for`، درک عمیق تابع `range()`، کنترل جریان حلقه با `break` و `continue`، ساختار `for...else`، کلمه کلیدی `pass` و ساختار `match/case`.
- **Algorithm Design:** مدیریت وضعیت (State Management) در طول اجرای حلقه، ردیابی کد (Code Tracing).
- **Git & Linux:** ناوبری در لینوکس (Exploring the System)، تاریخچه Commitها و لغو تغییرات (Undoing Changes).

---

## What I Learned

- **1. `for` vs `range()`**
  - **Persian:** فهمیدم که `for` و `range` دو مفهوم کاملاً مجزا هستند. `for` برای پیمایش (Iteration) روی هر نوع Iterable (مثل رشته‌ها) استفاده می‌شود، در حالی که `range()` صرفاً یک دنباله عددی تولید می‌کند که یکی از گزینه‌های مناسب برای پیمایش با `for` است.
  - **English:** Realized that `for` and `range` are distinct concepts. `for` is an iteration mechanism for ANY iterable, while `range()` simply generates a sequence of numbers which is just one of many possible iterables.

- **2. Loop Control (`break` & `continue`)**
  - **Persian:** دستور `continue` تکرار فعلی را رها کرده و به دور بعدی حلقه می‌رود، اما `break` کل حلقه را به طور کامل متوقف می‌کند.
  - **English:** `continue` skips the rest of the current iteration and moves to the next, whereas `break` entirely terminates the loop.

- **3. The `for...else` Construct**
  - **Persian:** بلوک `else` در حلقه `for` تنها زمانی اجرا می‌شود که حلقه به صورت طبیعی (بدون برخورد با `break`) تمام شود. اگر `break` اجرا شود، `else` نادیده گرفته می‌شود.
  - **English:** The `else` block in a `for` loop executes ONLY if the loop finishes normally. If the loop is terminated by a `break`, the `else` block is skipped.

- **4. Structural Pattern Matching (`match`) & `pass`**
  - **Persian:** `match` برای بررسی الگوهای ورودی (مثل منوها) بسیار خواناتر از `if/elif` است. همچنین `pass` یک عملیات خنثی (Null operation) است که فقط برای جلوگیری از خطای سینتکس در بلوک‌های خالی استفاده می‌شود (مثلاً `if condition: pass`).
  - **English:** `match` is cleaner than `if/elif` for matching input patterns (like menus). `pass` is a null operation used as a placeholder to avoid syntax errors in empty blocks.

---

## Exercises

- **Exercise 01 (Loop with Step & Conditions):**
  - **Persian:** پیمایش معکوس با `range(n, 0, -1)`، پرش از اعداد زوج با `continue` و توقف در عدد ۳ با `break`.
  - **English:** Backward iteration using `range(n, 0, -1)`, skipping even numbers using `continue`, and stopping at 3 using `break`.
```python
for i in range(n, 0, -1):
    if i % 2 == 0:
        continue
    if i == 3:
        break
    print(i)

```

* **Exercise 02 (Transfer Problem):**
* **Persian:** پیدا کردن اعدادی که همزمان مضرب ۲ و ۳ هستند و توقف کامل حلقه روی عدد ۷۲.
* **English:** Finding numbers divisible by both 2 and 3, and terminating the loop at 72.



```python
for i in range(1, 100): # Note: Stops at 99
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    if i == 72:
        break

```

---

## Mini Project

* **Account Login Simulator**
* **Persian:** شبیه‌ساز فرم ورود با حداکثر ۵ بار تلاش. استفاده از `for...else` برای قفل کردن حساب در صورت وارد نکردن رمز صحیح پس از اتمام تلاش‌ها. تشخیص دقیق خطای نام کاربری یا رمز عبور.
* **English:** Login simulator with a maximum of 5 attempts. Utilized `for...else` to lock the account if all attempts fail. Handled specific error messages for wrong username vs wrong password.



```python
username = "admin"
password = "1234"

for i in range(5):
    inputuser = input("Enter username:")
    inputpass = input("Enter password:")

    if inputuser == username and inputpass == password:
        print("Login successful")
        break
    elif inputuser != username:
        print("Unknown user")
    elif inputpass != password:
        print("Wrong password")
else:
    print("Account locked")

```

---

## Errors & Debugging

* **Logical Error in First Odd Number Finder:**
* **Persian:** در تمرین پیدا کردن اولین عدد فرد، حلقه روی اولین عدد (۱) متوقف می‌شد اما خروجی اشتباه بود. با Code Tracing فهمیدم شرط منطقی برعکس نوشته شده و جای `break` و `continue` اشتباه است.
* **English:** In the "find first odd number" script, the loop stopped at 1 but the logic was flawed. Code Tracing revealed that the logic was inverted; I used `continue` where a `break` was needed.


* **State Management Issue (Algorithm Problem 2):**
* **Persian:** در نوشتن الگوریتم، برای مدیریت وضعیتی مثل «پیدا شد/پیدا نشد» دچار مشکل شدم. متوجه شدم استفاده از `for...else` کافی نیست و گاهی باید وضعیت را در یک متغیر جداگانه (State Variable) ذخیره کنم تا خارج از حلقه از آن استفاده کنم.
* **English:** Struggled with managing state (e.g., "Found" vs "Not Found"). Realized that relying solely on `for...else` isn't always enough, and explicit state variables are often required to track data outside the loop.



---

## Documentation I Read & Concepts Explored

* `range(start, stop, step)`: Noticed that the `stop` parameter is exclusive. `range(1, 100)` ends at 99.
* `match / case`: Explored structural pattern matching as an alternative to long `if/elif` chains.

---

## New Vocabulary

| English | Persian |
| --- | --- |
| Iterable | تکرارپذیر / قابل پیمایش |
| Null Operation | عملیات خنثی / بی‌اثر (`pass`) |
| State Management | مدیریت وضعیت |
| Pattern Matching | تطبیق الگو |
| Cognitive Load | بار شناختی / خستگی ذهنی |

---

## Problems I Faced

* **Persian:** فاصله بین درک سینتکس (Syntax) و توانایی طراحی الگوریتم (Algorithm Design). وقتی صورت مسئله از کدنویسی ساده فاصله گرفت (مسئله D)، مغزم به شدت خسته شد و نتوانستم مراحل منطقی را به درستی بچینم.
* **English:** The gap between understanding Syntax and actual Algorithm Design. When the problem required stepping away from simple code to design logical steps (Problem D), I experienced high cognitive load and struggled to structure the solution.

---

## What I Solved Without AI

* **Persian:** ردیابی خط‌به‌خط کد (Code Tracing) در آزمون و پیدا کردن خطاهای منطقی مربوط به `continue` و توقف حلقه‌ها. پیاده‌سازی کامل ساختار `for...else` در مینی‌پروژه.
* **English:** Successfully performed manual Code Tracing in the quiz to find logical bugs related to `continue` and loop termination. Fully implemented the `for...else` construct independently in the mini-project.

---

## Review & Weak Areas

* **1. Algorithm Design (3/5):**
* **Persian:** تبدیل منطق انسانی به مراحل کدی هنوز انرژی ذهنی زیادی از من می‌گیرد. باید قبل از کد زدن، بیشتر روی کاغذ الگوریتم بنویسم.


* **2. State Management (3/5):**
* **Persian:** نیاز به تمرین بیشتر در استفاده از متغیرها برای نگهداری وضعیت (مثل شمارش تعداد تلاش‌ها `attempt count` یا وضعیت فعلی `current best`).



---

## Reflection

1. **What was the biggest realization today?**

* **Persian:** اینکه خستگی ذهنی در حل مسئله الگوریتمی یک شکست نیست، بلکه نشان‌دهنده این است که دانش Syntax من از مهارت تفکر الگوریتمی‌ام جلوتر است و باید روی پر کردن این فاصله کار کنم.
* **English:** Realizing that cognitive fatigue during algorithm design is not a failure, but a sign that my syntax knowledge has outpaced my algorithmic thinking, highlighting exactly what I need to practice next.

2. **How did you fix the bug in the debugging test?**

* **Persian:** با بررسی اینکه متغیرها در هر دور از حلقه چه مقداری می‌گیرند. فهمیدم برنامه به جای رد شدن از اعداد زوج، روی آن‌ها متوقف می‌شود؛ پس `continue` و `break` را جابه‌جا کردم.
* **English:** By tracking variable values iteration by iteration. I noticed the program was doing the exact opposite of skipping evens, so I swapped the logic of `continue` and `break`.

3. **What is the difference between `for` and `range`?**

* **Persian:** `for` مکانیزم حرکت روی داده‌هاست، در حالی که `range` فقط یک ابزار برای تولید اعداد است. `for` می‌تواند بدون `range` روی رشته‌ها یا لیست‌ها حرکت کند.
* **English:** `for` is the mechanism that iterates over data, while `range` is just a tool that generates numbers. `for` can iterate over strings or lists completely independently of `range`.

4. **What is your main focus for tomorrow?**

* **Persian:** تمرین بیشتر روی طراحی الگوریتم، نوشتن منطق برنامه‌ها روی کاغذ پیش از کدنویسی و یادگیری روش‌های بهتر برای مدیریت State در حلقه‌ها.
* **English:** Focusing heavily on algorithm design, writing out logic on paper before coding, and practicing how to manage states (variables) effectively inside loops.

```

```