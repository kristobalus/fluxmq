from abc import ABC, abstractmethod


class TopicFactory(ABC):
    @abstractmethod
    def status(self, service_id: str):
        pass

    @abstractmethod
    def configuration(self, service_id: str):
        pass

    @abstractmethod
    def control(self, service_id: str):
        pass

    @abstractmethod
    def time(self):
        pass

