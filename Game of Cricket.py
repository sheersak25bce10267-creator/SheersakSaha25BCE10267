import random
print("*/Start of the Cricket Match\*")
print()
toss = input("Choose batting or bowling : ")
print()
w_you = 2
w_comp = 2
runs_you, runs_comp = 0, 0
ball, check = 12, 0
dur = 0
while (dur < 2):
    if toss == 'bat' or toss == 'batting':
        print("You are Batting (choose runs between 1 and 6) and Computer is Bowling : ")
        check = 1
    elif toss == 'bowl' or toss == 'bowling':
        print("You are Bowling (choose bowl between 1 and 6) and Computer is Batting : ")
        check = 0
    while (ball > 0):
        you = int(input("You : "))
        if you > 6:
            print("Error! You cannot break BCCI rules")
            if check == 0:
                toss = "bat"
            else:
                toss = "bowl"
            break;
        comp = random.randint(1,6)
        print("Computer :", comp)
        if you == comp:
            if check == 1:
                w_you -= 1
                print("OUT!!! (Wickets left :" , w_you, ")")
            elif check == 0:
                w_comp -= 1
                print("OUT!!! (Wickets left :" , w_comp, ")")
        else :
            if check == 1:
                runs_you += you
            elif check == 0:
                runs_comp += comp
        print()
        if w_you == 0:
            toss, ball = 'bowl', 12
            print("All out!!! Your Innings is Over")
            w_you = 10
            break
        elif w_comp == 0:
            toss, ball = 'bat', 12
            print("All out!!! Computer's Innings is Over")
            w_comp = 10
            break
        elif ball == 0:
            if check == 0:
                toss = "bat"
            else:
                toss = "bowl"
            ball = 12
            break
        ball -= 1
    print("Your total score :", runs_you, "runs") if check == 1 else print("Computer's total score :", runs_comp, "runs")
    print("\n\n")
    dur += 1
if runs_you > runs_comp:
    print("You are the WINNER! I am positive you victory was a fluke")
else:
    print("Computer is the WINNER! You loser do better next time")
print("\n*/End of the Cricket Match\*")
