class ArtificialTree:
    count = 3
    type_name = "Штучна ялинка"

    def __init__(self, manufacturer="N/A", height=0, price=0.0, material="N/A"):
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material

    def __str__(self):
        return f"Виробник: {self.__manufacturer}, Висота: {self.__height} см, Ціна: {self.__price} грн, Матеріал: {self.__material}"

    def __repr__(self):
        return f"ArtificialTree(manufacturer='{self.__manufacturer}', height={self.__height}, price={self.__price}, material='{self.__material}')"

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value


if __name__ == "__main__":
    tree1 = ArtificialTree("EverGreen", 180, 2499.99, "PVC")
    tree2 = ArtificialTree("NordicArt", 210, 3499.0, "PE")
    tree3 = ArtificialTree("SnowTree", 160, 1999.5, "Plastic")
    tree1.count = "10"

    print(tree1.count)
    tree1.count = "10"
    print(tree1)      
    print(repr(tree1))  
    print(tree2.count)
    print(repr(tree2))
    print(tree3)
    print(repr(tree3))

