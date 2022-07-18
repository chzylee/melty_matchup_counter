class Logger:
    def __init__(self, shouldLog):
        self.shouldLog = shouldLog

    def log(self, message):
        if self.shouldLog:
            print(message)