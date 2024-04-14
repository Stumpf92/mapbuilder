import pygame

class Mouse:

    def __init__(self, game):
        self.update(game)
        self.left_click_mode = False
        self.right_click_mode = False

    def left_click_down(self,game):
        self.last_left_click_position_px = (int(self.pos_x_px),int(self.pos_y_px))
        self.last_left_click_position_grid = (int(self.pos_x_grid),int(self.pos_y_grid))
        self.left_click_mode = True


    def right_click_down(self,game):
        self.last_right_click_position_px = (int(self.pos_x_px),int(self.pos_y_px))
        self.last_right_click_position_grid = (int(self.pos_x_grid),int(self.pos_y_grid))
        self.right_click_mode = True

    def left_click_up(self,game):
        game.map.add_tile_square(self.last_left_click_position_grid, (self.pos_x_grid,self.pos_y_grid),1)
        self.left_click_mode = False
        print(self.last_left_click_position_grid, (self.pos_x_grid, self.pos_y_grid))


    def right_click_up(self,game):
        game.map.del_tile_square(game, self.last_right_click_position_grid, (self.pos_x_grid,self.pos_y_grid))
        self.right_click_mode = False


    def wheel_up(self, game):
        game.grid_size = max(game.grid_size -1 , game.min_grid_size)

    def wheel_down(self, game):
        game.grid_size = min(game.grid_size +1 , game.max_grid_size)

    def update(self, game):
        self.pos_x_px = pygame.mouse.get_pos()[0]
        self.pos_y_px = pygame.mouse.get_pos()[1]

        self.pos_x_grid = int((self.pos_x_px - game.screen_width/2 + game.camera.x_offset_px)//game.grid_size)
        self.pos_y_grid = int((self.pos_y_px - game.screen_height/2 + game.camera.y_offset_px)//game.grid_size)


    def render(self, game):
        if self.left_click_mode == True:
            rect = pygame.Rect(self.last_left_click_position_px[0], self.last_left_click_position_px[1],pygame.mouse.get_pos()[0]-self.last_left_click_position_px[0],pygame.mouse.get_pos()[1]-self.last_left_click_position_px[1] )
            pygame.draw.rect(game.surface,(10,150,90), rect, 1 , game.grid_size // 8)
        if self.right_click_mode == True:
            rect = pygame.Rect(self.last_right_click_position_px[0], self.last_right_click_position_px[1],pygame.mouse.get_pos()[0]-self.last_right_click_position_px[0],pygame.mouse.get_pos()[1]-self.last_right_click_position_px[1] )
            pygame.draw.rect(game.surface,(255,0,0), rect, 1 , game.grid_size // 8)