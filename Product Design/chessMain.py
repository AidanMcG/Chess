import socket, re
import pygame, sys, random
from pygame.locals import *

#NETWORK STUFF
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)

#DIMENSIONS
BOARD_HEIGHT = 8
BOARD_WIDTH = 8
TILE_SIZE = 60
WINDOW_WIDTH =1024
WINDOW_HEIGHT = 768

FPS = 30

#COLOURS
BLACK = (0,0,0)
WHITE = (255,255,255)
BRIGHT_BLUE = (0,50,255)
D_BROWN = (210, 180, 140)
L_BANNER = (200, 180, 135)

DARK_TURQUOISE = (2,54,73)
GREEN = (0,230,0)
GREY = (119, 136, 153)
L_BROWN = (242, 229, 210)
SILVER = (192,192,192)
GOLD = (255, 215, 0)
SAND = (224, 195, 137)
D_BLUE = (70, 130, 180)
D_SILVER = (213, 213, 213)
OFF_WHITE = (1, 57, 94)

#SETTING COLOURS AND TEXT SIZES
BGCOLOUR = SAND
TEXT_COLOUR = WHITE
PRESSED_COLOUR = OFF_WHITE
BORDERCOLOUR = L_BROWN
BASIC_FONT_SIZE = 55
LARGE_FONT_SIZE = 100
SMALL_FONT_SIZE = 25
BUTTON_COLOUR = WHITE
BUTTON_TEXT_COLOUR = BLACK
MESSAGE_COLOUR = WHITE
BANNER = D_BLUE
YOU_WIN = D_BROWN

BLACK_KING = pygame.image.load("blackkingicon.png")
WHITE_KING = pygame.image.load("whitekingicon.png")
B_ARROW = pygame.image.load("b_arrow.png")




def main():
    #global variables used all across the program
    global FPS_CLOCK, BASIC_FONT, DISPLAY_SURF, FORFEIT_RECT, FORFEIT_TEXT, HOST_RECT, HOST_SURF, JOIN_RECT, JOIN_SURF, LARGE_FONT, CHESS_SURF, CHESS_RECT, SMALL_FONT, B_ARROW, B_ARROW_BUTTON, WOOD_TEX, START_SURF, START_RECT, IP_SURF, IP_RECT, IP_SURF2, IP_RECT2, PRESSED_COLOUR, BLACK_KING, WHITE_KING
    
    pygame.init()

    FPS_CLOCK = pygame.time.Clock() #amount of ticks per second
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #the surface of the entire screen
    pygame.display.set_caption("Chess") #window caption
    
    #the rect object behind the arrow itself used for interaction
    B_ARROW_BUTTON = pygame.draw.rect(DISPLAY_SURF, WHITE, (50,50, 141, 124)) 
    
    #initialization of the fonts
    BASIC_FONT = pygame.font.Font("freesansbold.ttf", BASIC_FONT_SIZE) 
    LARGE_FONT = pygame.font.Font("freesansbold.ttf", LARGE_FONT_SIZE)
    SMALL_FONT = pygame.font.Font("freesansbold.ttf", SMALL_FONT_SIZE)
    
    #global buttons to be used widely across the program
    HOST_SURF, HOST_RECT = makeText("Host", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-40, WINDOW_HEIGHT-375)
    JOIN_SURF, JOIN_RECT = makeText("Join ", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-40, (WINDOW_HEIGHT/2)-100)
    CHESS_SURF, CHESS_RECT = makeText("CHESS", LARGE_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, (WINDOW_WIDTH/3), WINDOW_HEIGHT/8-15)
    START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-100, (WINDOW_HEIGHT/2)-100)
    IP_SURF, IP_RECT = makeText("Your IP address is ", SMALL_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/10)-100, (WINDOW_HEIGHT)-250)
    IP_SURF2, IP_RECT2 = makeText(IP, SMALL_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-280, (WINDOW_HEIGHT)-250)
    
    #before loading chess the main menu must be called
    username()
    
    
    
