import pygame
import random
import time

pygame.init()

# colors
grass_color = (65, 152, 10)
road_color = (90, 90, 90)

# display
res = (res_x, res_y) = (900, 800)
screen = pygame.display.set_mode(res)
screen.fill(grass_color)
pygame.display.set_caption("Racer")
pygame.display.set_icon(pygame.image.load("images/player_car.png"))

# setup
font = pygame.font.SysFont("helvetica", 64)
coins_amount = 0
clock = pygame.time.Clock()
running = True
speed = 2

# road
road_size = (road_width, road_height) = (450, 800)
road_surface = pygame.Surface(road_size)

# car
car_size = (car_width, car_height) = (80, 110)

# coin
coin_size = (coin_width, coin_height) = (32, 32)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player_car.png")
        self.image = pygame.transform.scale(self.image, car_size)
        self.rect = self.image.get_rect()
        self.rect.center = (road_width / 2, road_height - car_height)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not (self.rect.left < 0):
                self.rect.move_ip(-10, 0)
        if keys[pygame.K_RIGHT]:
            if not (self.rect.right > road_width):
                self.rect.move_ip(10, 0)
        # if keys[pygame.K_UP]:
        #     self.rect.move_ip(0, -5)
        # if keys[pygame.K_DOWN]:
        #     self.rect.move_ip(0, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy_car.png")
        self.image = pygame.transform.scale(self.image, car_size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(car_width, 300 - car_width), -50)

    def update(self):
        if self.rect.top > res_y:
            self.rect.center = (
                random.randint(car_width, road_width - car_width),
                -50,
            )
        self.rect.move_ip(0, speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, coin_size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(coin_width, 300 - coin_width), -100)

    def update(self):
        if self.rect.top > res_y:
            self.rect.center = (
                random.randint(coin_width, road_width - coin_width),
                -200,
            )
        self.rect.move_ip(0, speed + 3)

    def collected(self):
        self.rect.center = (
            random.randint(coin_width, road_width - coin_width),
            -200,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# objects
player = Player()
enemy = Enemy()
coin = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

# User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# difficulty
difficulty = 15

while running:
    screen.fill(grass_color)

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.1
        if event.type == pygame.QUIT:
            running = False

    # movement
    for entity in all_sprites:
        entity.update()
        entity.draw(road_surface)

    # road
    screen.blit(road_surface, (225, 0))
    road_surface.fill(road_color)

    # score
    score = font.render(str(coins_amount), True, (0, 0, 0))
    screen.blit(score, (res_x - 100, 20))

    # car collide
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound("sounds/car_crash.mp3").play()
        screen.fill((255, 0, 0))
        gameover_text = font.render("GAME OVER", True, (0, 0, 0))
        gameover_text_rect = gameover_text.get_rect(center=(res_x / 2, res_y / 2 - 20))
        score_text = font.render(f"Your score: {coins_amount}", True, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(res_x / 2, res_y / 2 + 40))
        screen.blit(gameover_text, gameover_text_rect)
        screen.blit(score_text, score_text_rect)

        pygame.display.flip()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        running = False

    # coin collect
    if pygame.sprite.spritecollideany(player, coins):
        coins_amount += random.randint(1, 5)
        for entity in coins:
            entity.collected()
        if coins_amount // difficulty == 1:
            speed += 2
            difficulty += 15

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
