#copyright cakrome 2019-2020

import string
from random import *


def password(cha,r):
  pwdlist = []
  for i in range(randint(r,r)):
    pwd = choice(cha)
    pwdlist.append(pwd)
    passwd = "".join(pwdlist)
  return passwd
  
def one():
  cha = string.digits
  print(password(cha,r))
def two():
  cha = string.digits + string.ascii_lowercase
  print(password(cha,r))
def three():
  cha = string.digits + string.ascii_uppercase
  print(password(cha,r))
def four():
  cha = string.ascii_uppercase
  print(password(cha,r))
def five():
  cha = string.ascii_lowercase
  print(password(cha,r))
def six():
  cha = string.ascii_letters
  print(password(cha,r))
def seven():
  cha = string.ascii_letters + string.digits
  print(password(cha,r))
  
options = {1 : one,
  2 : two,
  3 : three,
  4 : four,
  5 : five,
  6 : six,
  7 : seven,
}


print("Info: Enter 1 for digits only, 2 for digits plus lowercase letters and 3 for digits plus uppercase letters, 4 for uppercase letters only, 5 for lowercase letters only, 6 for letters and 7 for letters plus digits.")
flag = "y"

while flag == "y":
  sel = int(input("Please choose the password combination: "))
  if sel <= 7 and sel > 0:
    r = int(input("Please input the length of password you want: "))
    options[sel]()
  else:
    print("Please enter 1 to 7 only")
  flag = input("Do you want to generate another password(y/N)? ")
  if flag == "y": continue
  else: break

print("thanks for using this tool\nbye now!")
