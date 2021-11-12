# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
# A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


# if year is a leap year = True
# if year is not a leap year = False

# CODE =>

# def is_leap(year):
#     leap = False
    
#     if year%4 == 0:
#         leap = True
#         if year%100 ==0:
#             leap = False
#             if year%400 == 0:
#                 leap = True
    
#     return leap