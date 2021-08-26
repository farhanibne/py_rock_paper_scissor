#snake-water-gun


import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 'r':                  
        if you =='p':
            return False
        elif you == 's':
            return True
    elif comp == 'p':
        if you =='s':
            return False
        elif you == 'r':
            return True
    elif comp == 's':
        if you =='r':
            return False
        elif you == 'p':
            return True        

# print("comp one turn: snake(s) water(w) or gun(g)??")
randno = random.randint(1,3)
# print(randno)

if randno == 1 :
    comp =  'r'
elif randno == 2 :
    comp =  'p'
elif randno == 3 :
    comp =  's'    


you = input("your two turn: rock(r),paper(p),scissor(s)??")



a = gameWin(comp, you)


print(f"you choose {you}")
print(f"computer choose {comp}")


if a== None:
    print("this is a tie")
elif a:
    print("you win!!!")
else:
    print("you lose!!")        

