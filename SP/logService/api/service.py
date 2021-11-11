# from ..models import LogInstanceApp

dct = {
    "id_log": "d056ba04-8062-413e-bc25-b753c31c2108",
    "url_request": "http://restoran.com",
    "user_agent": "Mozilla",
    "ip_address": "192.168.0.243",
    "request_date": "2021-11-10T23:56:00Z",
    "methods": "GET",
    "status_code": 504,
    "response_body": "{\r\n    text\r\n}",
    "request_body": "{\r\n    text\r\n}",
    "log_app": "d458c01e-d2e1-4098-b663-8a0f2ba37973",
    "user": "30f40eac-55cd-4dd5-9cb6-0673e44f99b1"
}

def check_log():
    status_code = dct['status_code']
    if str(status_code)[0] == 4 or 5:
        print('Lf')
        # LogInstanceApp.objects.filter(app_log_id=dct['log_app']).update(end_app_time=dct['request_date'])

check_log()