# 8. Take an integer N as input and print the count of digits of that number. Here 10101 has 5 digits
n = int(input("Enter the number: "))
count = 0
while n > 0:
    n //= 10
    count += 1

print(count)
