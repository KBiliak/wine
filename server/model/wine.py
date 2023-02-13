

class Wine:
    def __init__(self, id, year, sort):
        self.id = id
        self.year = year
        self.sort = sort
        self.drink_counter = 0

    def drink(self):
        print(f"I drink: id = {self.id}, year = {self.year}, sort = {self.sort}")
        self.drink_counter += 1

    def drink_status(self):
        if self.drink_counter >= 5:
            print("you are drank", self.drink_counter)
        else:
            print('you can drink')

wine = Wine(1, 1998, 'white')
wine2 = Wine(2, 1997, 'black')

print("My new wine", wine.id, wine.year, wine.sort)
print("My new wine 2", wine2.id, wine2.year, wine2.sort)

for i in range(200):
    wine.drink()
wine.drink_status()
