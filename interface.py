from ticTacToeAiEval import getPossibleMovesInklScore
import Board
import Global_Vars
import main
from tkinter import *
from PIL import ImageTk, Image

from ticTacToe import *

# Global Variables for TicTacToe
LukasTicTacToeBoard: ndarray
LukasTurnCount: int
LukasRunningState: bool

# Global variable for GameMode
GameMode: int


# Predefined visual button styles
style_1 = {'fg': 'black', 'bg': 'RoyalBlue3', 'activebackground':
           'gray71', 'activeforeground': 'gray71'}

style_2 = {'fg': 'white', 'bg': 'OliveDrab2', 'activebackground':
           'gray71', 'activeforeground': 'gray71'}

style_3 = {'fg': 'black', 'bg': 'purple1', 'activebackground':
           'gray71', 'activeforeground': 'gray71'}

# Updates the currently running game of tictactoe according to which button is pressed


def doTicTacToeUpdate(row: int, column: int):
    global LukasRunningState
    global LukasTicTacToeBoard
    global LukasTurnCount

    # skips processing turn if game is not running
    if LukasRunningState == False:
        return LukasTicTacToeBoard[row][column]

    # Processes turn
    TurnResult = doAutoTurn(LukasTicTacToeBoard,
                            LukasTurnCount, LukasRunningState, row, column)

    # Deconstructs Turn results
    LukasTicTacToeBoard = TurnResult[0]
    LukasTurnCount = TurnResult[1]
    LukasRunningState = TurnResult[2]
    # Debugging printout
    printArrayColors(LukasTicTacToeBoard)

    '''
    Start Testing Area for AI preperation DONT TOUCH
    '''
    printErrorMsg("START TESTING AREA AI")

    playerFromTurn = LukasTurnCount + 1

    print(f"Player taken from turn: {playerFromTurn}")

    ScoredMoves = getPossibleMovesInklScore(
        LukasTicTacToeBoard, playerFromTurn)

    printYellowMsg("Inspect Scored Moves")
    print(ScoredMoves)

    printErrorMsg("END TESTING AREA AI")
    '''
    End Testing Area for AI preperation DONT TOUCH
    '''

    # Returns button state
    return LukasTicTacToeBoard[row][column]

# changes the style of a button


def setStyle(style, button: Button):
    if(style == 1):
        button.configure(style_2)
    if(style == 2):
        button.configure(style_3)

# Executes the appropriate Button action based on it's position as well as the game mode


def doAppropriateButtonAction(row: int, column: int, mode: int, button: Button):
    # Executed commands for Gamemode TicTacToe
    if mode == 1:
        setStyle(doTicTacToeUpdate(row, column), button)
        return
    # Executed commands for Gamemode Pawnchess
    if mode == 2:
        return
    # Executed commands for Gamemode Checkers
    if mode == 3:
        return
    # Skips button action for undefined modes
    return

# Creates the generic 6x6 playing are out of tkinter buttons.


