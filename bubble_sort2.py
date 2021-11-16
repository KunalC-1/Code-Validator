# Python program for Bubble Sort
a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    a.append(value)

for i in range(0,number -1,2):
    for j in range(0,number - i - 1, 2):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The Sorted List in Ascending Order : ", a)
