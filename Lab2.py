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