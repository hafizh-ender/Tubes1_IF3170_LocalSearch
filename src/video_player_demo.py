from State import State
from SteepestAscentAlgorithm import SteepestAscentAlgorithm
from VideoPlayer import VideoPlayer

initial_state = State()

result = SteepestAscentAlgorithm.solve(initial_state)

result.export_history("result/steepest_ascent.txt")

video_player = VideoPlayer()

video_player.setup_ui()

video_player.load_states("result/steepest_ascent.txt")

video_player.root.mainloop()

