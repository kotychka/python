import random
import simplegui

# Global variables
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ''
computer_choice = ''

def choice_to_number(choice):
	# if choice == 'rock':
	# 	return 0
	# elif choice == 'paper':
	# 	return 1
	# else: return 2
	return {'rock':0, 'paper':1, 'scissors':2}[choice]


def number_to_choice(number):
	# if number == 0:
	# 	return 'rock'
	# elif number == 1:
	# 	return 'paper'
	# else: return 'scissors'
	return {0:'rock', 1:'paper', 2:'scissors'}[number]

def random_computer_choice():
	return random.choice(['rock', 'paper', 'scissors'])

def choice_result(human_choice, computer_choice):
	global COMPUTER_SCORE
	global HUMAN_SCORE
	human_number = choice_to_number(human_choice)
	computer_number = choice_to_number(computer_choice)
	
	if (human_number - computer_number) % 3 == 1:
		COMPUTER_SCORE +=1
	elif human_number == computer_number:
		print('Tie')
	else:
		HUMAN_SCORE +=1

def test_choice_to_number():
	assert choice_to_number('rock') == 0
	assert choice_to_number('paper') == 1
	assert choice_to_number('scissors') == 2

def test_number_to_choice():
	assert number_to_choice(0) == 'rock'
	assert number_to_choice(1) == 'paper'
	assert number_to_choice(2) == 'scissors'

def test_all():
	test_choice_to_number()
	test_choice_to_number()

test_all()

# Handlers for mouse click on buttons
def rock():
	global human_choice, computer_choice
	global HUMAN_SCORE, COMPUTER_SCORE

	human_choice = 'rock'
	computer_choice = random_computer_choice()
	choice_result(computer_choice, human_choice)

def paper():
	global human_choice, computer_choice
	global HUMAN_SCORE, COMPUTER_SCORE

	human_choice = 'paper'
	computer_choice = random_computer_choice()
	choice_result(computer_choice, human_choice)

def scissors():
	global human_choice, computer_choice
	global HUMAN_SCORE, COMPUTER_SCORE

	human_choice = 'scissors'
	computer_choice = random_computer_choice()
	choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
	try:
		# Draw choices
		canvas.draw.text("You: " + human_choice, [10,40], 48, 'Green')
		canvas.draw.text("Comp: " + human_choice, [10,80], 48, 'Red')

		# Draw scores
		canvas.draw.text("Human score: " + str(HUMAN_SCORE), [10,190], 30, 'Green')
		canvas.draw.text("Comp score: " + str(COMPUTER_SCORE), [10,190], 30, 'Red')

	except TypeError:
		pass

# Create a frame and assign callbacks to event handlers
def play_rps():
	frame = simplegui.create_frame('Home', 300, 200)
	frame.add_button('Rock', rock)
	frame.add_button('Paper', paper)
	frame.add_button('Scissors', scissors)
	frame.set_draw_handler(draw)

	# Start the frame animation
	frame.start()

play_rps()