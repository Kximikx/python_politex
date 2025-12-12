class MyClass:

    number = 123
    string = "text"

    def __init__(self, var1 = 0, var2 = 0, var3 = 0):
        self.__var1 = var1
        self.__var2 = var2
        self.__var3 = var3

    def __del__(self):
        print("Class Deleted")

    def __str__(self):
        return f"{self.__var3} {self.__var1} {self.__var2}"

    def __repr__(self):
        return f"{self.__var3} {self.__var1} {self.__var2}"

    @property
    def var1(self):
        return self.__var1

    @var1.setter
    def var1(self, value):
        self.__var1 = value

    @property
    def var2(self):
        return self.__var2

    @var2.setter
    def var2(self, value):
        self.__var2 = value

    @property
    def var3(self):
        return self.__var3

    @var3.setter
    def var3(self, value):
        self.__var3 = value

class Main:
    @staticmethod
    def main():
        class1: MyClass = MyClass(5, 50, 20)
        class2: MyClass = MyClass(34, 84, 25)
        class3: MyClass = MyClass(6, 44, 32)

        print(class1)
        print(class2)
        print(class3)


Main.main()
