from abc import ABC, abstractmethod

class ApiClientPort(ABC):
  @abstractmethod
  def get_data(self, url: str):
    pass

  @abstractmethod
  def get_data_with_pagination(self, url: str):
    pass
