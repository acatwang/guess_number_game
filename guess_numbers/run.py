import numpy as np


def set_up():
	ans = np.random.choice(10, 4, replace=False)
	return(ans)

def conv_ans(nums):
	'''convert a list of numbers to a map: num <> position'''
	return dict(zip(map(str, nums), range(1,5)))
	

def evaluate(guess, ans_ints):
	'''
	guess: a four-digit number string
	ans_ints: a list of four numbers
	'''
	
	#ans: a map with four key<> position
	ans = conv_ans(ans_ints)

	num_a = 0
	num_b = 0

	for pos, i in enumerate(guess, 1):
		if ans.get(i): 
			num_b += 1
			if pos == ans[i]:
				num_a += 1
				num_b -= 1

	return [num_a, num_b]
	

def val_inputs(guess):
	if len(guess) != 4:
		print "You should guess a four-digit number."
		return 'invalid inputs'
	if guess.lower() == "e" :
		print("Bye!")
		return 'exit'
	return 'cont'

def main():
	ANS = set_up()
	tries = 0

	while True:
		guess = str(raw_input("Guess 4 numbers (Exit with E) : "))

		decision = val_inputs(guess)
		if decision == 'invalid inputs':
			continue
		elif decision == 'exit':
			break
		elif decision == 'cont':
			tries += 1
			a,b = evaluate(guess, ANS)
			if a == 4:
				print "You Win!! You get the answer with {0} tries.".format(tries)
				print "The answer is: " + "".join(str(i) for i in ANS)
				break
			else:
				print("{0} A {1} B".format(a, b))




if __name__ == '__main__':
	main()
