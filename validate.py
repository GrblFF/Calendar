from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True, None
    except ValueError:
        return False, "Неверный формат даты. Напишите в виде ГГГГ-ММ-ДД."

def validate_title(title):
    if len(title) <= 30:
        return True, None
    return False, "Заголовок должен быть не более 30 символов."

def validate_text(text):
    if len(text) <= 200:
        return True, None
    return False, "Сообщение должно быть не более 200 символов."