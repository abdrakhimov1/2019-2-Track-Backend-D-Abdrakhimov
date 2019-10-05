class User():

    def __init__(self, name, user_type):

        self.name = name

        if user_type == "cross":
            self.user_type = "cross"

        elif user_type == "zero":
            self.user_type = "zero"

        else:
            self.user_type = "wrong_type"

    def game_play(self):

        if self.user_type == 'cross':
            return 'X'
        
        if self.user_type == 'zero':
            return 'O'
