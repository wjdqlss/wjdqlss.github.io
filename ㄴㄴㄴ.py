import string
import random
 
_pw_length = 12 
 
string_pool = string.ascii_letters + string.digits + "!@#$%" 
 
result = ""
for i in range(_pw_length):
    result += random.choice(string_pool)
 
print("\n비밀번호:", result)
