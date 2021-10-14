import re
pattern1 = '[b|h][aeiou][t]'
test_string1 = "bat bit but hat hit hut"

result = re.findall(pattern1, test_string1)
for i in result:
    print(i)
print("\n")


pattern2 = "Samira Deepak"
test_string2 = "Python is my favorite programming language"
if re.search(pattern2,test_string2):
    print("WORD IS FOUND")
else:
    print("WORD IS MISSING")


email = "samiradeepak@gmail.in"
pattern3 = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#pattern3 = r"\b[A-Za-z0-9.%+-]{1,20} +@[A-Za-z0-9.%+-]{1,20} + \.[A-Z|a-z]{2,3}\b"
if re.match(pattern3, email):
    print("Email is correct")
else:
    print("Email is incorrect")