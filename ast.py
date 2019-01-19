class Num:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class MulStr:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value * 5
