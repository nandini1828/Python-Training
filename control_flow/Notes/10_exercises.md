# Control Flow Exercises

---

# Overview

This exercise set is divided into multiple levels.

🟢 Beginner

🟡 Intermediate

🔴 Advanced

🚀 Enterprise Challenges

💼 Mini Projects

🏆 Bonus Challenges

---

# 🟢 Beginner Exercises

## 1. Positive, Negative or Zero

Write a program that checks whether a number is

- Positive
- Negative
- Zero

---

## 2. Even or Odd

Determine whether a number is even or odd.

Example

```
Input

12

Output

Even
```

---

## 3. Adult or Minor

Determine whether a person is an adult.

Conditions

```
18 or above

↓

Adult

Otherwise

↓

Minor
```

---

## 4. Largest Number

Find the largest among

- two numbers

and later

- three numbers

---

## 5. Leap Year

Check whether a given year is a leap year.

---

## 6. Grade Calculator

Use

```
90+

A

80+

B

70+

C

60+

D

Below

F
```

---

## 7. Temperature Classifier

Classify temperature

```
Below 0

↓

Freezing

0-15

↓

Cold

16-30

↓

Pleasant

Above 30

↓

Hot
```

---

## 8. Vowel Checker

Determine whether a character is

- vowel

or

- consonant

---

## 9. Username Validation

Requirements

- Minimum 5 characters
- No spaces

---

## 10. Login Validation

Inputs

```
username

password
```

Allow login only if both are correct.

---

## 11. Calculator

Perform

- Addition
- Subtraction
- Multiplication
- Division

using conditions.

---

## 12. Electricity Bill

Create slabs.

Example

```
0-100

↓

₹0

101-300

↓

₹5/unit

Above 300

↓

₹8/unit
```

---

## 13. Movie Ticket

Children

↓

₹100

Adults

↓

₹200

Senior Citizens

↓

₹120

---

## 14. Traffic Signal

Input

```
Red

↓

Stop

Yellow

↓

Slow

Green

↓

Go
```

---

## 15. ATM PIN Validation

Allow withdrawal only when

- PIN is correct

---

# 🟡 Intermediate Exercises

## 16. Student Result

Determine

- Pass
- Fail
- Distinction

---

## 17. BMI Calculator

Return

- Underweight
- Normal
- Overweight
- Obese

---

## 18. Loan Eligibility

Conditions

- Salary
- Credit Score
- Existing Loan

---

## 19. Shipping Cost

Orders above ₹1000

↓

Free Shipping

Otherwise

↓

₹99

---

## 20. Employee Bonus

Calculate bonus using

- Years of Service
- Performance Rating

---

## 21. Library Fine

Calculate fine based on delayed days.

---

## 22. Password Strength

Check

- length
- uppercase
- lowercase
- digit

---

## 23. Triangle Type

Return

- Equilateral
- Isosceles
- Scalene

---

## 24. Voting Eligibility

Conditions

- Age
- Citizenship

---

## 25. Bank Withdrawal

Conditions

- PIN
- Balance
- Daily Limit

---

## 26. Shopping Discount

Premium customers receive additional discounts.

---

## 27. Weather Recommendation

Return

- Umbrella
- Jacket
- Sunglasses

based on weather.

---

## 28. File Extension Checker

Detect

- PDF
- Image
- Python
- Markdown

---

## 29. User Permission

Roles

- Admin
- Manager
- Employee
- Guest

---

## 30. Parking Fee

Calculate parking charges based on hours.

---

# 🔴 Advanced Exercises

## 31. Rewrite if-elif using match-case

Convert a long

```
if

↓

elif

↓

elif

↓

else
```

into

```
match-case
```

---

## 32. API Response Parser

Handle

```
Success

↓

Data

Error

↓

Message

Unauthorized

↓

Login
```

---

## 33. CLI Command Parser

Commands

```
copy

delete

move

rename
```

