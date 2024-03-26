import pygame
import os

pygame.init()

# SETUP

res_x, res_y = 600, 600
screen = pygame.display.set_mode((res_x, res_y))
clock = pygame.time.Clock()
running = 1

# MUSIC

music_path = "music/"
musics = [music for music in os.listdir(music_path)]
music_position = 0
pygame.mixer.music.load(music_path + musics[music_position])
pygame.mixer.music.play()
pygame.mixer.music.pause()
music_name = musics[music_position][0 : len(musics[music_position]) - 4]

# FONT

font = pygame.font.SysFont("timesnewroman", 32)
text = font.render(music_name, True, "black")

# IMAGES

image1 = pygame.image.load("images/play-solid.svg")
image1 = pygame.transform.scale(image1, (50, 60))
image1_rect = image1.get_rect(center=(res_x / 2, res_y / 2 + 40))
image2 = pygame.image.load("images/pause-solid.svg")
image2 = pygame.transform.scale(image2, (50, 60))
image2_rect = image2.get_rect(center=(res_x / 2, res_y / 2 + 40))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                if music_position + 1 == len(musics):
                    music_position = 0
                else:
                    music_position += 1
                pygame.mixer.music.load(music_path + musics[music_position])
                music_name = musics[music_position][0 : len(musics[music_position]) - 4]
                text = font.render(music_name, True, "black")
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                if music_position == 0:
                    music_position = len(musics) - 1
                else:
                    music_position -= 1
                pygame.mixer.music.load(music_path + musics[music_position])
                music_name = musics[music_position][0 : len(musics[music_position]) - 4]
                text = font.render(music_name, True, "black")
                pygame.mixer.music.play()

    # RENSER

    text_rect = text.get_rect(center=(res_x / 2, res_y / 2 - 30))
    screen.fill("white")
    screen.blit(text, text_rect)
    if pygame.mixer.music.get_busy():
        screen.blit(image2, image2_rect)
    else:
        screen.blit(image1, image1_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
