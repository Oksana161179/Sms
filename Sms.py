import smtplib
from email.message import EmailMessage
from wsgiref.simple_server import server_version

sender_email = 'evapython@yandex.ru'#адрес отправителя
recipient_mail = 'oksana.fomenko.16.11.1979@mail.ru'#адрес получателя
password = 'jwtdiqpoecddskbg'#пароль для почты
subject = 'Проверка связи!'#пишем тему письма
body = 'Привет из программы на Питоне!'#тело письма, то что мы хотим написать

msg = EmailMessage()
msg.set_content(body)#создаем контент и указываем что будет в письме-body
msg['Subject'] = subject
msg['From'] = sender_email#от кого
msg['To'] = recipient_mail#кому

try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)#указываем путь и номер порта
    server.login(sender_email, password)#указываем логин и пароль
    server.send_message(msg)#отправляем письмо
    print('Письмо отправлено!')#выводим сообщение об отправке
except Exception as e:#обрабатываем исключения
    print(f'Ошибка: {e}')#выводим сообщение об ошибке
finally:#то, что выполнится в любом случае
    if server:#если сервер работал
        server.quit()#то мы его закрываем

