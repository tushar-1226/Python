import time
name= input("Enter your name:-").title()
hour = int(time.strftime('%H'))

if 4<= hour<12:
   print("Good morning: ", name)
elif 12<=hour<17:
   print("Good afternoon: ", name)
elif 17<=hour<21:
   print("Good Evening: ", name)
else:
   print("Good night: ", name)         
    
