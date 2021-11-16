# Python program for Bubble Sort
a = []
number = int(input())
for i in input().split():
    a.append(int(i))

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

for i in a:
    print(i, end=" ")

