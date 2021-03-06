from flask import Flask, jsonify # из библиотеки flask импортирует класс Flask() и функцию jsonify()
import time # импортирует библиотеку для работы со временем


APP_NAME = 'MSGCHAT' # задаем название мессенджера


app = Flask(APP_NAME) # создаем объект Flask-приложения для дальнейшей работы с ним


@app.route('/') # говорим, что идущая за этой строкой функция будет вызвана, когда пользователь перейдет в браузере по адресу /
def index(): # функция для обработки захода на адрес, заданный строкой выше
    return APP_NAME # просто выводим в браузер имя мессенджера


@app.route('/status') # идущая за этой строкой функция будет вызвана, когда пользователь перейдет в браузере по адресу /status
def status():
    # задаем в переменную msg то, что нужно будет вывести
    msg = {
        'status': True,
        'name': APP_NAME,
        'time': time.time_ns() # время в наносекундах
    }

    return jsonify(msg) # выводим пользователю превращенный в JSON словарь


if __name__ == "__main__": # следующая строка будет выполнена только если этот файл будет вызван в качестве исполняемого, а не присоединен, как библиотека
    app.run() # запустить сервер