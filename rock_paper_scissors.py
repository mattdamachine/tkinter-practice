from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Rock Paper Scissors')

# List of possible Computer Choices
comp_choices = ['Rock', 'Paper', 'Scissors']


# PLay function
def play(hand):
    # Establish the computer's choice
    comp_hand = random.choice(comp_choices)

    # Establish tie scenario
    if hand == comp_hand:
        messagebox.showinfo('Rock Paper Scissors', 'The computer played ' + comp_hand + '\nIt\'s a tie!')
    # Winning scenario
    elif hand == 'Rock' and comp_hand == 'Scissors':
        messagebox.showinfo('Rock Paper Scissors', 'The Computer played ' + comp_hand +
                            '\nYou won!')
    elif hand == 'Paper' and comp_hand == 'Rock':
        messagebox.showinfo('Rock Paper Scissors', 'The Computer played ' + comp_hand +
                            '\nYou won!')
    elif hand == 'Scissors' and comp_hand == 'Paper':
        messagebox.showinfo('Rock Paper Scissors', 'The Computer played ' + comp_hand +
                            '\nYou won!')
    # Losing scenario
    else:
        messagebox.showinfo('Rock Paper Scissors', 'The Computer played ' + comp_hand +
                            '\nYou lost!')

# Create Buttons
rock = Button(root, text='Rock', height=3, width=6, command=lambda: play('Rock'))
paper = Button(root, text='Paper', height=3, width=6, command=lambda: play('Paper'))
scissors = Button(root, text='Scissors', height=3, width=6, command=lambda: play('Scissors'))

rock.grid(row=0, column=0)
paper.grid(row=0, column=1)
scissors.grid(row=0, column=2)

root.mainloop()