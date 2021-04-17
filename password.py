import string
import random

def password(a):
	p_word = ''.join(random.choice(string.ascii_letters) for i in range(length))

	print(p_word)

password(10)