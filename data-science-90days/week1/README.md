
# Week 1: Python & Environment Setup

## 🧭 Goal:
- Understand what Data Science is
- Learn why Python is important
- Set up your tools: Python, JupyterLab, VS Code
- Learn Python basics: variables, data types, inputs, outputs
- Practice with beginner-friendly code exercises

## 🗓️ Structure:
- **Day 1:** What is Data Science, Python setup, variables
- **Day 2:** Data types, input/output, simple calculations
- **Day 3:** Practice task or mini quiz to reinforce learning

## 📘 Resources:
- [Python.org - Download](https://www.python.org/downloads/)
- [Google Colab](https://colab.research.google.com)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Python for Beginners Book (free)](https://greenteapress.com/wp/think-python-2e/)
```

---

## 📅 Day 1: What is Data Science + Python + Variables (`Day1.md`)

````markdown
# 📅 Day 1: Getting Started

## 🎯 What You’ll Learn:
- What is Data Science?
- Why Python?
- How to install Python and VS Code
- How to write your first Python code

---

## 📌 What is Data Science?

**Data Science** is the practice of:
- Asking questions
- Collecting data (CSV, APIs, web scraping)
- Cleaning it (removing duplicates, fixing errors)
- Analyzing it with code
- Making decisions or predictions

Used in:
- Healthcare (predict disease risk)
- Finance (detect fraud)
- E-commerce (recommend products)

---

## 🐍 Why Python for Data Science?
- Simple syntax (easier than Java or C++)
- Tons of libraries:
  - `NumPy` – number magic 🧮
  - `Pandas` – table magic 📊
  - `Matplotlib` – chart magic 📈
  - `Scikit-learn` – ML magic 🤖

---

## ⚙️ Step-by-Step Setup

### 📦 Install Python
- Go to: [python.org](https://www.python.org/downloads/)
- Install the latest version (check ✅ “Add to PATH” during install)
- Open Terminal or CMD:
  ```bash
  python --version
````

### 🛠️ Install VS Code (optional)

* [code.visualstudio.com](https://code.visualstudio.com/)
* Install Python extension

### 💡 Try a simple Python file

```python
# filename: hello.py
print("Hello, Grace! Welcome to Data Science!")
```

Run it:

```bash
python hello.py
```

---

## 🔤 Python Variables (with Examples)

A **variable** stores a value:

```python
name = "Grace"
age = 25
height = 5.4
is_student = True

print("Hello", name)
```

Variables follow:

* `snake_case` 🐍
* Don't start with numbers
* Can change anytime (they’re flexible)

---

## ✅ Exercise:

1. Create a file `day1_practice.py`
2. Declare these:

   * A name (string)
   * Age (int)
   * CGPA (float)
   * Is\_student (bool)
3. Print them with `print()`

You can do this in:

* JupyterLab
* VS Code
* Google Colab

````

---

## 📅 Day 2: Data Types + Input/Output (`Day2.md`)

```markdown
# 📅 Day 2: Data Types + Input/Output

## 🧠 Concepts:

### 🔢 Data Types
| Type     | Example         |
|----------|-----------------|
| String   | "Hello"         |
| Integer  | 10              |
| Float    | 5.5             |
| Boolean  | True / False    |
| List     | [1, 2, 3]       |
| Dict     | {"name": "Grace"} |

---

### 🖥️ Input & Output

#### `input()`
Takes user input as string:
```python
name = input("Enter your name: ")
print("Welcome", name)
````

#### Type Conversion

```python
age = int(input("Enter your age: "))
print("In 5 years you will be:", age + 5)
```

---

## ✅ Practice Task:

1. Ask user for their name, age, favorite food
2. Print a custom sentence:

   > Hello Grace, you're 25 and you love Amala!

---

## 👀 Bonus:

Try creating a small calculator:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
```

````

---

## 📅 Day 3: Practice Task or Quiz (`Day3.md`)

```markdown
# 📅 Day 3: Practice & Reinforcement

## 👨‍💻 Your Task:

1. Create a `user_info.py` script:
   - Collect name, age, country, language, favorite food
   - Print a full sentence like:
     > "Hi, I’m Grace from Nigeria. I’m 25 years old and I love Python and Banga soup."

2. Create a `calculator.py`:
   - Ask user for two numbers
   - Print sum, difference, product, division

3. Create a `profile_card.py`:
   - Create variables for name, age, and bio
   - Format it nicely using:
```python
print(f"My name is {name}, I'm {age} years old.")
````

---

## 💬 Reflection:

* What was hard for you this week?
* What made sense quickly?
* What should you review again?

---

## 🔗 Helpful Links:

* [Python Input](https://www.w3schools.com/python/python_user_input.asp)
* [FreeCodeCamp Python Crash](https://www.freecodecamp.org/news/learn-python-basics-in-1-hour/)

```
