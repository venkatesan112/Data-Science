def guess(a):
  n=int(input())
  if(n==a):
    print("you guess it right")
  elif(n>a):
    print("Try a small number")
    guess(a)
  else:
    print("try a Big number")
    guess(a)
import random
a=random.randint(1,100)
guess(a)
