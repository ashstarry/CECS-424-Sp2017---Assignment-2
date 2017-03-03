import sys;

print("Welcome !\n")

#######################################
#                                     #
#               Variables             #
#                                     #
#######################################
turn = 1
coins = ['H','H','H','H','H','T','T','T','T','T']
Win = False
precedentMove = 0

#######################################
#                                     #
#               Play                  #
#                                     #
#######################################

def play(userChoice,moveCoinsTo):
    if(moveCoinsTo == 11 and len(coins) < 11):
        coins.append('-')
        coins.append('-')
    elif (moveCoinsTo == 1):
        coins.insert(0,'-')
        coins.insert(0,'-')
        userChoice += 2
    variableOne = coins[userChoice - 1]
    variableTwo = coins[userChoice]
    variableThree = coins[moveCoinsTo - 1]
    variableFour = coins[moveCoinsTo]

    coins[moveCoinsTo - 1] = variableOne
    coins[moveCoinsTo] = variableTwo
    coins[userChoice - 1] = variableThree
    coins[userChoice] = variableFour

#######################################
#                                     #
#               Input check           #
#                                     #
#######################################

def Validity(Choice):
    if(Choice <= 0 or Choice > len(coins)):
        print("Bad :( !")
        return False
    elif (coins[Choice - 1] == '-' or coins[Choice] == '-'):
        print("Sorry this is not possible :( !");
        return False
    return True

#######################################
#                                     #
#               Main                  #
#                                     #
#######################################

while turn <= 5 and Win == False:
    print("".join(coins))
    isValid = False
    userChoice = 0
    while isValid == False:
        choice = sys.stdin.readline()
        userChoice = len(choice)
        isValid = Validity(userChoice)
        if len(coins) == 10:
            userMoveDecision = False
            while (userMoveDecision == False):
                move = input("Choose a direction (1=Left End or 11=Right End) => ")
                moveCoinsTo = int(move)
                if(moveCoinsTo == 1 or moveCoinsTo == 11):
                    userMoveDecision = True
        else:
            moveCoinsTo = precedentMove
    precedentMove = userChoice
    play(userChoice,moveCoinsTo)
    turn = turn + 1
print("".join(coins))
if("".join(coins) == "HTHTHTHTHT" or "".join(coins) == "THTHTHTHTH"):
    Win = True
if(Win):
    print("CONGRATULATIONS !!!! You have won the game!")
else:
    print("SORRY, You have lost the game!")