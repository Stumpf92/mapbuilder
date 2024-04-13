import pygame

def draw_origin(game):
    pygame.draw.line(game.surface,(255,0,0),(-game.grid_size -game.camera.pos[0],0-game.camera.pos[1]),(game.grid_size -game.camera.pos[0],0-game.camera.pos[1]),3)
    pygame.draw.line(game.surface,(255,0,0),(0-game.camera.pos[0],-game.grid_size-game.camera.pos[1]),(0-game.camera.pos[0],game.grid_size-game.camera.pos[1]),3)

def draw_data(game):
    fps = 'FPS:   ' + str(int(game.clock.get_fps()))
    text = game.data_font.render(fps, 1, (255,255,255))
    game.surface.blit(text,(10,10))

    camerapos = 'Camera_pos:   ' + str(int(game.camera.pos[0]))+'  ,  '+str(int(game.camera.pos[1]))
    text = game.data_font.render(camerapos, 1, (255,255,255))
    game.surface.blit(text,(10,20))

    cameraoff = 'Camera_offset:   ' + str(int(game.camera.x_offset_px))+'  ,  '+str(int(game.camera.y_offset_px))
    text = game.data_font.render(cameraoff, 1, (255,255,255))
    game.surface.blit(text,(10,30))

    mousepos = 'Mousepos_px:   ' + str(int(game.mouse.pos_x_px))+'  ,  '+str(int(game.mouse.pos_y_px))
    text = game.data_font.render(mousepos, 1, (255,255,255))
    game.surface.blit(text,(10,40))

    mousepos = 'Mousepos_grid:   ' + str(int(game.mouse.pos_x_grid))+'  ,  '+str(int(game.mouse.pos_y_grid))
    text = game.data_font.render(mousepos, 1, (255,255,255))
    game.surface.blit(text,(10,50))


def grid_go_up(a,tilemap):
    temp = a[1] - 1
    string = str(a[0]) +';'+ str(temp)
    while string in tilemap:
        temp -= 1
        string = str(a[0]) +';'+ str(temp)
    sol = [a[0],temp]
    return sol

def grid_go_down(a,tilemap):
    temp = a[1] + 1
    string = str(a[0]) +';'+ str(temp)
    while string in tilemap:
        temp += 1
        string = str(a[0]) +';'+ str(temp)
    sol = [a[0],temp]
    return sol

def grid_go_left(a,tilemap):
    temp = a[0] - 1
    string = str(temp) +';'+ str(a[1])
    while string in tilemap:
        temp -= 1
        string = str(temp) +';'+ str(a[1])
    sol = [temp,a[1]]
    return sol

def grid_go_right(a,tilemap):
    temp = a[0] + 1
    string = str(temp) +';'+ str(a[1])
    while string in tilemap:
        temp += 1
        string = str(temp) +';'+ str(a[1])
    sol = [temp,a[1]]
    return sol