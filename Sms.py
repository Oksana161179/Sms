import smtplib
from email.message import EmailMessage
from tkinter import *


def send_email():
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

    server = None

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

window = Tk()#создаем окно
window.title('Отправка Email')#задаем заголовок окну
window.geometry("500x300")#задаем размеры окну

Label(text="Отправитель: ").grid(row=0, column=0, sticky=W)#создаем метку с первой строки с нулевым индексом,
# в первой колонке с нулевым индексом и которая растянется во все поле(W) в одну сторону
sender_email_entry = Entry()#соэдаем поле ввода отправителя
sender_email_entry.grid(row=0, column=1, sticky=W)

Label(text="Получатель: ").grid(row=1, column=0, sticky=W)#создаем метку с первой строки с нулевым индексом,
# в первой колонке с нулевым индексом и которая растянется во все поле(W) в одну сторону
recipient_email_entry = Entry()#соэдаем поле ввода получателя
recipient_email_entry.grid(row=1, column=1, sticky=W)

Label(text="Тема письма: ").grid(row=3, column=0, sticky=W)#создаем метку для ввода темы письма
subject_entry = Entry()#соэдаем поле ввода отправителя
subject_entry.grid(row=3, column=1, sticky=W)

Label(text="Сообщение: ").grid(row=3, column=0, sticky=W)#создаем метку для ввода сообщения
body_text = Text(width=45, height=10)#соэдаем многострочное текстовое поле и задаем ему размеры
body_text.grid(row=4, column=1, sticky=W)

Button(text='Отправить письмо', command=send_email).grid(row=5, column=1, sticky=W)
#создаем кнопку для отправления письма

result_label = Label(text='')
result_label.grid(row=6, column=1, sticky=W)

window.mainloop()

