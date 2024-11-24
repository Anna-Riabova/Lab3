# TODO Напишите функцию для поиска индекса товара
def find_index_item(list_, item):
    result = None
    is_found = False
    for i in range(len(list_)):
        if not is_found:
            if list_[i] == item:
                result = i
                is_found = True
    return result

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
