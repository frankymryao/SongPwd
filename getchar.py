import os,sys
import sys
import termios
x=1
def getchar():
    '''
    getchar in C
    '''
    fd = sys.stdin.fileno()
    if os.isatty(fd):
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6] [termios.VMIN] = 1
        new[6] [termios.VTIME] = 0
        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)
            termios.tcsendbreak(fd,0)
            ch = os.read(fd,2)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    else:
        ch = os.read(fd,2)
    return(ch.decode("utf-8"))

if __name__ == '__main__': 
    while True:
        print(getchar())
