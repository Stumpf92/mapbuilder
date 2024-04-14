import pygame
import math

class Player:

    def __init__(self):
        self.pos_pixel = [0,0]
        self.pos_grid = [0,0]
        self.real_pos_pixel = [0,0]
        self.movement_speed_base = 2

    def update(self, game):
        if (game.player_movement_mode[0] == True and game.player_movement_mode[3] == True) or (game.player_movement_mode[1] == True and game.player_movement_mode[3] == True) or (game.player_movement_mode[0] == True and game.player_movement_mode[2] == True) or (game.player_movement_mode[1] == True and game.player_movement_mode[2] == True):
            self.movement_speed = math.sqrt(self.movement_speed_base)
        else:
            self.movement_speed = self.movement_speed_base


        if game.player_movement_mode[0] == True:
            self.real_pos_pixel[1] -= self.movement_speed
            self.pos_pixel[1] = int(self.real_pos_pixel[1])
            self.pos_grid[1] = self.pos_pixel[1] // game.grid_size
            game.map.add_single_tile((self.pos_grid[0],self.pos_grid[1]), 1)
        if game.player_movement_mode[1] == True:
            self.real_pos_pixel[1] += self.movement_speed
            self.pos_pixel[1] = int(self.real_pos_pixel[1])
            self.pos_grid[1] = self.pos_pixel[1] // game.grid_size
            game.map.add_single_tile((self.pos_grid[0],self.pos_grid[1]), 1)
        if game.player_movement_mode[2] == True:
            self.real_pos_pixel[0] -= self.movement_speed
            self.pos_pixel[0] = int(self.real_pos_pixel[0])
            self.pos_grid[0] = self.pos_pixel[0] // game.grid_size
            game.map.add_single_tile((self.pos_grid[0],self.pos_grid[1]), 1)
        if game.player_movement_mode[3] == True:
            self.real_pos_pixel[0] += self.movement_speed
            self.pos_pixel[0] = int(self.real_pos_pixel[0])
            self.pos_grid[0] = self.pos_pixel[0] // game.grid_size
            game.map.add_single_tile((self.pos_grid[0],self.pos_grid[1]), 1)

        

    def render(self, game):
        self.rect = pygame.Rect((self.pos_grid[0]*game.grid_size) - game.camera.pos[0], (self.pos_grid[1]*game.grid_size) - game.camera.pos[1], game.grid_size, game.grid_size)
        pygame.draw.rect(game.surface,(255,0,0), self.rect, 2, game.grid_size//4)
