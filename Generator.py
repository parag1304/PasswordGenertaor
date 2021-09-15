import random
def generator(Deflength, Defchar):
  i = 0
  password = ""
  # generating password using random module
  while i <= Deflength:
    password += random.choice(Defchar)
    i += 1  
  print(f"Your password is {password}")
