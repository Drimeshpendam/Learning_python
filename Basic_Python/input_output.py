# Get input as a string
name = input("Enter your name: ")
print("Hello," , name)

# Get input as an integer
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Get input as a floating-point number
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

# Get input as a boolean
is_student = input("Are you a student? (True/False): ").lower() == 'true'
print(f"You are a student: {is_student}")

# Get input as a list of integers
numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_str.split()]
print(f"You entered: {numbers_list}")

