import random
while True:
    print(''' 1. roll the dice       0. exit     ''')
    user = int(input("enter number"))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    else:
     break
        