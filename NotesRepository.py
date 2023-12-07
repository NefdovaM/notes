import datetime
import json
from datetime import datetime
from Note import Note, DATE_FORMAT


def loadFromFile() -> [Note]:
    with open("database.json", "r") as read_file:
        return json.load(read_file, object_hook=lambda d: Note(**d))


LIST_OF_NOTES: [Note] = loadFromFile()


def get_all_notes() -> [Note]:
    return LIST_OF_NOTES


def get_by_date(date_time: datetime):
    result = []
    for note in LIST_OF_NOTES:
        edit_at = note.get_edit_at()
        if (edit_at.year == date_time.year and
                edit_at.day == date_time.day and
                edit_at.month == date_time.month):
            result.append(note)
    return result


def is_note_exist(id: int) -> bool:
    for item in LIST_OF_NOTES:
        if item.id == id:
            return True
    return False


def drop_note(id: int) -> Note:
    targetNote = get_note(id)
    LIST_OF_NOTES.remove(targetNote)
    return targetNote


def get_note(id: int) -> Note:
    for item in LIST_OF_NOTES:
        if item.id == id:
            return item
    return None


def create_note(title: str, body: str):
    new_note_id = get_all_notes()[-1].id + 1
    new_note = Note(new_note_id, title, body, datetime.now().strftime(DATE_FORMAT))
    LIST_OF_NOTES.append(new_note)


def safe_file():
    with open("database.json", "w") as read_file:
        read_file.write(json.dumps([obj.__dict__ for obj in LIST_OF_NOTES], default=serialize_datetime))


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime(DATE_FORMAT)
    raise TypeError("Type not serializable")


def update_note(id, title, body):
    i = 0
    while i != len(LIST_OF_NOTES):
        if LIST_OF_NOTES[i].id == id:
            LIST_OF_NOTES[i] = Note(id, title, body, datetime.now().strftime(DATE_FORMAT))
            return
        i = i + 1
