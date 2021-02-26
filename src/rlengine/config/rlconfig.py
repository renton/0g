from src.rlengine.game import Player
from src.rlengine.game.map import Map, Tile
# from src.rlengine.system import Logger
from src.rlengine.utils import InputManager, ResourceManager, AudioManager
from src.rlengine.custom.states import MainMenuState

# klass_player            = Player

# # system
# klass_logger            = Logger

RL_CONFIGS = {
    'klass_resource_manager': ResourceManager,
    'klass_input_manager': InputManager,
    'klass_init_state': MainMenuState,
    'klass_player': Player,
    'klass_audio_manager': AudioManager,
}
