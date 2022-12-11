import random

list1=["Very good!","Excellent!","Nice work!","Keep up the good work!"]
list2=["No. Please try again.","Wrong. Try once more.","Don't give up!","No. Keep trying."]
print("Let's learn multiplication! ")
while True:
    x=random.randint(0,9)
    y=random.randint(0,9)
    while True:
        ans=int(input(f"How much is {x} times {y}? "))  
        if(ans==x*y):
            print(random.choice(list1))
            break
        else: 
            print(random.choice(list2))