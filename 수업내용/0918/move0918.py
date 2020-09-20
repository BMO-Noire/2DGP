from pico2d import *
from gobj import *

#curr_state = a_state ? b_state

#while True:
	#curr_state.handle_events()
	#curr_state.update()
	#curr_state.draw()

def handle_events():
	global running
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			runing = False

open_canvas()


grass = Grass()

team = [ Boy() for i in range(11)]


running = True
while running:
	clear_canvas()
	grass.draw()
	for boy in team:
		boy.draw()
	update_canvas()

	handle_events()

	for boy in team:
		boy.update()

	grass.update()

	delay(0.03)

close_canvas()