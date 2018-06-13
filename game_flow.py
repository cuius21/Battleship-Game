from game_table_view import GameTableView
from message_box import MessageBox



class GameFlow:
    def __init__(self,game):
        self.game = game


    def run(self):
        showinformation = MessageBox(self.game)
        showinformation.preparinggame()
        gametableview = GameTableView(self.game, 10)



'''
        print('xD')
        for x in range(10):
            for y in range(10):
                print(gametableview.playerField[x][y], end='')
            print('')
        print('xD2')
        for x in range(10):
            for y in range(10):
                print(opponenttableview.playerField[x][y], end='')
            print('') '''
