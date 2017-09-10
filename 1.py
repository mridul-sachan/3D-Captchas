'''
def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    captcha_val = ''.join(random.choice(chars) for _ in range(size))
    return captcha_val
'''

import string 
import random 

captcha_list = []
size = 4
chars = string.ascii_uppercase + string.digits
for _ in range(size):
    captcha_val = ''.join(random.choice(chars))
    captcha_list.append(captcha_val)
	
captcha_str = ""	
for item in captcha_list:
    captcha_str = captcha_str + str(item)

print captcha_str	
	
	
'''
sentence = ['this','is','a','sentence']
sent_str = ""
for i in sentence:
    sent_str += str(i) + "-"
sent_str = sent_str[:-1]
print sent_str
'''
    