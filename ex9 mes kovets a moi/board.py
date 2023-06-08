from car import Car

car_names = ['Y','B','O','G','W','R']
possib_move = ['u','d','l','r']

class Board:
    """
    create the board of the game
    """

    def __init__(self):
        # Note that this function is required in your Board implementation.
        self.board_game = [['_','_','_','_','_','_','_','*'],
                           ['_','_','_','_','_','_','_','*'],
                           ['_','_','_','_','_','_','_','*'],
                           ['_','_','_','_','_','_','_','E'],
                           ['_','_','_','_','_','_','_','*'],
                           ['_','_','_','_','_','_','_','*'],
                           ['_','_','_','_','_','_','_','*']] #list of the board 
        self.__dict_car = {} #dict private @@ int: len , tuple: location , int orientation 


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        str_board = ''
        count = 0 
        for term in self.board_game:
            for i in term:
                str_board += str(i)
            str_board += '\n'
        return str_board



    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cells = []
        for row in range(len(self.board_game)):
            for col in range(len(self.board_game[row])-1):
                cells.append((row, col))
        cells.append((3,7))
        return cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        # ans = []
        # for name_car,prop_car in self.__dict_car.items():
        #     car_coor =prop_car.car_coordinates()
        #     row,col = car_coor[0][0],car_coor[0][1]
        #     dict_possible = prop_car.possible_moves()
        #     for movkey, description in dict_possible.items():
        #         if (row == 0 and movkey == 'u') or (row == len(self.board_game)-1 and movkey == 'd'):
        #             continue
        #         if (col == 0 and movkey == 'l') or (col == len(self.board_game[0])-1 and movkey == 'r'):
        #             continue
        #         ans.append((name_car, movkey, description))
        # return ans 
        # for name_car,ob_car in self.__dict_car.items():
        #     for move,description in ob_car.possible_moves().items():
        #         if all((i,j) in self.cell_list()
        #                and self.board[i][j] == "_"
        #                for i,j in ob_car.movement_requirements()):
        #             ans.append((name_car,move,description))
        
        return [(name_car,move,description) 
                for name_car,ob_car in self.__dict_car.items() 
                for move,description in ob_car.possible_moves().items()
                if all((i,j) in self.cell_list()
                       and self.board_game[i][j] in ["_","E"]
                       for i,j in ob_car.movement_requirements(move))]


    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3,7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if self.board_game[coordinate[0]][coordinate[1]] not in ['_', 'E']:
            return self.board_game[coordinate[0]][coordinate[1]]
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        name = car.get_name()
        if name in self.__dict_car:
            return False
        for coor in car.car_coordinates():
            if coor not in self.cell_list():
                return False
            if self.board_game[coor[0]][coor[1]] not in ['_','E']: 
                return False
        

        self.__dict_car[name]= car
        for coor in car.car_coordinates():
            self.board_game[coor[0]][coor[1]] = name
        return True     


    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        if name not in self.__dict_car:
            return False

        car = self.__dict_car[name]

        if move_key not in car.possible_moves():    
            return False

        if not all((i,j) in self.cell_list()
                and self.board_game[i][j] in ["_",'E']
                for i,j in car.movement_requirements(move_key)):
            return False

        # requirements = car.movement_requirements(move_key)
        # if requirements == []:
        #     return False

        # for coor in requirements:
        #     if self.cell_content(coor) is not None:
        #         return False

        for coor in car.car_coordinates():
            self.board_game[coor[0]][coor[1]] = '_'
        car.move(move_key)
        for coor in car.car_coordinates():
            self.board_game[coor[0]][coor[1]] = name

        return True
