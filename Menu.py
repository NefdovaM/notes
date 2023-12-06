import datetime

from NotesController import *

MENU_EXIT = "0"
MENU_SHOW_ALL = "1"
MENU_FIND_BY_DATE = "2"

NODE_ACTION_DELETE = "1"
NODE_ACTION_EDIT = "2"


def startMainMenu():
    while True:
        print('Введите ваш выбор: ')
        print(MENU_EXIT + " для выхода")
        print(MENU_SHOW_ALL + " для вывода списка заметок")
        print(MENU_FIND_BY_DATE + " поиск по дате")
        userInput = input()
        if userInput == MENU_EXIT:
            break
        if userInput == MENU_SHOW_ALL:
            nodes = get_all_notes()
            print("Выбуруте заметку")
            for currentNode in nodes:
                print(currentNode.id.__str__() + ") " + currentNode.title)
            id = int(input())
            if not is_node_exist(id):
                print("нету такой заметки")
                break

            print("Что дулать")
            print(NODE_ACTION_DELETE + ") удалить")
            print(NODE_ACTION_EDIT + "2) обновить")
            action = int(input())
            do_action_with_node(get_node(id), action)

        elif userInput == MENU_FIND_BY_DATE:
            print("введите дату dd-mm-yyyy")
            date = input()
            day, month, year = map(int, date.split('-'))
            inputted_date = datetime.date(year, month, day)
            get_by_date(inputted_date)

    print("Хорошего дня ")


def do_action_with_node(node: Node, action: int):
    if action.__str__() == NODE_ACTION_DELETE:
        print("вы удалили " + drop_node(node.id).title)
