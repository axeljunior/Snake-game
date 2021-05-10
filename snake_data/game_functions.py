import pygame, os, time

from snake_data.toolkit import *

from snake_data.game_objects.rectangles import *
from snake_data.game_objects.snake import *
from snake_data.game_objects.wall import *
from snake_data.game_objects.food import *

class Game_Screens(object):
    def __init__(self, **objectScene):
        wScreen = Responsivity.width_screen()
        hScreen = Responsivity.height_screen()

        self.screen = pygame.display.set_mode((wScreen, 550))
        pygame.display.set_caption("Snake Game")
        
        self.objectScene = objectScene

        self.ground = Rectangle((25,25))
        self.ground.set_texture(ArtResource.image_load('ground1.png'),(wScreen, hScreen))

        self.background = Rectangle((25,25))
        self.background.set_texture(ArtResource.image_load('menurun.jpg'),(wScreen, 70))
        self.background.update((0,480))

    def stamp_screen(self):
        self.screen.fill((0,0,0))

        self.__blit(self.ground.image,self.ground.rect)
        
        self.__blit(self.background.image,self.background.rect)

        for coordinates in list(self.objectScene['wall'].wall.keys()):
            self.__blit(self.objectScene['wall'].wall[coordinates].image,
                    self.objectScene['wall'].wall[coordinates].rect)
          
        self.__draw(self.objectScene['food'].foodCollor,self.objectScene['food'].food)

        self.__draw(self.objectScene['snake'].snakeCollor,self.objectScene['snake'].snakeHead)
        for count,snakePart in enumerate(list(range(self.objectScene['snake'].size))):
            self.__draw(Collors.change_collor(tam=count,cor=self.objectScene['snake'].snakeCollor),
                    self.objectScene['snake'].snakeBody[snakePart])

        self.__score(self.objectScene['snake'].size)

    def __score(self,score):    
        Text.draw_text(self.screen,f'PONTOS: {score-2}',Collors.collor('white'),(600,500),filefont='Pixeled.ttf')

    def __draw(self,objectCollor,objectRectangle):
        if isinstance(objectCollor, str):
            pygame.draw.rect(self.screen, Collors.collor(objectCollor), objectRectangle)
        else:
            pygame.draw.rect(self.screen, objectCollor, objectRectangle)

    def __blit(self,objectImage,objectRect):
        self.screen.blit(objectImage,objectRect)
        

class Collider(object):
    def __init__(self, **colliders):
        self.colliders = colliders

    def collision_calculate(self,IMORTAL=False):
        body = self.colliders['snake'].snakeBody
        wall = list(self.colliders['wall'].wall.values())
        food = self.colliders['food'].food

        if self.colliders['snake'].snakeHead.rect.collidepoint(food.rect.center):
            self.colliders['snake'].eating(self.colliders['food'].foodCollor)
            ArtResource.sound_play_sfx('sfx_point')
            self.colliders['food'].new_food_position(self.colliders['snake'].snakeCoordinates,self.colliders['wall'].centralCoordinates)
        
        for obstacle in wall:
            if self.colliders['snake'].snakeHead.rect.contains(obstacle.rect):
                ArtResource.sound_play_sfx('sfx_hit')
                time.sleep(0.15)
                if IMORTAL:
                    print('MORREU MURO')
                else:
                    self.colliders['snake'].snakeViva = False
        
        for obstacle in body:
            if self.colliders['snake'].snakeHead.rect.contains(obstacle.rect):
                ArtResource.sound_play_sfx('sfx_hit')
                time.sleep(0.15)
                if IMORTAL:
                    print('MORREU CORPO')
                else:
                    self.colliders['snake'].snakeViva = False

if __name__ == '__main__':
    pass