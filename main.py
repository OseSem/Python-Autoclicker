from flask import *
import pyautogui, time


class Click:
    def __init__(self, amount:int):
        self.amount = int(amount)
        time.sleep(1)
        for i in range(self.amount):
            pyautogui.leftClick()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    Click(name)
    return render_template('index.html', name = name)

def run():
    app.run(port=6969, debug=True)

if __name__ == "__main__":
    run()