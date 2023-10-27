# Game manual: http://markthompson.us/intv/IntvFlashbackGameManuals.pdf
# Page 696

import pygame, random, os, math
from pygame.locals import *

pygame.init()
print("A")



class Coordinates:
    """Coordinates of any point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Hex:
    occupies = "empty"
    #  protected: 0 = player one, 1 = player two, 2 = No, 11/12/13 = contains rebel - 10-x is how many turns it has been on the board
    protected = 2
    type = None
    X = None
    Y = None
    building = None

    def __init__(self, hex_type, row, column):
        """0 = player one
           1 = player two
           2 = sea"""
        self.type = hex_type
        self.Y = row
        self.X = column


class PlayerInfo:
    money = 1000
    factories = 0
    income_multiplier = 0
    fishing_boats = 0
    income = 0

    pop = 0
    pop_fed = 0
    pop_increase = 0

    points = 0

    placing = 0

    harbour = (0, 0)

    mode = "cursor"

    # ["speed in x, speed in y, boat type (1=pt boat,2=fishing boat)]
    boat_info = [0, 0, None]
    boat_position = Coordinates(0, 0)
    boat_next_pos = Coordinates(0, 0)

    def calc_income(self):
        self.income = self.factories * 4 * self.income_multiplier + self.fishing_boats + 10
        return self.income

    def calc_money(self):
        self.money += self.income
        return self.money





class Boat:
    velocity = Coordinates(0,0)

    def __init__(self, x=0, y=0):
        self.position = Coordinates(x, y)

    def update_position(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def is_collision(self):
        if board[int(players[i].(self.position.y+self.velocity.y)/hex_size)][int(players[i].self.position.x+self.velocity.x/hex_size)].type == 2:
            return True
        else:
            return False



            # calculating collisions:
            # if the hex the boat will be in next is not sea, it updates the current position of the boat
            # int(players[i].boat_position.y/hex_size)
            print("collision", board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)].type)
            print("position, (y,x)", (players[i].boat_position.y/hex_size), (players[i].boat_position.x/hex_size))

            if board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)].type == 3:
                players[i].boat_position.x = players[i].boat_next_pos.x
                players[i].boat_position.y = players[i].boat_next_pos.y





test_boat = Boat(y=1)
print(test_boat.position.x, test_boat.position.y)



"""pygame.display.quit()
pygame.quit()
quit()"""












players = [PlayerInfo(), PlayerInfo()]

board_setup = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
               [3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 2, 3, 3, 3, 3],
               [3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],
               [3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3],
               [3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3],
               [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3],
               [3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3],
               [3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
               ]

board = []
for row in range(len(board_setup)):
    board.append([])
    # set up the board with "Hex" classes in each hex
    for column in range(len(board_setup[row])):
        board[-1].append(Hex(board_setup[row][column] - 1, row, column))

display_width = 1200
display_height = 700
hex_size = 50

res_X = 1
res_Y = 1

# boat_speed = units/pixels per second
boat_speed = 180
fps = 60

gameDisplay = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption("Utopia")

clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Empty_Utopia_Map.jpg"),
                                    (display_width, display_height))
cursor_one = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Cursor_one.png")
cursor_two = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Cursor_two.png")

fort = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Fort.png")
factory = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Factory.png")
crops = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Crops.png")
school = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/School.png")
hospital = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Hospital.png")
houses = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Houses.png")
rebels = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Rebel.png")
pt_boat_one = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Pt_boat_red.png")
pt_boat_two = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Pt_boat_green.png")
fishing_boat_one = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Fishing_boat_red.png")
fishing_boat_two = pygame.image.load("C:/Users/giri5/PycharmProjects/Utopia/Fishing_boat_green.png")

font = pygame.font.SysFont(None, 25)

cursor_one_X = 50
cursor_one_Y = 50
cursor_two_X = 100
cursor_two_Y = 100

cursor_width = hex_size
cursor_height = hex_size

players[0].harbour = (3, 8)
players[1].harbour = (19, 4)


# functions for placing buildings
def fort_placed(player, X, Y):
    """Places a fort for "player," removing money, placing the fort and adding protected regions around it"""
    board[Y][X].building = 1
    players[player].money -= buildings[players[player].placing][2]
    for i in range(3):
        for j in range(3):
            board[Y - 1 + i][X - 1 + j].protected = player


def factory_placed(player, X, Y):
    """Places a factory for "player," removing money and incrementing factories and decreasing pop_increase"""
    board[Y][X].building = 2
    players[player].money -= buildings[players[player].placing][2]
    players[player].factories += 1
    players[player].pop_increase -= 10


def crops_placed(player, X, Y):
    """Places a crop for "player," removing money and incrementing pop_fed"""
    board[Y][X].building = 3
    players[player].money -= buildings[players[player].placing][2]
    players[player].pop_fed += 500


def school_placed(player, X, Y):
    """Places a school for "player," removing money and income_multiplier"""
    board[Y][X].building = 4
    players[player].money -= buildings[players[player].placing][2]
    players[player].income_multiplier += 0.25


def hospital_placed(player, X, Y):
    """Places a hospital for "player," removing money and increasing multiplier and increases pop_increase"""
    board[Y][X].building = 5
    players[player].money -= buildings[players[player].placing][2]
    players[player].income_multiplier += 0.5
    players[player].pop_increase += 100


def houses_placed(player, X, Y):
    """Places houses, adding to pop_fed"""
    board[Y][X].building = 6
    players[player].money -= buildings[players[player].placing][2]
    players[player].pop_fed += 500


def rebels_placed(player):
    """Places rebels on other player's land if possible. If it was placed, removes money"""
    possible_targets = []
    # cycles through all of the board
    for Y in range(len(board)):
        for X in range(len(board[Y])):
            # if it is a land tile owned by the other player
            if board[Y][X].type == (player + 1) % 2:
                # and does not have a building or is protcted
                if board[Y][X].building == None and board[Y][X].protected == 2:
                    # it adds the tile to "possible targets"
                    possible_targets.append((Y, X))
    print(possible_targets)
    if len(possible_targets) != 0:
        players[player].money -= buildings[players[player].placing][2]
        target = possible_targets[random.randint(0, len(possible_targets) - 1)]
        print("target", target)
        print(target[0])
        board[target[0]][target[1]].building = 7
        print("placed")
    else:
        return False


