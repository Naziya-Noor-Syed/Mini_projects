import random
import string

pass_len = 12
charval = string.punctuation + string.ascii_letters + string.digits

#list comprehension[function i in range(n)]]

password = "".join([random.choice(charval) for i in range(pass_len)])

print(password)
# password = ""
# for i in range(pass_len):
#     password += random.choice(charval)

# print(password)
