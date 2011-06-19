from pychart import *
from usrOperate import *
import os

theme.get_options()
can = canvas.default_canvas()
size = (300, 200)
def plotDraw(data):
    sortResult = simpleSort(data)
    drawArea = area.T(size = size, legend = None, y_range = (sortResult[0] - 100, sortResult[1] + 100),
                      x_axis = axis.X(format = "%d", label = "times"),
                      y_axis = axis.Y(format = "%d", label = "interval"))
    drawArea.add_plot(line_plot.T(data = data))
    drawArea.draw()
    can.show(drawArea.x_pos(4), drawArea.y_pos(9070), "/a45{}Intrvals")

def simpleSort(data):
    dataMin = data[0][1]
    dataMax = data[0][1]
    for i in range(1, len(data)):
        if data[i][1] < dataMin: dataMin = data[i][1]
        if data[i][1] > dataMax: dataMax = data[i][1]
    return(dataMin, dataMax)
