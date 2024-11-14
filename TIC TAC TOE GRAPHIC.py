import tkinter as tk
import tkinter.messagebox as tkm


game = tk.Tk()
game.title('Tic Tac Toe')
game.geometry("600x600")
game.resizable(False,False)


#Area
area = []
turn = 1
print(f"Make a move O")
def click(button):
    global turn
    print(turn)
    if turn%2 == 0:
        turn_char='X'
    else:
        turn_char = '0'
    print(f"Make a move {turn_char}") 
    if button["text"] is "":
        button["text"] = turn_char
        turn+=1
        if winner() == "X":
            tkm.showinfo(title="Winner", message="The winner are Х") 
            print("The winner is X.")
            new_game()
        if winner() == "0":
            print("The winner is 0.")
            new_game()
        if winner() == "" and turn == 10:
            print("Its a tie!")
            new_game()
        
def new_game():

    global area, turn

    turn = 1

    for x in range(3):

        for y in range(3):

            area[x][y]["text"] = ""



#Check Winner
def winner():
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":
        return "0"
    if area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":
        return "0"
    if area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    if area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    return ""


for i in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(game,text = '', width=26, height=12)
        area[i].append(button)
        area[i][y].place(x=i*200, y=y*200)
        area[i][y]["command"] = lambda selbtn = button: click(selbtn)
    


print(area)







































game.mainloop()