def pt_boat_placed(player):
    """Places a pt boat for 'player'"""
    # pt boat is 8 for player 1 and 9 for player 2
    board[players[player].harbour[1]][players[player].harbour[0]].building = 8 + player
    players[player].money -= buildings[players[player].placing][2]


def fishing_boat_placed(player):
    """Places a fishing boat for 'player'"""
    # pt boat is 10 for player 1 and 11 for player 2
    board[players[player].harbour[1]][players[player].harbour[0]].building = 10 + player
    players[player].money -= buildings[players[player].placing][2]


buildings = [None,
             ["fort", "building", 50, fort, fort_placed],
             ["factory", "building", 40, factory, factory_placed],
             ["crops", "building", 3, crops, crops_placed],
             ["school", "building", 35, school, school_placed],
             ["hospital", "building", 75, hospital, hospital_placed],
             ["houses", "building", 60, houses, houses_placed],
             ["rebels", "agro", 30, rebels, rebels_placed],
             ["pt boat one", "boat", 40, pt_boat_one, pt_boat_placed],
             ["pt boat two", "boat", 40, pt_boat_two, pt_boat_placed],
             ["fishing boat one", "boat", 25, fishing_boat_one, fishing_boat_placed],
             ["fishing boat two", "boat", 25, fishing_boat_two, fishing_boat_placed]
             ]


