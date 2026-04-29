# 5-m
class Telefon:
    def __init__(self, model):
        self.model = model

    def info(self):
        print(f"Model:, {self.model}")


class Smartfon(Telefon):
    def __init__(self, model, xotira):
        super().__init__(model)
        self.xotira = xotira

    def info(self):
        super().info()
        print(f"Xotira:, {self.xotira}")


s = Smartfon("iPhone", "256GB")
s.info()
