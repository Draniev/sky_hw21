from storage import Storage


class Store(Storage):
    """
    Хранится любое количество любых товаров.
    Не может быть заполнен если свободное место закончилось
    """

    def __init__(self, capacity: int = 100, name: str = 'Store'):
        self._name = name
        self._storage = {}
        self._capacity = capacity

    def add(self, title: str, qty: int) -> bool:
        """
        Увеличивает запас title на qty штук
        Возвращает успешность операции
        """
        is_add_compleated = False

        if self.is_enouth_capacity(title, qty):
            if self._storage.get(title):
                self._storage[title] += qty
            else:
                self._storage[title] = qty
            is_add_compleated = True

        return is_add_compleated

    def remove(self, title: str, qty: int) -> tuple[str, int]:
        """
        Уменьшает запас title на qty штук
        """

        if self._storage.get(title):
            qty_in_stor = self._storage[title]
            if qty < qty_in_stor:
                self._storage[title] = qty_in_stor - qty
                return title, qty
            else:
                self._storage[title] = 0
                return title, qty_in_stor
        else:
            return title, 0
