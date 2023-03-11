from storage import Storage


class Shop(Storage):
    """
    Хранится не больше 5 (хардкодим) разных товаров.
    Не может быть заполнен если свободное место закончилось
    """

    def __init__(self, capacity: int = 20, name: str = 'Shop'):
        self._name = name
        self._storage = {}
        self._capacity = capacity

    def add(self, title: str, qty: int) -> bool:
        """
        Увеличивает запас title на qty штук
        Проверяет чтобы видов товаров не больше 5 штук было
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

    def is_enouth_capacity(self, title: str, qty: int) -> bool:
        """
        Места достаточно если позволяет объем
        И вместе с новым предметом будет не более 5 объектов
        на хранении
        """
        if self.get_free_space < qty:
            return False

        is_new_item_in_stor = 0 if self._storage.get(title) else 1

        if self.get_unique_items_count + is_new_item_in_stor <= 5:
            return True
        else:
            return False
