# Program for number greater than or equal to zero
n = int(input("Enter a number: "))
n %= 10
print("Provided last diggit is: ",n)

# For negative numbers we use abs() to convert to positive
n = int(input("Enter a number: "))
n = abs(n)%10
print("The last digit is: ",n)