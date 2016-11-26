## problems 4.1.18 and 4.1.27

from numpy import array, arange
import pylab
import error, time

###########################################################
# problem4_1_18
# Fill in the '??' lines below, specifically:
# 1) take the derivative of function f(u) and add that
# to the code as function df(u).
# 2) call newtonRaphsonMOD() to solve for u
############################################################

## problem4_1_18
def newtonRaphsonMOD(f,df,a,b,tol=1.0e-9):
# NOTE: Modified to help create an animated plot for problem 4.1.18
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0: error.err('Root is not bracketed')
    x = 0.5*(a + b)    
                    
    for i in range(30):
        fx = f(x)
        if abs(fx) < tol: return x
      # Tighten the brackets on the root 
        if fa*fx < 0.0:
            b = x  
        else:                  
            a = x; fa = fx
      # Try a Newton-Raphson step    
        dfx = df(x)

      # construct a tangent line, store pts for later animated plotting
        slope = dfx
        y = f(x)
        intercept = slope*(-1)*x + y  
        ys = []
        for q in xs:
          y = slope*q+intercept #tangent line eq in slope-icept form
          ys.append(y)
        all_ys.append(ys)

      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx

      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b-a)                      
            x = a + dx

      # Check for convergence     
        all_xs.append(x)
        if abs(dx) < tol*max(abs(b),1.0): return x
    print 'Too many iterations in Newton-Raphson'


# Let u = h0/h; the equation given in the problem can
# then be re-arranged into the following function:
def f(u): return 0.10487*(1.0-1.0/u**2) - u + 0.875

# (1) The derivative of the function above is:
#def df(u): return ??

print "\nProblem 4.1.18\n"
all_ys = []
all_xs = []
# set up the figure window
fig = pylab.figure(1)

myplot = pylab.subplot(111)

pylab.xlabel("u (u = h/h0)")
pylab.ylabel("f(u)")
pylab.title("Problem 4.1.18")
myplot.text(0.5, 0.4, "After h2 is displayed, close this window")
myplot.text(0.5, 0.36, "to continue onto problem 4.1.27")

xs = [0.30,0.9]; ys = [0,0]
myplot.plot(xs,ys,'k')
fig.show()

# plot the function
xs = arange(0.35, 0.9, 0.001)
ys = []
for x in xs:
  ys.append(f(x))
myplot.plot(xs, ys)


h0 = 0.6 # given in the problem
a = 0.2
b = 0.5
all_xs.append(0.5*(a+b))
xs =  arange(0.4, 0.5, 0.001)

# 2a) solve for the first root, u1
#u1 = newtonRaphsonMOD(??)

all_ys.pop(0) # remove first item (ini guess does not produce a valid tangent line)
i = 0
for ys in all_ys:
  myplot.plot(xs, ys, 'r')
  myplot.plot([all_xs[i]], [0], 'rx')
  i+=1
  myplot.axis([0.35, 0.9, -0.5, 0.5])
  pylab.draw()
  time.sleep(2)
  
u1 = round(u1,4)
print "u1 = ", u1
h1 = round(u1*h0, 4)
print "h1 = ", h1
U1 = "u1 = %.4f"%u1
H1 = "h1 = %.4f m"%h1
myplot.text(0.4, 0.2, U1)
myplot.text(0.4, 0.15, H1)

a = 0.46
b = 0.95
all_ys = []
all_xs = []
all_xs.append(0.5*(a+b))
xs =  arange(0.75, 0.85, 0.001)

# 2b) solve for the second root, u2
#u2 = newtonRaphsonMOD(??)

all_ys.pop(0) # remove first item (ini guess does not produce a valid tangent line)
i = 0;
for ys in all_ys:
  myplot.plot(xs, ys, 'g')
  myplot.plot([all_xs[i]], [0], 'gx')
  i+=1
  myplot.axis([0.35, 0.9, -0.5, 0.5])
  pylab.draw()
  time.sleep(2)

u2 = round(u2,4)
print "u2 = ", u2
h2 = round(u2*h0, 4)
print "h2 = ", h2
U2 = "u2 = %.4f"%u2
H2 = "h2 = %.4f m"%h2
myplot.text(0.75, 0.2, U2)
myplot.text(0.75, 0.15, H2)


pylab.show()
###################################################################################
# 4.1.27
# Fill in the '??' lines below
# Should get the following answer:
# (C,e,alpha) = [ 6.81929379e+03 4.05989591e-02 3.40783998e-01]
# Rmin = 6553.23910701 km
# Theta = 70.4745151918 deg
#################################################################
from numpy import zeros,array,float64
from math import sin,pi
from newtonRaphson2 import *

# f() consists of 3 equations, the first one is given. Fill in the other two
# note that vector x consists of the following:
# x[0] = C; x[1] = e = eccentricity constant
# x[2] = alpha
# an initial guess for vector x is provided for you below (6800, 0.5, 0.0)
def f(x):
  f = zeros((len(x)),dtype=float64)
  f[0] = x[0]/(1.0 + x[1]*sin(-pi/6.0 + x[2])) - 6870.0
  #f[1] = ??
  #f[2] = ??
  return f
print "\nProblem 4.1.27\n"
x = array([6800, 0.5, 0.0])
#x = newtonRaphson2(??)
print "(C,e,alpha) = ",x
print "Rmin = ",x[0]/(1.0 + x[1])," km"
print "Theta = ",(pi/2.0 - x[2])*180.0/pi," deg"
