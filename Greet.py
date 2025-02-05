# import time
# name=input("Please enter your name: ")
# currentTime = int(time.strftime('%H')) 

# if currentTime < 12:
#   print('Good morning ',name)
# elif currentTime >12:
#   print('Good afternoon ',name)
# elif currentTime > 6:
#   print('Good night',name)  


# import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))

# if(hour>=0 and hour<12):
#    print("Good morning!")
# elif(hour>=12 and hour<17):
#    print("Good afternoon!")  
# elif(hour>=17 and hour<0):
#    print("Good night!")  

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
    