import Board
import Global_Vars
from tkinter import *
from PIL import ImageTk, Image



def create_board ():
    checkersBoard = Frame(mainDisplay, width=690, height=695, bg="white")
    checkersBoard.grid(row=0, rowspan=1, column=1, columnspan=1)
    checkersBoard.grid_propagate(0)
    cell11 = Button(checkersBoard, width=15, height=7)
    cell12 = Button(checkersBoard, width=15, height=7)
    cell13 = Button(checkersBoard, width=15, height=7)
    cell14 = Button(checkersBoard, width=15, height=7)
    cell15 = Button(checkersBoard, width=15, height=7)
    cell16 = Button(checkersBoard, width=15, height=7)
    cell11.grid(row=0, column=0)
    cell12.grid(row=0, column=1)
    cell13.grid(row=0, column=2)
    cell14.grid(row=0, column=3)
    cell15.grid(row=0, column=4)
    cell16.grid(row=0, column=5)
    cell21 = Button(checkersBoard, width=15, height=7)
    cell22 = Button(checkersBoard, width=15, height=7)
    cell23 = Button(checkersBoard, width=15, height=7)
    cell24 = Button(checkersBoard, width=15, height=7)
    cell25 = Button(checkersBoard, width=15, height=7)
    cell26 = Button(checkersBoard, width=15, height=7)
    cell21.grid(row=1, column=0)
    cell22.grid(row=1, column=1)
    cell23.grid(row=1, column=2)
    cell24.grid(row=1, column=3)
    cell25.grid(row=1, column=4)
    cell26.grid(row=1, column=5)
    cell31 = Button(checkersBoard, width=15, height=7)
    cell32 = Button(checkersBoard, width=15, height=7)
    cell33 = Button(checkersBoard, width=15, height=7)
    cell34 = Button(checkersBoard, width=15, height=7)
    cell35 = Button(checkersBoard, width=15, height=7)
    cell36 = Button(checkersBoard, width=15, height=7)
    cell31.grid(row=2, column=0)
    cell32.grid(row=2, column=1)
    cell33.grid(row=2, column=2)
    cell34.grid(row=2, column=3)
    cell35.grid(row=2, column=4)
    cell36.grid(row=2, column=5)
    cell41 = Button(checkersBoard, width=15, height=7)
    cell42 = Button(checkersBoard, width=15, height=7)
    cell43 = Button(checkersBoard, width=15, height=7)
    cell44 = Button(checkersBoard, width=15, height=7)
    cell45 = Button(checkersBoard, width=15, height=7)
    cell46 = Button(checkersBoard, width=15, height=7)
    cell41.grid(row=3, column=0)
    cell42.grid(row=3, column=1)
    cell43.grid(row=3, column=2)
    cell44.grid(row=3, column=3)
    cell45.grid(row=3, column=4)
    cell46.grid(row=3, column=5)
    cell51 = Button(checkersBoard, width=15, height=7)
    cell52 = Button(checkersBoard, width=15, height=7)
    cell53 = Button(checkersBoard, width=15, height=7)
    cell54 = Button(checkersBoard, width=15, height=7)
    cell55 = Button(checkersBoard, width=15, height=7)
    cell56 = Button(checkersBoard, width=15, height=7)
    cell51.grid(row=4, column=0)
    cell52.grid(row=4, column=1)
    cell53.grid(row=4, column=2)
    cell54.grid(row=4, column=3)
    cell55.grid(row=4, column=4)
    cell56.grid(row=4, column=5)
    cell61 = Button(checkersBoard, width=15, height=7)
    cell62 = Button(checkersBoard, width=15, height=7)
    cell63 = Button(checkersBoard, width=15, height=7)
    cell64 = Button(checkersBoard, width=15, height=7)
    cell65 = Button(checkersBoard, width=15, height=7)
    cell66 = Button(checkersBoard, width=15, height=7)
    cell61.grid(row=5, column=0)
    cell62.grid(row=5, column=1)
    cell63.grid(row=5, column=2)
    cell64.grid(row=5, column=3)
    cell65.grid(row=5, column=4)
    cell66.grid(row=5, column=5)



def create_bauernschachArray_btn ():
    Global_Vars.board = Board.create_board_bauernschach()
    consoleLog = print(Global_Vars.board)

def create_checkersArray_btn ():
    Global_Vars.board = Board.create_board_checkers()
    consoleLog = print(Global_Vars.board)

def create_tictactoeArray_btn ():
    Global_Vars.board = Board.create_board_tictactoe()
    consoleLog = print(Global_Vars.board)




root = Tk()
root.title("Strategie-Spiele-Sammlung")
root.geometry("1250x720")
root.resizable(width=True, height=True)
# root.attributes("-transparentcolor", "green")

myImg = ImageTk.PhotoImage(Image.open("code-editoren-t.jpg"))

listGames = Frame(root, width=300, height=402, padx=5, pady=5, bg="white")
listGames.grid(row=0, rowspan=1, column=0, padx=5)
listGames.pack_propagate(0)

info = LabelFrame(root, width=300, height=293, padx=5, pady=5, bg="yellow")
info.grid(row=1, rowspan=1, column=0, padx=5)
info.pack_propagate(0)


mainDisplay = Frame(root, width=930, height=705, padx=5, pady=5, bg="green")
mainDisplay.grid(row=0, rowspan=2, column=1, columnspan=2, pady=5, padx=5)
mainDisplay.grid_propagate(0)


#Game listing
btn1 = Button(listGames, text="Bauernschach", command=lambda:[create_board(), create_bauernschachArray_btn()],width=50, height=7, padx=0, pady=0)
btn2 = Button(listGames, text="Dame", command=lambda:[create_board(), create_checkersArray_btn()], width=50, height=7, padx=0, pady=0)
btn3 = Button(listGames, text="Tic-Tac-Toe", command=lambda:[create_board(), create_tictactoeArray_btn()], width=50, height=7, padx=0, pady=0)

btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)

myInfo = Label(info, text="test 1213", wraplength=290, bg="white")
myInfo.pack()
#Info Box
# myInfo = Label(info, text=test2, wraplength=290, bg="white")

root.mainloop()


