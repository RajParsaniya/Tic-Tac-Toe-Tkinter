from tkinter import *
from tkinter import messagebox
import webbrowser


root = Tk()
root.title("Tic Tac Toe - Raj Parsaniya")
#root.geometry("800x600")


# X starts so true
clicked = True
count = 0


def visitWebsite():
    url = 'https://rajparsaniya.000webhostapp.com/'
    webbrowser.open_new_tab(url)
    root.destroy()


def disableButtons():
    Button1.config(state=DISABLED)
    Button2.config(state=DISABLED)
    Button3.config(state=DISABLED)

    Button4.config(state=DISABLED)
    Button5.config(state=DISABLED)
    Button6.config(state=DISABLED)

    Button7.config(state=DISABLED)
    Button8.config(state=DISABLED)
    Button9.config(state=DISABLED)


def someoneWon():
    global winner
    winner = False

    #Check for X
    if Button1["text"] == "X" and Button2["text"] == "X" and Button3["text"] == "X":
        Button1.config(bg="#008000")
        Button2.config(bg="#008000")
        Button3.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button4["text"] == "X" and Button5["text"] == "X" and Button6["text"] == "X":
        Button4.config(bg="#008000")
        Button5.config(bg="#008000")
        Button6.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button7["text"] == "X" and Button8["text"] == "X" and Button9["text"] == "X":
        Button7.config(bg="#008000")
        Button8.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()
        
    elif Button1["text"] == "X" and Button4["text"] == "X" and Button7["text"] == "X":
        Button1.config(bg="#008000")
        Button4.config(bg="#008000")
        Button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button2["text"] == "X" and Button5["text"] == "X" and Button8["text"] == "X":
        Button2.config(bg="#008000")
        Button5.config(bg="#008000")
        Button8.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button3["text"] == "X" and Button6["text"] == "X" and Button9["text"] == "X":
        Button3.config(bg="#008000")
        Button6.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button1["text"] == "X" and Button5["text"] == "X" and Button9["text"] == "X":
        Button1.config(bg="#008000")
        Button5.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    elif Button3["text"] == "X" and Button5["text"] == "X" and Button7["text"] == "X":
        Button3.config(bg="#008000")
        Button5.config(bg="#008000")
        Button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n X Win...")
        disableButtons()

    #Check for O
    elif Button1["text"] == "O" and Button2["text"] == "O" and Button3["text"] == "O":
        Button1.config(bg="#008000")
        Button2.config(bg="#008000")
        Button3.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button4["text"] == "O" and Button5["text"] == "O" and Button6["text"] == "O":
        Button4.config(bg="#008000")
        Button5.config(bg="#008000")
        Button6.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button7["text"] == "O" and Button8["text"] == "O" and Button9["text"] == "O":
        Button7.config(bg="#008000")
        Button8.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()
        
    elif Button1["text"] == "O" and Button4["text"] == "O" and Button7["text"] == "O":
        Button1.config(bg="#008000")
        Button4.config(bg="#008000")
        Button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button2["text"] == "O" and Button5["text"] == "O" and Button8["text"] == "O":
        Button2.config(bg="#008000")
        Button5.config(bg="#008000")
        Button8.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button3["text"] == "O" and Button6["text"] == "O" and Button9["text"] == "O":
        Button3.config(bg="#008000")
        Button6.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button1["text"] == "O" and Button5["text"] == "O" and Button9["text"] == "O":
        Button1.config(bg="#008000")
        Button5.config(bg="#008000")
        Button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()

    elif Button3["text"] == "O" and Button5["text"] == "O" and Button7["text"] == "O":
        Button3.config(bg="#008000")
        Button5.config(bg="#008000")
        Button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe"," Congratulations !!! \n O Win...")
        disableButtons()


    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe"," Ohh It's A Tie !!! \n No One Wins...")
        disableButtons()



def buttonClick(b):

    global clicked, count
    
    #lable.config(text="X")
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        someoneWon()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        someoneWon()

    else:
        messagebox.showerror("Tic Tac Toe"," That box has already been selected \n Please pick another one...")


def reset():

    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9
    global clicked, count

    clicked = True
    count = 0
    
    #Button
    Button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button1)  )
    Button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button2)  )
    Button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button3)  )

    Button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button4)  )
    Button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button5)  )
    Button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button6)  )

    Button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button7)  )
    Button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button8)  )
    Button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3", command=lambda: buttonClick(Button9)  )

    #Grid This 9 Buttons
    Button1.grid(row=0, column=0)
    Button2.grid(row=0, column=1)
    Button3.grid(row=0, column=2)

    Button4.grid(row=1, column=0)
    Button5.grid(row=1, column=1)
    Button6.grid(row=1, column=2)

    Button7.grid(row=2, column=0)
    Button8.grid(row=2, column=1)
    Button9.grid(row=2, column=2)


#Create Menu
MyCustomMenu = Menu(root)
root.config(menu=MyCustomMenu)

#Create options menu
OptionsMenu = Menu(MyCustomMenu, tearoff= False)
MyCustomMenu.add_cascade(label="Options", menu=OptionsMenu)
OptionsMenu.add_command(label="Reset Game", command=reset)
OptionsMenu.add_command(label="About Developer", command=visitWebsite)


reset()

root.mainloop()
