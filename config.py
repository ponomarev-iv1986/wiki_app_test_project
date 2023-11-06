import os
from typing import Literal

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)

EnvType = Literal['bstack', 'local']


class Settings(pydantic_settings.BaseSettings):
    ENVIRONMENT: EnvType = 'local'
    BSTACK_USER: str
    BSTACK_ACCESS_KEY: str


settings = Settings(_env_file=os.path.join(BASE_DIR, '.env'))
