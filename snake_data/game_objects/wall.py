import os, random
from snake_data.game_objects.rectangles import *
from snake_data.toolkit import *

class Wall(object):
    def __init__(self):
        self.__wall = {}

        wR_scale = Reponsity.rectangle_scale()
        wR_height_screen = Reponsity.height_screen()
        wR_width_screen = Reponsity.width_screen()

        responsyHeight = Reponsity.height_screen()//Reponsity.rectangle_scale()
        responsyWidth = Reponsity.width_screen()//Reponsity.rectangle_scale()

        coordinates = [(x*Reponsity.rectangle_scale(),0) for x in list(range(responsyWidth))]

        coordinates += [(0, y*wR_scale) for y in list(range(responsyHeight))]
        coordinates += [(x*wR_scale, wR_height_screen-wR_scale) for x in list(range(responsyWidth))]
        coordinates += [(wR_width_screen-wR_scale, y*wR_scale) for y in list(range(responsyHeight))]

        self.__wall = {coord : Rectangle((wR_scale,wR_scale)) for coord in coordinates}
        for key in self.__wall.keys():
            self.__wall[key].set_texture(ArtResource.image_load('box12.png'),(wR_scale,wR_scale))
            self.__wall[key].update(key)

    @property
    def wall(self):
        return self.__wall

if __name__ == '__main__':
    pass