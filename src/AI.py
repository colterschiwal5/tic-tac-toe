import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 15

# Colors
WHITE = (255, 255, 255)

# Load images
X_IMG = pygame.image.load("X1.png")
O_IMG = pygame.image.load("circle1.png")
BOARD_IMG = pygame.image.load("track1.png")

# Resize images
X_IMG = pygame.transform.scale(X_IMG, (CELL_SIZE, CELL_SIZE))
O_IMG = pygame.transform.scale(O_IMG, (CELL_SIZE, CELL_SIZE))
BOARD_IMG = pygame.transform.scale(BOARD_IMG, (WIDTH, HEIGHT))

# Game variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.SysFont(None, 48)

# Board state
board = [["" for _ in range(3)] for _ in range(3)]
player_turn = "X"  # "X" always goes first


def draw_board():
    screen.blit(BOARD_IMG, (0, 0))
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                screen.blit(X_IMG, (col * CELL_SIZE, row * CELL_SIZE))
            elif board[row][col] == "O":
                screen.blit(O_IMG, (col * CELL_SIZE, row * CELL_SIZE))


def check_winner():
    # Check rows, cols and diagonals
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    for row in board:
        for cell in row:
            if cell == "":
                return None  # game still going

    return "Draw"  # No empty cells and no winner


def ai_move():
    best_score = -float('inf')
    best_move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = ""
                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    return best_move

def minimax(board_state, depth, is_maximizing):
    result = check_winner()
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "O"
                    score = minimax(board_state, depth + 1, False)
                    board_state[r][c] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "X"
                    score = minimax(board_state, depth + 1, True)
                    board_state[r][c] = ""
                    best_score = min(score, best_score)
        return best_score

def reset():
    global board, player_turn
    board = [["" for _ in range(3)] for _ in range(3)]
    player_turn = "X"


def run_game(mode="pvai"):
    global player_turn
    reset()
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        screen.fill(WHITE)
        draw_board()
        winner = check_winner()

        if winner:
            msg = f"{winner} wins!" if winner != "Draw" else "Draw!"
            text = font.render(msg, True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        else:
            if mode == "aivai" or (mode == "pvai" and player_turn == "O"):
                pygame.time.delay(500)
                move = ai_move()
                if move:
                    r, c = move
                    board[r][c] = player_turn
                    player_turn = "O" if player_turn == "X" else "X"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                if (mode == "pvp") or (mode == "pvai" and player_turn == "X"):
                    x, y = pygame.mouse.get_pos()
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    if board[row][col] == "":
                        board[row][col] = player_turn
                        player_turn = "O" if player_turn == "X" else "X"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()

        pygame.display.update()
