from storage import Storage


class Request():
    def __init__(self, storages: list[Storage], req: str):
        """
        При инициализации  принимает список всех складов и строку типа
        'Доставить 3 печеньки из склад в магазин'
        И возвращает объект класса Request
            from =  "склад",
            to =  "магазин",
            amount = 3,
            product = "печеньки"
        """
        self._storages = storages
        self._from = None
        self._to = None
        self._amount: int = 0
        self._product: str = ""

        request_str = req.split()
        if len(request_str) != 7:
            raise ValueError("Запрос составлен не корректно, мало аргументов")

        try:
            self._amount = int(request_str[1])
        except Exception:
            raise ValueError("Не возможно получить кол-во объектов")

        self._product = request_str[2]

        for item in storages:
            # Предусмотрим вариант в запросе менять местами из|от / в|до
            if item.get_name == request_str[4]:
                if request_str[3] in ('из', 'от', 'from'):
                    self._from = item
                if request_str[3] in ('в', 'до', 'to'):
                    self._to = item

            if item.get_name == request_str[6]:
                if request_str[5] in ('из', 'от', 'from'):
                    self._from = item
                if request_str[5] in ('в', 'до', 'to'):
                    self._to = item

        if not all([self._from, self._to]):
            raise ValueError("Один из пунктов назначения не распознан")
        if self._from is self._to:
            raise ValueError("Запрошено бессмысленное перемещение по кругу")

    def __repr__(self):
        return (f"FROM {self._from.get_name} TO {self._to.get_name}:"
                f" {self._amount} {self._product}")

    def execute(self) -> bool:
        """
        Исполняет запрос и перемещает товары в соответствии с запросом.
        """

        print(f"\nПроверяю наличие мест в {self._to.get_name}")
        is_enouth = self._to.is_enouth_capacity(self._product, self._amount)
        if not is_enouth:
            print(f"Места в {self._to.get_name} не достаточно")
            return False

        print(f"Приступаю к отгрузке из {self._from.get_name}")
        _, qty = self._from.remove(self._product, self._amount)

        if qty == 0:
            print(f"Запрошенного {self._product} "
                  f"нет в {self._from.get_name}, завершаю")
            return False
        elif qty == self._amount:
            print(f"Отгрузили {self._amount} {self._product}"
                  f" из {self._from.get_name}")
        elif qty < self._amount:
            print(f"Отгрузили только {qty} {self._product}"
                  f" из {self._from.get_name}. Больше не было!")

        print(f"Везу {qty} {self._product} в {self._to.get_name}")
        is_ok = self._to.add(self._product, qty)
        if is_ok:
            print(f"Загрузка {self._product} в {self._to.get_name} завершена")
        else:
            print("Что-то пошло не так, но мы не знаем что!")
