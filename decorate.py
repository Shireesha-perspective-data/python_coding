#decorator 
def smart_division(func_n):
	def inner(x,y):
	    if y==0:
	       print ("the x value is ")
	    else:
	      print("not x value")
	      return func_n(x,y);

	return inner;

def divide(a,b):
    return a/b;
divide=smart_division(divide)
print(divide(1,2))
