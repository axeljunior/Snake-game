import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, area, position=None):
        super().__init__()
        self.image=pygame.Surface(area)
        self.rect=self.image.get_rect()
        if not isinstance(position,type(None)):
            self.update((position))
    
    def set_texture(self, texture, deform=None):
        self.image = pygame.image.load(texture)
        if not isinstance(deform,type(None)):
            self.image = pygame.transform.scale(self.image,(deform[0],deform[1]))
        self.rect=self.image.get_rect()

    def update(self, cordenates):
        self.rect.x, self.rect.y = cordenates

if __name__ == '__main__':
    pass