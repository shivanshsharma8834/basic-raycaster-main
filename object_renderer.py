import pygame as pg 
from settings import * 

class ObjectRenderer:

    def __init__(self,game) -> None:
        self.game = game 
        self.screen = game.screen 
        self.wall_textures = self.load_wall_textures()


    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):

        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):

        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/1.png'),
            3: self.get_texture('resources/textures/1.png'),
            4: self.get_texture('resources/textures/1.png'),
            5: self.get_texture('resources/textures/1.png'),
        }
    
    