def create_board():

    # Reference to global Gamemode in order to be able to reference it during button calls
    global GameMode

    checkersBoard = Frame(mainDisplay, width=690, height=695, bg="white")
    checkersBoard.grid(row=0, rowspan=1, column=1, columnspan=1)
    checkersBoard.grid_propagate(0)
    print("Next is Button")
    cell11 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 0, GameMode, cell11)], width=15, height=7)
    cell12 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 1, GameMode, cell12)], width=15, height=7)
    cell13 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 2, GameMode, cell13)], width=15, height=7)
    cell14 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 3, GameMode, cell14)], width=15, height=7)
    cell15 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 4, GameMode, cell15)], width=15, height=7)
    cell16 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(0, 5, GameMode, cell16)], width=15, height=7)
    cell11.grid(row=0, column=0)
    cell12.grid(row=0, column=1)
    cell13.grid(row=0, column=2)
    cell14.grid(row=0, column=3)
    cell15.grid(row=0, column=4)
    cell16.grid(row=0, column=5)
    cell21 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 0, GameMode, cell21)], width=15, height=7)
    cell22 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 1, GameMode, cell22)], width=15, height=7)
    cell23 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 2, GameMode, cell23)], width=15, height=7)
    cell24 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 3, GameMode, cell24)], width=15, height=7)
    cell25 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 4, GameMode, cell25)], width=15, height=7)
    cell26 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(1, 5, GameMode, cell26)], width=15, height=7)
    cell21.grid(row=1, column=0)
    cell22.grid(row=1, column=1)
    cell23.grid(row=1, column=2)
    cell24.grid(row=1, column=3)
    cell25.grid(row=1, column=4)
    cell26.grid(row=1, column=5)
    cell31 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 0, GameMode, cell31)], width=15, height=7)
    cell32 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 1, GameMode, cell32)], width=15, height=7)
    cell33 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 2, GameMode, cell33)], width=15, height=7)
    cell34 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 3, GameMode, cell34)], width=15, height=7)
    cell35 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 4, GameMode, cell35)], width=15, height=7)
    cell36 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(2, 5, GameMode, cell36)], width=15, height=7)
    cell31.grid(row=2, column=0)
    cell32.grid(row=2, column=1)
    cell33.grid(row=2, column=2)
    cell34.grid(row=2, column=3)
    cell35.grid(row=2, column=4)
    cell36.grid(row=2, column=5)
    cell41 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 0, GameMode, cell41)], width=15, height=7)
    cell42 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 1, GameMode, cell42)], width=15, height=7)
    cell43 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 2, GameMode, cell43)], width=15, height=7)
    cell44 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 3, GameMode, cell44)], width=15, height=7)
    cell45 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 4, GameMode, cell45)], width=15, height=7)
    cell46 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(3, 5, GameMode, cell46)], width=15, height=7)
    cell41.grid(row=3, column=0)
    cell42.grid(row=3, column=1)
    cell43.grid(row=3, column=2)
    cell44.grid(row=3, column=3)
    cell45.grid(row=3, column=4)
    cell46.grid(row=3, column=5)
    cell51 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 0, GameMode, cell51)], width=15, height=7)
    cell52 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 1, GameMode, cell52)], width=15, height=7)
    cell53 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 2, GameMode, cell53)], width=15, height=7)
    cell54 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 3, GameMode, cell54)], width=15, height=7)
    cell55 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 4, GameMode, cell55)], width=15, height=7)
    cell56 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(4, 5, GameMode, cell56)], width=15, height=7)
    cell51.grid(row=4, column=0)
    cell52.grid(row=4, column=1)
    cell53.grid(row=4, column=2)
    cell54.grid(row=4, column=3)
    cell55.grid(row=4, column=4)
    cell56.grid(row=4, column=5)
    cell61 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 0, GameMode, cell61)], width=15, height=7)
    cell62 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 1, GameMode, cell62)], width=15, height=7)
    cell63 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 2, GameMode, cell63)], width=15, height=7)
    cell64 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 3, GameMode, cell64)], width=15, height=7)
    cell65 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 4, GameMode, cell65)], width=15, height=7)
    cell66 = Button(checkersBoard, command=lambda: [
                    doAppropriateButtonAction(5, 5, GameMode, cell66)], width=15, height=7)
    cell61.grid(row=5, column=0)
    cell62.grid(row=5, column=1)
    cell63.grid(row=5, column=2)
    cell64.grid(row=5, column=3)
    cell65.grid(row=5, column=4)
    cell66.grid(row=5, column=5)


# Creates Pawnchess Game
def create_bauernschachArray_btn():
    Global_Vars.board = Board.create_board_bauernschach()

    # Change Gamemode
    global GameMode
    GameMode = 2

    consoleLog = print(Global_Vars.board)


# Creates Checkers Game
def create_checkersArray_btn():
    Global_Vars.board = Board.create_board_checkers()

    # Change Gamemode
    global GameMode
    GameMode = 3

    myInfo.config(text="Checkers anleitung")

    consoleLog = print(Global_Vars.board)

# Creates TicTacToe Game


def create_tictactoeArray_btn():
    Global_Vars.board = Board.create_board_tictactoe()

    # Change Game Mode
    global GameMode
    GameMode = 1

    # Setting up Globals for TicTacToe
    global LukasTicTacToeBoard
    LukasTicTacToeBoard = createEmptyBoard(6, 6)

    global LukasTurnCount
    LukasTurnCount = 0

    global LukasRunningState
    LukasRunningState = True

    myInfo.config(text="Sie setzen abwechselnd mit dem Computer Ihre Farbe (also Grün) in die freien Kästchen des Spielfelds. Ziel ist es, die eigene Farbe vier Mal in einer Zeile, in einer Spalte oder in einer Diagonale zu platzieren. Wem das zuerst gelingt, hat gewonnen.")

    consoleLog = print(Global_Vars.board)


