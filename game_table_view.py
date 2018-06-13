import tkinter
from tkinter import *
from opponent_game_table_view import OpponentGameTableView


class GameTableView:
    def __init__(self, game, size):#onclick):
        self.game = game
        self.window = tkinter.Tk()
        self.window.title('Twoja tablica')
        self.window.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
        self.window.geometry('{}x{}+150+150'.format(800, 700))
        self.direction = 'horizontal'
        self.playerField = [['0'] * size for x in range(size)]
        for x in range(size):
            for y in range(size):
                print(self.playerField[x][y], end='')
            print('')
        self.battleshipSize = [4,3,3,2,2,2,1,1,1,1]
        self.battleshipCounter = 0
        self.fourcounter = 0
        self.threecounter_o = 0
        self.threecounter_t = 0
        self.twocounter_o = 0
        self.twocounter_t = 0
        self.twocounter_th = 0
        self.wrapperframe = tkinter.Frame(self.window)
        self.wrapperframe.grid()
        self.formframe = tkinter.Frame(self.wrapperframe)
        self.formframe.grid(row=0, column=11)
        self.buttonsFrame = tkinter.Frame(self.wrapperframe)
        self.buttonsFrame.grid(row=0, column=0)
        self.buttons = [[tkinter.Button(self.buttonsFrame, width=4, height=4, bg='deep sky blue',
                                        command= lambda x=x, y=y:self.mark_area(x, y))#lambda x=x, y=y:onclick(x, y))
                         for y in range(size)] for x in range(size)]
        for x in range(size):
            for y in range(size):
                self.buttons[x][y].grid(column=x, row=y)

        self.label = Label(self.formframe, text = 'Kierunek statku: \n poziomo', font=("Helvetica", 15))
        self.label.grid(row=0,column=0, sticky=N)
        self.label2 = Label(self.formframe, text = 'Wielkość statku: ' + str(self.battleshipSize[self.battleshipCounter]), font=("Helvetica", 15))
        self.label2.grid(row=1,column=0, sticky=N)
        self.window.bind("<Key>", self.setdirection)
        self.reset = tkinter.Button(self.formframe, height=3, width=10, text = 'Reset', command = self.reset_game)
        self.reset.grid(row=2,column=0, sticky=N, pady=6)


    def mark_area(self, x, y):
        tmp = False #zmienna, ktora sprawdza czy statek poprawnie sie wykonal,
        # jesli nie mozna bylo ustawic statku to licznik statku nie jest inkrementowany

        #self.checkShips(x, y, self.direction)

        if self.direction == 'horizontal':
            if self.checkShips(x, y, self.direction): #true
                for a in range(y-1,y+2):
                    for b in range(x-1, x+self.battleshipSize[self.battleshipCounter]+1):
                        if a > -1 and b > -1 and a < 10 and b < 10:
                            self.playerField[a][b] = 'W'
                            self.buttons[b][a].config(state="disabled")
                for z in range(x,x+self.battleshipSize[self.battleshipCounter]):
                    if self.battleshipCounter == 0:
                        self.playerField[y][z] = 'A'
                        self.Ax = x
                        self.Ay = y
                    elif self.battleshipCounter == 1:
                        self.playerField[y][z] = 'B'
                        self.Bx = x
                        self.By = y
                    elif self.battleshipCounter == 2:
                        self.playerField[y][z] = 'C'
                        self.Cx = x
                        self.Cy = y
                    elif self.battleshipCounter == 3:
                        self.playerField[y][z] = 'D'
                        self.Dx = x
                        self.Dy = y
                    elif self.battleshipCounter == 4:
                        self.playerField[y][z] = 'E'
                        self.Ex = x
                        self.Ey = y
                    elif self.battleshipCounter == 5:
                        self.playerField[y][z] = 'F'
                        self.Fx = x
                        self.Fy = y
                    else:
                        self.playerField[y][z] = 'G'
                    self.buttons[z][y].config(bg="dim gray")
                tmp = True
        if self.direction == 'vertical':
            if self.checkShips(x, y, self.direction): #true
                for a in range(y-1, y+self.battleshipSize[self.battleshipCounter]+1):
                    for b in range(x-1,x+2):
                        if a > -1 and b > -1 and a < 10 and b < 10:
                            self.playerField[a][b] = 'W'
                            self.buttons[b][a].config(state="disabled")
                for z in range(y,y+self.battleshipSize[self.battleshipCounter]):
                    if self.battleshipCounter == 0:
                        self.playerField[z][x] = 'A'
                        self.Ax = x
                        self.Ay = y
                    elif self.battleshipCounter == 1:
                        self.playerField[z][x] = 'B'
                        self.Bx = x
                        self.By = y
                    elif self.battleshipCounter == 2:
                        self.playerField[z][x] = 'C'
                        self.Cx = x
                        self.Cy = y
                    elif self.battleshipCounter == 3:
                        self.playerField[z][x] = 'D'
                        self.Dx = x
                        self.Dy = y
                    elif self.battleshipCounter == 4:
                        self.playerField[z][x] = 'E'
                        self.Ex = x
                        self.Ey = y
                    elif self.battleshipCounter == 5:
                        self.playerField[z][x] = 'F'
                        self.Fx = x
                        self.Fy = y
                    else:
                        self.playerField[z][x] = 'G'
                    self.buttons[x][z].config(bg="dim gray")
                tmp = True


        print('\n')
        for x in range(10):
            for y in range(10):
                print(self.playerField[x][y], end='')
            print('')

        if self.battleshipCounter == 9:
            for i in range(10):
                for j in range(10):
                    self.buttons[i][j].config(state='disabled')
            self.label.config(text = 'Wszystkie statki \n zostały rozstawione')
            self.label2.config(text =" ")
            self.buttonend = tkinter.Button(self.formframe, height=3, width=10, text = 'Graj', command = self.play_game)
            self.buttonend.grid(row=3,column=0, sticky=N, pady=6)

        elif (self.battleshipCounter !=9 and tmp == True):
            self.battleshipCounter += 1
            tmp = True
            self.label2.config(text = 'Wielkość statku: ' + str(self.battleshipSize[self.battleshipCounter]))

        else:
            self.label2.config(text = 'Prosze ponownie \nustawić statek\n'
                                      'Wielkość statku: ' + str(self.battleshipSize[self.battleshipCounter]))

    def setdirection(self, event):
        if self.direction == 'horizontal':
            self.direction = 'vertical'
            self.label.config(text = 'Kierunek statku:\n pionowo')
        else:
            self.direction = 'horizontal'
            self.label.config(text = 'Kierunek statku:\n poziomo')


    def checkShips(self, x, y, dir):
        #copy=self.playerField[:] #kopia
        if dir == 'horizontal':
            if x+self.battleshipSize[self.battleshipCounter] < 11: #lewy górny róg
                for a in range(y-1,y+2):
                    for b in range(x-1, x+self.battleshipSize[self.battleshipCounter]+1):
                        if a > -1 and b > -1 and a < 10 and b < 10:
                            if self.playerField[a][b] == 'A' or self.playerField[a][b] == 'B' or self.playerField[a][b] == 'C' \
                                    or self.playerField[a][b] == 'D' or self.playerField[a][b] == 'E' or self.playerField[a][b] == 'F' \
                                    or self.playerField[a][b] == 'G':
                                return False
                return True
            return False
        elif dir == 'vertical':
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

    def play_game(self):
        opponentgametableview = OpponentGameTableView(self.game, 10, self)
        self.buttonend.config(state='disabled')
        self.reset.config(state='disabled')


    def reset_game(self):
        reset = GameTableView(self.game, 10)
        remove = self.window.destroy()

