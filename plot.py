from pychart import *
from usrOperate import *
from string import *

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
    plotData = addSN(m_data)
    width = canAttr.getWidth()
    height = canAttr.getHeight()
    y_low = canAttr.getYLow()
    y_high = canAttr.getYHigh()
    drawArea = area.T(size = (width, height), 
            legend = None,
            y_range = (y_low, y_high),
            x_axis = axis.X(format = "%d", label = "times"),
            y_axis = axis.Y(format = "%d", label = "intervals(ns)"))
    drawArea.add_plot(line_plot.T(data = plotData))
    drawArea.draw()
   # can.show(drawArea.x_pos(4), drawArea.y_pos(min), "/a45{}Intrvals")

def simpleSort(data):
    dataMin = data[0]
    dataMax = data[0]
    for i in range(1, len(data)):
        if data[i] < dataMin: dataMin = data[i]
        if data[i] > dataMax: dataMax = data[i]
    return(dataMin, dataMax)

def addSN(SN_data):
    plotData = []
    for i in range(0, len(SN_data)):
        plotData.append([i + 1, atof(SN_data[i])])
    return(plotData)


if __name__ == '__main__':
    can = canvas.default_canvas()
    name, times, pwd = getUsrData()
    x = canAttr(300, 200, 300000, 450000)
    tData = [300000, 400000, 420000]
    plotDraw(can, x, pwd)
    plotDraw(can, x, tData)
