def find_gcf(num1, num2):
    # Find the smaller number between num1 and num2
    smallernumber = min(num1, num2)
    
    # Iterate from 1 to the smaller number
    for i in range(1, smallernumber + 1):
        # Check if i is a factor of both num1 and num2
        if num1 % i == 0 and num2 % i == 0:
            gcf = i  # Update the GCF
    return gcf

# Get user input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCF of the two numbers
result = find_gcf(num1, num2)
print(f"The GCF of {num1} and {num2} is: {result}")