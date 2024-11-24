# TODO Напишите функцию find_common_participants
def find_common_participants(str_list1, str_list2, delimetr=","):
    result_list = []
    list_1 = str_list1.split(delimetr)
    list_2 = str_list2.split(delimetr)
    for el1 in set(list_1):
        for el2 in set(list_2):
            if el1 == el2:
                result_list.append(el1)
    result_list.sort()
    return result_list
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
