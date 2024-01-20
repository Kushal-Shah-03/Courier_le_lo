import flask
from flask import Flask, render_template, redirect, url_for
from flask_cas import CAS, login_required
import jsonify

app = Flask(__name__)
cas = CAS(app, '/cas')
app.secret_key = 'longsecretkey'
app.config['CAS_SERVER'] = 'https://login.iiit.ac.in'
app.config['CAS_AFTER_LOGIN'] = 'route_dashboard'  

@app.route('/')
def front_page():
    return render_template('front_page.html')

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
        email = cas.attributes.get('cas:E-Mail', '')
        first_name = cas.attributes.get('cas:FirstName', '')
        last_name = cas.attributes.get('cas:LastName', '')
        roll_no = cas.attributes.get('cas:RollNo', '')
        return render_template('dashboard.html', username=cas.username, email=email, first_name=first_name, last_name=last_name, roll_no=roll_no)
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