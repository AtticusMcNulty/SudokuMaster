easyBoards = [
    [[40, 3, 2, 10], [2, 10, 40, 30], [10, 20, 30, 4], [30, 4, 1, 20]]
]
mediumBoards = [
    [
        [20, 50, 4, 10, 60, 30],
        [60, 30, 10, 5, 4, 2],
        [1, 60, 30, 2, 50, 40],
        [5, 40, 20, 6, 30, 10],
        [40, 10, 50, 3, 2, 6],
        [30, 20, 6, 40, 10, 50],
    ]
]
hardBoards = [
    [
        [80, 40, 1, 3, 60, 70, 5, 20, 90],
        [2, 3, 60, 90, 10, 5, 80, 4, 70],
        [50, 90, 70, 2, 4, 80, 10, 60, 3],
        [60, 50, 8, 40, 7, 9, 20, 3, 10],
        [1, 7, 40, 60, 30, 20, 90, 8, 5],
        [30, 2, 90, 5, 8, 10, 6, 70, 40],
        [9, 10, 30, 70, 2, 6, 40, 50, 80],
        [40, 8, 20, 1, 50, 30, 70, 9, 6],
        [70, 60, 5, 80, 90, 4, 3, 10, 20],
    ]
]

def printTutorial():
    print("\nThis program provides three different difficulties of Sudoku Boards. Selecting Easy will give you 4x4 boards, Medium will be 6x6, and Hard is 9x9.\n")
    print("After selecting a difficulty, you will be able to select between a number of predefined levels. Levels that appear in green you have already solved, levels in yellow you have not attempted but not solved, and white levels you have not yet attempted.\n")
    print("Once you select a level, you will be able to perform various operations on the board.\n")
    print("Enter a 1 to place a number on the Sudoku board. You should enter the row, column, and value separated by spaces. Note that if you attempt to place a number in a taken box, you will be prompted to enter a new number. New numbers will appear in green, while old predefined numbers will appear in white.\n")
    print("Enter a 2 to remove a number from the Sudoku board. You will be prompted for the row and column. Note that if you enter a number outside the bounds or attempt to remove a predefined number, you will be reprompted for a new row and column. The box from which you remove a number will appear in red for 1 turn.\n")
    print("Enter a 3 to get a random hint. This will appear in yellow.\n")
    print("Enter a 4 to reset the board. Note that this will remove all your current progress, and you will be prompted twice to ensure your intentions.\n")
    print("Enter a 5 to show the completed board. This will bring up the stats screen and fill in all uncompleted boxes with a red number.\n")
    print("Enter a 6 to return to the level selection screen. Note that this will also get rid of any current progress you have on a board.\n")
    print("The stats screen will show you various things about your latest performance. This includes time used, hints used, mistakes detected, and total time. Both mistakes and hints add to your total time, as does requesting the completed board.\n")

def generateBoard(board):
    for row in board:
        # Print horizontal lines
        print("+" + "---+" * len(row))
        # Print row with vertical lines
        for cell in row:
            print(f"| {cell if cell <= 9 else ' '}", end=" ")
        print("|")
    # Print the last horizontal line
    print("+" + "---+" * len(board[0]))

def selectLevel(boards):
    num_boards = len(boards)
    for x in range(num_boards):
        if x % 3 == 0:
            print("\t" + str(x + 1))
        else:
            print(str(x + 1) + "\t")
    board_index = int(input("Select a level by entering its number: "))
    while board_index < 1 or board_index > num_boards:
        print("Invalid input. Try again.")
        board_index = int(input("Select a level by entering its number: "))
    return board_index - 1

def getBoard(difficulty, boards):
    board_index = selectLevel(boards[difficulty - 1])
    numRows = len(boards[difficulty - 1][board_index])
    generateBoard(boards[difficulty - 1][board_index])
    return numRows, boards[difficulty - 1][board_index]

def enterNumber(numRows, board):
    while True:
        num = int(input("Enter a number to add to the Sudoku Board: "))
        if not 1 <= num <= numRows:
            print("Invalid input. Number must be between 1 and", numRows)
            continue

        row = int(input("Enter the desired row: "))
        if not 1 <= row <= numRows:
            print("Invalid input. Row must be between 1 and", numRows)
            continue

        col = int(input("Enter the desired column: "))
        if not 1 <= col <= numRows:
            print("Invalid input. Column must be between 1 and", numRows)
            continue

        if checkValidPlacement(num, row, col, numRows, board):
            break

    board[row - 1][col - 1] = num

def checkValidPlacement(num, row, col, numRows, board):
    subgrid_size = int(numRows ** 0.5)
    box_start_row = (row - 1) // subgrid_size * subgrid_size
    box_start_col = (col - 1) // subgrid_size * subgrid_size

    # Check subgrid
    for i in range(box_start_row, box_start_row + subgrid_size):
        for j in range(box_start_col, box_start_col + subgrid_size):
            if board[i][j] == num:
                print("Invalid input. Number already exists in the subgrid.")
                return False

    # Check row
    if num in board[row - 1]:
        print("Invalid input. Number already exists in the row.")
        return False

    # Check column
    if num in [board[i][col - 1] for i in range(numRows)]:
        print("Invalid input. Number already exists in the column.")
        return False

    return True

def runSudoku():
    action = 0
    tutorial = input("Welcome to SudokuMaster. Enter 't' for a tutorial, or 's' to skip the walkthrough and jump in: ")
    if tutorial == "t":
        printTutorial()

    difficulty = int(input("Select the level of difficulty: Enter 1 for Easy, 2 for Medium, and 3 for Hard: "))
    while difficulty not in [1, 2, 3]:
        print("Invalid input. Please try again.")
        difficulty = int(input("Select the level of difficulty: Enter 1 for Easy, 2 for Medium, and 3 for Hard: "))

    print("Here are the levels available to you: ")
    numRows, board = getBoard(difficulty, [easyBoards, mediumBoards, hardBoards])

    while action != 6:
        print("Pick an action: ")
        print("1 - Enter a number")
        print("2 - Remove a number")
        print("3 - Get a hint")
        print("4 - Reset the board")
        print("5 - Show solution")
        print("6 - Quit")
        action = int(input("Enter your choice: "))

        if action == 1:
            enterNumber(numRows, board)
            generateBoard(board)

runSudoku()