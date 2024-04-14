import pygame
import json
import random
from utilities import *

class Map:

    def __init__(self, game):
        self.reset(game)
        self.min_x_grid = 0
        self.max_x_grid = 0
        self.min_y_grid = 0
        self.max_y_grid = 0
        
    def reset(self, game):
        self.tilemap = {}
        self.add_tile_square((0,0), (0,0), 1)

    def update(self, game):
        if game.shuffle_mode == True:
            self.add_random_single_tile(1)

    @timeit
    def render(self, game):
        for tile in self.tilemap:
            x , y = int(tile.split(';')[0]) , int(tile.split(';')[1])
            rect = pygame.Rect((x*game.grid_size) - game.camera.pos[0], (y*game.grid_size) - game.camera.pos[1], game.grid_size, game.grid_size)
            pygame.draw.rect(game.surface,(10,150,90), rect, 4 , game.grid_size // 8)
        
        # if game.editor_mode == True:
        #     rect = pygame.Rect((self.min_x_grid*game.grid_size) - game.camera.pos[0], (self.min_y_grid*game.grid_size) - game.camera.pos[1], (self.max_x_grid -self.min_x_grid+1)*game.grid_size, (self.max_y_grid - self.min_y_grid+1)* game.grid_size)
        #     pygame.draw.rect(game.surface,(255,0,0), rect, 1 , game.grid_size // 8)

    def save(self):
        f = open('map.json', 'w')
        json.dump({'tilemap': self.tilemap}, f)
        f.close()

    def add_tile_square(self, list_start, list_stop, value):
        x_min_grid, x_max_grid = min(list_start[0], list_stop[0]), max(list_start[0], list_stop[0])
        y_min_grid, y_max_grid = min(list_start[1], list_stop[1]), max(list_start[1], list_stop[1])

        for x in range(x_min_grid, x_max_grid+1):
            for y in range(y_min_grid, y_max_grid+1):
                string = str(x) + ';' + str(y)
                self.tilemap[string] = value
        #self.update_max_values()
    
    def add_single_tile(self, list, value):
        string = str(list[0]) + ';' + str(list[1])
        self.tilemap[string] = value
        #self.update_max_values()

    def add_random_single_tile(self,value):
        rnd_position= random.choice(list(self.tilemap.keys()))
        options = [grid_go_up([int(rnd_position.split(';')[0]),int(rnd_position.split(';')[1])],self.tilemap),
                   grid_go_down([int(rnd_position.split(';')[0]),int(rnd_position.split(';')[1])],self.tilemap),
                   grid_go_left([int(rnd_position.split(';')[0]),int(rnd_position.split(';')[1])],self.tilemap),
                   grid_go_right([int(rnd_position.split(';')[0]),int(rnd_position.split(';')[1])],self.tilemap)]
        rnd_new = random.choice(options)
        string = str(rnd_new[0]) + ';' + str(rnd_new[1])
        self.tilemap[string] = 1
        #self.update_max_values()
    
    def del_tile_square(self, game, list_start, list_stop):
        x_min_grid, x_max_grid = min(list_start[0], list_stop[0]), max(list_start[0], list_stop[0])
        y_min_grid, y_max_grid = min(list_start[1], list_stop[1]), max(list_start[1], list_stop[1])

        for x in range(x_min_grid, x_max_grid+1):
            for y in range(y_min_grid, y_max_grid+1):
                string = str(x) + ';' + str(y)
                if string in self.tilemap.keys():
                    del self.tilemap[string]


        #self.update_max_values()
    
    @timeit
    def update_max_values(self):
        self.min_x_grid = 0
        self.max_x_grid = 0
        self.min_y_grid = 0
        self.max_y_grid = 0
        for tile in self.tilemap:
            x , y = int(tile.split(';')[0]) , int(tile.split(';')[1])
            self.min_x_grid = min(self.min_x_grid, x)
            self.max_x_grid = max(self.max_x_grid, x)
            self.min_y_grid = min(self.min_y_grid, y)
            self.max_y_grid = max(self.max_y_grid, y)


    def load(self, game):
        f = open('map.json', 'r')
        map_data = json.load(f)
        f.close()

        self.reset(game)
        self.tilemap = map_data['tilemap']