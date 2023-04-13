import consts
import state

use_ai = False

def get_input():
   # todo (Seth define this function)
   return consts.DOWN

state = state.State()
state.start_game()
while True:
   state.display()
   if state.lost: break

   if use_ai:
      action=state.search()
   else:
      action=get_input()

   prev_state = state.dup()
   state.move(action)
   if action==consts.DOWN and state==prev_state:
      state.place()
