##Иерархического логирование

В первую таблицу LogInstanceApp пишеться информация 
о каждом старте приложения:

* app_log_id - уникальный номер
* log_instance_name - название приложения
* start_app_time - время начала логгирования
* error_time - ключ, который относится к Таблице TimeErrorApp

Вторая Таблица TimeErrorApp пишеться информация, в какой
момент времени произошла ошибка

* id_time_error - уникальный номер
* end_app_time - время остановки логгирования из-за ошибки

Третья Таблица Логов (Log) в ней указываеться

* id_log - уникальный номер
* url_request - адресс, по которому пользователь сделал запрос
* user_agent - какого клиента использовал пользователь
* ip_address - IP пользователя
* request_date - время запроса
* response_date - время отклика
* methods - HTTP метод
* status_code - статус код HTTP протакола
* request_body - тело запроса
* response_body - тело отклика
* log_app - ключ к приложению
* user - ключ к пользователю

Четвертая Таблица Пользователя (Users)

* id_user - уникальный номер
* email - email
* phone_number - телефон

##Важно

поле end_app_time определяеться по значению поля status_code в Таблице Логов, 
когд приходит 4xx или 5xx ошибка это поле сразу же записываеться и привязываеться к таблице LogInstanceApp