def username():
    global USER_NAME
    USER_NAME = ""
    
    
    
    user_surf, user_rect = makeText("Enter a username", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, 272, (WINDOW_HEIGHT/2)-120)
    
    DISPLAY_SURF.fill(BGCOLOUR)
    pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
    DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
    pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
    pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
    pygame.draw.rect(DISPLAY_SURF, WHITE, (275, 345, 475, 70))
    DISPLAY_SURF.blit(user_surf, user_rect)
    DISPLAY_SURF.blit(BLACK_KING, [230, 32])
    DISPLAY_SURF.blit(WHITE_KING, [700, 32])
    
    pygame.display.flip()
    
    while True:
        
        checkForQuit()
        
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.unicode.isalnum() and len(USER_NAME) < 12:
                    USER_NAME += event.unicode
                elif event.key == K_BACKSPACE:
                    USER_NAME = USER_NAME[:-1]
                elif event.key == K_RETURN:
                    menu()
                
                DISPLAY_SURF.fill(BGCOLOUR)
                
                pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
                
                pygame.draw.rect(DISPLAY_SURF, WHITE, (275, 345, 475, 70)) #Text box
                
                pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
                pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
                DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
                DISPLAY_SURF.blit(user_surf, user_rect)
                
                DISPLAY_SURF.blit(BLACK_KING, [230, 32])
                DISPLAY_SURF.blit(WHITE_KING, [700, 32])
                     
                block =  BASIC_FONT.render(USER_NAME, True, (BLACK))
                rect = block.get_rect()
                
                
                rect.center = DISPLAY_SURF.get_rect().center
                DISPLAY_SURF.blit(block, rect)
                
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)
        
        
        
        
def menu():
    
    #main menu
    
    JOIN_SURF, JOIN_RECT = makeText("Join ", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, (WINDOW_HEIGHT/2)-100)
    HOST_SURF, HOST_RECT = makeText("Host", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, WINDOW_HEIGHT-375)
    
    while True:
        #print screen objects, background, buttons and text etc
        #keep in while loop or problems arise
        DISPLAY_SURF.fill(BGCOLOUR)
        pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
        
        
        
        
        #DISPLAY_SURF.blit(WOOD_TEX, [0,0])
        DISPLAY_SURF.blit(HOST_SURF, HOST_RECT)
        DISPLAY_SURF.blit(JOIN_SURF, JOIN_RECT)
        DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
        DISPLAY_SURF.blit(B_ARROW, [50, 50])
        DISPLAY_SURF.blit(BLACK_KING, [230, 32])
        DISPLAY_SURF.blit(WHITE_KING, [700, 32])
        
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
        
        checkForQuit()
        #check for mouse input/ if the buttons get clicked
        
        for event in pygame.event.get():
            
            if JOIN_RECT.collidepoint(pygame.mouse.get_pos()):
                JOIN_SURF, JOIN_RECT = makeText("Join ", BASIC_FONT_SIZE, PRESSED_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(JOIN_SURF, JOIN_RECT)
                pygame.display.flip()
                
            else:
                JOIN_SURF, JOIN_RECT = makeText("Join ", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(JOIN_SURF, JOIN_RECT)
                pygame.display.flip()
                
            if HOST_RECT.collidepoint(pygame.mouse.get_pos()):
                HOST_SURF, HOST_RECT = makeText("Host", BASIC_FONT_SIZE, PRESSED_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, WINDOW_HEIGHT-375)
                DISPLAY_SURF.blit(HOST_SURF, HOST_RECT)
                pygame.display.flip()
                
            else:
                HOST_SURF, HOST_RECT = makeText("Host", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, WINDOW_HEIGHT-375)
                DISPLAY_SURF.blit(HOST_SURF, HOST_RECT)
                pygame.display.flip()
                
            if event.type == MOUSEBUTTONUP:
                
                #JOIN BUTTON PRESSED
                if B_ARROW_BUTTON.collidepoint(event.pos):
                    username()
                
                elif JOIN_RECT.collidepoint(event.pos):
                    opp_ip_address = get_opp_ip() #can only come back with a valid ip address
                    
                    #for testing
                    print("Connecting to:", opp_ip_address, "...") 
                    print(IP)
                    
                #HOST BUTTON PRESSED
                elif HOST_RECT.collidepoint(event.pos):
                    HOST_SURF, HOST_RECT = makeText("Host", BASIC_FONT_SIZE, PRESSED_COLOUR, BANNER, (WINDOW_WIDTH/2)-45, WINDOW_HEIGHT-375)
                    DISPLAY_SURF.blit(HOST_SURF, HOST_RECT)
                    pygame.display.flip()
                    pygame.time.wait(100)
                    host_menu_screen()
                
        
        pygame.display.update() #updates the screen blits
        FPS_CLOCK.tick(FPS) #framerate tick
        
def checkForQuit():
    for event in pygame.event.get(QUIT): #get all the quit events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the keyup events
        if event.key == K_ESCAPE:
            terminate() # terminate if esc key pressed
        pygame.event.post(event) # put the other keyup event objects back


def terminate():
    pygame.quit()
    sys.exit()
    
def is_valid_ip(ip):
    #regular expression that matches valid ipv4 addresses only
    matchObj = re.match(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', ip, flags=0)
    if matchObj:
        return True
    
def get_opp_ip(retry = False): #Please enter an ip address
    
    opp_ip_surf, opp_ip_rect = makeText("Please enter an IP address below", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/10)-20, (WINDOW_HEIGHT/2)-100)
    invalid_ip_surf, invalid_ip_rect = makeText("Invalid IP address, try again", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/7), (WINDOW_HEIGHT/2)-100)
    
    ip = ""
    DISPLAY_SURF.fill(BGCOLOUR)
    
    pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
    
    if retry == False:
        DISPLAY_SURF.blit(opp_ip_surf, opp_ip_rect)
    else:
        DISPLAY_SURF.blit(invalid_ip_surf, invalid_ip_rect)
        
    DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
    DISPLAY_SURF.blit(B_ARROW, [50, 50])
    
    pygame.draw.rect(DISPLAY_SURF, WHITE, (275, 345, 475, 70))
    
    pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
    pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
    
    DISPLAY_SURF.blit(BLACK_KING, [230, 32])
    DISPLAY_SURF.blit(WHITE_KING, [700, 32])
        
    pygame.display.flip()
    
    while True:
        
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if B_ARROW_BUTTON.collidepoint(event.pos):
                    menu()
                
            if event.type == KEYDOWN:
                
                if event.unicode.isdigit() or event.key == K_PERIOD:
                    ip+= event.unicode
                elif event.key == K_BACKSPACE:
                    ip = ip[:-1]
                elif event.key == K_RETURN:
                    if is_valid_ip(ip):
                        connect(ip)
                    else:
                        get_opp_ip(True)
            
                DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
        
                pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
                
                pygame.draw.rect(DISPLAY_SURF, WHITE, (275, 345, 475, 70)) #Text box
                
                pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
                pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
                
                DISPLAY_SURF.blit(BLACK_KING, [230, 32])
                DISPLAY_SURF.blit(WHITE_KING, [700, 32])
        
                if retry == False:
                    DISPLAY_SURF.blit(opp_ip_surf, opp_ip_rect)
                else:
                    DISPLAY_SURF.blit(invalid_ip_surf, invalid_ip_rect)
                checkForQuit()
                block =  BASIC_FONT.render(ip, True, (BLACK))
                rect = block.get_rect()
                
                
                rect.center = DISPLAY_SURF.get_rect().center
                DISPLAY_SURF.blit(block, rect)
                pygame.display.flip()
                FPS_CLOCK.tick(FPS)
        
def host_menu_screen():
    
    START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-110, (WINDOW_HEIGHT/2)-100)
    
    while True:
        checkForQuit()
        DISPLAY_SURF.fill(BGCOLOUR)
        pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
        DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
        DISPLAY_SURF.blit(START_SURF, START_RECT)
        DISPLAY_SURF.blit(IP_SURF, IP_RECT)
        DISPLAY_SURF.blit(IP_SURF2, IP_RECT2)
        DISPLAY_SURF.blit(B_ARROW, [50, 50])
        
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
        
        DISPLAY_SURF.blit(BLACK_KING, [230, 32])
        DISPLAY_SURF.blit(WHITE_KING, [700, 32])
        
        pygame.display.flip()
        for event in pygame.event.get():
            if START_RECT.collidepoint(pygame.mouse.get_pos()):
                START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, PRESSED_COLOUR, BANNER, (WINDOW_WIDTH/2)-110, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(START_SURF, START_RECT)
                pygame.display.flip()
            else:
                START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-110, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(START_SURF, START_RECT)
                pygame.display.flip()
            
            if event.type == MOUSEBUTTONUP:
                if B_ARROW_BUTTON.collidepoint(event.pos):
                    return
                if START_RECT.collidepoint(event.pos):
                    chess()
            if event.type == KEYDOWN and event.key == K_RETURN:
                return
        
        FPS_CLOCK.tick(FPS)
           
