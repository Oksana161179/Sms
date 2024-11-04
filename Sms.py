import smtplib
from email.message import EmailMessage
from tkinter import *


def save():#создаем функцию для сохранения в файл
    with open('save.txt', 'w') as file:#открываем файл на запись(w) с именем file.
# если этого файла нет в нашей папке, то он будет создан.
        file.write(sender_email_entry.get() + '\n')#записываем в файл адрес отправителя
#чтобы было на следующей строке нужно прибавить символ переноса строки
        file.write(recipient_email_entry.get() + '\n')#записываем в файл адрес получателя
        file.write(password_entry.get() + '\n')#записываем в файл пароль для почты

def load():#создаем функцию загрузки
    try:#пробуем открыть файл
        with open('save.txt', 'r') as file:#открываем файл для чтения,
            # считали информацию и автоматически закрыли файл
            info = file.readlines()#readlines-читает информацию построчно и возвращает нам в список
            sender_email_entry.insert(0, info[0].strip())#вставляем информацию в поле,
            # на нулевое место в самое начало строки вставляем что-то из нашей информации.
            # первый элемент с индексом ноль.это поле отправителя. strip-удаляет все лишнее из строки
            recipient_email_entry.insert(0, info[1].strip())#вставляем информацию в поле получателя,
            # во вторую строку с индексом 1
            password_entry.insert(0, info[2].strip())#вставляем информацию в поле пароля,
            # в третью строку с индексом 2
    except FileNotFoundError:#обрабатываем ошибку, если не найден файл
        pass#чтобы программа не вылетела при первом запуске, когда файла еще нет


def send_email():#создаем функцию отправки
    save()#перед тем как все отправлять, вызываем функцию сохранения
    sender_email = sender_email_entry.get()#адрес отправителя
    recipient_mail = recipient_email_entry.get()#адрес получателя
    password = password_entry.get()#пароль для почты
    subject = subject_entry.get()#пишем тему письма
    body = body_text.get(1.0, END)#тело письма, то что мы хотим написать

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
        result_label.config(text='Письмо отправлено!')#выводим сообщение об отправке
    except Exception as e:#обрабатываем исключения
        result_label.config(text=f'Ошибка: {e}')#выводим сообщение об ошибке
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

Label(text="Пароль приложения: ").grid(row=2, column=0, sticky=W)#создаем метку для ввода темы письма
password_entry = Entry()#соэдаем поле ввода отправителя
password_entry.grid(row=2, column=1, sticky=W)

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

