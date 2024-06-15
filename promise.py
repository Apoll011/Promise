import threading

class Promise:
    def __init__(self):
        self.resolved = False
        self.rejected = False
        self.value = None
        self.error = None
        self.then_callback = None
        self.catch_callback = None
        self.lock = threading.Lock()  # Lock to ensure thread-safe access

    def then(self, callback):
        with self.lock:
            if self.resolved:
                callback(self.value)
            else:
                self.then_callback = callback
        return self

    def catch(self, callback):
        with self.lock:
            if self.rejected:
                callback(self.error)
            else:
                self.catch_callback = callback
        return self

    def resolve(self, value):
        threading.Thread(target=self.do_resolve, args=(value,)).start()

    def do_resolve(self, value):
        with self.lock:
            if not self.resolved and not self.rejected:
                try:
                    v = value()
                    if v:
                        self.value = v
                        self.resolved = True
                        if self.then_callback:
                            self.then_callback(v)
                except Exception as e:
                    self.reject(e)

    def reject(self, error):
        with self.lock:
            if not self.rejected and not self.resolved:
                self.rejected = True
                self.error = error
                if self.catch_callback:
                    self.catch_callback(error)
