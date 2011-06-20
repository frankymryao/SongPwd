from pychart import *
from usrOperate import *
from getUsrData import *
from string import *
import os

theme.get_options()

class canAttr:
    __width = 0
    __height = 0
    __y_low = 0
    __y_high = 0
    def __init__(self, size_x, size_y, y_range_low, y_range_high):
        self.__width = size_x
        self.__height = size_y
        self.__y_low = y_range_low
        self.__y_high = y_range_high
    def getWidth(self):
        return(self.__width)
    def getHeight(self):
        return(self.__height)
    def getYLow(self):
        return(self.__y_low)
    def getYHigh(self):
        return(self.__y_high)



def plotDraw(can, canAttr, m_data):
    min, max = simpleSort(m_data)
    width = canAttr.getWidth()
    height = canAttr.getHeight()
    y_low = canAttr.getYLow()
    y_high = canAttr.getYHigh()
    drawArea = area.T(size = (width, height), 
            legend = None,
            y_range = (y_low, y_high),
            x_axis = axis.X(format = "%d", label = "times"),
            y_axis = axis.Y(format = "%d", label = "intervals(ns)"))
    drawArea.add_plot(line_plot.T(data = m_data))
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
    can = canvas.default_canvas()
    name, times, pwd = getUsrData()
    pData = addSN(pwd)
    x = canAttr(300, 200, 300000, 900000)
    print(x.getWidth(), x.getHeight())
    tData = [ [1, 300000], [2, 400000], [3, 500000] ]
    plotDraw(can, x, pData)
    plotDraw(can, x, tData)
