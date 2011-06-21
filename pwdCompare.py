from pychart import *
from plot import *
from string import *
from usrOperate import *
theme.get_options()

def dualPlot(first_data, second_data):
    can = canvas.default_canvas()
    min_data, max_data = dualSort(first_data, second_data)
    canvasAttribute = canAttr(300, 200, min_data, max_data)
    plotDraw(can, canvasAttribute, first_data)
    plotDraw(can, canvasAttribute, second_data)

def dualSort(first_data, second_data):
    min_first_data, max_first_data = simpleSort(first_data)
    min_second_data, max_second_data = simpleSort(second_data)
    if min_first_data > min_second_data:
        min_data = min_second_data
    else:
        min_data = min_first_data
    if max_first_data > max_second_data:
        max_data = max_first_data
    else:
        max_data = max_second_data
    return(atof(min_data), atof(max_data))


if __name__ == '__main__':
    #get data from file and output the diagram
    #1.get pwd
    cmp1 = getCmpPwd('cmp1')
    cmp2 = getCmpPwd('cmp2')
    dualPlot(cmp1, cmp2)
