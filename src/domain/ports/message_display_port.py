from abc import ABC, abstractmethod

class MessageDisplayPort(ABC):
  @abstractmethod
  def display(self, message: str, message_type: str) -> None:
      pass
