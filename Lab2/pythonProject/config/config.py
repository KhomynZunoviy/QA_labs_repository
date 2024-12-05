import os
from .environments import dev, staging, prod

def load_config():
    env = os.getenv('ENV', 'dev')
    if env == 'staging':
        return staging
    elif env == 'prod':
        return prod
    return dev
