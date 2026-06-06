# Python — Class 1 Notes

**Student:** Muhammad Danish
**Topics:** Print, Variables, Data Types, Type Conversion, Input, Operators

---

## 1. `print()` Function

Used to display output on the screen.

```python
print("Hello, World!")
print(344)

# sep parameter — controls what goes between multiple values
print("Muhammad Danish", "I am learning Python", sep=" - ")
# Output: Muhammad Danish - I am learning Python
```

---

## 2. Variables

Variables are like containers — they store data that you can use later.

```python
name = "Muhammad Danish"   # string variable
age = 21                   # integer variable
is_live = True             # boolean variable

print(name)
print(age)
print(is_live)
```

### Checking data type with `type()`

```python
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(is_live))  # <class 'bool'>
```

### Common data types

| Type    | Example         | Description         |
|---------|-----------------|---------------------|
| `str`   | `"Danish"`      | Text / string       |
| `int`   | `21`            | Whole number        |
| `float` | `3.14`          | Decimal number      |
| `bool`  | `True / False`  | Boolean (yes/no)    |

---

## 3. Type Conversion

You can convert one data type to another using built-in functions.

```python
score = "50"              # this is a string

value = int(score) + 10   # convert to int → 60
print(value)

value = float(score) + 10 # convert to float → 60.0
print(value)
```

| Function  | Converts to       |
|-----------|-------------------|
| `int()`   | Whole number      |
| `float()` | Decimal number    |
| `str()`   | Text / string     |

---

## 4. `input()` Function

Used to take data from the user.

> **Important:** `input()` always returns a **string** by default.

```python
name = input("Enter your name: ")
print(name)

# Without conversion — input is a string
age = input("Enter your age: ")
print(type(age))   # <class 'str'>

# With int() conversion — input becomes an integer
age = int(input("Enter your age: "))
print(type(age))   # <class 'int'>
```

---

## 5. Operators

### Arithmetic Operators

```python
num_1 = 10
num_2 = 3

print(num_1 + num_2)   # 13  — addition
print(num_1 - num_2)   # 7   — subtraction
print(num_1 * num_2)   # 30  — multiplication
print(num_1 / num_2)   # 3.33 — division
print(num_1 % num_2)   # 1   — modulus (remainder)
print(num_1 // num_2)  # 3   — floor division (no decimal)
```

> `%` (modulus) gives the **remainder** after division.
> `//` (floor division) gives the **quotient** without the decimal.

### Comparison Operators

These always return `True` or `False`.

```python
value_1 = 5
value_2 = 10

print(value_1 == value_2)  # False — equal?
print(value_1 != value_2)  # True  — not equal?
print(value_1 >  value_2)  # False — greater than?
print(value_1 <  value_2)  # True  — less than?
print(value_1 >= value_2)  # False — greater than or equal?
print(value_1 <= value_2)  # True  — less than or equal?
```

---

## Quick Recap — Class 1

- ✅ `print()` — display output, use `sep` for custom separators
- ✅ Variables — containers for storing data
- ✅ `type()` — check the data type of a variable
- ✅ Type conversion — `int()`, `float()`, `str()`
- ✅ `input()` — get user input (always returns string by default)
- ✅ Arithmetic operators — `+`, `-`, `*`, `/`, `%`, `//`
- ✅ Comparison operators — `==`, `!=`, `>`, `<`, `>=`, `<=`
