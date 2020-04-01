import pygame
import random

# constants
SQUARE_SIZE = 64
TILES_COUNT = 3


# initialize pygame
pygame.init()

# change title and display
pygame.display.set_caption('Sliding Tiles')

# game variables
board_final_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

board_initial_state = [
    [1, 0, 2],
    [3, 4, 5],
    [6, 7, 8]
]

GAME_RUNNING_STATUS = True
GAME_END_DISPLAY = False

IMG_num_1 = pygame.image.load('pictures/one.png')
IMG_num_2 = pygame.image.load('pictures/two.png')
IMG_num_3 = pygame.image.load('pictures/three.png')
IMG_num_4 = pygame.image.load('pictures/four.png')
IMG_num_5 = pygame.image.load('pictures/five.png')
IMG_num_6 = pygame.image.load('pictures/six.png')
IMG_num_7 = pygame.image.load('pictures/seven.png')
IMG_num_8 = pygame.image.load('pictures/eight.png')
IMG_num_9 = pygame.image.load('pictures/nine.png')


# display logic
display_width = SQUARE_SIZE*TILES_COUNT
display_height = SQUARE_SIZE*TILES_COUNT
moves_count = 0

screen = pygame.display.set_mode((display_width, display_height))

# font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


# create a display
def initialize_board():
    rand_numbers = random.sample(range(0, 9), 9)
    for i in range(len(board_initial_state)):
        for j in range(len(board_initial_state[i])):
            board_initial_state[i][j] = rand_numbers[i*len(board_initial_state) + j]


def is_finished():
    if board_initial_state == board_final_state:
        return True


def draw_number(img, x, y):
    screen.blit(img, (x, y))


def get_board_index_by_position(x, y):
    return int(x/SQUARE_SIZE), int(y/SQUARE_SIZE)


def draw_board():
    for i in range(len(board_initial_state)):
        for j in range(len(board_initial_state[i])):
            if board_initial_state[i][j] == 1:
                draw_number(IMG_num_1, j*SQUARE_SIZE, i*SQUARE_SIZE)
            if board_initial_state[i][j] == 2:
                draw_number(IMG_num_2, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 3:
                draw_number(IMG_num_3, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 4:
                draw_number(IMG_num_4, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 5:
                draw_number(IMG_num_5, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 6:
                draw_number(IMG_num_6, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 7:
                draw_number(IMG_num_7, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 8:
                draw_number(IMG_num_8, j * SQUARE_SIZE, i * SQUARE_SIZE)
            if board_initial_state[i][j] == 9:
                draw_number(IMG_num_9, j * SQUARE_SIZE, i * SQUARE_SIZE)


def show_ending():
    screen.fill((0, 0, 0))
    end_text = myfont.render('Total Moves: ' + str(moves_count), False, (0, 0, 255))
    screen.blit(end_text, (0, display_width/2))


initialize_board()
# game loop
while GAME_RUNNING_STATUS:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING_STATUS = False

        if event.type == pygame.MOUSEBUTTONDOWN and not GAME_END_DISPLAY:
            print(pygame.mouse.get_pos())
            j, i = get_board_index_by_position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if i-1 >= 0 and board_initial_state[i-1][j] == 0:
                board_initial_state[i-1][j] = board_initial_state[i][j]
                board_initial_state[i][j] = 0
                moves_count += 1
            elif i+1 < TILES_COUNT and board_initial_state[i+1][j] == 0:
                board_initial_state[i+1][j] = board_initial_state[i][j]
                board_initial_state[i][j] = 0
                moves_count += 1
            elif j-1 >= 0 and board_initial_state[i][j-1] == 0:
                board_initial_state[i][j-1] = board_initial_state[i][j]
                board_initial_state[i][j] = 0
                moves_count += 1
            elif j+1 < TILES_COUNT and board_initial_state[i][j+1] == 0:
                board_initial_state[i][j+1] = board_initial_state[i][j]
                board_initial_state[i][j] = 0
                moves_count += 1

            print(is_finished())
            if is_finished():
                GAME_END_DISPLAY = True
                show_ending()

    if not GAME_END_DISPLAY:
        draw_board()
    else:
        show_ending()
    pygame.display.update()
