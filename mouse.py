import pygame

class Mouse:

    def __init__(self, game):
        self.update(game)
        self.left_click_mode = False
        self.right_click_mode = False

    def left_click(self,game):
        self.last_left_click_position_grid = (int(self.pos_x_grid),int(self.pos_y_grid))

    def right_click(self,game):
        self.last_right_click_position_grid = (self.pos_x_grid,self.pos_y_grid)

    def update(self, game):
        self.pos_x_px = pygame.mouse.get_pos()[0]
        self.pos_y_px = pygame.mouse.get_pos()[1]

        self.pos_x_grid = int((self.pos_x_px - game.screen_width/2 + game.camera.x_offset_px)//game.grid_size)
        self.pos_y_grid = int((self.pos_y_px - game.screen_height/2 + game.camera.y_offset_px)//game.grid_size)


    def render(self, game):
        pass