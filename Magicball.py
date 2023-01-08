#!/opt/homebrew/bin/python3
import random
import time
random_number = random.randint(1, 13)

print("Welcome. The magic-ball will answer any of your yes/no questions.")

name = input("Tell me your name." )

question = input("Write your question." )


print(name, "asks:", question)

answer = ""

time.sleep(2)

print("MAGIC 8-ball answers:" + answer)
#it works.
if random_number == 1:
  print("Yes, definetely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Maybe.")
elif random_number == 9:
  print("Very doubtful.")
elif random_number == 10:
  print("No.")
elif random_number == 11:
  print("Unlikely, and you will suffer.")
elif random_number == 12:
  print("No, but something good will happen.")
elif random_number == 13:
  print("Perhaps, but hey, at least you're hot.")

else:
  answer = "Error"



