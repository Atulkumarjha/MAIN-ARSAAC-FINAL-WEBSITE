from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import subprocess
from project1 import AACChatbot

app = Flask(__name__)
aac_chatbot = AACChatbot()


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'aftab18',
    'database': 'aac',
}


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        udid = request.form['udid']
        password = request.form['password']
        phone_no = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']

        try:

            connection = mysql.connector.connect(**db_config)
            print("Connection successful")
            cursor = connection.cursor()

            query = "INSERT INTO users (name, email_id, udid, password, phone, gender, age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (name, email, udid, password, phone_no, gender, age)

            cursor.execute(query, values)

            connection.commit()
            cursor.close()
            connection.close()

            return redirect(url_for('login'))
        except mysql.connector.Error as err:

            print(f"Error: {err}")

    return render_template('signup.html')


def verify_user(email, password):
    try:

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email_id = %s AND password = %s"
        values = (email, password)
        cursor.execute(query, values)

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user

    except mysql.connector.Error as err:

        print(f"Error: {err}")
        return None


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login_success')
def success():
    return render_template('login_sucsess.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = verify_user(email, password)

        if user:

            return render_template('login_success.html', email=email)

        error_message = 'Invalid email or password. Please try again.'
        return render_template('login.html', error_message=error_message)

    return redirect(url_for('home'))


@app.route('/paralytic')
def paralytic():
    return render_template('paralytic.html')


@app.route('/home')
def main():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/food')
def food():
    return render_template('food.html')


@app.route('/drink')
def drink():
    return render_template('drink.html')


@app.route('/places')
def places():
    return render_template('places.html')


@app.route('/activities')
def activities():
    return render_template('activities.html')


@app.route('/feeling')
def feeling():
    return render_template('feeling.html')


@app.route('/medical')
def medical():
    return render_template('medical.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')


@app.route('/body')
def body():
    return render_template('body.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


@app.route('/dishes')
def dishes():
    return render_template('dishes.html')


@app.route('/hygiene')
def hygiene():
    return render_template('hygiene.html')


@app.route('/sports')
def sports():
    return render_template('sports.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')


@app.route('/hindi')
def hindi():
    return render_template('hindi.html')


@app.route('/hindi_index')
def hindi_index():
    return render_template('hindi_index.html')


@app.route('/bodyhindi')
def hindibody():
    return render_template('bodyhindi.html')


@app.route('/clothes_hindi')
def clothes_hindi():
    return render_template('clothes_hindi.html')


@app.route('/food_hindi')
def food_hindi():
    return render_template('food_hindi.html')


@app.route('/hygiene_hindi')
def hygiene_hindi():
    return render_template('hygiene_hindi.html')


@app.route('/sports_hindi')
def sports_hindi():
    return render_template('sports_hindi.html')


@app.route('/indexhindi')
def indexhindi():
    return render_template('indexhindi.html')


@app.route('/foodhindi')
def foodhindi():
    return render_template('foodhindi.html')


@app.route('/drinkhindi')
def drinkhindi():
    return render_template('drinkhindi.html')


@app.route('/activitieshindi')
def activitieshindi():
    return render_template('activitieshindi.html')


@app.route('/medicalhindi')
def medicalhindi():
    return render_template('medicalhindi.html')


@app.route('/placeshindi')
def placeshindi():
    return render_template('placeshindi.html')


@app.route('/feelinghindi')
def feelinghindi():
    return render_template('feelinghindi.html')


@app.route('/paralytic')
def paralytic_page():
    return render_template('paralytic.html')


@app.route('/runeyscript', methods=['POST'])
def run_eye_gaze_script():
    try:
        subprocess.run(
            ['python', 'C:/Users/shahid khan/Downloads/integration project/eyegaze.py'], check=True)
        return jsonify({'status': 'success', 'message': 'Script executed successfully'})
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': f'Script execution failed: {e}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'An unexpected error occurred: {e}'})


@app.route('/chatbotlogin')
def chatbotlogin():
    return render_template('chatbotlogin.html')


@app.route('/process_input', methods=['POST'])
def process_user_input():
    user_input = request.form['user_input']

    if user_input.lower() in ["exit", "quit", "bye"]:
        return jsonify({"response": "Goodbye! Take care."})

    entities, response = aac_chatbot.process_input(user_input)

    if entities:
        print("Entities:", entities)
    if response is not None:
        print("Chatbot:", response)
    if response is None:
        print("I'm sorry, I didn't understand that.")

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
