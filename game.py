import pygame
import sys
import os

from player import Player
from camera import Camera
from map import Map
from mouse import Mouse
from utilities import *
from win32api import ClipCursor


class Game:
    def __init__(self):
        #############
        #GLOBALS
        #############

        self.screen_width = 1800   
        self.screen_height = 1000
        self.max_grid_size = 48
        self.min_grid_size = 4
        self.grid_size = 12
        self.camera_offset = [-self.screen_width/2 ,-self.screen_height/2]



        pygame.init()
        pygame.display.set_caption('Mapbuilder')
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.surface = pygame.Surface((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()


        
        #######
        #STATES
        #######

        self.player_movement_mode = [False, False, False, False] #wsad#
        self.camera_movement_mode = [False, False, False, False] #oben unten links rechts#
        self.shift_mode = False
        self.alt_mode = False
        self.ctrl_mode = False
        self.editor_mode = False
        self.data_mode = False
        self.shuffle_mode = False

        ########
        #LOADING
        ########

        self.data_font = pygame.font.SysFont("Arial" , 10, bold=False)

        ###############
        #INITIALIZATION
        ###############

        self.camera = Camera(self)
        self.player = Player()
        self.map = Map(self)
        self.mouse = Mouse(self)

    def reset(self):
        self.player.real_pos_pixel = [0,0]
        self.player.pos_pixel = [0,0]
        self.player.pos_grid = [0,0]
        self.grid_size = 4
        self.camera.center(self, self.player)
        self.map.reset(self)
    

    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.surface.fill((0,0,0))

            ###############
            #UPDATING
            ###############

            self.player.update(self,)
            self.camera.update(self)
            self.map.update(self)
            self.mouse.update(self)



            ###############
            #RENDERING
            ###############
            
            self.map.render(self)
            if self.editor_mode:
                draw_origin(self)
            self.player.render(self)
            if self.data_mode:
                draw_data(self)
            self.mouse.render(self)



            ################
            #INPUT HANDLE
            ################

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_w:
                        self.player_movement_mode[0] = True
                    if event.key == pygame.K_s:
                        self.player_movement_mode[1] = True
                    if event.key == pygame.K_a:
                        self.player_movement_mode[2] = True
                    if event.key == pygame.K_d:
                        self.player_movement_mode[3] = True
                    if event.key == pygame.K_UP:
                        self.camera_movement_mode[0] = True
                    if event.key == pygame.K_DOWN:
                        self.camera_movement_mode[1] = True
                    if event.key == pygame.K_LEFT:
                        self.camera_movement_mode[2] = True
                    if event.key == pygame.K_RIGHT:
                        self.camera_movement_mode[3] = True
                    if event.key == pygame.K_f:
                        self.shuffle_mode = True


                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.shift_mode = True
                    if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                        self.alt_mode = True
                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        self.ctrl_mode = True

                    if event.key == pygame.K_F1:
                        self.editor_mode = not self.editor_mode
                    if event.key == pygame.K_F2:
                        self.data_mode = not self.data_mode
                    if event.key == pygame.K_F5:
                        self.map.save()
                    if event.key == pygame.K_F8:
                        self.map.load(self)
                    if event.key == pygame.K_r:
                        self.reset()
                    if event.key == pygame.K_SPACE:
                        self.camera.center(self, self.player)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player_movement_mode[0] = False
                    if event.key == pygame.K_s:
                        self.player_movement_mode[1] = False
                    if event.key == pygame.K_a:
                        self.player_movement_mode[2] = False
                    if event.key == pygame.K_d:
                        self.player_movement_mode[3] = False
                    if event.key == pygame.K_UP:
                        self.camera_movement_mode[0] = False
                    if event.key == pygame.K_DOWN:
                        self.camera_movement_mode[1] = False
                    if event.key == pygame.K_LEFT:
                        self.camera_movement_mode[2] = False
                    if event.key == pygame.K_RIGHT:
                        self.camera_movement_mode[3] = False
                    if event.key == pygame.K_f:
                        self.shuffle_mode = False


                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.shift_mode = False
                    if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                        self.alt_mode = False
                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        self.ctrl_mode = False    

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse.left_click_down(self)
                    if event.button == 3:
                        self.mouse.right_click_down(self)
                    if event.button == 4:
                        self.mouse.wheel_up(self)
                    if event.button == 5:
                        self.mouse.wheel_down(self)
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.mouse.left_click_up(self)
                    if event.button == 3:
                        self.mouse.right_click_up(self)
                    

            self.screen.blit(self.surface,(0,0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()