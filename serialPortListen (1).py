#Python code to interface with the game
#code taken from
#https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#https://stackoverflow.com/questions/35936644/python-read-from-the-serial-port-data-line-by-line-into-a-list-when-available
import serial
import serial.tools.list_ports as list_ports
import re
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.001

def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

def main():
    print('looking for microbit')
    ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser_micro:
        print('microbit not found')
        return
    print('opening and monitoring microbit port')
    ser_micro.open()
    gameData = ''
    while True:
        #check if there is any data waiting in the serial buffer
            size = ser_micro.inWaiting()
            if size:
                data = ser_micro.read(size).decode('utf-8')
                gameData += data.strip(' ')
                
            x = re.search("E{1,3}$", gameData)
            
            if  x:
                #print(repr(gameData[:x.end()]))
                T= re.search("(T.*)\n",gameData[:x.end()])
                if T:
                    print(repr(T.group(1).strip()))
                LI= re.search("(L.*)\n",gameData[:x.end()])
                if LI:
                    print(repr(LI.group(1).strip()))
                #print(gameData)
                C= re.search("(C.*)\n",gameData[:x.end()])
                if C:
                    print(repr(C.group(1).strip()))
                gameData = gameData[x.end():]
            
          
    ser_micro.close()
main()


