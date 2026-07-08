matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested comprehension
comp_result = [num * 2 for row in matrix for num in row if num % 2 == 0 if num > 3]
print("Using comprehension:", comp_result)

# Normal loop version
loop_result = []
for row in matrix:
    for num in row:
        if num % 2 == 0 and num > 3:
            loop_result.append(num * 2)

print("Using normal loop:", loop_result)



"""If a nested comprehension has 2–3 loops/conditions in one line, 
should we still use it or convert it into a normal loop for readability? """