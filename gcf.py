def find_gcf(num1, num2):
    # Find the smaller number between num1 and num2
    smallernumber = min(num1, num2)
    
    # Iterate from 1 to the smaller number
    for i in range(1, smallernumber + 1):
        # check if i is a factor of both num1 & num2
        if num1 % i == 0 and num2 % i == 0:
            gcf = i  # runs the loop until it finds that i is the gcf of both num1 and num2
    return gcf # returns and changes the value of gcf once it finds a proper gcf

# Get user input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCF of the two numbers
result = find_gcf(num1, num2)
print(f"The GCF of {num1} and {num2} is: {result}")

