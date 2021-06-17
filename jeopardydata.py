import pandas as pd

path = r'' #Insert your file path here

#Read excel file and put each category into its own dataframe
questions = pd.read_excel(path, sheet_name='board')
questions = pd.DataFrame(questions)
#print(questions)

#Main Route
def find_final_money(session):
	if 'final_money' not in session:
		session['final_money'] = 0
	else:
		session['final_money']

def is_it_there(session):
	if 'buttoncount' not in session:
		session['buttoncount'] = list()
	else:
		session['buttoncount']

#Questions Route
class Money():
	def __init__(self, buttonid):
		self.button = buttonid

	def get_money(self):
		'''function returns corresponding dollar value of question'''
		index = questions.set_index('Button ID', inplace=False)
		return questions['Dollar'].loc[self.button]

class Questions():
	def __init__(self, buttonid):
		self.button = buttonid
	
	def get_question(self):
		'''function returns the corresponding question based on button selection from main page'''
		index = questions.set_index('Button ID', inplace=False)
		return questions['Question'].loc[self.button]

#Results Route
class Answers():
	def __init__(self, buttonid):
		self.button = buttonid

	def get_answer(self):
		'''function returns answer to corresponding question in dataframe'''
		index = questions.set_index('Button ID', inplace=False)
		return questions['Answer'].loc[self.button]

class Validate():
	def __init__(self, player_answer, correct_answer, round_money, final_money):
		self.panswer = player_answer
		self.canswer = correct_answer
		self.rmoney = round_money
		self.fmoney = final_money

	def score_calc(self):
		'''function validates whether or not player answer matches and adds the dollar value to total'''	
		if self.panswer == self.canswer:
			return self.fmoney + self.rmoney
		else:
			return self.fmoney
