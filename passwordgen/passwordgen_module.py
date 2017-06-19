from random import randint

def passwordgen():
    pw = chr(randint(33, 47))+chr(randint(48, 57))+chr(randint(65, 90))+ chr(randint(97, 122))
    for j in range(randint(4, 20)):
        i = randint(0, 3)       
        if i == 0:
            pw = pw + chr(randint(33, 47)) # symbol
        if i == 1:
            pw = pw + chr(randint(48, 57)) # number
        if i == 2:
            pw = pw + chr(randint(65, 90)) # upper
        if i == 3:
            pw = pw + chr(randint(97, 122)) # lower
    return pw


def main():
    difficulty = input("Weak or Strong?: ")
    if difficulty == "Weak":
        listweak = ["hurka", "kolbász", "tejfel", "tojás", "frissföl"]
        pw = listweak[randint(0, 4)]
        print(pw)
    elif difficulty == "Strong":
        pw = passwordgen()
        print(pw)
    else:
        raise SyntaxError("Retard User hahahaha")

    return


if __name__ == '__main__':
    main()
