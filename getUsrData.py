def getUsrData():
    file_object = open('usrData')
    try:
        usrData = file_object.read().replace('\n', '').split('#')
        name = usrData[0]
        times = usrData[1]
    finally:
        file_object.close()
    pwd = usrData[2:len(usrData) - 1]
    return((name, times, pwd))
