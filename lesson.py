
import pygame

pygame.init()

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()
fps = 30


class Player:
    def __init__(self, x, y, width, height, color, up, down):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.up = up
        self.down = down

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

    def move(self, keys):
        if keys[self.up] and self.y > 0:
            self.y -= self.speed

        if keys[self.down] and self.y + self.height < screen_height:
            self.y += self.speed


player1 = Player(
    50, 50, 30, 100, white,
    pygame.K_UP, pygame.K_DOWN
)

player2 = Player(
    820, 50, 30, 100, white,
    pygame.K_w, pygame.K_s
)

ball = pygame.Rect(440, 340, 20, 20)
ball_x = 5
ball_y = 5

running = True

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player1.move(keys)
    player2.move(keys)

    ball.x += ball_x
    ball.y += ball_y

    # Отскок мяча от верхней и нижней границ
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_y *= -1

    rect1 = pygame.Rect(
        player1.x, player1.y,
        player1.width, player1.height
    )

    rect2 = pygame.Rect(
        player2.x, player2.y,
        player2.width, player2.height
    )

    # Столкновение мяча с игроками
    if ball.colliderect(rect1) and ball_x < 0:
        ball_x *= -1

    if ball.colliderect(rect2) and ball_x > 0:
        ball_x *= -1

    player1.draw(screen)
    player2.draw(screen)

    pygame.draw.rect(screen, white, ball)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()