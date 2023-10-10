#Task 1
# try:
#     number = int(input())
#     if(number%1000>0):
#         number_1 = (number//1000)
#         number_2 = (number%1000)//100
#         number_3 = (number%100)//10
#         number_4 = number%10
#         if(number_1+number_4==number_2-number_3):
#             print(f"YES")
#         else:
#             print(f"NO")
#     else:
#         print(f"Please, try another number")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 2
# user_age = int(input())
# if(user_age<18):
#     print(f"Access denied")
# else:
#     print("Access is allowed")


#Task 3
# try:
#     n = 3
#     a1 = int(input())
#     a2 = int(input())
#     a3 = int(input())
#     if (a2-a1==a3-a2):
#         d = a2-a1==a3-a2
#         print(f"YES")
#     else:
#         print(f"NO")
# except ValueError:
#     print ("Invalid input, please input a valid number")


#Task 4
# try:
#     row1 = int(input())
#     column1 = int(input())

#     row2 = int(input())
#     column2 = int(input())

#     if (row1 == row2) or (column1 == column2):
#         print("YES")
#     else:
#         print("NO")
# except ValueError:
#     print("Invalid input. Please enter valid integers between 1 and 8 for row and column.")
# except IndexError:
#     print("Error. Rows and columns start from 1 to 8")


#Task 5
# try:
#     # Input the coordinates of the first cell and the second cell
#     col1 = int(input())
#     row1 = int(input())
#     col2 = int(input())
#     row2 = int(input())
#     # Check if the coordinates are within the valid range (1 to 8)
#     if 1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8:
#         # Check if the king can move from the first cell to the second cell in one move
#         if abs(col1 - col2) <= 1 and abs(row1 - row2) <= 1:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("Invalid input. Coordinates must be between 1 and 8.")

# except ValueError:
#     print("Invalid input. Please enter four integers.")

#Task 6
# try:
#     number1 = int(input())
#     number2 = int(input())
#     number3 = int(input())
#     if (number1 > number2 & number3 > number2):
#         average = (number1+number3)/2
#         print(f"{average+0.5}")
#     elif (number2 > number1 & number3 > number1):
#         average =  (number2+number3)/2
#         print(f"{average+0.5}")
#     elif (number1 > number3 & number2 > number3):
#         average =  (number1+number2)/2
#         print(f"{average+0.5}")
# except ValueError:
#     print("Invalid input. Please enter valid integers between 1 and 8 for row and column.")

#Task 7
# try:
#     # Input the month number
#     month = int(input("Enter the month number (1-12): "))

#     # Create a dictionary to map month numbers to the number of days
#     month_days = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31
#     }

#     # Check if the input is a valid month number
#     if 1 <= month <= 12:
#         # Get the number of days for the specified month from the dictionary
#         days = month_days[month]
#         print(f"Number of days in month {month}: {days}")
#     else:
#         print("Invalid input. Please enter a month number between 1 and 12.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


#Task 8
# try:
#     # Input the weight of the amateur boxer as an integer
#     weight = int(input("Enter the weight of the boxer (in kg): "))

#     # Determine the weight category based on the weight
#     if weight <= 60:
#         category = "Light weight"
#     elif weight <= 64:
#         category = "First Welterweight"
#     elif weight <= 69:
#         category = "Welterweight"
#     else:
#         category = "Unknown"

#     if category != "Unknown":
#         print(f"{category}")
#     else:
#         print("The weight is too high for any category.")

# except ValueError:
#     print("Invalid input. Please enter a valid integer for the boxer's weight.")


#Task 9
# try:
#     # Input the password
#     password = input("Enter your password: ")

#     # Input the password confirmation
#     confirmation = input("Confirm your password: ")

#     # Check if the password and confirmation match
#     if password == confirmation:
#         print("Password accepted")
#     else:
#         print("Password not accepted")

# except Exception as e:
#     # Handle any potential exceptions, such as KeyboardInterrupt (Ctrl+C)
#     print("An error occurred: ", e)


#Task 10
# try:
#     # Input a number
#     num = int(input("Enter a number: "))

#     # Check if the number is even or odd
#     if num % 2 == 0:
#         print("Even value.")
#     else:
#         print("Odd number")

# except ValueError:
#     # Handle the case when the input is not a valid integer
#     print("Invalid input. Please enter a valid integer.")

# except Exception as e:
#     # Handle any other potential exceptions
#     print("An error occurred: ", e)


#Task 11
# try:
#     # Input the first number
#     num1 = int(input("Enter the first number: "))

#     # Input the second number
#     num2 = int(input("Enter the second number: "))

#     # Compare the two numbers to find the smallest
#     if num1 < num2:
#         smallest = num1
#     else:
#         smallest = num2

#     print(f"{smallest}")

# except ValueError:
#     # Handle the case when the input is not a valid number
#     print("Invalid input. Please enter valid numbers.")

# except Exception as e:
#     # Handle any other potential exceptions
#     print("An error occurred: ", e)


#Task 12
# try:
#     # Input the user's age
#     age = int(input("Enter your age: "))

#     # Determine the age group based on the age
#     if age <= 13:
#         age_group = "childhood"
#     elif 14 <= age <= 24:
#         age_group = "youth"
#     elif 25 <= age <= 59:
#         age_group = "maturity"
#     else:
#         age_group = "old age"

#     print(f"{age_group}")

# except ValueError:
#     # Handle the case when the input is not a valid integer
#     print("Invalid input. Please enter a valid age.")

# except Exception as e:
#     # Handle any other potential exceptions
#     print("An error occurred: ", e)


#Task 13
# try:
#     # Input three positive integers as side lengths
#     side1 = int(input("Enter the length of the first side: "))
#     side2 = int(input("Enter the length of the second side: "))
#     side3 = int(input("Enter the length of the third side: "))

#     # Check if the input values are positive
#     if side1 > 0 and side2 > 0 and side3 > 0:
#         # Check if the input values can form a triangle
#         if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#             # Determine the shape of the triangle
#             if side1 == side2 == side3:
#                 shape = "Equilateral"
#             elif side1 == side2 or side1 == side3 or side2 == side3:
#                 shape = "Isosceles"
#             else:
#                 shape = "Versatile"

#             print(f"{shape}")
#         else:
#             print("These side lengths cannot form a triangle.")
#     else:
#         print("Side lengths must be positive integers.")

# except ValueError:
#     # Handle the case when the input is not a valid integer
#     print("Invalid input. Please enter valid positive integers.")

# except Exception as e:
#     # Handle any other potential exceptions
#     print("An error occurred: ", e)