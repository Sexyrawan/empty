
total_sum = 0
iteration_count = 0

for i in range(1, 51):
    total_sum += i
    iteration_count += 1
    print("Step:", iteration_count)
    print("Number Added:", i)
    print("Sum so far:", total_sum)
    print("-------------")  # just a separator for better reading

print("Final Sum is:", total_sum)
print("Total Steps:", iteration_count)
print("-------------")  # just a final separator for better reading
