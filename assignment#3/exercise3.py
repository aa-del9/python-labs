import random

list1=["Very good!","Excellent!","Nice work!","Keep up the good work!"]
list2=["No. Please try again.","Wrong. Try once more.","Don't give up!","No. Keep trying."]
while True:
    print("Let's learn multiplication! ")
    correct=0
    for x in range(0,5):
        x=random.randint(0,9)
        y=random.randint(0,9)
        ans=int(input(f"How much is {x} times {y}? "))
        if ans==x*y:
            correct+=1
            print(random.choice(list1))
        else: 
            print(random.choice(list2))
    prcntge=(correct/5)*100
    print("Your percentage is",prcntge)
    if prcntge<75:
        
        print("Please ask your teacher for extra help.")
    elif prcntge>=80:
        print("Congratulations, you are ready to go to the next level!")   