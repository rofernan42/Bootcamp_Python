import time
from random import randint

class CoffeeMachine():
    water_level = 100

    def log(func):
        def fct(*args, **kwargs):
            f = open("machine.log", "a")
            fct_name = " ".join(i.capitalize() for i in func.__name__.split('_'))
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time() - start
            unit = "s"
            if end < 0.001:
                end *= 1000
                unit = "ms"
            txt = f"(rofernan)Running: {fct_name}\t[ exec-time = {end:.3f} {unit} ]\n"
            f.write(txt)
            return res
        return fct

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)