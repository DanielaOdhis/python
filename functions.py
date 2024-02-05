x=9+8
def func():
    print(x)

func()

x = "awesome"

def func2():
  x = "fantastic"
  print("Python is " + x)

func2()

print("Python is " + x)

def func3():
  global x
  x = "the best"

func3()

print("Python is " + x)