def openLogIn():
    logwin = Toplevel(root)
    logwin.title("LogIn")
    logwin.geometry("200x80")

    def login_entry_fields():
        print("Username: %s\nPasswort: %s" %
              (userInput.get(), passwortInput.get()))
        username = userInput.get()
        password = passwortInput.get()

        query = main.conn.execute(
            f"select * from player where username='{username}'")
        query_result = query.fetchall()
        print(query_result)

        for row in query_result:
            index = row[1]
            if main.passComparison(username, password):
                print("Authorized!")
            else:
                print("Not Authorized")

        userInput.delete(0, END)
        passwortInput.delete(0, END)
        logwin.quit()

    def registration():
        logwin.geometry("200x100")
        lbl3 = Label(logwin, text="E-Mail")
        lbl3.grid(row=1)
        eMailInput = Entry(logwin)
        eMailInput.grid(row=1, column=1)
        btn1.config(state=DISABLED)
        btn2.config(text="SignUp", command=lambda: reg_entry_fields())

        def reg_entry_fields():
            print("Username: %s\nPasswort: %s\nE-Mail: %s" %
                  (userInput.get(), passwortInput.get(), eMailInput.get()))

            main.insertNewData(
                userInput.get(), passwortInput.get(), eMailInput.get())
            userInput.delete(0, END)
            passwortInput.delete(0, END)
            eMailInput.delete(0, END)
            logwin.quit()

    lbl1 = Label(logwin, text="Username")
    lbl2 = Label(logwin, text="Password")

    lbl1.grid(row=0)
    lbl2.grid(row=2)

    userInput = Entry(logwin)
    passwortInput = Entry(logwin)

    userInput.grid(row=0, column=1)
    passwortInput.grid(row=2, column=1)

    btn1 = Button(logwin, text='LogIn', command=login_entry_fields)
    btn1.grid(row=3, column=0, sticky=W, pady=4)
    btn2 = Button(logwin, text='Registrate', command=registration)
    btn2.grid(row=3, column=1, sticky=W, pady=4)


root = Tk()
infoText = StringVar()
infoText.set('Test')
root.title("Strategie-Spiele-Sammlung")
root.geometry("1250x720")
root.resizable(width=True, height=True)
# root.attributes("-transparentcolor", "green")

myImg = ImageTk.PhotoImage(Image.open("code-editoren-t.jpg"))

listGames = Frame(root, width=300, height=402, padx=5, pady=5, bg="white")
listGames.grid(row=0, rowspan=1, column=0, padx=5)
listGames.pack_propagate(0)

info = LabelFrame(root, width=300, height=243, padx=5, pady=5, bg="yellow")
info.grid(row=1, rowspan=1, column=0, padx=5)
info.grid_propagate(0)

regLog = Button(root, text="Registration / LogIn", command=lambda: openLogIn(),
                width=30, height=2, padx=5, pady=5, state=NORMAL)
regLog.grid(row=2, rowspan=1, column=0, padx=5)

mainDisplay = Frame(root, width=930, height=705, padx=5, pady=5, bg="green")
mainDisplay.grid(row=0, rowspan=3, column=1, columnspan=2, pady=5, padx=5)
mainDisplay.grid_propagate(0)


# Game listing
btn1 = Button(listGames, text="Bauernschach", command=lambda: [create_board(
), create_bauernschachArray_btn()], width=50, height=7, padx=0, pady=0)
btn2 = Button(listGames, text="Dame", command=lambda: [create_board(
), create_checkersArray_btn()], width=50, height=7, padx=0, pady=0)
btn3 = Button(listGames, text="Tic-Tac-Toe", command=lambda: [
              create_board(), create_tictactoeArray_btn()], width=50, height=7, padx=0, pady=0)

btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)


myInfo = Label(info, text="In dieser Spielesammlung können Sie sich mental fordern. Hierfür haben Sie die Möglichkeit zwischen TicTacToe und Bauernschach zu wählen. In diesen Spielen treten Sie gegen unsere selbst programmierte KI an", wraplength=290, bg="white")
myInfo.grid(row=0, column=0)


mainloop()
