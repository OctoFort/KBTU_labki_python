import pygame

# SETUP
pygame.init()
res_x = 900
res_y = 720
screen = pygame.display.set_mode((res_x, res_y))
screen_color = (255, 255, 255)
clock = pygame.time.Clock()
running = True

# CIRCLE
speed = 5
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
circle_color = (255, 0, 0)
circle_radius = 25

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(screen_color)

    # RENDER

    pygame.draw.circle(screen, circle_color, player_pos, circle_radius)

    # CONTROLS

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not player_pos.y <= circle_radius:
            player_pos.y -= speed
    if keys[pygame.K_DOWN]:
        if not player_pos.y >= res_y - circle_radius:
            player_pos.y += speed
    if keys[pygame.K_LEFT]:
        if not player_pos.x <= circle_radius:
            player_pos.x -= speed
    if keys[pygame.K_RIGHT]:
        if not player_pos.x >= res_x - circle_radius:
            player_pos.x += speed

    # FPS

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
