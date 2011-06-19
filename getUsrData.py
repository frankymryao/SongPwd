def getUsrData():
    file_object = open('usrData')
    try:
        usrData = file_object.read().replace('\n', '').split('#')
    finally:
        file_object.close()
    usrData = usrData[0:len(usrData) - 1]
    print(usrData)
