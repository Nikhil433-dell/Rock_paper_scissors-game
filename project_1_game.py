import random
# Rock(R),Paper(P),scissor(S)
# rock(1),paper(2),scissors(3)
def game(comp,you):
    if comp == you:
        return None
    elif comp == 'R':
        if you == 'P':
            return True
        elif you == 'S':
            return False
    elif comp == 'P':
        if you == 'S':
            return True
        elif you == 'R':
            return False
    elif comp == 'S':
        if you == 'R':
            return True
        elif you == 'P':
            return False
print("computer's turn: Rock(R),Paper(P),scissor(S) !")
randno = random.randint(1,3)
# print(randno)
if randno == 1:
    comp = 'R'
elif randno == 2:
    comp = 'P'
elif randno == 3:
    comp = 'S'

print("computer chosed his object.")
you = input("your's turn: Rock(R),Paper(P),scissor(S):\n")
a = game(comp,you)
# print("computer chose :" randno)

print(f"computer choose {comp} and you choose {you}")


if a == None:
    print("Game is tie")
elif a == True:
    print("you Won the Game ")
else:
    print("you Lose the Game")