def connect(ip):
    if True:
        successfulConnect()
    
    
def successfulConnect():
    
    con_surf, con_rect = makeText("Connected", SMALL_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/10)-100, (WINDOW_HEIGHT)-280)
    START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-100, (WINDOW_HEIGHT/2)-100)
    while True:
        checkForQuit()
        DISPLAY_SURF.fill(BGCOLOUR)
        pygame.draw.rect(DISPLAY_SURF, BANNER, (0, 200, WINDOW_WIDTH, 350))
        DISPLAY_SURF.blit(CHESS_SURF, CHESS_RECT)
        DISPLAY_SURF.blit(START_SURF, START_RECT)
        DISPLAY_SURF.blit(con_surf, con_rect)
        DISPLAY_SURF.blit(IP_SURF, IP_RECT)
        DISPLAY_SURF.blit(IP_SURF2, IP_RECT2)
        DISPLAY_SURF.blit(B_ARROW, [50, 50])
        
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
        
        DISPLAY_SURF.blit(BLACK_KING, [230, 32])
        DISPLAY_SURF.blit(WHITE_KING, [700, 32])
        
        pygame.display.flip()
        for event in pygame.event.get():
            if START_RECT.collidepoint(pygame.mouse.get_pos()):
                START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, PRESSED_COLOUR, BANNER, (WINDOW_WIDTH/2)-100, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(START_SURF, START_RECT)
                pygame.display.flip()
            else:
                START_SURF, START_RECT = makeText("Start ", LARGE_FONT_SIZE, TEXT_COLOUR, BANNER, (WINDOW_WIDTH/2)-100, (WINDOW_HEIGHT/2)-100)
                DISPLAY_SURF.blit(START_SURF, START_RECT)
                pygame.display.flip()
                
            
            if event.type == MOUSEBUTTONUP:
                if B_ARROW_BUTTON.collidepoint(event.pos):
                    menu()
                if START_RECT.collidepoint(event.pos):
                    
                    chess()
            if event.type == KEYDOWN and event.key == K_RETURN:
                return
        
        FPS_CLOCK.tick(FPS)
        
