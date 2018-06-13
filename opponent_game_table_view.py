import tkinter
import time
from tkinter import *
import random
from message_box import MessageBox

class OpponentGameTableView:
    def __init__(self, game, size, gametableview):#onclick):
        #self.img = tkinter.PhotoImage(file="images/empty.png")
        self.game = game
        self.GameTableView = gametableview #wywolanie klasy wczesniejszej podanej przez parametr gametableview
        #przez referencje
        self.window = tkinter.Tk()
        self.window.title('Tablica przeciwnika')
        self.window.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
        self.window.geometry('{}x{}+950+150'.format(800, 700))
        self.direction = 'horizontal'
        self.playerField = [['0'] * size for x in range(size)]
        for x in range(size):
            for y in range(size):
                print(self.playerField[x][y], end='')
            print('')
        self.battleshipSize = [4,3,3,2,2,2,1,1,1,1]
        self.battleshipCounter = 0
        self.wrapperframe = tkinter.Frame(self.window)
        self.wrapperframe.grid()
        self.formframe = tkinter.Frame(self.wrapperframe)
        self.formframe.grid(row=0, column=11)
        self.buttonsFrame = tkinter.Frame(self.wrapperframe)
        self.buttonsFrame.grid(row=0, column=0)
        self.buttons = [[tkinter.Button(self.buttonsFrame, width=4, height=4, bg='deep sky blue', command = lambda x=x,y=y:self.movement(x,y))
                         for y in range(size)] for x in range(size)]
        for x in range(size):
            for y in range(size):
                self.buttons[x][y].grid(column=x, row=y)

        self.label = Label(self.formframe, text = 'Twój ruch', font=("Helvetica", 15))
        self.label.grid(row=0, column=0, ipadx=50, sticky=E+W+S+N)
        self.label2 = Label(self.formframe, text = '', font=("Helvetica", 15))
        self.label2.grid(row=1, column=0, sticky=N)

        while self.battleshipCounter < 10:
            tmp = False
            self.rand_direction = random.randint(1,2)
            self.rand_x = random.randint(0,9)
            self.rand_y = random.randint(0,9)
            if (self.rand_direction == 1):
                #horizontal
                if self.checkShips(self.rand_x, self.rand_y, 1): #true
                    for a in range(self.rand_y-1, self.rand_y+2):
                        for b in range(self.rand_x-1, self.rand_x+self.battleshipSize[self.battleshipCounter]+1):
                            if a > -1 and b > -1 and a < 10 and b < 10:
                                self.playerField[a][b] = 'W' #woda wokol statku
                    for z in range(self.rand_x, self.rand_x+self.battleshipSize[self.battleshipCounter]):
                        if self.battleshipCounter == 0:
                            self.playerField[self.rand_y][z] = 'A'
                            #print(self.battleshipCounter,' - ','X = ', self.rand_x, ' Y = ', self.rand_y, '\n')
                        elif self.battleshipCounter == 1:
                            self.playerField[self.rand_y][z] = 'B' #pierwszy 3masztowiec
                        elif self.battleshipCounter == 2:
                            self.playerField[self.rand_y][z] = 'C' #drugi 3masztowiec
                        elif self.battleshipCounter == 3:
                            self.playerField[self.rand_y][z] = 'D' #pierwszy 2masztowiec
                        elif self.battleshipCounter == 4:
                            self.playerField[self.rand_y][z] = 'E'
                        elif self.battleshipCounter == 5:
                            self.playerField[self.rand_y][z] = 'F'  #trzeci 2masztowiec
                        else:
                            self.playerField[self.rand_y][z] = 'G' #wszystkie 1masztowce
                        #self.buttons[z][self.rand_y].config(bg="orchid")
                    tmp = True
            else:
                #vertical
                if self.checkShips(self.rand_x, self.rand_y, 2): #true
                    for a in range(self.rand_y-1, self.rand_y+self.battleshipSize[self.battleshipCounter]+1):
                        for b in range(self.rand_x-1, self.rand_x+2):
                            if a > -1 and b > -1 and a < 10 and b < 10:
                                self.playerField[a][b] = 'W' #woda wokol statku
                    for z in range(self.rand_y, self.rand_y+self.battleshipSize[self.battleshipCounter]):
                        if self.battleshipCounter == 0:
                            self.playerField[z][self.rand_x] = 'A'
                            #print(self.battleshipCounter,' - ','X = ', self.rand_x, ' Y = ', self.rand_y, '\n')
                        elif self.battleshipCounter == 1:
                            self.playerField[z][self.rand_x] = 'B' #pierwszy 3masztowiec
                        elif self.battleshipCounter == 2:
                            self.playerField[z][self.rand_x] = 'C'
                        elif self.battleshipCounter == 3:
                            self.playerField[z][self.rand_x] = 'D'
                        elif self.battleshipCounter == 4:
                            self.playerField[z][self.rand_x] = 'E'
                        elif self.battleshipCounter == 5:
                            self.playerField[z][self.rand_x] = 'F'
                        else:
                            self.playerField[z][self.rand_x] = 'G' #wszystkie 1masztowce
                        #self.buttons[self.rand_x][z].config(bg="orchid")
                    tmp = True

            for x in range(10):
                for y in range(10):
                    print(self.playerField[x][y], end='')
                print('')

            if (self.battleshipCounter == 9 and tmp == True):
                break
            elif (self.battleshipCounter !=9 and tmp == True):
                self.battleshipCounter += 1

        self.start_game()


    def checkShips(self, x, y, dir):
        if dir == 1:
            if x+self.battleshipSize[self.battleshipCounter] < 11: #lewy górny róg
                for a in range(y-1,y+2):
                    for b in range(x-1, x+self.battleshipSize[self.battleshipCounter]+1):
                        if a > -1 and b > -1 and a < 10 and b < 10:
                            if self.playerField[a][b] == 'A' or self.playerField[a][b] == 'B' or self.playerField[a][b] == 'C'\
                                    or self.playerField[a][b] == 'D' or self.playerField[a][b] == 'E' or self.playerField[a][b] == 'F'\
                                    or self.playerField[a][b] == 'G':
                                return False
                return True
            return False
        elif dir == 2:
            if y+self.battleshipSize[self.battleshipCounter] < 11: #lewy górny róg
                for a in range(y-1, y+self.battleshipSize[self.battleshipCounter]+1):
                    for b in range(x-1,x+2):
                        if a > -1 and b > -1 and a < 10 and b < 10:
                            if self.playerField[a][b] == 'A' or self.playerField[a][b] == 'B' or self.playerField[a][b] == 'C' \
                                    or self.playerField[a][b] == 'D' or self.playerField[a][b] == 'E' or self.playerField[a][b] == 'F' \
                                    or self.playerField[a][b] == 'G':
                                return False
                return True
            return False

    def start_game(self):
        start_game_info = MessageBox(self.game)
        start_game_info.startgame()
        self.usercounter_ships = 20  #ilosc wszystkich kafelek na statki
        self.compcounter_ships = 20
        #counter do zliczania strzalow by zatopic konkretny statek
        self.fourcounter = 0
        self.threecounter_o = 0
        self.threecounter_t = 0
        self.twocounter_o = 0
        self.twocounter_t = 0
        self.twocounter_th = 0
        self.shot = True #flaga strzalu komputera
        self.Xright = True
        self.Xleft = False
        self.Yup = False
        self.Ydown = False
        self.s = 0
        self.dx = 0
        self.dy = 0

        #self.GameTableView.buttons[2][2].config(bg='yellow')
        #self.buttons[2][2].config(bg='yellow')

    def movement(self, i, j):

        if (self.playerField[j][i] != 'W' and self.playerField[j][i] != '0'):
            self.buttons[i][j].config(bg='red')
            self.buttons[i][j].config(state='disabled')
            self.compcounter_ships -= 1
        #sprawdzenie czy statek jest zatopiony, nie moze byc
            if self.destroyed_enemyShips(i ,j) == True:
                self.label2.config(text = 'Trafiony zatopiony')
            else:
                self.label2.config(text = 'Trafiony')
            self.playerField[j][i] = 'X'
        else:
            self.buttons[i][j].config(bg='blue')
            self.buttons[i][j].config(state='disabled')
            self.label2.config(text='Pudło')

        for x in range(10):
            for y in range(10):
                print(self.playerField[x][y], end='')
            print('')
        print('\n')

        if self.shot == True:
            self.rand_x = random.randint(0,9)
            self.rand_y = random.randint(0,9)
        if (self.GameTableView.playerField[self.rand_y][self.rand_x] == 'X' or self.GameTableView.playerField[self.rand_y][self.rand_x] == 'U') and self.shot == True:
            tmp = True
            while tmp == True:
                self.rand_x = random.randint(0,9)
                self.rand_y = random.randint(0,9)
                if (self.GameTableView.playerField[self.rand_y][self.rand_x] != 'X' and self.GameTableView.playerField[self.rand_y][self.rand_x] !='U'):
                    tmp = False

        if (self.GameTableView.playerField[self.rand_y][self.rand_x] != 'W' and self.GameTableView.playerField[self.rand_y][self.rand_x] != '0' and self.GameTableView.playerField[self.rand_y][self.rand_x] !='U'):
            self.GameTableView.buttons[self.rand_x][self.rand_y].config(bg = 'red')
            self.usercounter_ships -=1
            if self.destroyed_myShips(self.rand_x, self.rand_y) == True:
                self.GameTableView.label2.config(text='Trafiony zatopiony !!!')
                self.shot = True
                self.Xright = True
                self.Xleft = False
                self.Yup = False
                self.Ydown = False
                self.GameTableView.playerField[self.rand_y][self.rand_x] = 'X'
                #jesli vertical to caly statek dookola oznaczam litera U tak jak przy nietrafieniu, aby losowe strzaly nie obejmowaly wiadomych miejsc gdzie nie moze byc statku.

                try:
                    if (self.GameTableView.playerField[self.dy+1][self.dx] =='X'):
                        for a in range(self.dy-1, self.dy + self.s+1):
                            for b in range(self.dx-1, self.dx+2):
                                if a > -1 and b > -1 and a < 10 and b < 10:
                                    self.GameTableView.playerField[a][b] = 'U'
                    elif (self.GameTableView.playerField[self.dy][self.dx+1] == 'X'):
                        for a in range(self.dy-1, self.dy+2):
                            for b in range(self.dx-1, self.dx + self.s+1):
                                if a > -1 and b > -1 and a < 10 and b < 10:
                                    self.GameTableView.playerField[a][b] = 'U'
                    #jesli to byl jednomasztowiec
                    else:
                        for a in range(self.rand_y-1, self.rand_y+2):
                            for b in range(self.rand_x-1, self.rand_x+2):
                                if a > -1 and b > -1 and a < 10 and b < 10:
                                    self.GameTableView.playerField[a][b] = 'U'
                except IndexError:
                    pass

            else:
                self.GameTableView.label2.config(text="Trafiony")
                self.shot = False
                self.GameTableView.playerField[self.rand_y][self.rand_x] = 'X'

                if self.rand_x < 9 and self.Xright == True:
                    if self.GameTableView.playerField[self.rand_y][self.rand_x+1] !='U':
                        self.rand_x = self.rand_x+1
                        self.Xright = True
                    elif self.GameTableView.playerField[self.rand_y][self.rand_x+1] == 'U':
                        self.Xright = False
                        if self.rand_x == 0:
                            self.Xleft = False
                            if self.GameTableView.playerField[self.rand_y+1][self.rand_x] !='U' and self.rand_y<9:
                                self.Yup = True
                                self.rand_y = self.rand_y + 1
                            elif self.GameTableView.playerField[self.rand_y+1][self.rand_x] == 'U' or self.rand_y == 9:
                                self.Yup = False
                                self.Ydown = True
                                self.rand_y = self.rand_y - 1
                        elif self.GameTableView.playerField[self.rand_y][self.rand_x-1] !='U' and self.GameTableView.playerField[self.rand_y][self.rand_x-1] !='X':
                            self.Xleft = True
                            self.rand_x = self.rand_x-1
                        elif self.GameTableView.playerField[self.rand_y][self.rand_x-2] != 'U' and self.GameTableView.playerField[self.rand_y][self.rand_x-2] !='X' and self.GameTableView.playerField[self.rand_y][self.rand_x-1] == 'X':
                            self.Xleft = True
                            self.rand_x = self.rand_x-2
                        elif self.GameTableView.playerField[self.rand_y][self.rand_x-3] != 'U' and self.GameTableView.playerField[self.rand_y][self.rand_x-3] !='X' and self.GameTableView.playerField[self.rand_y][self.rand_x-1] == 'X' and self.GameTableView.playerField[self.rand_y][self.rand_x-2] == 'X':
                            self.Xleft = True
                            self.rand_x = self.rand_x-3
                        elif self.GameTableView.playerField[self.rand_y][self.rand_x-1] == 'U':
                            self.Xleft = False
                            if self.rand_y == 9:
                                self.Yup = False
                                self.Ydown = True
                                self.rand_y = self.rand_y -1
                            elif self.GameTableView.playerField[self.rand_y+1][self.rand_x] == 'U':
                                self.Yup = False
                                self.Ydown = True
                                self.rand_y = self.rand_y - 1
                            elif self.GameTableView.playerField[self.rand_y+1][self.rand_x] != 'U':
                                self.Yup = True
                                self.Ydown = False
                                self.rand_y = self.rand_y + 1

                elif self.rand_x == 9 and self.Xright == True:
                    if self.GameTableView.playerField[self.rand_y][self.rand_x-2] !='X' and self.GameTableView.playerField[self.rand_y][self.rand_x-1] =='X' :
                        self.rand_x = self.rand_x-2
                        self.Xright = False
                        self.Xleft = True
                    elif self.GameTableView.playerField[self.rand_y][self.rand_x-3] !='X' and self.GameTableView.playerField[self.rand_y][self.rand_x-2] =='X' :
                        self.rand_x = self.rand_x-3
                        self.Xright = False
                        self.Xleft = True
                    elif self.GameTableView.playerField[self.rand_y][self.rand_x-1] != 'U':
                        self.Xright = False
                        self.Xleft = True
                        self.rand_x = self.rand_x -1

                    elif self.rand_y < 9:
                        if self.GameTableView.playerField[self.rand_y+1][self.rand_x] !='U':
                            self.rand_y = self.rand_y+1
                            self.Xright= False
                            self.Xleft = False
                            self.Yup = True
                        else:
                            self.rand_y = self.rand_y - 1
                            self.Xright = False
                            self.Xleft = False
                            self.Yup = False
                            self.Ydown = True
                    elif self.rand_y == 9:
                        self.rand_y = self.rand_y - 1
                        self.Xright = False
                        self.Xleft = False
                        self.Ydown = True
                        self.Yup = False

                elif self.rand_x > 0 and self.Xleft == True:
                    if self.GameTableView.playerField[self.rand_y][self.rand_x-1] !='U':
                        self.rand_x = self.rand_x-1
                        self.Xleft = True
                    else:
                        self.Xleft = False
                        self.Yup = True
                elif self.rand_x == 0 and self.Xleft == True:
                    if self.GameTableView.playerField[self.rand_y+1][self.rand_x] !='U' and self.rand_y<9:
                        self.Xleft = False
                        self.Yup = True
                    elif self.GameTableView.playerField[self.rand_y+1][self.rand_x] == 'U' or self.rand_y == 9:
                        self.Yup = False
                        self.Ydown = True

                elif self.rand_y < 9 and self.Yup == True:
                    if self.GameTableView.playerField[self.rand_y+1][self.rand_x] !='U':
                        self.rand_y = self.rand_y + 1
                        self.Yup = True
                    else:
                        self.Yup = False
                        self.Ydown = True
                        if self.GameTableView.playerField[self.rand_y-2][self.rand_x] == 'X':
                            if self.GameTableView.playerField[self.rand_y-3][self.rand_x] != 'X':
                                self.rand_y = self.rand_y - 3
                        elif self.GameTableView.playerField[self.rand_y-2][self.rand_x] !='X':
                            self.rand_y = self.rand_y - 2
                elif self.rand_y == 9 and self.Yup == True:
                    self.Yup = False
                    self.Ydown = True
                    if self.GameTableView.playerField[self.rand_y-1][self.rand_x] !='X':
                        self.rand_y = self.rand_y-1
                    elif self.GameTableView.playerField[self.rand_y-2][self.rand_x] !='X':
                        self.rand_y = self.rand_y-2
                    elif self.GameTableView.playerField[self.rand_y-3][self.rand_x] !='X':
                        self.rand_y = self.rand_y-3
                elif self.rand_y > 0 and self.Ydown == True:
                    self.rand_y = self.rand_y -1
                    self.Ydown = True
        else:
            self.GameTableView.buttons[self.rand_x][self.rand_y].config(bg='blue')
            self.GameTableView.label2.config(text='Pudło')
            self.GameTableView.playerField[self.rand_y][self.rand_x] = 'U'

            if self.shot == False and self.Xright == True:
                self.Xright = False
                if self.rand_x >1 and self.GameTableView.playerField[self.rand_y][self.rand_x-2] != 'X' and self.GameTableView.playerField[self.rand_y][self.rand_x-2]!='U':
                    self.rand_x = self.rand_x - 2
                    self.Xleft = True
                elif self.rand_x == 1:
                    self.Xleft = False
                    self.rand_x = self.rand_x -1
                    if self.rand_y <9 and self.GameTableView.playerField[self.rand_y+1][self.rand_x] != 'U':
                        self.Yup = True
                        self.rand_y = self.rand_y+1
                    else:
                        self.rand_y = self.rand_y - 1
                        self.Ydown = True
                elif self.GameTableView.playerField[self.rand_y][self.rand_x-2] =='U':
                    self.Xleft = False
                    self.rand_x = self.rand_x-1
                    if self.rand_y == 9:
                        self.Yup = False
                        self.Ydown = True
                        self.rand_y = self.rand_y-1
                    elif self.GameTableView.playerField[self.rand_y+1][self.rand_x] != 'U' and self.rand_y<9:
                        self.rand_y = self.rand_y+1
                        self.rand_x = self.rand_x
                        self.Yup = True

                elif self.GameTableView.playerField[self.rand_y][self.rand_x-3] != 'X' :
                    self.rand_x = self.rand_x - 3
                    self.Xleft = True
                elif self.GameTableView.playerField[self.rand_y][self.rand_x-4] != 'X':
                    self.rand_x = self.rand_x - 4
                    self.Xleft = True

            elif self.shot == False and self.Xleft == True:
                if self.rand_y <9 and self.GameTableView.playerField[self.rand_y+1][self.rand_x+1] !='U':
                    self.rand_x = self.rand_x+1
                    self.rand_y = self.rand_y+1
                    self.Xleft = False
                    self.Yup = True
                elif self.rand_y == 9:
                    self.rand_x = self.rand_x+1
                    self.rand_y = self.rand_y-1
                    self.Xleft = False
                    self.Yup = False
                    self.Ydown = True
                elif self.GameTableView.playerField[self.rand_y+1][self.rand_x+1] == 'U':
                    self.rand_x = self.rand_x+1
                    self.rand_y = self.rand_y-1
                    self.Xleft = False
                    self.Yup = False
                    self.Ydown = True

            elif self.shot == False and self.Yup == True:
                if self.GameTableView.playerField[self.rand_y-2][self.rand_x] != 'X':
                    self.rand_y = self.rand_y - 2
                    self.rand_x = self.rand_x
                    self.Yup = False
                    self.Ydown = True
                elif self.GameTableView.playerField[self.rand_y-3][self.rand_x] != 'X':
                    self.rand_y = self.rand_y - 3
                    self.rand_x = self.rand_x
                    self.Yup = False
                    self.Ydown = True
                elif self.GameTableView.playerField[self.rand_y-4][self.rand_x] != 'X':
                    self.rand_y = self.rand_y - 4
                    self.rand_x = self.rand_x
                    self.Yup = False
                    self.Ydown = True

            elif self.shot == False and self.Ydown == True:
                if self.GameTableView.playerField[self.rand_y+2][self.rand_x] != 'X':
                    self.rand_y = self.rand_y + 2
                    self.Ydown = False
                elif self.GameTableView.playerField[self.rand_y+3][self.rand_x] != 'X':
                    self.rand_y = self.rand_y + 3
                    self.Ydown = False
                elif self.GameTableView.playerField[self.rand_y+4][self.rand_x] != 'X':
                    self.rand_y = self.rand_y + 4
                    self.Ydown = False


        for t in range(10):
            for r in range(10):
                print(self.GameTableView.playerField[t][r], end='')
            print('')
        print('\n')

        if self.compcounter_ships == 0:
            won = MessageBox(self.game)
            won.win()
            for a in range(10):
                for b in range(10):
                    self.buttons[a][b].config(state = 'disabled')
            self.reset_button = tkinter.Button(self.formframe, height=3, width=10, text = 'Zagraj ponownie', command = self.reset_game)
            self.reset_button.grid(pady = 6)
            self.endgame_button = tkinter.Button(self.formframe, height=3, width=10, text = 'Zakoncz', command = self.end_game)
            self.endgame_button.grid(pady = 6)
        elif self.usercounter_ships ==0:
            lose = MessageBox(self.game)
            lose.lose()
            for a in range(10):
                for b in range(10):
                    self.buttons[a][b].config(state = 'disabled')
            for c in range(10):
                for d in range(10):
                    if (self.playerField[d][c]!='W' and self.playerField[d][c]!='X' and self.playerField[d][c]!='0'):
                        self.buttons[c][d].config(bg='dim gray')
            self.reset_button = tkinter.Button(self.formframe, height=3, width=10, text = 'Zagraj ponownie', command = self.reset_game)
            self.reset_button.grid(pady = 6)
            self.endgame_button = tkinter.Button(self.formframe, height=3, width=10, text = 'Zakoncz', command = self.end_game)
            self.endgame_button.grid(pady = 6)

    def destroyed_enemyShips(self, x, y):
        if self.playerField[y][x] == 'A':
            self.fourcounter += 1
            if self.fourcounter == 4:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'B':
            self.threecounter_o += 1
            if self.threecounter_o == 3:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'C':
            self.threecounter_t += 1
            if self.threecounter_t == 3:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'D':
            self.twocounter_o += 1
            if self.twocounter_o == 2:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'E':
            self.twocounter_t += 1
            if self.twocounter_t == 2:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'F':
            self.twocounter_th += 1
            if self.twocounter_th == 2:
                return True
            else:
                return False
        elif self.playerField[y][x] == 'G':
            return True

    def destroyed_myShips(self, x, y):
        if self.GameTableView.playerField[y][x] == 'A':
            self.GameTableView.fourcounter += 1
            if self.GameTableView.fourcounter == 4:
                self.s = 4
                self.dx = self.GameTableView.Ax
                self.dy = self.GameTableView.Ay
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'B':
            self.GameTableView.threecounter_o += 1
            if self.GameTableView.threecounter_o == 3:
                self.s = 3
                self.dx = self.GameTableView.Bx
                self.dy = self.GameTableView.By
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'C':
            self.GameTableView.threecounter_t += 1
            if self.GameTableView.threecounter_t == 3:
                self.s = 3
                self.dx = self.GameTableView.Cx
                self.dy = self.GameTableView.Cy
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'D':
            self.GameTableView.twocounter_o += 1
            if self.GameTableView.twocounter_o == 2:
                self.s = 2
                self.dx = self.GameTableView.Dx
                self.dy = self.GameTableView.Dy
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'E':
            self.GameTableView.twocounter_t += 1
            if self.GameTableView.twocounter_t == 2:
                self.s = 2
                self.dx = self.GameTableView.Ex
                self.dy = self.GameTableView.Ey
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'F':
            self.GameTableView.twocounter_th += 1
            if self.GameTableView.twocounter_th == 2:
                self.s = 2
                self.dx = self.GameTableView.Fx
                self.dy = self.GameTableView.Fy
                return True
            else:
                return False
        elif self.GameTableView.playerField[y][x] == 'G':
            return True


    def reset_game(self):
        reset = self.GameTableView.reset_game()
        remove = self.window.destroy()

    def end_game(self):
        end_your_table = self.GameTableView.window.destroy()
        end_my_table = self.window.destroy()
