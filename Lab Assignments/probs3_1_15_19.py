## problems 3.1.15 and 3.1.19
from newtonPoly import *
from numpy import array, append
import pylab # a.k.a. 'matplotlib'

# 3.1.15
# Use newtonPoly.py for interpolation.
# Fill in the '??' lines and answer the questions below
# using the pylab.text('<answer 1>'), pylab.text('<answer 2>') lines.
# (cp @ T=200 ~= 0.993; cp @ T=400 ~= 0.986)

xData = #??
yData = #??
a = coeffts(#??)
fx200 = evalPoly(#??)
fx400 = evalPoly(#??)
print "\nProblem 3.1.15"
print "T = 200 C. cp (kJ/kg.K) = ", fx200
print "T = 400 C. cp (kJ/kg.K) = ", fx400, "\n"

# The code below plots the original data and the interpolation function on the same
# graph. Based on the plot, make a conclusion as to the accuracy of
# cp estimates for T=200 C and T=400 C. Comment on the use of polynomial interpolation
# for extrapolation. Fill in your answers into the <answer 1> and <answer 2> pylab.text()
# lines below.
pylab.text(-120, 0.5, 'Does the cp for T=400 C appear accurate?')
pylab.text(-120, 0.45, 'What do you think it should be?')
# answer the above questions using the line below:
pylab.text(-120, 0.40, '<answer 1>')
pylab.text(-120, 0.35, 'Should polynomial interpolation be used for extrapolation?')
# answer the above question using the line below:
pylab.text(-120, 0.30, '<answer 2>')

xs = pylab.arange(-250, 300.0, 1.0)
ys = []
for x in xs:
  y = evalPoly(a,xData,x)
  ys.append(y)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.title("Problem 3.1.15")

# plots the resulting interpolation function
pylab.plot(xs, ys, 'b')

# plots the original data (including the T=200, T= 400 points)
xData = append(xData, 200.0)
yData = append(yData, fx200)
xData = append(xData, 400.0)
yData = append(yData, fx400)

pylab.plot(xData, yData, 'ro')

pylab.axis([-260, 410, 0.0, 1.1])


# 3.1.19
print "\nProblem 3.1.19"
## problem3_1_19
# Use cubic splines to interpolate.
# Remove the comments on the lines below, fill in the '??' lines.
# (ans: ~ 1.47, 0.87, 0.45, 0.31)
from cubicSpline import *

#tData = ??
#mData = ??
#k = curvatures(??)

#inter_pts = array([10.0, 30.0, 60.0, 90.0])
#for pt in inter_pts:
#  print "Viscocity = ", evalSpline(??), "\n"

pylab.show()
