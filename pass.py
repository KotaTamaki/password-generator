import string
import secrets
dict1={}

print("how long do you need a pass?")
a=int(input("input..."))
print("pass's name?")
b=input("input...")

def pass_gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '%&!$#()'

   return ''.join(secrets.choice(chars) for x in range(size))

def make_dict(a):
    made_pass=pass_gen(a)
    dict1[b]=made_pass
    print("\033[H\033[2J")
    print("created password👇")
    print(dict1)
    
make_dict(a)
