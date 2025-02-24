from datetime import datetime

class Event:
    def __init__(self, id, date, title, text):
        self.id = id
        self.date = date
        self.title = title
        self.text = text

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'text': self.text
        }