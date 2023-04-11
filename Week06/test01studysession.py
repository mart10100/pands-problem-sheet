# test03studysession.py
# From https://www.youtube.com/watch?v=99ABkygm2Xg&ab_channel=StudySession

x = int(input("Please enter a positive number: "))

def newtonsmethod(func, funcderiv, x, n):

    def f(x):
        f = eval(func)
        return f
    
    def df(x):
            df = eval(funcderiv)
            return df
    
    for intercept in range(1, n):
         i = x -(f(x)/df(x))
         x = i
    print (f'The square root was found to be {x} after {n} iterations.')
 
x = int(input("Please enter a positive number: "))
newtonsmethod("x**2 -2", "2*x", x, 10)