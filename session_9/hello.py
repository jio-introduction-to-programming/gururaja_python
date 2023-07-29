#filename = hello.py

def hello():
    print("Hello from module")

HELLO =  "I am a constant"
RED = "#FF0000"
WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri","Sat"]

class Hello:
    def __init__(self):
        print("Class from module..hello.py initialised")

print(__name__)