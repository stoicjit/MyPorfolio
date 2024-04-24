from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/submitted.html")
def hesubmitted():
    return render_template('submitted.html')

def write_to_csv(data):
    with open('database.csv', mode='a', newline = '') as database2:
        name = data["name"]
        email = data["email"]
        phone = data['phone']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter = ',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,  email,  phone,  message])

@app.route('/submit-form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/submitted.html")
    else:
        return 'something went wrong'
    


