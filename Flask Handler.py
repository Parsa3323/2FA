from flask import Flask, render_template, json, request
import Main
import random

app = Flask(__name__, template_folder='public')

@app.route('/', methods=['POST', 'GET'])
def main():
    thin = "sd"
    if request.method == 'POST':
        thin = request.form.get('Pin')
        print(thin)
    return render_template(template_name_or_list='index.html')
@app.route('/go', methods=['POST'])
def POsST():
    code = request.form.get('Pin')
    valr = Main.get_and_check(user="None", code_provided=code)
    if valr is not False:
        return "yoo sighned up succses"
    else:
        return "sorry"
    # thin = "sd"
    # if request.method == 'POST':
    #     thin = request.form.get('Pin')
    #     print(thin)
    # return thin
@app.route('/create-accc')
def create():



    return render_template('CreateAcc.html')

app.run(debug=True)
