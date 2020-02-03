#option validation
def optValidate(prompt,yArray):
  y = 0
  while y not in yArray:
    y = str(input(prompt))
    if y not in yArray:
      print("\nPlease enter one of the available options.\n")
  return y
#option validation

#variable type validation
def numTypeSubValidate(x,extender,y):
  x = subValidate(extender)
  return numTypeValidate(x,extender,y)

def numTypeValidate(x,extender,y):
  if any(c.isalpha() for c in x) == y:
    x = numTypeSubValidate(x,extender,y)
  return x

def subValidate(extender):
  x = input("Please enter " + extender)
  return x
#variable type validation
