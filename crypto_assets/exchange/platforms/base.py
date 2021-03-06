from abc import ABC, abstractmethod


class BaseExchange(ABC):
    @abstractmethod
    def get_price(self, coin) -> int:
        pass

    @abstractmethod
    def cache_all_prices(self, coin) -> None:
        pass
