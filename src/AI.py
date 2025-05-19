import pygame
import sys
import random

# Initialize
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQSIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)

# Load Images
x_img = pygame.image.load("X.png")
x_img = pygame.transform.scale(x_img, (SQSIZE, SQSIZE))

o_img = pygame.image.load("circle.png")
o_img = pygame.transform.scale(o_img, (SQSIZE, SQSIZE))

bg_img = pygame.image.load("track.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")
font = pygame.font.SysFont(None, 48)

# Game State
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
player_turn = True  # True = X, False = O (AI)
difficulty = "hard"  # Options: 'easy', 'medium', 'hard'
game_over = False

# Functions
def draw_board():
    screen.blit(bg_img, (0, 0))
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                screen.blit(x_img, (col * SQSIZE, row * SQSIZE))
            elif board[row][col] == "O":
                screen.blit(o_img, (col * SQSIZE, row * SQSIZE))

def get_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def board_full():
    return all(all(cell is not None for cell in row) for row in board)

def ai_move():
    empty = [(r, c) for r in range(ROWS) for c in range(COLS) if board[r][c] is None]

    if difficulty == "easy":
        return random.choice(empty)

    elif difficulty == "medium":
        # Try to win, else random
        for r, c in empty:
            board[r][c] = "O"
            if get_winner() == "O":
                return (r, c)
            board[r][c] = None
        return random.choice(empty)

    elif difficulty == "hard":
        return minimax(board, True)[1]

def minimax(state, is_maximizing):
    winner = get_winner()
    if winner == "O": return 1, None
    if winner == "X": return -1, None
    if board_full(): return 0, None

    moves = []
    for r in range(ROWS):
        for c in range(COLS):
            if state[r][c] is None:
                state[r][c] = "O" if is_maximizing else "X"
                score = minimax(state, not is_maximizing)[0]
                moves.append((score, (r, c)))
                state[r][c] = None

    if is_maximizing:
        return max(moves, key=lambda x: x[0])
    else:
        return min(moves, key=lambda x: x[0])

# Game loop
while True:
    screen.fill(WHITE)
    draw_board()

    if game_over:
        winner = get_winner()
        if winner:
            text = font.render(f"{winner} wins!", True, (0, 0, 0))
        else:
            text = font.render("It's a draw!", True, (0, 0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    else:
        if not player_turn:
            row, col = ai_move()
            board[row][col] = "O"
            player_turn = True
            if get_winner() or board_full():
                game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQSIZE, x // SQSIZE
            if board[row][col] is None:
                board[row][col] = "X"
                player_turn = False
                if get_winner() or board_full():
                    game_over = True

    pygame.display.flip()

