from art import tprint

from storage import Storage
from store import Store
from shop import Shop
from request import Request


def print_all_storages(storages: list[Storage]):
    print("\n=== Вот так сейчас на складах ===")
    for store in storages:
        print(store)
        print(store.get_items)
    print("\n===")


if __name__ == '__main__':
    tprint("items mover", font="univerce")

    new_store = Store(120)
    new_shop = Shop()
    store_list = [new_store, new_shop]

    new_store.add('apples', 10)
    new_store.add('oranges', 20)
    new_store.add('bananas', 10)
    new_store.add('grapes', 10)
    new_store.add('pineapples', 20)
    new_store.add('watermelons', 20)

    new_shop.add('bananas', 5)

    print_all_storages(store_list)

    user_input = ""
    while user_input not in ('exit', 'stop', 'стоп'):
        user_input = input("\nВведите запрос или stop|status: ")
        if user_input in ('status', 'статус', 'exit', 'stop', 'стоп'):
            print_all_storages(store_list)
        else:
            try:
                new_request = Request(store_list, user_input)
                new_request.execute()
            except Exception as e:
                print(f"Error: {e}")
