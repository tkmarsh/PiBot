#PiBot Server
from bluedot.btcomm import BluetoothServer
from signal import pause
import explorerhat

def data_received(data):
    print(data)
    if data == "left":
        explorerhat.motor.one.forward(100)
    elif data == "leftstop":
        explorerhat.motor.one.forward(0)
        s.send(str(data))
    
    elif data == "right":
        explorerhat.motor.two.backward(100)
    elif data == "rightstop":
        explorerhat.motor.two.backward(0)
        s.send(str(data))

    elif data == "back":
        explorerhat.motor.two.forward(100)
        explorerhat.motor.one.backward(100)
    elif data == "backstop":
        explorerhat.motor.two.forward(0)
        explorerhat.motor.one.backward(0)
        s.send(str(data))
        
s = BluetoothServer(data_received)
pause()
