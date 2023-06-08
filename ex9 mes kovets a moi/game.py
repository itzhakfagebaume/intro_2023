from car import Car
from board import Board
from sys import argv
import helper


car_names = {'Y','B','O','G','W','R'}
possib_move = ['u','d','l','r']
WIN_MESSAGE = """You won!

WIN     WIN     WIN    WIN    WIN     WIN
 WIN   WIWIN   WIN     WIN    WININ   WIN
  WIN WIN WIN WIN      WIN    WIN WIN WIN
   WININ   WININ       WIN    WIN   WIWIN
    WIN     WIN        WIN    WIN     WIN"""

def name_error(name):
        return False if name not in car_names else True
    
def move_error(move):
    return False if move not in possib_move else True


class Game:
    """
    play the game
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

            
    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        
        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        while 1:
            user = input("choose a car and the direction that you want to go")
            if user == "!":
                return False
            try:
                user = user.split(',')
                name , key = user[0],user[1]
            except:
                print("you need to separe the name and key by ,")
                continue

            if name_error(name) and move_error(key):
                    verif = self.board.move_car(name,key)
                    if verif:
                        break
                    else:
                        print("not a valid move")

        print((self.board))
        return True

        

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print("lets play")
        print(self.board)
        while self.board.cell_content(self.board.target_location()) is None:
            stop = self.__single_turn()
            if not stop:
                break
            if self.board.possible_moves() == []:
                print("you can't move")
                break
        if self.board.cell_content(self.board.target_location()) is not None:
            print(WIN_MESSAGE)
        else:
            print("game over bye")




def create_board(file_name): # en fonction des voitures et du tableaupython3 game.py 'car_config.json' 
    dict_car = helper.load_json(file_name)
    board = Board()
    for name,prop_car in dict_car.items():
        if name not in car_names:
            continue
        try:
            new_car = Car(name,prop_car[0],(prop_car[1][0],prop_car[1][1]),prop_car[2])
            if not all(coor in board.cell_list() for coor in new_car.car_coordinates()):
                continue
            board.add_car(new_car)
        except:
            continue
    return board

def main(args):
    # verif the 
    board= create_board(args[0])
    # if board is None:
    #     return 1
    game = Game(board)
    game.play()
    
    


if __name__== "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    main(argv[1:])
