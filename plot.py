from pychart import *
from usrOperate import *
from getUsrData import *
from string import *
import os

theme.get_options()
can = canvas.default_canvas()
size = (300, 200)
def plotDraw(data):
    min, max = simpleSort(data)
    drawArea = area.T(size = size, legend = None,
            y_range = (min * 0.9, max * 1.1),
            x_axis = axis.X(format = "%d", label = "times"),
            y_axis = axis.Y(format = "%d", label = "intervals(ns)"))
    drawArea.add_plot(line_plot.T(data = data))
    drawArea.draw()
   # can.show(drawArea.x_pos(4), drawArea.y_pos(min), "/a45{}Intrvals")

def simpleSort(data):
    dataMin = data[0][1]
    dataMax = data[0][1]
    for i in range(1, len(data)):
        if data[i][1] < dataMin: dataMin = data[i][1]
        if data[i][1] > dataMax: dataMax = data[i][1]
    return(dataMin, dataMax)

def addSN(SN_data):
    plotData = []
    for i in range(0, len(SN_data)):
        plotData.append([i + 1, atof(SN_data[i])])
    return(plotData)
if __name__ == '__main__':
    name, times, pwd = getUsrData()
    pData = addSN(pwd)
    tData = [ [1, 9], [2, 1], [3, 0], [4, 0], [5, 0] , [6, 0] ]
    plotDraw(pData)
