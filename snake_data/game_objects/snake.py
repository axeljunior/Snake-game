<<<<<<< HEAD
from snake_data.game_objects.rectangles import *
from snake_data.toolkit import *


class Snake(object):
    def __init__(self, startPosition):
        self.__scale = Responsivity.rectangle_scale()
        self.__size = 3
        self.__snakeCollor = 'violet'
        self.__snakeViva = True
        self.__orientation = 'Right'
        self.__snakeCoordinates = []
        self.__snakeCoordinates.append(startPosition)
        self.__xHead, self.__yHead = startPosition

        self.__snakeHead = Rectangle(area=(self.__scale,self.__scale), position=startPosition)
        self.__snakeBody = [Rectangle(area=(self.__scale,self.__scale), position=(self.__xHead-self.__scale*num,self.__yHead)) 
                                    for num in list(range(1,self.__size))]

        self.__snakeCoordinates.extend([(self.__xHead-self.__scale*num,self.__yHead) 
                                        for num in list(range(1,self.__size))])


    def move_snake(self):
        self.__snakeBody.insert(0,Rectangle(area=(self.__scale,self.__scale),position=(self.__xHead,self.__yHead)))
        self.__snakeCoordinates.insert(0,(self.__xHead,self.__yHead))
        self.__snakeBody.pop()
        self.__snakeCoordinates.pop()

        if self.orientation == 'Left':
            self.__xHead-=self.__scale           
        elif self.orientation == 'Right':
            self.__xHead+=self.__scale           
        elif self.orientation == 'Up':
            self.__yHead-=self.__scale           
        elif self.orientation == 'Down':
            self.__yHead+=self.__scale

        self.__snakeHead.update((self.__xHead,self.__yHead))
        self.__snakeCoordinates[0] = (self.__xHead,self.__yHead)            

    def eating(self,foodcollor=None):
        self.__size += 1
        self.__snakeBody.insert(len(self.__snakeBody), Rectangle((self.__scale,self.__scale)))
        xTail = self.__snakeBody[-2:][0].rect.x
        yTail = self.__snakeBody[-2:][0].rect.y
        self.__snakeBody[len(self.__snakeBody)-1].update((xTail,yTail))
        self.__snakeCoordinates.append((xTail,yTail))
        

    @property
    def snakeHead(self):
        return self.__snakeHead
    @property
    def snakeBody(self):
        return self.__snakeBody
    @property
    def snakeCoordinates(self):
        return self.__snakeCoordinates
    @property
    def snakeCollor(self):
        return self.__snakeCollor
    @property
    def scale(self):
        return self.__scale
    @property
    def size(self):
        return self.__size-1

    @property
    def snakeViva(self):
        return self.__snakeViva
    @snakeViva.setter
    def snakeViva(self, newStatus):
        self.__snakeViva = newStatus

    @property
    def orientation(self):
        return self.__orientation
    @orientation.setter
    def orientation(self, newOrientation):
        self.__orientation = newOrientation

if __name__ == '__main__':
=======
from snake_data.game_objects.rectangles import *
from snake_data.toolkit import *


class Snake(object):
    def __init__(self, startPosition):
        self.__scale = Responsivity.rectangle_scale()
        self.__size = 3
        self.__snakeCollor = 'violet'
        self.__snakeViva = True
        self.__orientation = 'Right'
        self.__snakeCoordinates = []
        self.__snakeCoordinates.append(startPosition)
        self.__xHead, self.__yHead = startPosition

        self.__snakeHead = Rectangle(area=(self.__scale,self.__scale), position=startPosition)
        self.__snakeBody = [Rectangle(area=(self.__scale,self.__scale), position=(self.__xHead-self.__scale*num,self.__yHead)) 
                                    for num in list(range(1,self.__size))]

        self.__snakeCoordinates.extend([(self.__xHead-self.__scale*num,self.__yHead) 
                                        for num in list(range(1,self.__size))])


    def move_snake(self):
        self.__snakeBody.insert(0,Rectangle(area=(self.__scale,self.__scale),position=(self.__xHead,self.__yHead)))
        self.__snakeCoordinates.insert(0,(self.__xHead,self.__yHead))
        self.__snakeBody.pop()
        self.__snakeCoordinates.pop()

        if self.orientation == 'Left':
            self.__xHead-=self.__scale           
        elif self.orientation == 'Right':
            self.__xHead+=self.__scale           
        elif self.orientation == 'Up':
            self.__yHead-=self.__scale           
        elif self.orientation == 'Down':
            self.__yHead+=self.__scale

        self.__snakeHead.update((self.__xHead,self.__yHead))
        self.__snakeCoordinates[0] = (self.__xHead,self.__yHead)            

    def eating(self,foodcollor=None):
        self.__size += 1
        self.__snakeBody.insert(len(self.__snakeBody), Rectangle((self.__scale,self.__scale)))
        xTail = self.__snakeBody[-2:][0].rect.x
        yTail = self.__snakeBody[-2:][0].rect.y
        self.__snakeBody[len(self.__snakeBody)-1].update((xTail,yTail))
        self.__snakeCoordinates.append((xTail,yTail))
        

    @property
    def snakeHead(self):
        return self.__snakeHead
    @property
    def snakeBody(self):
        return self.__snakeBody
    @property
    def snakeCoordinates(self):
        return self.__snakeCoordinates
    @property
    def snakeCollor(self):
        return self.__snakeCollor
    @property
    def scale(self):
        return self.__scale
    @property
    def size(self):
        return self.__size-1

    @property
    def snakeViva(self):
        return self.__snakeViva
    @snakeViva.setter
    def snakeViva(self, newStatus):
        self.__snakeViva = newStatus

    @property
    def orientation(self):
        return self.__orientation
    @orientation.setter
    def orientation(self, newOrientation):
        self.__orientation = newOrientation

if __name__ == '__main__':
>>>>>>> a1898a2831cad84583c5092c78c5c460e9a24d7c
    pass