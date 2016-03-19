class EventBus:

    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def unregister_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def broadcast(self, message):
        for listener in self.listeners:
            listener.recieve_message(message)