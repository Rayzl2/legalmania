from flask import Flask, render_template, request, url_for, redirect

import telebot

bot = telebot.TeleBot("5797412715:AAH83RHIhmku97FSZAgaBTrVapeZd8JE8_I")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
	if request.method == 'POST':
		name = request.form.get('name')
		tel = request.form.get('tel')
		question = request.form.get('question')
		print(name)
		print(tel)
		print(question)

		bot.send_message(-1001609265022, f'''Новая заявка!
Имя: {name}
Телефон: {tel}
Вопрос: {question}''')

		return redirect(url_for('contact'))

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
	app.run()