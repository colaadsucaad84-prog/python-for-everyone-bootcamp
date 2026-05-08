from dataclasses import dataclass

@dataclass
class Game:
    name:str
    year:str
    platform:str # pc, playstation, xbox, nintendo, mobile

    def __str__(self):
        return f"name: {self.name}, year: {self.year}, platform: {self.platform}"

class Catalog:
    def __init__(self):
        self.items = []
    
    def add(self,catalog):
        self.items.append(catalog)

    def list_all(self):
        for item in self.items:
            print(item)    


def load_catalog(path, catalog):
    pass

def save_catalog(path, catalog):
    pass

def main():
    pass


if __name__ == "__main__":
    main()