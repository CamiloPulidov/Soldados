class ITaxesBehavior():
    def Taxes(self):
        pass

class Taxes1(ITaxesBehavior):
    
    def Taxes(self):
        print("hola")

class Taxes2(ITaxesBehavior):
    def Taxes(self):
        pass
class Country():

    def __init__(self,taxes_behavior:ITaxesBehavior):
        self._taxes_behavior=taxes_behavior
       

    def perform_taxes(self):
        self._taxes_behavior.Taxes()

   

class USA(Country):
    def __init__(self):
        super().__init__(Taxes1())

    
class UE(Country):
    def __init__(self):
        super().__init__(Taxes2())

if __name__=="__main__":
    usa=USA()
    usa.perform_taxes()

