import numpy
from matplotlib import pyplot

#create data
x = numpy.arange(-5,5.001,0.1)
target = numpy.cos(x)
data = target +  numpy.random.normal(0,.2,x.shape)


#plot data points and line
pyplot.plot(x,data,"rx",label = "data")
pyplot.plot(x,target,"b-",label = "line")

#limit axes and provide labels
pyplot.xlim((-5,5)); pyplot.ylim((-1.5,1.5))
pyplot.xlabel("x"); pyplot.ylabel("y")

# create legend and write to file
pyplot.legend(loc="upper left")
pyplot.savefig("Example.pdf")
