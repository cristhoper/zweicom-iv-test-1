from flask import Flask

app = Flask(__name__)


def fibonacci(n):
    n_1, n_2 = 1, 0
    for i in range(n):
        n_1, n_2 = n_2, n_1 + n_2
    return n_2


@app.route('/number/<number>', methods=['GET'])
def fibonacci_element(number):
    try:
        number = int(number)
        return str(fibonacci(number))
    except Exception as err:
        print(err)
        return "Input Error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
