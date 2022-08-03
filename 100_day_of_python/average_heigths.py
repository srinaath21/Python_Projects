students_height = input(" Enter the list of students height: ").split()
sum_of_height = 0
for i in range(len(students_height)):
    sum_of_heights = sum_of_heights + int(students_height[i])
average_height = round(sum_of_heights / len(students_height))
print(average_height)
