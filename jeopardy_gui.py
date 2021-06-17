from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import jeopardydata

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

app.config['SECRET_KEY'] = 'elpZKAufdmr9OqohwiM3'


@app.route('/', methods=['GET', 'POST'])
def player_name():
	title = 'Welcome to Jeopardy!'
	session.clear()
	return render_template('player.html',
							the_title = title)


@app.route('/main', methods=['GET', 'POST'])
def main_page():
	title = 'Jeopardy'
	if 'final_money' not in session:
		session['final_money'] = 0
	else:
		pass
	#Grey out buttons already clicked
	if 'buttoncount' not in session:
		session['buttoncount'] = list()
	else:
		pass
	if len(session['buttoncount']) < 25:
		return render_template('main.html',
								the_title=title)
	else:
		return redirect(url_for('end_game'))


@app.route('/select_question', methods=['GET', 'POST'])
def ask_question():
	title = 'Jeopardy'
	session['buttonid'] = int(request.form.get('clicked_btn'))
	session['buttoncount'].append(session.get('buttonid'))
	session.modified = True
	money_c = jeopardydata.Money(session.get('buttonid'))
	session['round_money'] = money_c.get_money()
	question_c = jeopardydata.Questions(session.get('buttonid'))
	question = question_c.get_question()
	return render_template('question.html',
							the_title=title,
							the_money=session.get('round_money'),
							the_question=question)


@app.route('/results', methods=['GET', 'POST'])
def get_it_right():
	title = 'Jeopardy'
	player_answer = request.form['Player Answer']
	answer_c = jeopardydata.Answers(session.get('buttonid'))
	correct_answer = answer_c.get_answer()
	moneyf = jeopardydata.Validate(player_answer, correct_answer, session.get('round_money'), session.get('final_money'))
	session['final_money'] = moneyf.score_calc()
	return render_template('result.html',
							the_title=title,
							player_answer=player_answer,
							correct_answer=correct_answer,
							the_money=session.get('final_money'))


@app.route('/finish', methods=['GET', 'POST'])	
def end_game():
	title = 'Jeopardy'
	moneyf = session.get('final_money')
	return render_template('finished.html',
							the_title = title,
							final_money = moneyf)


if __name__ == '__main__':
	app.run(debug=True)