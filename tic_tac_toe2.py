from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

# Create the possible winning scenarios (list of lists)
win_scenarios = [[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [1,4,7],
                 [2,5,8],
                 [3,6,9],
                 [1,5,9],
                 [3,5,7]]


# Disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check to see if someone won
def checktowin():
    global winner
    winner = False

    # Check for X win
    for scenario in win_scenarios:
        win_counter = 0
        for num in x_moves:
            if num in scenario:
                win_counter += 1
        if win_counter == 3:
            winner = True
            messagebox.showinfo('Tic Tac Toe', 'X wins!')
            disable_all_buttons()

    # Check for O Win
    for scenario in win_scenarios:
        win_counter = 0
        for num in o_moves:
            if num in scenario:
                win_counter += 1
        if win_counter == 3:
            winner = True
            messagebox.showinfo('Tic Tac Toe', 'O wins!')
            disable_all_buttons()

    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo('Tie Tac Toe', 'It\'s a tie!')
        disable_all_buttons()


# Button click function
def b_click(b, move):
    global clicked, count

    # If the square is empty and it's X's turn
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        x_moves.append(move)
        checktowin()
    # Else if the square is empty and it's O's turn
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        o_moves.append(move)
        checktowin()
    # Else the box has already been played
    else:
        messagebox.showerror('Tic Tac Toe', 'That box has already been selected \n'
                                            'Pick another box')

# Start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    global x_moves, o_moves

    clicked = True  # Keep track of who's turn it is
    count = 0  # Count until we get to the max # of moves (9)
    # Create our lists to keep track of current plays
    x_moves = []
    o_moves = []

    # Build our buttons
    b1 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b1,1))
    b2 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b2,2))
    b3 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b3,3))

    b4 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b4,4))
    b5 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b5,5))
    b6 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b6,6))

    b7 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b7,7))
    b8 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b8,8))
    b9 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='white', command=lambda: b_click(b9,9))

    # Grid our buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset Game', command=reset)

reset()
root.mainloop()