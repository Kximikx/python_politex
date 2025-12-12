
class ArtificialTree:
    # Публічні поля (одне числове, одне стрічкове)
    count = 3
    type_name = "Штучна ялинка"

    # Конструктор із параметрами (та значеннями за замовчуванням)
    #Авт запуск при створенні нового проекту 
    def __init__(self, manufacturer="N/A", height=0, price=0.0, material="N/A"):
        # Приватні поля та збереження данних
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material

    # Перевизначення __str__ і __repr__
    #Front
    def __str__(self):
        return f"{self.__manufacturer}, {self.__height} см, {self.__price} грн, {self.__material}"
    #Back
    def __repr__(self):
        return f"{self.__manufacturer}, {self.__height} см, {self.__price} грн, {self.__material}"

    # Методи доступу (get/set через property)
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


# Основна частина програми (створення об’єктів і виведення)
if __name__ == "__main__":
    tree1 = ArtificialTree("EverGreen", 180, 2499.99, "PVC")
    tree2 = ArtificialTree("NordicArt", 210, 3499.0, "PE")
    tree3 = ArtificialTree("SnowTree", 160, 1999.5, "Plastic")

    print(tree1)
    print(tree2)
    print(tree3)
