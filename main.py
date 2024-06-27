def Platforms():
    while(True):
        print("Platforms: 1- Xbox One, 2- PS4, 3- Nintendo Switch, 4- PC ")
        try:
            selected_console_number = int(input("Type the number of your platform: ")) -1
        except ValueError:
            print("", end="")
        try:
            if(selected_console_number <0 or selected_console_number >3):
                print("Invalid number, type one of the numbers above.")
        except UnboundLocalError:
            print("Please, type a number.")
        else:
            return selected_console_number
        
def Menu():
     while(True):
        print("1- Register new game, 2- List games, 3- Leave")
        try:
            what_to_do =  int(input("Type the number of the option you want: "))
        except ValueError:
            print("", end="")
        try:
            if(what_to_do<=0 or what_to_do>3):
                print("Invalid number, type one of the numbers above.")
        except UnboundLocalError:
            print("Please, type a number.")
        else:
            return what_to_do

        
def Game():
    return input("Type the name of the game: ")

def RedoArray(arraystring = [], gamename = True, arraystringname = []):
    tempgamename = [""] * (len(arraystring)+1)
    for i in range(len(tempgamename)):
        if(i>0):
            tempgamename[i] = arraystring[i-1]
        if(not tempgamename[i] == ""):
            if(i == len(arraystring)):
                arraystring = tempgamename
                if(not gamename):
                    with open("gamelist.txt", "w") as read:
                        read.writelines("\n".join(arraystring))
                        read.close()
            i+=1
        else:
            if(gamename):

                tempgamename[i] = Game()
               
            else:
                tempgamename[i] = f"{arraystringname[i]} - {platform[selected_number_console]}"
                
            if(i == len(arraystring)):
                 
                 
                arraystring = tempgamename
                if( not gamename):
                    with open("gamelist.txt", "w") as read:
                        read.writelines("\n".join(tempgamename))
                        read.close()
            i+=1
    return arraystring

def List(games = []):
    for i in range(len(games)):
        print(games[i])
        i+=1

def Load():
    try:
        with open("gamelist.txt") as read:
            game_name = [line.strip("\n") for line in read]
            read.close()
        return game_name
    except FileNotFoundError:
        game_name = []
        file = open("gamelist.txt", "wt+")
        file.close()
        return game_name
        

game_name = []
game = Load()
platform = ["Xbox One","PS4", "Nintendo Switch", "PC"]

while(True):
    what_to_do = Menu()
    if(what_to_do == 1):
        selected_number_console = Platforms()
        game_name = RedoArray(game_name, True, game_name)
        game = RedoArray(game, False, game_name)
    if(what_to_do == 2):
        List(game)
    if(what_to_do == 3):
        exit()
