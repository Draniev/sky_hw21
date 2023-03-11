from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, capacity: int, name: str = 'Storage'):
        self._name = name
        self._storage = {}
        self._capacity = capacity

    @abstractmethod
    def add(self, title: str, qty: int):
        """
        Увеличивает запас title на qty штук
        """

    @abstractmethod
    def remove(self, title: str, qty: int):
        """
        Уменьшает запас title на qty штук
        """

    @property
    def get_free_space(self) -> int:
        """
        Возвращает кол-во свободных мест на складе
        """
        occupied_capacity = 0
        for volume in self._storage.values():
            occupied_capacity += volume
        return self._capacity - occupied_capacity

    @property
    def get_items(self) -> dict[str: int]:
        """
        Возвращает содержание склада в виде словаря
        """
        return self._storage

    @property
    def get_unique_items_count(self) -> int:
        """
        Возвращает кол-во SCU на складе
        """
        return len(self._storage.keys())

    @property
    def get_name(self) -> str:
        return self._name

    def is_enouth_capacity(self, title: str, qty: int) -> bool:
        """
        Решил добавить в базовый класс публичную проверку того,
        поместится ли конкретный товар в текущее хранилище
        Иначе в классе Shop нет возможности узнать, влезет ли
        товар пока не поробуем засунуть, что не правильно.
        """
        return self.get_free_space >= qty

    def __repr__(self):
        return (f"В {self._name} свободно {self.get_free_space} "
                f"из {self._capacity}. Всего {self.get_unique_items_count} "
                "объектов хранения.")
