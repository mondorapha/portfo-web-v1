import os
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_portfolio():
    return render_template('index.html')


@app.route("/<page_name>")
def my_portfolio_page(page_name):
    return render_template(page_name)


def write_to_csv_database(data):
    try:
        with open('./database.csv', mode='a', newline='', encoding='UTF-8') as csv_database_to_append:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(
                csv_database_to_append)
            csv_writer.writerow([email, subject, message])
    except FileNotFoundError as err1:
        print('Ooops, something went wrong. Database file not found.')
        raise err1
    except IOError as err2:
        print('Ooops, something went wrong. IO error.')
        raise err2


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data_received = request.form.to_dict()
            write_to_csv_database(data_received)
            return redirect('/thankyou.html')
        except Exception:
            return 'Ooops, something went wrong. Could not save to database.'
    else:
        return 'Ooops, something went wrong'
