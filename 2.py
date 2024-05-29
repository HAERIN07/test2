import pygame
import sys

# 화면 크기 및 색상 정의
WIDTH, HEIGHT = 300, 300  # 화면 크기 변경
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (100, 100, 100)
WIN_COLOR = (255, 0, 0)  # 승리 메시지 색상 (빨간색)
DRAW_COLOR = (0, 0, 255)  # 무승부 메시지 색상 (파란색)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# 보드 초기화
board = [[' ' for _ in range(3)] for _ in range(3)]  # 보드 크기 변경

# 보드 그리기
def draw_board():
    screen.fill(WHITE)
    # 가로 선
    for i in range(1, 3):  # 범위 변경
        pygame.draw.line(screen, LINE_COLOR, (0, i * 100), (500, i * 100), 3)  # 좌표 및 선 굵기 변경
    # 세로 선
    for i in range(1, 3):  # 범위 변경
        pygame.draw.line(screen, LINE_COLOR, (i * 100, 0), (i * 100, 500), 3)  # 좌표 및 선 굵기 변경
    # 현재 상태 표시
    for row in range(3):  # 범위 변경
        for col in range(3):  # 범위 변경
            if board[row][col] != ' ':
                font = pygame.font.SysFont(None, 80)  # 폰트 크기 변경
                text = font.render(board[row][col], True, BLACK)
                text_rect = text.get_rect(center=(col * 100 + 50, row * 100 + 50))  # 좌표 및 크기 변경
                screen.blit(text, text_rect)

# 승리 여부 확인
def check_win(player):
    for row in range(3):  # 범위 변경
        if all(board[row][col] == player for col in range(3)):  # 범위 변경
            return True
    for col in range(3):  # 범위 변경
        if all(board[row][col] == player for row in range(3)):  # 범위 변경
            return True
    if all(board[i][i] == player for i in range(3)):  # 범위 변경
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # 범위 변경
        return True
    return False

# 게임 루프
current_player = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 100, x // 100  # 좌표 및 크기 변경
            if board[row][col] == ' ':
                board[row][col] = current_player
                if check_win(current_player):
                    draw_board()
                    pygame.display.flip()
                    font = pygame.font.SysFont(None, 80)
                    text = font.render(f"Player {current_player} wins!", True, WIN_COLOR)
                    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    screen.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(3000)  # 3초 대기
                    running = False
                elif all(board[row][col] != ' ' for row in range(3) for col in range(3)):  # 범위 변경
                    draw_board()
                    pygame.display.flip()
                    font = pygame.font.SysFont(None, 80)
                    text = font.render("It's a draw!", True, DRAW_COLOR)
                    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    screen.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(3000)  # 3초 대기
                    running = False
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    pygame.display.flip()
    clock.tick(30)


