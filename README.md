# Calendar
*** 
Сервис замметок в календаре.

## 1. Подготовка к запуску
***

Перед запуском необходим проверить наличие установленного фреймворка Flask в окружении Python. Для этого в командной строке (в зависимости как установлены глобальные переменные) пишем `flask --version` или `python3 -m flask --version`. 

Если вы получили ошибку занчит нужно установить Flask, для этого в командной строке пишем `pip install Flask`.

## 2. Запуск приложения
*** 
Для запуска приложения откройте терминал, перейдите в каталог с приложением и запустите его командой `python app.py` или `python3 app.py` или `flask run` или `python3 flask run`. 

После этого прииложение будет доступно в браузере по адресу http://127.0.0.1:5000 и можно будет использовать веб-интерфейс.

## 3. Основные методы
*** 
### Получение списка событий

При открытии приложения в браузере http://127.0.0.1:5000 список созданных событий будет виден сразу.

Для просмотра в консоли отправьте запрос  (GET /api/v1/calendar/events)
`curl -X GET http://127.0.0.1:5000/api/v1/calendar/events`

### Создание события 
В браузере нажмите кнопку "Добавить событие", заполните все поля.

В консоли создайте запрос (POST /api/v1/calendar/events)
`curl -X POST http://127.0.0.1:5000/api/v1/calendar/events -H "Content-Type: application/json" -d '{"date": "2025-02-15", "title": "Мое событие", "text": "Описание события"}'`
Принимает JSON с полями date, title, text. Событие проверяется на уникальность и соответствие требованиям.

### Обновление события 
В браузере нажмите кнопку "Редактировать" у нужного события. Измените поля и нажмите кнопку "Редактировать".

В консоли создайте запрос (PUT /api/v1/calendar/events/event_id)
`curl -X PUT http://127.0.0.1:5000/api/v1/calendar/events/<event_id> -H "Content-Type: application/json" -d '{"date": "2025-02-15", "title": "Мое событие", "text": "Описание события"}`
Принимает JSON с полями date, title, text.

### Получение события по ID 
Для просмотра в консоли отправьте запрос  (GET /api/v1/calendar/events/event_id)
`curl -X GET http://127.0.0.1:5000/api/v1/calendar/events/<event_id>`


### Удаление события 
В браузере нажмите кнопку "Удалить" у нужного события. Подтвердите удаление.

Для удаления в консоли отправте запрос (DELETE /api/v1/calendar/events/event_id)
`curl -X DELETE http://127.0.0.1:5000/api/v1/calendar/events/<event_id>`