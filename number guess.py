def guess(a,count):
  n=int(input("Enter the Guess : "))
  if(n==a):
    print("you guess it right")
    print(a,count)
  elif(n>a):
    print("Try a small number")
    count+=1
    guess(a,count)
  else:
    print("try a Big number")
    count+=1
    guess(a,count)
import random
a=random.randint(1,100)
count=1
guess(a,count)
#function recursion 
