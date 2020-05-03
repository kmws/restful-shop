from app import get_manager
from tools.config_properties import init_config

if __name__ == '__main__':
    init_config()
    manager = get_manager()
    manager.run()
