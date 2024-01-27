import random, string
import pyperclip as clip
password_length = 18

string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits = '0123456789'
string.punctuation = '@#$%&!?'

characters = string.digits + string.punctuation

password = ""   

for index in range(int(password_length/2)):
    password = password + random.choice(characters)

for index in range(int(password_length/2)):
    password = password + random.choice(string.ascii_letters)

password = ''.join(random.sample(password,len(password)))

clip.copy(format(password))