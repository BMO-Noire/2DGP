from pico2d import *
from helper import *

def handle_events():
    global running, dx, x, y, deltaX, deltaY ,state, e, mx, my
    global xx, yy, move, speed 
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif state == False and e.type == SDL_MOUSEBUTTONDOWN:
            mx,my = e.x, 600 - e.y
            deltaX,deltaY = delta((x,y),(mx , my), speed)
            speed += 1
        elif e.type == SDL_MOUSEBUTTONDOWN:
            mx,my = e.x, 600 - e.y
            deltaX,deltaY = delta((x,y),(mx , my), speed)
            move = True

        #elif e.type == SDL_MOUSEBUTTONUP:
    
    


open_canvas()

gra = load_image('../res/grass.png')
cha = load_image('../res/animation_sheet.png')

state = True
speed = 1
move = False
state = True
x, y = get_canvas_width() // 2, 85
dx = 0
frame_index = 0
action = 0

running = True
while running:
    clear_canvas()
    gra.draw(400,30)
    cha.clip_draw(100 * frame_index, 100 * action, 100, 100, x, y)
    update_canvas()

    handle_events()
    if move == True:
        (x,y),state = move_toward((x, y), (deltaX,deltaY), (mx, my))

    if state == True:
        speed = 1
    print(speed)
    #x += dx


    frame_index = (frame_index + 1) % 8

    delay(0.02)

close_canvas()

