restart = 0
result = 0

def main(restart,result):
  if restart:
    num1 = result
  else:
    num1 = input("What's the first number?: ")
  result=calculate(num1)
  again= input(f"Type 'y' to continue calculating with {result} or type'n' to start a new calculation: ").lower()
  if again == "y":
    restart = True
  elif again == "n":
    restart = False
  main(restart,result)
    
def calculate(num1):
  print("+\n-\n*\n/")
  choice = input("Pick an opertaion: ")
  num2 = input("What's the next number?: ")
  result=0
  if choice == "+":
    result = add(num1,num2)
  elif choice == "*":
    result = multiply(num1,num2)
  elif choice == "-":
    result = subtract(num1,num2)
  elif choice == "/":
    result = divide(num1,num2)
  print(f"{num1} {choice} {num2} = {result}")
  return result



#Calculations
def multiply(a,b):
  return float(a)*float(b)
def add(a,b):
  return float(a)+float(b)
def subtract(a,b):
  return float(a)-float(b)
def divide(a,b):
  return float(a)/float(b)

main(restart,result)