from datetime import datetime as dt

def logger(action, data):
    time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('data\log\log.csv', 'a', encoding='utf-8') as file:
        file.write('{},{},{}\n'
                    .format(time, action, data))