from tkinter import *
import tkinter.messagebox
import random
tk=Tk()
tk.title("Tic Tac Toe")
 
bclick = True
answers = [[0, 4, 8],[2, 4, 6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
choices = set([0,1,2,3,4,5,6,7,8])
mov = [0,2,6,8]
other = [1,3,5,7]
P1 = set([])
com = set([])
button_list = [" "," "," "," "," "," "," "," "," ",]

""" makes a set of 9 buttons for user to input move """
def make_button(n, row, col):
    button_list[n] = Button(tk,text=" ",bg='gray',fg='white',height=4,width=8,command=lambda:ttt(bclick, P1, n))
    button_list[n].grid(row=row,column=col, sticky=S+N+E+W)

a = 0
B = [0,0,0,1,1,1,2,2,2]
C = [0,1,2,0,1,2,0,1,2]
while a != 9:
    b=B[a]
    c=C[a]
    make_button(a, b, c)
    a+=1

""" Function which takes the button pressed and checks its valid before marking X """
def ttt(bclick, P1, n):
     if n not in P1 and n not in com and bclick == True:
         P1.add(n)
         button_list[n]["text"] = "X"
         bclick = False
         print(P1)
         check_move(bclick, P1, n)

""" computers move does checks to see player can win first then does corner move then middle then sides """
def com_move(bclick, P1, n):
        for i in range(8):
            if (((answers[i][0] in P1) and (answers[i][1] in P1)) or ((answers[i][1] in P1) and (answers[i][2] in P1)) or ((answers[i][0] in P1) and (answers[i][2] in P1))):
                for j in range(3):
                    if answers[i][j-1] not in com and answers [1][j-1] not in P1:
                        n = answers[i][j-1]

        if n in P1:
            i = 0
            while i < len(mov):
                if mov[i] in P1 or mov[i] in com:
                    mov.remove(mov[i]) #removes played moves from list of moves
                    i-=1 #sets index back one in response to shortened list length
                i+=1
            if len(mov) != 0:
                n = mov[random.randint(0,len(mov)-1)]
            if len(mov) == 0 and 4 not in P1 and 4 not in com:
                n = 4
            elif len(mov) == 0:
                n = other[random.randint(0,3)]
                if n in P1:
                    com_move(bclick, P1, n)
        print(n)
        button_list[n]["text"] = "O"
        com.add(n)
        bclick = True
        check_move(bclick, P1, n)

""" checks who wins using sets of winning button combos """
def check_move(bclick, P1, n):
    end = False #will be set to true once winner/tie
    for i in range(8):
        if ((answers[i][0] in P1) and (answers[i][1] in P1) and (answers[i][2] in P1)) or ((answers[i][0] in com) and (answers[i][1] in com) and (answers[i][2] in com)):
            if bclick == False:
                end = True
                tkinter.messagebox.showinfo("Player x", "You win")
            else:
                end = True
                tkinter.messagebox.showinfo("computer", "Computer wins")
    if len(P1) == 5 and end != True:
        tkinter.messagebox.showinfo("Player x", "It's a tie")
        end = True
    if bclick == False and end == False:
                com_move(bclick, P1, n)
    elif end == False:
                ttt(bclick, P1, n)
    
    