def chess():
    
    turn = "player 1"
    check = True
    
    counter = 60
    chess_board_img = pygame.image.load("chessboard.png")
    hourglass_img = pygame.image.load("hourglass.png")
    
    player1_surf, player1_rect = makeText("Player 1", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 430, 690)
    player2_surf, player2_rect = makeText("Player 2", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 430, 10)
    over_surf, over_rect = makeText("Player 1 wins!", LARGE_FONT_SIZE, TEXT_COLOUR, YOU_WIN, 180, 220)
    restart_surf, restart_rect = makeText("Restart", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 440, 370)
    con_ip_surf, con_ip_rect = makeText("Connect to another IP address", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 125, 450)
    check_surf, check_rect = makeText("Check!", BASIC_FONT_SIZE, TEXT_COLOUR, BANNER, 10, 125)
    
    
    DISPLAY_SURF.fill(BANNER)
    
    DISPLAY_SURF.blit(chess_board_img, [225, 85])
    DISPLAY_SURF.blit(hourglass_img, [860, 537])
    pygame.display.flip()
    
    while counter > 50:
        checkForQuit()
        counter -= 1 #timer
        
        timer_surf, timer_rect = makeText("00:" + str(counter), SMALL_FONT_SIZE, BLACK, BANNER, (WINDOW_WIDTH)-135, (WINDOW_HEIGHT)-280) #timer surface has to be reinitialized every loop to put new loop in
        
        DISPLAY_SURF.fill(BANNER)
        
        pygame.draw.rect(DISPLAY_SURF, BGCOLOUR, (0, 0, WINDOW_WIDTH, 85))
        pygame.draw.rect(DISPLAY_SURF, BGCOLOUR, (0, 671, WINDOW_WIDTH, 100))
        
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 85, WINDOW_WIDTH, 5))
        pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 671, WINDOW_WIDTH, 5))
        
        DISPLAY_SURF.blit(chess_board_img, [225, 85])
        DISPLAY_SURF.blit(hourglass_img, [860, 537])
        DISPLAY_SURF.blit(timer_surf, timer_rect)
        DISPLAY_SURF.blit(player1_surf, player1_rect)
        DISPLAY_SURF.blit(player2_surf, player2_rect)
        
        if check == True:
            DISPLAY_SURF.blit(check_surf, check_rect)
            
        pygame.display.flip()
        pygame.time.delay(1000)
        FPS_CLOCK.tick(FPS)
        
        
            
    
    if turn == "player 1":
        while True:
            checkForQuit()
            pygame.draw.rect(DISPLAY_SURF, YOU_WIN, (0, 200, WINDOW_WIDTH, 350))
            pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 200, WINDOW_WIDTH, 5))
            pygame.draw.rect(DISPLAY_SURF, BORDERCOLOUR, (0, 550, WINDOW_WIDTH, 5))
            DISPLAY_SURF.blit(over_surf, over_rect)
            DISPLAY_SURF.blit(restart_surf, restart_rect)
            DISPLAY_SURF.blit(con_ip_surf, con_ip_rect)
            
            for event in pygame.event.get():
                if restart_rect.collidepoint(pygame.mouse.get_pos()):
                    restart_surf, restart_rect = makeText("Restart", BASIC_FONT_SIZE, PRESSED_COLOUR, YOU_WIN, 440, 370)
                    DISPLAY_SURF.blit(restart_surf, restart_rect)
                    pygame.display.flip()
                else:
                    restart_surf, restart_rect = makeText("Restart", BASIC_FONT_SIZE, TEXT_COLOUR, YOU_WIN, 440, 370)
                    DISPLAY_SURF.blit(restart_surf, restart_rect)
                    pygame.display.flip()
                
                if con_ip_rect.collidepoint(pygame.mouse.get_pos()):
                    con_ip_surf, con_ip_rect = makeText("Connect to another IP address", BASIC_FONT_SIZE, PRESSED_COLOUR, YOU_WIN, 125, 450)
                    DISPLAY_SURF.blit(con_ip_surf, con_ip_rect)
                    pygame.display.flip()
                else:
                    con_ip_surf, con_ip_rect = makeText("Connect to another IP address", BASIC_FONT_SIZE, TEXT_COLOUR, YOU_WIN, 125, 450)
                    DISPLAY_SURF.blit(con_ip_surf, con_ip_rect)
                    pygame.display.flip()
                
                
                
                if event.type == MOUSEBUTTONUP:
                    if restart_rect.collidepoint(event.pos):
                        chess()
                    elif con_ip_rect.collidepoint(event.pos):
                        get_opp_ip()
                    
            
            pygame.display.flip()
            FPS_CLOCK.tick(FPS)
        
def makeText(text, size, color, BGCOLOUR, top, left):
    #create the Surface and Rect objects for some text
    if size == BASIC_FONT_SIZE:
        textSurf = BASIC_FONT.render(text, True, color, BGCOLOUR)
    elif size == LARGE_FONT_SIZE:
        textSurf = LARGE_FONT.render(text, True, color, BGCOLOUR)
    elif size == SMALL_FONT_SIZE:
        textSurf = SMALL_FONT.render(text, True, color, BGCOLOUR)
    
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    