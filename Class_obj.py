class Event:
    def __init__(self, eventname):
        self.eventname = eventname 

    def display(self):
        print("Event Name:" ,self.eventname)
obj = Event("Conference")
obj.display()
