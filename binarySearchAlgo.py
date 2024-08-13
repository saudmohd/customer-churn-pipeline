numbers = []

n = int(input("Enter the Range of Input of Number: "))

for i in range(n):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)


numbers.sort()
print("Sorted List:", numbers)
x = int(input("Enter Number to Find to in List Through Binary Search: "))

low = 0 
high = n - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == x:
        print(f"Number {x} found at index {mid}.")
        break
    elif numbers[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"Number {x} not found in the list.")
