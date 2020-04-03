import random

guessCount = 0
startNum = 5
number = random.randint(1,20)
correctGuess = 0

while guessCount < 10:
	currNum = number
	number = random.randint(1,20)
	if guessCount == 0:
		currNum = startNum
	guess = input("Higher(h) or Lower(l) than " + str(currNum) + "? ")
	if number - currNum > 0:
		if guess == "h":
			print ("correct! The number is " + str(number))
			correctGuess += 1
		else:
			print ("wrong :( The number is " + str(number))
	else:
		if guess == "l":
			print ("correct! The number is " + str(number))
			correctGuess += 1
		else:
			print ("wrong :( The number is " + str(number))
	guessCount += 1
print ("Game over, You got " + str(correctGuess) + " out of 10")

