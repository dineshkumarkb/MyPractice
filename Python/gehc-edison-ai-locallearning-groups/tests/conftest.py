# Defining all fixtures here
from src.groups.api import app
import pytest



@pytest.fixture(name="flasky")
def init_app():
    return app
