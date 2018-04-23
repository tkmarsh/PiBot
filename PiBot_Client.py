#PiBot Client
from gpiozero import Button
from bluedot.btcomm import BluetoothClient

left = Button(27)
right = Button(22)
back = Button(17)

def data_received(data):
    print(data)

def print_bt_error():
    print("Error: Check BT connection...")

def left_pressed():
    c.send("left")
def right_pressed():
    c.send("right")
def left_released():
    c.send("leftstop")
def right_released():
    c.send("rightstop")
def back_pressed():
    c.send("back")
def back_released():
    c.send("backstop")

try:
    c = BluetoothClient("piserver", data_received)
except:
    print_bt_error()


left.when_pressed=left_pressed
left.when_released=left_released
right.when_pressed=right_pressed
right.when_released=right_released
back.when_pressed=back_pressed
back.when_released=back_released
