import sqlite3
from flask import Flask, request, render_template, redirect, url_for,flash,jsonify
import flask
import csv
from flask_cas import CAS, login_required

app = Flask(__name__)
cas = CAS(app, '/cas')
app.secret_key = 'longsecretkey'
app.config['CAS_SERVER'] = 'https://login.iiit.ac.in'
app.config['CAS_AFTER_LOGIN'] = 'route_dashboard'  

@app.route('/')
def front_page():
    return render_template('front_page.html')

@app.route('/test/<data>',methods=['GET'])
def test(data):
    print(data)
    print("Bhajiya")
    return redirect(url_for('logout'))

@app.route('/login')
def login():
    return flask.redirect(flask.url_for('cas.login', _external=True))

@app.route('/logout')
def logout():
    return flask.redirect(flask.url_for('cas.logout', _external=True))

@app.route('/route_dashboard')
@login_required # Ensure that this function is only called if the user is logged in
def route_dashboard():
    username = cas.username
    if cas.username:
        # try:
        #     email = cas.attributes.get('cas:E-Mail', '')
        #     if (email=="security@iiit.ac.in" or email=="kushal.s@students.iiit.ac.in"):
        #         return render_template('security_dashboard.html', username=cas.username, email=email, first_name=first_name, last_name=last_name, roll_no=roll_no)
        #     first_name = cas.attributes.get('cas:FirstName', '')
        #     last_name = cas.attributes.get('cas:LastName', '')
        #     roll_no = cas.attributes.get('cas:RollNo', '')
        #     return render_template('student_dashboard.html', username=cas.username, email=email, first_name=first_name, last_name=last_name, roll_no=roll_no)
        # except:
        #     print("CAS failed")
        jsonified=jsonify([{'hi': 2}])
        print(jsonified)
        print("HI")
        return redirect(url_for('test',data="Hello",code=200))
    else:
        return redirect(url_for('login'))
    
@app.route('/new_courier')
@login_required
def new_courier():
    # If data is sent
    if flask.request.method == 'POST':
        # Get the data
        name = flask.request.form.get('name')
        hostel = flask.request.form.get('hostel')
        room_number = flask.request.form.get('room_number')
        courier_handler = flask.request.form.get('courier_handler')
        date = flask.request.form.get('date')
        description = flask.request.form.get('description')
        taken = flask.request.form.get('taken')
        
        try:
            # TODO: Save to db

            # Return a JSON response indicating success
            return jsonify({'status': 'success', 'message': 'Courier details entered successfully!'})

        except Exception as e:
            # Return a JSON response indicating failure
            return jsonify({'status': 'error', 'message': str(e)}), 500

        
    # Show the new courier form
    return render_template('new_courier.html')

if __name__ == '__main__':
    app.run(debug=True)
    

connection=sqlite3.connect('courier.db')
cursor = connection.cursor()

create_table="""
CREATE TABLE Couriers (
    Order_id INT AUTO_INCREMENT,
    Email_id VARCHAR,
    Name VARCHAR,
    Hostel VARCHAR,
    Room_no VARCHAR,
    Type VARCHAR,
    Date VARCHAR,
    Address VARCHAR,
    Taken VARCHAR,
    PRIMARY KEY (Order_id)
);
"""
# cursor.execute(create_table)
# connection.commit()

# csv_path = './output_1.csv'

# with open(csv_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     i=int(0)
#     # Clean up data like OBHD OBH OBHE using regex identify patterns ig
#     # do i want to minimise data ya seedha idk
#     for row in csv_reader:
#         if (i==0):
#             i=1
#             continue
#         query=f"INSERT INTO Couriers VALUES({row[0]},NULL,'{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')"
#         cursor.execute(query)
# connection.commit()
# cursor.fetchall()
query="SELECT * FROM Couriers WHERE Name like 'Prithvi%'"
# query="SELECT * FROM Couriers WHERE Email_id='prithvi.karthik@students.iiit.ac.in'"
cursor.execute(query)
answers=cursor.fetchall()
for ans in answers:
    # data about all orders for that person if email id use other query
    print(ans)
# query="INSERT INTO Transactions VALUES(3,0,2,3,20)"
# cursor.execute(query)
# query="INSERT INTO CurrUser VALUES(1,'Harry')"
# cursor.execute(query)

app = Flask(__name__)
DATABASE = 'split.db'
app.config['TEMPLATE_AUTO_RELOAD']=True
# Function to get a database connection
def get_db_conn():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# # Route to display the add user form
@app.route('/add_entry')
def add_user_form():
    return render_template('add_entry.html')

# # Route to add a new user to the database
@app.route('/add_entry', methods=['POST'])
def add_user():
    conn = get_db_conn()
    cursor2 = conn.cursor()
    # Get data from form how dekhna padega
    cursor2.execute(f"INSERT INTO Couriers VALUES ('')")
    conn.commit()
    conn.close()
    return redirect(url_for('add_entry_form'))