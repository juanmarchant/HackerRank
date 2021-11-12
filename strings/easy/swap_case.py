# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  





# def swap_case(s):
#     s = ",".join(s).split(",")
#     s_str= ""
#     for i,letter in enumerate(s):
#         if letter.islower() == True:
#             s[i] = letter.upper()
#         else:
#             s[i] = letter.lower()
    
#     for letter in s:
#         s_str += letter
#     return s_str