def refresh_screen(update=True):
    """Refreshes everything on the screen (if update is false, doesn't visually update the screen)"""
    # resizing of elements on screen done here - for the purposes of the game, resizing doesn't exist
    # displays background
    gameDisplay.blit(pygame.transform.scale(background, (int(display_width * res_X), int(display_height * res_Y))),
                     (0, 0))

    # displays buildings
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].building:
                gameDisplay.blit(pygame.transform.scale(buildings[board[i][j].building][3],
                                                        (int(cursor_width * res_X), int(cursor_height * res_Y))),
                                 (j * cursor_width * res_X, i * cursor_height * res_Y))

            # if board[i][j].building == "fort":
            #     gameDisplay.blit(pygame.transform.scale(fort, (int(cursor_width * res_X), int(cursor_height * res_Y))),
            #                      (j * cursor_width * res_X, i * cursor_height * res_Y))

    # displays cursors
    gameDisplay.blit(pygame.transform.scale(cursor_one, (int(cursor_width * res_X), int(cursor_height * res_Y))),
                     (cursor_one_X * res_X, cursor_one_Y * res_Y))
    gameDisplay.blit(pygame.transform.scale(cursor_two, (int(cursor_width * res_X), int(cursor_height * res_Y))),
                     (cursor_two_X * res_X, cursor_two_Y * res_Y))

    # displays building in corner of cursor
    for i in range(2):
        to_blit = ""
        if players[i].placing == 0:
            to_blit == ""
        else:
            to_blit = buildings[players[i].placing][3]

        if to_blit != "":
            if i == 0:
                gameDisplay.blit(pygame.transform.scale(to_blit, (
                    int(cursor_width * 0.4 * res_X), int(cursor_height * 0.4 * res_Y))),
                                 (cursor_one_X * res_X, cursor_one_Y * res_Y))
            elif i == 1:
                gameDisplay.blit(pygame.transform.scale(to_blit, (
                    int(cursor_width * 0.4 * res_X), int(cursor_height * 0.4 * res_Y))),
                                 (cursor_two_X * res_X, cursor_two_Y * res_Y))

    if update == True:
        pygame.display.update()


def get_hex(player):
    """returns the class which refers to the hex where the player's cursor is """
    if player == 0:
        return board[int(cursor_one_Y / cursor_height)][int(cursor_one_X / cursor_width)]
    elif player == 1:
        return board[int(cursor_two_Y / cursor_height)][int(cursor_two_X / cursor_width)]


