
import pygame, os, time, random
from pygame.locals import *

from snake_data.toolkit import *
from snake_data.lab import *
from snake_data.game_functions import *

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
                if event.key == K_a and player.orientation != 'Right':            
                    player.orientation = 'Left'
                if event.key == K_s and player.orientation != 'Up':             
                    player.orientation = 'Down'
                if event.key == K_d and player.orientation != 'Left':          
                    player.orientation = 'Right'

        collider.collision_calculate()
        player.move_snake()
        pygame.display.flip()

game_snake()