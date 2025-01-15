# import re
# # Sample string
# text = "Hello World! Welcome to Coding Saturday 123."
# # 1. Matches any single character
# pattern1 = r'H.llo'
# match1 = re.search(pattern1, text)
# print(f"Pattern '{pattern1}':", match1.group() if match1 else "No match found.")
# # 2. Matches the start of the string
# pattern2 = r'^Hello'
# match2 = re.search(pattern2, text)
# print(f"Pattern '{pattern2}':", match2.group() if match2 else "No match found.")
# # 3. Matches the end of the string
# pattern3 = r'123.$'
# match3 = re.search(pattern3, text)
# print(f"Pattern '{pattern3}':", match3.group() if match3 else "No match found.")
# # 4. Matches zero or more repetitions of the preceding element
# pattern4 = r'o*'
# matches4 = re.findall(pattern4, text)
# print(f"Pattern '{pattern4}':", matches4)
 
# # 5. Matches one or more repetitions of the preceding element
# pattern5 = r'o+'
# matches5 = re.findall(pattern5, text)
# print(f"Pattern '{pattern5}':", matches5)

import re
email = input("Enter an email:")
valid = re.match(r'^[a-zA-Z0-9_%.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
 
print("Valid email address." if valid else "Invalid email address.")


# # valid contact no.
# import re
# indian_phone_with_country_code_regex = r'^(\+91|91)?[6-9]\d{9}$'

# def is_valid_indian_phone_with_country_code(phone):
#     return re.match(indian_phone_with_country_code_regex, phone) is not None

# # Test
# phone = input("Enter the number: ")
# print(is_valid_indian_phone_with_country_code(phone))  # True if valid, False if not
