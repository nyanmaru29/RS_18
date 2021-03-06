class EventManager:
    # responsible for coordinating most communication
    # between the Model, View, and Controller
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def Post(self, event):
        # Post a new event.  It will be broadcast to all listeners
        keys = list(self.listeners.keys())
        for listener in keys:
            listener.Notify(event)