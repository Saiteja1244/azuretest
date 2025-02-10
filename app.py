from flask import Flask

app = Flask(__name__)

@app.route('/api1')
def api1():
    return "Hello from API 1!"

@app.route('/api2')
def api2():
    return "Welcome to API 2!"

@app.route('/api3')
def api3():
    return "This is API 3!"

@app.route('/api4')
def api4():
    return "You're accessing API 4!"

@app.route('/api5')
def api5():
    return "Greetings from API 5!"

if __name__ == '__main__':
    app.run(debug=True)
