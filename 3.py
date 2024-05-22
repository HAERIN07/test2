import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_size = [500, 900]
screen = pygame.display.set_mode(screen_size)
title = "HANGMAN"
pygame.display.set_caption(title)

# 시간 관리를 위한 clock 객체 생성
clock = pygame.time.Clock()

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 폰트 설정
header_font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 80)
entry_font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 60)
note_font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 40)

# 함수: 튜플 내 모든 요소를 반올림하여 반환
def round_tuple(tup):
    rounded_list = [] 
    for value in tup:
        rounded_list.append(round(value))
    return tuple(rounded_list)

# 게임 진행을 관리하는 변수들 초기화
is_enter_pressed = False
is_drop = False
is_exit = False
k = 0
try_count = 0
entered_text = ""

# voca 파일을 읽어들임
word_file = open('voca.txt', 'r', encoding='UTF-8')
raw_data = word_file.read()
word_file.close()
word_list = raw_data.split('\n')
word_list = word_list[:-1]  # 마지막 공백 줄 제거

# 게임 루프
while not is_exit:
    # 단어 목록에서 랜덤으로 단어 선택
    random_index = random.randrange(0, len(word_list))
    selected_word = word_list[random_index].replace(u"\xa0", u" ").split(' ')[1]
    if len(selected_word) <= 6:  # 단어 길이가 6 이하인 경우에만 선택
        break
selected_word = selected_word.upper()  # 선택된 단어를 대문자로 변환

# 선택된 단어와 같은 길이의 밑줄 문자열 생성
word_display = "_" * len(selected_word)
try_count = 0
correct_letters = []
wrong_letters = []

# 게임 루프
while not is_exit:
    clock.tick(60)  # FPS 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_exit = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if (key_name == "return" or key_name == "enter"):
                if entered_text != '' and (correct_letters + wrong_letters).count(entered_text) == 0:
                    is_enter_pressed = True
            elif len(key_name) == 1:
                if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                    entered_text = key_name.upper()
                else:
                    entered_text = ''
            else:
                entered_text = ''

    if try_count == 8:
        k + 1
    if is_enter_pressed == True:
        ans = entered_text
        result = selected_word.find(ans)
        if result == -1:
            try_count += 1
            wrong_letters.append(ans)
        else:
            correct_letters.append(ans)
            for i in range(len(selected_word)):
                if selected_word[i] == ans:
                    word_display = word_display[:i] + ans + word_display[i + 1:]
        is_enter_pressed = False
        entered_text = ''

    k = k + 1
    screen.fill(white)

    # 거꾸로 떨어지는 그림 그리기
    A = round_tuple((0, screen_size[1] * 2 / 3))
    B = (screen_size[0], A[1])
    C = (screen_size[0] / 6, A[1])
    D = (C[0], C[0])
    E = round_tuple((screen_size[0] / 2, D[1]))   
    pygame.draw.line(screen, black, A, B, 3)
    pygame.draw.line(screen, black, C, D, 3)
    pygame.draw.line(screen, black, D, E, 3)
    F = (E[0], E[1] + C[0])

    if is_drop == False:
        pygame.draw.line(screen, black, E, F, 3)
    head = round(screen_size[0] / 12)
    if is_drop == True: 
        G = (F[0], F[1] + head + k * 5)
    else:  
        G = (F[0], F[1] + head)

    if try_count >= 1:
        pygame.draw.circle(screen, black, G, head, 3)

    # 아래로 떨어지는 그림 그리기
    H = (G[0], G[1] + head)
    I = (H[0], H[1] + head / 2)
    if try_count >= 2: 
        pygame.draw.line(screen, black, I, H, 3)
    J = (I[0], I[1] + head * 2)
    if try_count >= 3: 
        pygame.draw.line(screen, black, I, J, 3)
    K = (J[0] - head, I[1] + head)
    if try_count >= 4: 
        pygame.draw.line(screen, black, I, K, 3)
    L = (J[0] + head, K[1])
    if try_count >= 5: 
        pygame.draw.line(screen, black, I, L, 3)
    M = (J[0] - head, J[1] + head)
    if try_count >= 6: 
        pygame.draw.line(screen, black, J, M, 3)
    N = (J[0] + head, M[1])
    if try_count >= 7: 
        pygame.draw.line(screen, black, J, N, 3)

    # 거꾸로 떨어지는 그림의 줄이 끝까지 도달했을 때, 빨간 줄 그리기
    if is_drop == False and try_count == 8:
        O = (F[0] - C[0], F[1])
        P = (O[0] + k * 2, O[1])
        if P[0] >= E[0] + C[0]:
            is_drop = True
            k = 0
        pygame.draw.line(screen, red, O, P, 3)

    # 단어 힌트를 화면에 표시
    hint = header_font.render(word_display, True, black)
    h_size = hint.get_size()
    h_pos = round_tuple((screen_size[0] / 2 - h_size[0] / 2, screen_size[1] * 5 / 6 - h_size[1] / 2))
    screen.blit(hint, h_pos)

    # 입력된 글자를 화면에 표시
    entry = entry_font.render(entered_text, True, white)
    e_size = entry.get_size()
    e_pos = round_tuple((screen_size[0] / 2 - e_size[0] / 2, screen_size[1] * 17 / 18 - e_size[1] / 3))
    e_bg_size = 80
    pygame.draw.rect(screen, black, (screen_size[0] / 2 - e_bg_size / 2, screen_size[1] - e_bg_size, e_bg_size, e_bg_size))
    screen.blit(entry, e_pos)

    # 틀린 글자 목록을 화면에 표시
    wrong_text = ''.join(wrong_letters)
    wrong_rendered = note_font.render(wrong_text, True, red)
    wrong_pos = round_tuple((20, screen_size[1] * 2 / 3 + 20))
    screen.blit(wrong_rendered, wrong_pos)

    pygame.display.flip()  # 화면 업데이트

pygame.quit()  # Pygame 종료

