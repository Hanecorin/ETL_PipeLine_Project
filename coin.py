from flask import Flask, request, render_template
from dto import bitDTO
from dao import bitDAO
import json

app = Flask(__name__)

@app.route("/")
def intro():
    print("intro")
    return render_template("index.html")

@app.route('/select', methods=['GET','POST'])
def select():
    name = request.form.get("name")
    myresult = bitDAO().allcoin(name)
    result_json = json.dumps(myresult)

    return result_json

@app.route('/minmax', methods={'POST'})
def minmaxCoin():
    name = request.form.get("name")
    myresult = bitDAO().minmax(name)
    
    result_json = json.dumps(myresult)

    return result_json
    
    

@app.route('/intro', methods=['POST'])
def selectname():
    
    myresult = bitDAO().selectname()
    
    result_json = json.dumps(myresult)

    return result_json
    

if __name__ == "__main__":
    app.run(debug=True)
