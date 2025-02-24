from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from methods import create_event, read_event, read_events, update_event, delete_event
import uuid

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    events = read_events()[0]
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        event_id = str(uuid.uuid4())
        date = request.form['date']
        title = request.form['title']
        text = request.form['text']
        response, status_code = create_event(event_id, date, title, text)
        if status_code == 201:
            flash(response['message'], "success")
            return redirect(url_for('index'))
        else:
            flash(response['error'], "error")
    return render_template('add.html')

@app.route('/edit/<event_id>', methods=['GET', 'POST'])
def edit(event_id):
    event = read_event(event_id)[0]
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['title']
        text = request.form['text']
        response, status_code = update_event(event_id, date, title, text)
        if status_code == 200:
            flash(response['message'], "success")
            return redirect(url_for('index'))
        else:
            flash(response['error'], "error")
    return render_template('edit.html', event=event)

@app.route('/delete/<event_id>', methods=['GET', 'POST'])
def delete(event_id):
    event = read_event(event_id)[0]
    if request.method == 'POST':
        response, status_code = delete_event(event_id)
        if status_code == 200:
            flash(response['message'], "success")
            return redirect(url_for('index'))
        else:
            flash(response['error'], "error")
    return render_template('delete.html', event=event)


@app.route('/api/v1/calendar/events', methods=['POST'])
def api_add_event():
    data = request.get_json()
    event_id = str(uuid.uuid4())
    date = data.get('date')
    title = data.get('title')
    text = data.get('text')
    return jsonify(create_event(event_id, date, title, text))

@app.route('/api/v1/calendar/events', methods=['GET'])
def api_list_events():
    return jsonify(read_events())

@app.route('/api/v1/calendar/events/<event_id>', methods=['GET'])
def api_get_event(event_id):
    return jsonify(read_event(event_id))

@app.route('/api/v1/calendar/events/<event_id>', methods=['PUT'])
def api_update_event(event_id):
    data = request.get_json()
    date = data.get('date')
    title = data.get('title')
    text = data.get('text')
    return jsonify(update_event(event_id, date, title, text))

@app.route('/api/v1/calendar/events/<event_id>', methods=['DELETE'])
def api_delete_event(event_id):
    return jsonify(delete_event(event_id))

if __name__ == '__main__':
    app.run(debug=True)