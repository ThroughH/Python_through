import pygame
pygame.init()

# 스크린 정의
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode([screen_width, screen_height])

# 게임 이름
pygame.display.set_caption("Through Bubble Game")

# 배경 이미지
background = pygame.image.load("C:/data/Python/Test/background.jpg")

# 게임 주인공
hero = pygame.image.load("C:/data/Python/Test/hero.png")
hero_size = hero.get_rect().size
hero_width = hero_size[0]
hero_height = hero_size[1]
hero_x_pos = screen_width / 2 - hero_width / 2 #주인공 가로 위치
hero_y_pos = screen_height - hero_height #주인공 세로 위치

print (hero_x_pos)
# 게임 실행
running = True
while running:

    # 게임 종료 조건
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 백그라운드 불러오기
    screen.blit(background, (0, 0))

    # 주인공 그리기
    screen.blit(hero, (hero_x_pos, hero_y_pos))

    # 화면 다시 그리기
    pygame.display.flip()

# 게임 종료
pygame.quit()
