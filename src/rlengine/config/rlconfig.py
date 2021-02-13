# from src.rlengine.player import Player
# from src.rlengine.system import Logger
from src.rlengine.utils import InputManager, ResourceManager
from src.rlengine.custom.states import MainMenuState

# klass_player            = Player

# # system
# klass_logger            = Logger

RL_CONFIGS = {
    'klass_resource_manager': ResourceManager,
    'klass_input_manager': InputManager,
    'klass_init_state': MainMenuState
}
