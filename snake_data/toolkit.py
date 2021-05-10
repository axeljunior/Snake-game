import pygame, os

class Responsivity(object):
    __widthScreen = 720 #Largura
    __heightScreen = 480 #Altura
    __rectangle_scale = 20
    @classmethod
    def height_screen(cls):
        return cls.__heightScreen
    @classmethod
    def width_screen(cls):
        return cls.__widthScreen
    @classmethod
    def rectangle_scale(cls):
        return cls.__rectangle_scale

class Text(object):
    @staticmethod
    def draw_text(screen,text, color, surface,size=20,filefont='arial.ttf'):
        fontobj = pygame.font.Font(os.path.join('assets/fonts',filefont), size)

        if filefont != 'arial.ttf':
            fontobj = pygame.font.Font(os.path.join('assets/fonts',filefont), size)

        textobj = fontobj.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = surface
        screen.blit(textobj, textrect)

class Collors(object):
    @staticmethod
    def collor(collorName):
        collor={        
                'white' : (255,255,255),
                'black' : (0,0,0),
                'gray' : (50,50,50),
                'red' : (250,0,0),
                'orange' : (250,160,0),
                'yellow' : (250,230,40),
                'green' : (0,250,50),
                'blue' : (0,50,250),
                'anil' : (10,60,120),
                'violet' : (180,40,250)}
        return collor.get(collorName)

    @staticmethod
    def change_collor(tam,cor,num=0):
        if tam <= 3:
            return Collors.collor(cor)
        else:
            r,g,b = Collors.collor(cor)

            num = 5*tam

            if num >= 250:
                num = 250

            if num > r and num <= 250:
                r = num
            if num > g and num <= 250:
                g = num
            if num > b and num <= 250:
                b = num

            return (r,g,b)

class ArtResource(object):
    __sfxLibrary={}
    @staticmethod
    def image_load(filename):
        return os.path.join('assets/images',filename)

    @classmethod
    def sound_add_sfx(cls,filename,extension,volume=None):
        cls.__sfxLibrary[filename] = pygame.mixer.Sound(os.path.join('assets/sounds',f'{filename}.{extension}'))
        if not isinstance(volume,type(None)):
            cls.__sfxLibrary[filename].set_volume(float(volume))
    @classmethod
    def sound_play_sfx(cls,filename):
        cls.__sfxLibrary.get(filename).play()

    @staticmethod
    def sound_add_bgm(filename,extension,volume):
        pygame.mixer.music.load(os.path.join('assets/sounds',f'{filename}.{extension}'))
        pygame.mixer.music.set_volume(float(volume))
    @staticmethod
    def sound_play_bgm():
        pygame.mixer.music.play(-1)

if __name__ == '__main__':
    pass