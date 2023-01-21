import datetime

def log_data(regim, result):
    with open ('log.txt', 'a', encoding='utf=8') as file:
        file.write(f'{regim}={result}, Время запроса: {str(datetime.datetime.now())} \n')
