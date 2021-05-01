import random
from snake_data.toolkit import *
from snake_data.game_objects.rectangles import *

class Food(object):
    def __init__(self):
        
        self.__rectScale = (Reponsity.rectangle_scale(),Reponsity.rectangle_scale())
        self.__responsyHeight = Reponsity.height_screen()//Reponsity.rectangle_scale()
        self.__responsyWidth = Reponsity.width_screen()//Reponsity.rectangle_scale()
         
        self.__foodCollor = 'red'
        self.__xFood = (random.randint(1, self.__responsyWidth-2))*self.__rectScale[0]
        self.__yFood = (random.randint(1, self.__responsyHeight-2))*self.__rectScale[0]
        self.__food = Rectangle(self.__rectScale,(self.__xFood, self.__yFood))
        self.__food = Rectangle(self.__rectScale)
        self.__food.update((self.__xFood, self.__yFood))

    def new_food_position(self,blockSpace):
        self.__xFood, self.__yFood = ((random.randint(1,self.__responsyWidth-2))*self.__rectScale[0],
                                    (random.randint(1,self.__responsyHeight-2))*self.__rectScale[0])

        if (self.__xFood, self.__yFood) not in set(blockSpace):
            self.__food.update((self.__xFood, self.__yFood))
        else:
            self.new_food_position(blockSpace)

    @property
    def food(self):
        return self.__food
    @property
    def foodCollor(self):
        return self.__foodCollor
    @foodCollor.setter
    def foodCollor(self, newCollor):
        self.__foodCollor = newCollor

if __name__ == '__main__':
    pass