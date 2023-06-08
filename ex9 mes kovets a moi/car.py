class Car:
    """
    create a car of the game
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name # name car: ['Y','B','O','G','W','R']
        self.length = length # entre deux et 4
        self.location =location # coordones minimale de la voiture
        self.orientation = orientation # 0 verticale 1 horizontale
        

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        return [(self.location[0], self.location[1]+i) if self.orientation == 1 
                else (self.location[0]+i, self.location[1]) for i in range(self.length)]


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        return {"l": "the car goes left", "r": "the car goes right"} if self.orientation == 1 else {"u": "the car goes up", "d": "the car goes down"}

        

    def movement_requirements(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').

        if (self.orientation == 1 and (move_key != 'l' and move_key != "r")) or (self.orientation == 0 and (move_key != 'u' and move_key != 'd')):
            return []
        if self.orientation == 1:
            if move_key == 'l':
                return [(self.location[0], self.location[1] - 1)]
            if move_key == 'r':
                return [(self.location[0], self.location[1] + self.length)]
        if self.orientation == 0:
            if move_key == 'u':
                return [(self.location[0] - 1, self.location[1])]
            if move_key == 'd':
                return [(self.location[0] + self.length, self.location[1])]

                                                                    


    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if (self.orientation == 1 and (move_key != 'l' and move_key != "r")) or (self.orientation == 0 and (move_key != 'u' and move_key != 'd')):
            return False
        else:
            if self.orientation == 1:
                if move_key == 'l':
                    self.location = (self.location[0], self.location[1] - 1)
                if move_key == 'r':
                    self.location = (self.location[0], self.location[1] + 1)
            if self.orientation == 0:
                if move_key == 'u':
                    self.location = (self.location[0] - 1, self.location[1])
                if move_key == 'd':
                    self.location = (self.location[0] + 1, self.location[1])
            return True


    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
