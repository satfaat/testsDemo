from enum import Enum


class Endpoints(str, Enum):
    AUTH = 'auth'
    INFO = 'info'
    CAST = 'cast'
    POSTS = 'posts'
    EPISODES = 'episodes'
    QUESTIONS = 'questions'
    INVENTORY = 'inventory'
    CHARACTERS = 'characters'

    def __str__(self) -> str:
        return self.value