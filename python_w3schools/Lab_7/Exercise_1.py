import pygame
import datetime

# time

system_time = datetime.datetime.now()

system_time_second = system_time.strftime("%S")
system_time_second = int(system_time_second)

system_time_minute = system_time.strftime("%M")
system_time_minute = int(system_time_minute)

pygame.init()
running = True
res_x = 700
res_y = 700
screen = pygame.display.set_mode((res_x, res_y))
clock = pygame.time.Clock()

# minute
minute = pygame.image.load("images/minute.png").convert_alpha()
angle_m = system_time_minute * -6
print(angle_m)
rotate_minute = pygame.transform.rotate(minute, angle_m)

# mickey
mickey = pygame.image.load("images/mickey1.png").convert_alpha()
mickey = pygame.transform.scale(mickey, (res_x, res_y))

# second
second = pygame.image.load("images/second.png").convert_alpha()
angle_s = system_time_second * -6
print(system_time_second)
print(angle_s)
rotate_second = pygame.transform.rotate(second, angle_s + 55)


while running:
    system_time = datetime.datetime.now()
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER

    screen.blit(mickey, (0, 0))

    rotate_minute = pygame.transform.rotate(minute, angle_m)

    system_time_minute = system_time.strftime("%M")
    system_time_minute = int(system_time_minute)

    angle_m = system_time_minute * -6
    minute_rectt = rotate_minute.get_rect(center=(res_x / 2, res_y / 2))
    screen.blit(rotate_minute, minute_rectt)

    system_time_second = system_time.strftime("%S")
    system_time_second = int(system_time_second)

    rotate_second = pygame.transform.rotate(second, angle_s)

    angle_s = system_time_second * -6 + 32
    second_rect = rotate_second.get_rect(center=(res_x / 2, res_y / 2))
    screen.blit(rotate_second, second_rect)

    # FPS

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