using match-case.

---

## 34. HTTP Status Interpreter

Convert status codes

```
200

404

500
```

into messages.

---

## 35. Build a Rule Engine

Example

```
Age

↓

Salary

↓

Credit Score

↓

Approve Loan
```

---

## 36. Configuration Loader

Priority

```
Environment

↓

Config File

↓

Default
```

using short-circuit evaluation.

---

## 37. Shopping Cart Validator

Check

- Empty cart
- Invalid items
- Out-of-stock products

---

## 38. Authentication System

Validate

- Username
- Password
- OTP
- User Status

---

## 39. Permission System

Implement

```
Admin

Manager

Developer

Guest
```

using logical operators.

---

## 40. Command Dispatcher

Build a command dispatcher using

```
match-case
```

---

## 41. Safe Dictionary Lookup

Use

```
.get()

defaultdict
```

instead of raising KeyError.

---

## 42. Nested Dictionary Pattern Matching

Parse

```python
{
    "user": {
        "name": "...",
        "role": "admin"
    }
}
```

---

## 43. Data Validation Engine

Validate multiple fields before processing.

---

## 44. Decision Tree

Design a decision tree for an insurance company.

---

## 45. Build Your Own Truthy Object

Implement

```
__bool__()
```

or

```
__len__()
```

---

# 🚀 Enterprise Challenges

## Challenge 1

Build an Authentication Service

Requirements

- Username
- Password
- OTP
- Account Status
- Login Attempts

---

## Challenge 2

E-Commerce Checkout

Validate

- Cart
- Address
- Payment
- Coupon
- Inventory

---

## Challenge 3

Employee Leave Approval

Based on

- Role
- Leave Balance
- Manager Approval

---

## Challenge 4

API Gateway

Handle

- GET
- POST
- PUT
- DELETE

using match-case.

---

## Challenge 5

Fraud Detection

Approve or reject transactions using

- Location
- Device
- Amount
- Login History

---

# 💼 Mini Projects

## Project 1

Student Management Decision System

Features

- Grade
- Attendance
- Pass/Fail
- Scholarship Eligibility

---

## Project 2

Banking Decision Engine

Features

- Deposit
- Withdrawal
- Transfer
- Loan Approval
- PIN Validation

---

## Project 3

Smart Traffic Controller

Handle

- Red
- Yellow
- Green
- Emergency Vehicles
- Pedestrian Crossing

---

# 🏆 Bonus Challenges

## Challenge 1

Recreate Python's `max()` using only conditional statements.

---

## Challenge 2

Implement a simple rules engine that accepts a dictionary of conditions and returns a decision.

---

## Challenge 3

Design a finite state machine for an elevator using `match-case`.

---

## Challenge 4

Create a menu-driven command-line application that dispatches commands using structural pattern matching.

---

## Challenge 5

Refactor a deeply nested `if` statement into clean, readable code using:

- Guard clauses
- Helper functions
- Logical operators
- Short-circuit evaluation

---

# Recommended Order

Complete the exercises in this order:

1. Beginner (1–15)
2. Intermediate (16–30)
3. Advanced (31–45)
4. Enterprise Challenges
5. Mini Projects
6. Bonus Challenges

---

# Success Checklist

By the end of this module, you should be able to:

- ✅ Write clean `if`, `elif`, and `else` statements
- ✅ Understand Truthy and Falsy values
- ✅ Use logical operators correctly
- ✅ Apply short-circuit evaluation
- ✅ Use ternary operators appropriately
- ✅ Solve problems using `match-case`
- ✅ Refactor nested conditions into readable code
- ✅ Build small decision engines
- ✅ Write testable, maintainable control-flow logic

Congratulations! 🎉

You have completed the **Control Flow** module. The next step is **Loop Foundations & Basic Iteration**, where you'll learn how to repeat actions efficiently using `for`, `while`, `break`, `continue`, `pass`, and loop `else` clauses.