from abc import ABC, abstractmethod

class RPSLS_player(ABC):

  @abstractmethod
  def shoot(self) -> str:
    pass

  @abstractmethod
  def update(self, result: str, competitor_shot: str):
    pass


from RPSLS_player import RPSLS_player
import random

class P16107(RPSLS_player):
  def __init__(self):
    pass
    

  def shoot(self):
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


  def update(self, result: str, competitor_shot: str):
    pass
