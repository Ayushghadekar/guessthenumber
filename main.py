from random import randint
Easy_Level=5
hard_level=10
turns=0

def set_difficulty():
     try:
        level=input("choose any difficulty level hard/easy...")
     except:
            print("enter easy/hard")
     finally:
            if level=="easy":
               global turns
               turns=Easy_Level
               return turns
            else:
               turns=hard_level
               return turns



def check_answer(guess,answer,turns):
      if guess>answer:
          print("too high")
          return turns-1
      elif guess<answer:
          print("too low")
          return turns-1
      else:
          print("you got it !!tha answer is",answer)
def game():
     print("welcome tho guesing game!!")
     print("i am thinking a no between 1 to 200...")
     answer=randint(1,200)
     turns=set_difficulty()
     guess=0
     while guess!=answer:

         guess=int(input("make a  guess"))
         turns=check_answer(guess,answer,turns)
         print(" your remaining turns are {turns}")
         if turns==0:

             print("you havr run out of guessing you loss...")
             break
         elif guess!=answer:
             print("guess again")


game()