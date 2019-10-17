import tic_tac_toe_user


class registerForm:

    def __init__(self):
        self.register_form_instructions = "Please register new user. Follow instructions below. \n"

    def get_user(self, user1):

        print(self.register_form_instructions)

        name = input("What is your name?\n")
        print("Hi, %s\n" %name)
        user_type = input("Choose your role: cross, zero\n")

        if user_type != "cross" and user_type != "zero":

            print("Wrong role, try again.")
            self.get_user(user1)

        if user1 != "init_user":
            if user1.user_type == user_type:
                print("Choose another role.\n")
                return None

        user = tic_tac_toe_user.User(name, user_type)

        return user

class gameForm:
    
    def __init__(self):
        
        self.register_form = registerForm()
        self.game_play_instructions = "You should make 3 in row faster than your opponent.\n"

    def user_init(self):

        user1 = self.register_form.get_user("init_user")
        user2 = self.register_form.get_user(user1)

        if user2 == None:

            while user2 == None:

                user2 = self.register_form.get_user(user1)

    
        return user1, user2


    @staticmethod
    def we_have_winner(field_list):

        variants = []

            
        variants.append(field_list[0] + field_list[1] + field_list[2])
        variants.append(field_list[3] + field_list[4] + field_list[5])
        variants.append(field_list[6] + field_list[7] + field_list[8])

        variants.append(field_list[0] + field_list[3] + field_list[6])
        variants.append(field_list[1] + field_list[4] + field_list[7])
        variants.append(field_list[2] + field_list[5] + field_list[8])

        variants.append(field_list[0] + field_list[4] + field_list[8])
        variants.append(field_list[2] + field_list[4] + field_list[6])

        check_list = []

        for i in range(9):
            if str(i+1) not in field_list:
                check_list.append(i+1)

        for i in variants:
            if i == "XXX":
                print("We have winner!\n")
                return "cross"
            elif i == "OOO":
                print("We have winner!\n")
                return "zero"
            elif len(set(check_list)) == 9:
                print("We dont have winner!\n")
                return "noone"

        
        return "no"

    

    def game_play(self):
        
        print(self.game_play_instructions)

        first_user, second_user = self.user_init()




        move_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        field = "_____________\n"  + "|_" + move_list[0] + "_|_" +  move_list[1]+ "_|_" + move_list[2] + "_|\n"  + "|_" + move_list[3] + "_|_" + move_list[4] + "_|_" + move_list[5] + "_|\n"  + "|_" + move_list[6] + "_|_" + move_list[7] + "_|_" + move_list[8] + "_|\n" 



        if first_user.user_type == "cross":

            moving = first_user
            waitng = second_user

        else:
            moving = second_user
            waitng = first_user
        
        someone_won = "no"

        while someone_won == "no":

            print("%s, your move. " %moving.name)
            print(field)
            
            move = input("Choose number: ")

            while  not move in move_list:
                move = input("There is no such numbers. Choose correct number: ")
            
            while int(move) - 1 > len(move_list):
                 move = input("Number is too big. Choose correct number: ")

            move = int(move) - 1
            
            move_list[move] = moving.game_play()

            field = "_____________\n"  + "|_" + move_list[0] + "_|_" +  move_list[1]+ "_|_" + move_list[2] + "_|\n"  + "|_" + move_list[3] + "_|_" + move_list[4] + "_|_" + move_list[5] + "_|\n"  + "|_" + move_list[6] + "_|_" + move_list[7] + "_|_" + move_list[8] + "_|\n" 
            
            someone_won = type(self).we_have_winner(move_list)

            moving, waitng = waitng, moving

        
        print(field)
        if moving.user_type == someone_won:

            print("Great job, %s" %moving.name)
            
            print("Try again? (yes) \n")

        elif waitng.user_type == someone_won:

             print("Great job, %s" %waitng.name)
             
             print("Try again? (yes) \n")

        else:

            print("Friendship forever!")
            print("Try again? (yes) \n")
            

        return 0



if __name__ == '__main__':

    game = gameForm()

    game.game_play()

    while input() == "yes":
        game.game_play()
