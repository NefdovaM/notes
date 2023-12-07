from NotesRepository import *
import datetime

MENU_EXIT = "0"
MENU_SHOW_ALL = "1"
MENU_NEW_NOTE = "2"
MENU_FIND_BY_DATE = "3"

NOTE_SHOW = "1"
NOTE_ACTION_EDIT = "2"
NOTE_ACTION_DELETE = "3"
MENU_PREVIOUS_STEP = "0"


def startMainMenu():
    while True:
        print('Введите необходимый пункт меню: ')
        print("Выберите " + MENU_EXIT + " для выхода")
        print(MENU_SHOW_ALL + " Все заметки")
        print(MENU_NEW_NOTE + " Создать новую заметку")
        print(MENU_FIND_BY_DATE + " Поиск заметки по дате")
        user_input = input()
        if user_input == MENU_EXIT:
            break
        if user_input == MENU_SHOW_ALL:
            while True:
                notes = get_all_notes()
                print("Выберите необходимую заметку. Для возврата в главное меню нажмите " + MENU_PREVIOUS_STEP)
                for currentNote in notes:
                    print(
                        currentNote.id.__str__() + " заголовок: " + currentNote.title + ", содержимое: " + currentNote.body)
                id = int(input())
                if id.__str__() == MENU_PREVIOUS_STEP:
                    break
                if not is_note_exist(id):
                    print("Такой заметки нет")
                    continue

                print("Что необходимо сделать? Для возврата нажмите " + MENU_PREVIOUS_STEP)
                print(NOTE_SHOW + " Показать заметку")
                print(NOTE_ACTION_EDIT + " Изменить заметку")
                print(NOTE_ACTION_DELETE + " Удалить заметку")
                action = input()
                if action == MENU_PREVIOUS_STEP:
                    continue
                do_action_with_note(get_note(id), action)

        elif user_input == MENU_FIND_BY_DATE:
            print("Введите дату в формате dd.mm.yyyy")
            date = input()
            day, month, year = map(int, date.split('.'))
            inputted_date = datetime.date(year, month, day)
            find_notes = get_by_date(inputted_date)
            if len(find_notes) == 0:
                print("Нет заметки от такой даты")
            else:
                print("Найдено " + len(find_notes).__str__() + " заметка(ок)")
                for note in find_notes:
                    print_note(note)
        elif user_input == MENU_NEW_NOTE:
            print("Введите заголовок")
            title = input()
            print("Введите содержимое заметки")
            body = input()
            create_note(title, body)
            print("Заметка создана")
            safe_file()
    safe_file()
    print("Хорошего дня ")


def do_action_with_note(note: Note, action: str):
    if action == NOTE_ACTION_DELETE:
        print("вы удалили " + drop_note(note.id).title)
        safe_file()
    elif action == NOTE_ACTION_EDIT:
        print("Введите новый заголовок")
        title = input()
        print("Введите новое содержимое заметки")
        body = input()
        print("Сохранить заметку? Y или N")
        safe = str(input())
        if safe == "Y":
            update_note(note.id, title, body)
            safe_file()
            print("Заметка сохранена")
        else:
            print("Заметка не сохранена")
    elif action == NOTE_SHOW:
        print_note(note)


def print_note(note: Note):
    print("Заголовок: " + note.title + " содержимое: " + note.body + " дата изменения: " + note.get_formatted_date())
