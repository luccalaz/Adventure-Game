import csv, time

def getInput():
    userInput = input("> ")

    # checks user input
    while (userInput not in ["1", "2", "3"]):
        userInput = input("Invalid Input! Try again: ")

    return userInput

def readFile(line):
    # opens the story.csv file and creates csv reader list
    infile = open("story.csv", "r")
    csvReader = list(csv.reader(infile))

    # reads the file and returns the required information
    if (len(csvReader[line]) == 1):
        return csvReader[line][0]
    else:
        question = csvReader[line][0]
        choice1 = csvReader[line][1]
        choice2 = csvReader[line][2]
        line1 = int(csvReader[line][3]) - 1
        line2 = int(csvReader[line][4]) - 1
        return question, choice1, choice2, line1, line2

def displayPrompt(line):
    # check if the line is a game over line
    if (not isinstance(readFile(line), tuple)):
        print(f"\n{readFile(line)}")
        return "end"

    # get the info from the story.csv file
    question, choice1, choice2, line1, line2 = readFile(line)

    # display the question/choices text and ask for user input
    print(f"\n{question}")
    print(f"1 - {choice1}")
    print(f"2 - {choice2}")
    print(f"3 - Save Game")
    userInput = getInput()

    # returns current line number if user wants to save the game
    if (userInput == "1"):
        return line1
    elif (userInput == "2"):
        return line2
    elif (userInput == "3"):
        return line

def startGame(line):
    # checks the existence of the story.csv file before starting
    try:
        open("story.csv", "r")
    except:
        print("\n>>> Error! No story.csv file found!")
        return

    while (line != "end"):
        lastLine = line
        line = displayPrompt(line)

        # checks if user wants to save the game
        if (lastLine == line):
            # saves the game
            outfile = open("saved.txt", "w")
            outfile.write(str(line))
            print("\n>>> Game Saved")

def main():
    while True:
        print("\n******* Test Adventure Game v1.0 *******")
        print("*                                      *")
        print("*           1 - New Game               *")
        print("*           2 - Load Game              *")
        print("*           3 - Quit                   *")
        print("*                                      *")
        print("****************************************")
        mainMenuChoice = getInput()

        if (mainMenuChoice == "1"):
            # starts new game
            startGame(0)
        elif (mainMenuChoice == "2"):
            # tries loading the game or starts new game if no savegame found.
            try:
                infile = open("saved.txt","r")
                print("\n>>> Game Loaded")
                startGame(int(infile.readline()))
            except:
                print("\n>>> No savegame found, starting a new game instead.")
                startGame(0)
        else:
            # closes the program
            break

        time.sleep(2)
            
main()