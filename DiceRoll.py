#DiceRoll.py
#Name: Mia Garcia
#Date: 2/2/26
#Assignment: Lab 6 
import random

def main():
  trials = 10000

  rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  

  for i in range(trials):
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)

      total = die1 + die2
      rolls[total] += 1
  
  
  
  print("Total Rolls:", trials)
  

  total_percent = 0

  for total in range(2, 13):
      count = rolls[total]
      percent = (count / trials) * 100
      total_percent += percent

      print(f"{total}   {count}   {percent:.2f}%")


  print("Sum of counts =", sum(rolls))
  print("Sum of percentages ≈", round(total_percent, 2), "%")



if __name__ == '__main__':
  main()
