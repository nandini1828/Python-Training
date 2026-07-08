nums = range(1, 11)

# Task: take even numbers and square them

# 1) Normal loop
loop_result = []
for n in nums:
    if n % 2 == 0:
        loop_result.append(n ** 2)

print("Using normal loop:", loop_result)

# 2) List comprehension
comp_result = [n ** 2 for n in nums if n % 2 == 0]
print("Using list comprehension:", comp_result)

# 3) Generator expression
gen_result = (n ** 2 for n in nums if n % 2 == 0)
print("Using generator:", list(gen_result))




""" In Python, 
 when is it actually better to use a generator instead of just creating a normal list? """