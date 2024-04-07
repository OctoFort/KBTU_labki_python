import pygame
import random
import time

pygame.init()

res = (res_x, res_y) = (600, 600)
screen = pygame.display.set_mode(res)
screen.fill("white")
running = True
clock = pygame.time.Clock()
score = 0
level = 0
font = pygame.font.SysFont("Helvetica", 32)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.direct = self.x_motion, self.y_motion = 0, 0
        self.segments = [
            pygame.Rect(
                50 * random.randint(1, 10),
                50 * random.randint(1, 10),
                self.x,
                self.y,
            )
        ]
        self.grow = False

    def direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x_motion == 0:
            self.direct = self.x_motion, self.y_motion = -50, 0
        if keys[pygame.K_RIGHT] and self.x_motion == 0:
            self.direct = self.x_motion, self.y_motion = 50, 0
        if keys[pygame.K_UP] and self.y_motion == 0:
            self.direct = self.x_motion, self.y_motion = 0, -50
        if keys[pygame.K_DOWN] and self.y_motion == 0:
            self.direct = self.x_motion, self.y_motion = 0, 50

    def move(self):
        if self.direct != (0, 0):
            new_head = self.segments[0].copy()
            new_head.move_ip(self.direct)
            self.segments.insert(0, new_head)
            if not self.grow:
                self.segments.pop()
            self.grow = False

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, "green", segment)
        pygame.draw.rect(screen, (0, 220, 0), self.segments[0])

    def get_head_sprite(self):
        head_sprite = pygame.sprite.Sprite()
        head_sprite.rect = self.segments[0]
        return head_sprite


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.surface = pygame.Surface((self.x, self.y))
        self.surface.fill("red")
        self.rect = self.surface.get_rect()
        self.rect.center = (
            25 + 50 * random.randint(1, 10),
            25 + 50 * random.randint(1, 10),
        )

    def move(self):
        self.rect.center = (
            25 + 50 * random.randint(1, 10),
            25 + 50 * random.randint(1, 10),
        )

    def draw(self):
        screen.blit(self.surface, self.rect)


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, center):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = pygame.Surface((self.x, self.y))
        self.surface.fill("blue")
        self.rect = self.surface.get_rect()
        self.rect.center = center

    def draw(self):
        screen.blit(self.surface, self.rect)


head = Snake()
apple = Fruit()
fruits = pygame.sprite.Group()
fruits.add(apple)

border_left = Border(50, 600, (25, res_y / 2))
border_right = Border(50, 600, (res_x - 25, res_y / 2))
border_up = Border(600, 50, (res_x / 2, 25))
border_down = Border(600, 50, (res_x / 2, res_y - 25))
borders = pygame.sprite.Group()
borders.add(border_left, border_right, border_up, border_down)

# custom event
FRUIT_RESPAWN = pygame.USEREVENT + 1


while running:
    for event in pygame.event.get():
        if event.type == FRUIT_RESPAWN:
            apple.move()
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # rendering
    for border in borders:
        border.draw()

    apple.draw()

    head.direction()
    head.move()
    head.draw()

    # text
    text = font.render(str(score), True, "black")
    text2 = font.render(f"level: {level}", True, "black")
    screen.blit(text, (res_x - 40, 20))
    screen.blit(text2, (20, 20))

    # collision
    head_sprite = head.get_head_sprite()
    if pygame.sprite.spritecollideany(head_sprite, fruits):
        apple.move()

        score += 1
        level = score // 4
        head.grow = True
        # Timer
        pygame.time.set_timer(FRUIT_RESPAWN, 9000 - level * 1000)

    if (
        pygame.sprite.spritecollideany(head_sprite, borders)
        or head.segments[0].collidelist(head.segments[1:]) != -1
    ):
        pygame.mixer.Sound("sounds/car_crash.mp3").play()
        screen.fill((255, 0, 0))
        gameover_text = font.render("GAME OVER", True, (0, 0, 0))
        gameover_text_rect = gameover_text.get_rect(center=(res_x / 2, res_y / 2 - 40))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(res_x / 2, res_y / 2 - 5))
        screen.blit(gameover_text, gameover_text_rect)
        screen.blit(score_text, score_text_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False

    pygame.display.flip()
    clock.tick(3 + level)

pygame.quit()
