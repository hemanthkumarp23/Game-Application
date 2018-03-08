from module_Game import ConsoleGame

myGame = ConsoleGame()

while(True):

    userinput = int(input("Enter the integer value in the range (1 - 50): "))
    myGame.run_game(userinput)
