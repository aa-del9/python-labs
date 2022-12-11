import random

print("Let's learn multiplication! ")
while True:
    x=random.randint(0,9)
    y=random.randint(0,9)
    while True:
        ans=int(input(f"How much is {x} times {y}? "))  
        if(ans==x*y):
            print("Very good!")
            break
        else: 
            print("No. Please try again. ")
            hehe