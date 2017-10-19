import sys,tty,termios
from motorManager import forward, backward, left, right
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
            
def getKey():
        inkey = _Getch()
        k=inkey()
        if k=='\x1b[A':
            print("not an arrow key!")
            forward(2)
        elif k=='\x1b[B':
            print("not an arrow key!")
            backward(2)
        elif k=='\x1b[C':
            print("not an arrow key!")
            right(2)
        elif k=='\x1b[D':
            print("not an arrow key!")
            left(2)
        else:
            print("not an arrow key!")

while(1):
    getKey()	
