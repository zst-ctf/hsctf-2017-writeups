import random
random.randint
#doing this first this time
inp = str(input("Enter the password: "))
print inp
#so secure you can't get in even if you know the password
password = random.randint(0,2**30)
print password
if (inp == password):
    flag = open("flagfilename",'r').read() #flagfilename is different serverside
    print flag 
else:
    print "WRONG password"