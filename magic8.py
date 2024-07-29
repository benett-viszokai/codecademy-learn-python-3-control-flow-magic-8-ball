# The Magic 8-Ball
import random

# Player's name
name = "Lacika"

# Player's question - Yes or No type
question = "Do you like me?"

# 8-Ball's answer (empty string for now)
answer = ""

# Generating a random number between 1 and 9
random_number = random.randint(1, 11)

# Answers
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Wow... IDK"
elif random_number == 11:
  answer = "No idea"
else:
  answer = "Error"

# Seeing the result
if question == "":
  print("No question, no answers.")
else:
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks the following: " + question)
  print("Magic 8-Ball says: " + answer + ".")
