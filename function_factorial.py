#factorial number
#f(n) = n * f(n-1)

def factorial(n):
  if n<=1: return 1
  return n * factorial(n-1)

def main():
  fact = int(input("Enter the number: "))
  a1 = factorial(fact)
  print("%d of factorial is %d " %(fact,a1))

if __name__=='__main__': main()
