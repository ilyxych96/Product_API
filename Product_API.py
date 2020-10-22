from flask import Flask, request
import csv

'''
2) Стратегия масштабирования:
    1) Разбить входной файл на несколько файлов таким образом, что в каждом таком файле хранятся только товары, 
    название которых начинается на одну букву. При запросе открывать только необходимый файл. 
    2) Реалиовать многопоточное считвание данных из файла
    3) Реализованый мной алгоритм имеет сложность О(n) по времени, использование памяти не зависит от размера фала.
'''

app = Flask(__name__)
input_file = 'recommends.csv'

@app.route('/', methods=['GET'])
def welcome_page():
    return r"Example: http://127.0.0.1:5000/recommends/R66uXO6er6?min_probability=0.7"


@app.route('/recommends/<string:product_name>', methods=['GET'])
def get_products(product_name):
    if 'min_probability' in request.args:
        min_probability = float(request.args['min_probability'])
    else:
        min_probability = 0.0

    output_string = ''
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == product_name and float(row[2]) >= min_probability:
                output_string += row[1] + '<br />'

    return output_string


if __name__ == '__main__':
    app.run()
