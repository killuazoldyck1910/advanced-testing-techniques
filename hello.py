def addthis(x,y):
  print(f"This is x {x} and this x-type is {type(x)}")
  print(f"This is y {y} and this y-type is {type(y)}")

  try:
    result=x+y
  except TypeError:
    print(f"The wrong type passed")
    result = int(x)+int(y)

  print(f"This is the result {result}")
  return x+y


print(addthis("1",2))