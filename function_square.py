
def square(num):
  return num*num

def cube(poll):
  return poll*poll, poll*poll*poll

def main():
  count = int(input("Enter the number: "))
  sqr = square(count)
  print("number is %d and sqaure of number is %d " %(count,sqr))

  t1 = int(input("Enter the number: "))
  t2, cuba = cube(t1)
  print("Square number is %d and cube number is %d " %(t2,cuba))

if __name__=='__main__': main()
