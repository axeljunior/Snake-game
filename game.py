import pygame, sys, os, time, random
from pygame.locals import *

from snake_data.toolkit import *
# from snake_data.lab import *
from snake_data.game_functions import *

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

def game_snake():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    timer = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()

    ArtResource.sound_add_sfx('sfx_point','wav')
    ArtResource.sound_add_sfx('sfx_hit','wav',0.4)
    ArtResource.sound_add_bgm('s_gamerun','mp3',0.25)

    player = Snake((240,360))
    scenery = Wall()
    food = Food()

    collider = Collider(snake=player, wall=scenery, food=food)
    updateScreen = Game_Screens(snake=player, wall=scenery, food=food)

    ArtResource.sound_play_bgm()

    IMORTAL = False
    while player.snakeViva:
        timer.tick(15)
        updateScreen.stamp_screen()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w and player.orientation != 'Down':
                    player.orientation = 'Up'
                    break
                elif event.key == K_a and player.orientation != 'Right': 
                    player.orientation = 'Left'
                    break
                elif event.key == K_s and player.orientation != 'Up': 
                    player.orientation = 'Down'
                    break
                elif event.key == K_d and player.orientation != 'Left':  
                    player.orientation = 'Right'
                    break
                elif event.key == K_0:
                    if IMORTAL:
                        IMORTAL=False
                        print('IMORTAL off')
                    else:
                        IMORTAL=True
                        print('IMORTAL on')

        collider.collision_calculate(IMORTAL=IMORTAL)
        player.move_snake()
        pygame.display.flip()

game_snake()