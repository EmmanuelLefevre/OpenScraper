from abc import ABC, abstractmethod

class SaveFilePort(ABC):
  @abstractmethod
  def save(self, data):
    pass
