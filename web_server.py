from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)


@app.route('/submit_email', methods=['POST', 'GET'])
def submit_email():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_data(data)
            return redirect('/thank_you.html')
        except:
            return 'Error saving to database'
    else:
        return 'something wrong submiting email'


def write_data(data):
    with open('web/database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_w = csv.writer(database, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_w.writerow([email, subject, message])