while True:
    clock.tick(fps)
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
        pygame.quit()
        quit()

    elif event.type == KEYDOWN:
        # print("pygame.event", event.key)
        # players[0].mode

        if True:
            if event.key == pygame.K_w:
                if players[0].mode == "cursor":
                    if cursor_one_Y > 0:
                        cursor_one_Y -= cursor_height

                # if they are in boat mode
                elif players[0].mode == "boat":
                    print("In boat mode")
                    players[0].boat_info[1] -= 1

            elif event.key == pygame.K_a:
                if players[0].mode == "cursor":
                    if cursor_one_X > 0:
                        cursor_one_X -= cursor_width

                # if they are in boat mode
                elif players[0].mode == "boat":
                    print("In boat mode")
                    players[0].boat_info[0] -= 1

            elif event.key == pygame.K_s:
                if players[0].mode == "cursor":
                    if cursor_one_Y < display_height - 3 * cursor_height:
                        cursor_one_Y += cursor_height

                # if they are in boat mode
                elif players[0].mode == "boat":
                    print("In boat mode")
                    players[0].boat_info[1] += 1


            elif event.key == pygame.K_d:
                if players[0].mode == "cursor":
                    if cursor_one_X < display_width - 3 * cursor_width:
                        cursor_one_X += cursor_width

                # if they are in boat mode
                elif players[0].mode == "boat":
                    print("In boat mode")
                    players[0].boat_info[0] += 1


            elif event.key == pygame.K_q:
                # if it is on a boat of the other player
                if players[0].placing == 8 or players[0].placing == 10:
                    players[0].placing += 1
                if players[0].placing >= len(buildings) - 1:
                    players[0].placing = 0
                else:
                    players[0].placing += 1


            # places a building/agro/boat for player one or puts player one into boat mode
            elif event.key == pygame.K_e:
                if players[0].mode == "cursor":

                    print("Hex type, building on hex", get_hex(0).type == 0, get_hex(0).building)

                    # if the cursor is on a boat owned by player one ...
                    if get_hex(0).type == 2 and (get_hex(0).building == 8 or get_hex(0).building == 10):
                        # sets "wasd" to control the boat
                        players[0].mode = "boat"
                        print("Boat Mode")
                        # if it is a pt boat, sets boat_info[2] to 1, if it is a fishing boat, sets it to 2
                        if get_hex(0).building == 8:
                            players[0].boat_info[2] = 1
                        elif get_hex(0).building == 10:
                            players[0].boat_info[2] = 2
                        board[get_hex(0).Y][get_hex(0).X].building = None

                        print(buildings[players[0].placing])

                    # there is nothing selected
                    elif buildings[players[0].placing] == None:
                        print("None placed")

                    # there is a building selected
                    elif buildings[players[0].placing][1] == "building":
                        print("Player money, cost:", players[0].money, buildings[players[0].placing][2])
                        print("Hex type, building on hex:", get_hex(0).type, get_hex(0).building)
                        # check to see if on valid hex(their continent and no other buildings) and has enough money
                        if players[0].money >= buildings[players[0].placing][2] and get_hex(0).type == 0 and get_hex(
                                0).building == None:
                            print(buildings[players[0].placing][0])
                            # places the building where player one's cursor is
                            buildings[players[0].placing][4](0, get_hex(0).X, get_hex(0).Y)
                            print(buildings[players[0].placing][0], " placed")
                        else:
                            print("Cannot place")

                    # for spawning rebels in enemy territory
                    elif buildings[players[0].placing][1] == "agro":
                        print("Player money, cost:", players[0].money, buildings[players[0].placing][2])
                        if players[0].money >= buildings[players[0].placing][2]:
                            print(buildings[players[0].placing][0])
                            # if there are no valid locations, will return False
                            if (buildings[players[0].placing][4](0)) == False:
                                print("Cannot place")
                            else:
                                print(buildings[players[0].placing][0], " placed")
                        else:
                            print("Cannot place")

                    # for spawning boats
                    elif buildings[players[0].placing][1] == "boat":
                        print("Player money, cost:", players[0].money, buildings[players[0].placing][2])
                        # check to see if they have enough money
                        if players[0].money >= buildings[players[0].placing][2]:
                            print(buildings[players[0].placing][0])
                            # if there is nothing on their harbour:
                            if board[players[0].harbour[1]][players[0].harbour[0]].building == None:
                                # places the boat for player 1
                                buildings[players[0].placing][4](0)
                                print(buildings[players[0].placing][0], " placed")
                            else:
                                print("There is already something in your harbour")
                        else:
                            print("Cannot place")


                # Removes player from boat mode
                elif players[0].mode == "boat":
                    # if the boat is on an empty hex:
                    if board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)].buildings == None:

                        board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)]
                        # Places boat back on the board
                        buildings[players[0].placing][4](0)

                    
                    


















































                        players[0].mode = "cursor"
                        print("Cursor mode")




            # debug keys
            # shows who the hex player one is on is protected by
            elif event.key == pygame.K_p:
                print(board[get_hex(0).Y][get_hex(0).X].protected)

            # shows what is build on the hex player one is on
            elif event.key == pygame.K_o:
                print(board[get_hex(0).Y][get_hex(0).X].building)

            elif event.key == pygame.K_i:
                refresh_screen()

            elif event.key == pygame.K_u:
                print((get_hex(0).X, get_hex(0).Y))

            elif event.key == pygame.K_y:
                print((players[0].placing, players[1].placing))

            elif event.key == pygame.K_l:
                players[0].points = 10
                print((players[0].points, players[1].points))



        # player two
        elif event.key == pygame.K_UP:
            if players[1].mode == "cursor":
                if cursor_two_Y > 0:
                    cursor_two_Y -= cursor_height

        elif event.key == pygame.K_LEFT:
            if mode_two[0] == "cursor":
                if cursor_two_X > 0:
                    cursor_two_X -= cursor_width

        elif event.key == pygame.K_DOWN:
            if mode_two[0] == "cursor":
                if cursor_two_Y < display_height - 3 * cursor_height:
                    cursor_two_Y += cursor_height

        elif event.key == pygame.K_RIGHT:
            if mode_two[0] == "cursor":
                if cursor_two_X < display_width - 3 * cursor_width:
                    cursor_two_X += cursor_width

        refresh_screen()







    elif event.type == KEYUP:
        # removes the velocity from the boat when the button is no longer depressed
        if players[0].mode == "boat":
            if event.key == pygame.K_w:
                players[0].boat_info[1] += 1

            elif event.key == pygame.K_a:
                players[0].boat_info[0] += 1
                print(players[0].boat_info)

            elif event.key == pygame.K_s:
                players[0].boat_info[1] -= 1


            elif event.key == pygame.K_d:
                players[0].boat_info[0] -= 1







    elif event.type == VIDEORESIZE:
        # changes res_X and res_Y, which are used when displaying on the screen
        print("video resize")
        gameDisplay = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        # res = resize ratio
        print(event.dict['size'], display_width, display_height)
        res_X = event.dict['size'][0] / display_width
        res_Y = event.dict['size'][1] / display_height
        print(res_X, res_Y)
        refresh_screen()

        pygame.display.update()


    # if there is nothing in the event queue, adds USEREVENT so the while loop continues
    elif not pygame.event.peek(USEREVENT):
        pygame.event.post(pygame.event.Event(USEREVENT))

    # moves boats
    for i in range(2):
        if players[i].mode == "boat":

            ## adds the velocity (1*speed per vector) of the boat onto the position of the boat. This is stored in players[i].boat_next_pos
            #players[i].boat_next_pos.x = players[i].boat_position.x + (players[i].boat_info[0]) * (1 / fps)
            #players[i].boat_next_pos.y = players[i].boat_position.y + (players[i].boat_info[1]) * (1 / fps)

            ## calculating collisions:
            ## if the hex the boat will be in next is not sea, it updates the current position of the boat
            ## int(players[i].boat_position.y/hex_size)

            #print("collision", board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)].type)
            #print("position, (y,x)", (players[i].boat_position.y/hex_size), (players[i].boat_position.x/hex_size))

            #if board[int(players[i].boat_position.y/hex_size)][int(players[i].boat_position.x/hex_size)].type == 3:
            #    players[i].boat_position.x = players[i].boat_next_pos.x
            #    players[i].boat_position.y = players[i].boat_next_pos.y


            # if a collision does happen:
            #else:





            
















            # determines which boat is being moved
            to_blit_index = -1
            to_blit_index += 2*i
            to_blit_index += players[i].boat_info[2]

            if to_blit_index == 0:
                to_blit = pt_boat_one
            elif to_blit_index == 1:
                to_blit = fishing_boat_one
            elif to_blit_index == 2:
                to_blit = pt_boat_two
            elif to_blit_index == 3:
                to_blit = fishing_boat_two


            gameDisplay.blit(pygame.transform.scale(to_blit,(
                int(players[i].boat_position.x * res_X), int(players[i].boat_position.y * res_Y))),
                             (players[i].boat_position.x * res_X, players[i].boat_position.y * res_Y))

            # updates screen only in portion of screen that might have changed: (new boat pos. - distance it travelled to get there [prev. pos],
            #                                                                    , same as above, but y
            #                                                                    , size of a hex plus the distance it moved
            #                                                                    , same as above, but x)
            # pygame.display.update(int(players[i].boat_position.x * res_X) - int(players[i].boat_position.x * res_X),
            #                       int(players[i].boat_position.y * res_Y) - int(players[i].boat_position.y * res_Y),
            #                           int(cursor_width * res_X) + int(players[i].boat_position.x * res_X),
            #                               int(cursor_height * res_Y) + int(players[i].boat_position.y * res_Y))

            pygame.display.update()


            print(players[0].boat_info, players[i].boat_position.x, players[i].boat_position.y)