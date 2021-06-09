from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_db(data):
#     with open('database.txt',mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'\nEmail : {email}\t,Subject : {subject}\t,Message : {message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/form_submitted', methods=['POST','GET'])
def form_submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_db(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            print('something went wrong... data did not save to the database\n Try again later')
    else:
        print('Something went wrong.Try again....')
