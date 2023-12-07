import datetime

DATE_FORMAT = "%d.%m.%Y %H:%M"


class Note:
    def __init__(self, id: int, title: str, body: str, editAt: str):
        self.id = id
        self.title = title
        self.body = body
        self.editAt = datetime.datetime.strptime(editAt, DATE_FORMAT)

    def get_formatted_date(self) -> str:
        return datetime.datetime.strftime(self.editAt, DATE_FORMAT)

    def get_edit_at(self) -> datetime:
        return self.editAt
