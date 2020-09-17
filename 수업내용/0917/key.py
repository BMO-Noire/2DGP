from pico2d import *

def handle_events():
    global running
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                print("escape key") #running = false

#함수의 events,running는 지역변수. 함수가 끝나면 사라짐.
#global로 전역변수로 사용
                
open_canvas()

gra = load_image('../res/grass.png')
cha = load_image('../res/animation_sheet.png')

x = 0
frame_index = 0
action = 0

#running = True
while x < 800: #while running
    clear_canvas()
    gra.draw(400,30)
    cha.clip_draw(100 * frame_index, 100 * action, 100, 100, x, 85)
    update_canvas()

    handle_events()
    
    #루프를 빠져나가기 위해? running = true -> false
    #for e in events:
        #print(e.type)
    #발생한 이벤트가 무엇인지

    x += 2

    if x % 100 == 0:
        action = (action + 1) % 4

    frame_index = (frame_index + 1) % 8

    delay(0.02)

close_canvas()

#프로그램 쪼갠다 -> 모듈화
