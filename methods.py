from storage import add_event, get_event_by_id, get_events, update_event as update_event_storage, delete_event as delete_event_storage, get_event_by_date
from validate import validate_date, validate_title, validate_text

def create_event(event_id, date, title, text):
    is_valid_date, date_error = validate_date(date)
    if not is_valid_date:
        return {"error": date_error}, 400

    is_valid_title, title_error = validate_title(title)
    if not is_valid_title:
        return {"error": title_error}, 400

    is_valid_text, text_error = validate_text(text)
    if not is_valid_text:
        return {"error": text_error}, 400

    exist_event = get_event_by_date(date)
    if exist_event:
        return {"error": "На указанную дату уже записано событие!"}, 400

    event = {
        "id": event_id,
        "date": date,
        "title": title,
        "text": text
    }
    add_event(event)
    return {"message": "Событие добавлено успешно!"}, 201

def read_event(event_id):
    event = get_event_by_id(event_id)
    if event:
        return event, 200
    return {"error": "Событие не найдено"}, 404

def read_events():
    return get_events(), 200

def update_event(event_id, date, title, text):
    is_valid_date, date_error = validate_date(date)
    if not is_valid_date:
        return {"error": date_error}, 400

    is_valid_title, title_error = validate_title(title)
    if not is_valid_title:
        return {"error": title_error}, 400

    is_valid_text, text_error = validate_text(text)
    if not is_valid_text:
        return {"error": text_error}, 400

    event = get_event_by_id(event_id)
    if not event:
        return {"error": "Событие не найдено"}, 404

    exist_event = get_event_by_date(date)
    if exist_event and exist_event['id'] != event_id:
        return {"error": "На указанную дату уже записано событие!"}, 400

    updated_event = {
        "id": event_id,
        "date": date,
        "title": title,
        "text": text
    }
   
    if update_event_storage(event_id, updated_event):
        return {"message": "Событие обновлено."}, 200
    return {"error": "Ошибка обновления события."}, 500

def delete_event(event_id):
    if delete_event_storage(event_id):
        return {"message": "Событие удалено."}, 200
    return {"error": "Событие не найдено."}, 404