import pygame

class Camera:

    def __init__(self,game):
        self.pos = [-game.screen_width/2 ,-game.screen_height/2]
        self.max_speed = 4
        self.mouse_scroll_margin = 80

        #camera offset = distance between center of the screen and origin
        self.x_offset_px = 0
        self.y_offset_px = 0
    
    def update(self,game):

        #### MOUSE SCROLL ####
        mp = pygame.mouse.get_pos()
        if mp[0] < self.mouse_scroll_margin:
            self.pos[0] -= self.max_speed*(1-(mp[0]/self.mouse_scroll_margin))
        if mp[0] > game.screen_width - self.mouse_scroll_margin:            
            self.pos[0] += self.max_speed*((mp[0]-(game.screen_width-self.mouse_scroll_margin))/self.mouse_scroll_margin)
        if mp[1] < self.mouse_scroll_margin:
            self.pos[1] -= self.max_speed*(1-(mp[1]/self.mouse_scroll_margin))
        if mp[1] > game.screen_height - self.mouse_scroll_margin:            
            self.pos[1] += self.max_speed*((mp[1]-(game.screen_height-self.mouse_scroll_margin))/self.mouse_scroll_margin)


        #### UP DOWN LEFT RIGHT SCROLL ####
        if game.camera_movement_mode[0] == True:
            self.pos[1] += self.max_speed
        if game.camera_movement_mode[1] == True:
            self.pos[1] -= self.max_speed
        if game.camera_movement_mode[2] == True:
            self.pos[0] += self.max_speed
        if game.camera_movement_mode[3] == True:
            self.pos[0] -= self.max_speed

        self.x_offset_px = game.screen_width/2 + self.pos[0]
        self.y_offset_px = game.screen_height/2 + self.pos[1]
        
    
    def center(self, game, player):
        self.pos[0] = (player.pos_grid[0] * game.grid_size) -game.screen_width/2 
        self.pos[1] = (player.pos_grid[1] * game.grid_size) -game.screen_height/2