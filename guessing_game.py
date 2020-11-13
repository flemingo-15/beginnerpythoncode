import random #Used to import all random number functions

name = input("What's your name player? ")
player_answer = input("Hi there, would you like to play a number game? (Y or N): ")

while player_answer != ("y") and player_answer != ("Y") and player_answer != ("n") and player_answer != ("N"):
  player_answer = input("Please enter valid answer. ")
  #Ensures that as long as player inputs a non valid answer (Answer that is not y, Y, n, or N will reesult in a continuous "Please enter valid answer loop) If you were to take out the player_answer = input(), and just print, Please enter valid answer yould continously loop.

if player_answer == ("Y") or player_answer == ("y"):
  print("Great! Allow me to explain the rules. " + name + ", I am thinking of a number between 1 and 10. The goal is to guess my secret number in as few tries as possible. Good luck!") 
else: #Only else option is "n" or "N", as was clarified by the while statement
  print("Okay, I hope to see you again soon!")
  raise SystemExit

def main(): #This defines all code below as "main". This is so at the end of the code, I can repeat main and the code will loop in the play again option. Everything below main, needs to be indented, as all code below falls under main.

  secret_num = random.randint(1, 10) #The function random.randit continuos chooses a random interger between the field of intergers (1,10)

  for guessesTaken in range (1, 10): #Beginning of forloop, guessesTaken is a variable to represent player attempts
    guess = int(input("Take a guess. ")) #Converts guess input to an integer so it can be used in below integer if statements

    if guess < secret_num:
      print("Number is too low. Please try again ")
    elif guess > secret_num:
      print("Number is too high. Please try again ")
    else:
      break #The break statement in Python terminates the current loop and resumes execution at the next statement
  if guess == secret_num:
    print("Congratulations player! It took you " + str(guessesTaken) + " guess to win the game!")
  if guessesTaken < 5: #guessesTaken is an int so no need to convert to str
    print("You're not too shabby. Nice playing!")
  else:
    print("You need to improve your determining skills. Better luck next time!")

  rerun = input("Would you like to play again (Y or N): ")

  while rerun != ("y") and rerun != ("Y") and rerun != ("n") and rerun != ("N"):
    rerun = input("Invalid answer. Please enter valid answer!: ")
  if rerun == ("Y") or rerun == ("y"):
    main()
  else: 
    print("Goodbye!")

main() #Signals as the end of main, and allows the code to loop from def main to here using the play again option.
