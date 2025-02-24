events = []

def add_event(event):
    events.append(event)

def get_event_by_id(event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    return None

def get_events():
    return events

def update_event(event_id, new_event):
    for i, event in enumerate(events):
        if event['id'] == event_id:
            events[i] = new_event
            return True
    return False

def delete_event(event_id):
    for i, event in enumerate(events):
        if event['id'] == event_id:
            del events[i]
            return True
    return False

def get_event_by_date(date):
    for event in events:
        if event["date"] == date:
            return event
    return None