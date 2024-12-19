from main import Currency as CurrencyInterface
import json,pandas as pd

cur = CurrencyInterface()

class CurriencesList(CurrencyInterface):
    def result(self):
        return super().result        
        
        
    

class Decorator(CurrencyInterface):
    
    _component : CurrencyInterface = None
    
    def __init__(self, component: CurrencyInterface) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def result(self) -> str:
        return self._component.result()

class ConcreteDecoratorJSON(Decorator):
    def result(self) -> str:
        
        dict_res = self._component.result()
        json_res = json.dumps(dict_res,indent=4,ensure_ascii = False)
        return json_res
    
class ConcreteDecoratorCSV(Decorator):
    def result(self) -> str:
        dict_res = self._component.result()
        pd.DataFrame(dict_res).to_csv('out.csv',index=False)
        return 'Записано в файл'


def client_code(component: CurrencyInterface) -> None:
    print(component.result())

    
    

simple = CurriencesList()

print('Standart Behaviour:')
client_code(simple)

dec1 = ConcreteDecoratorJSON(simple)
print('JSON:')
client_code(dec1)

dec2 = ConcreteDecoratorCSV(simple)
print('CSV:')
client_code(dec2)

dec3 = ConcreteDecoratorCSV(dec1)
print('CSV on decoratorA:')
client_code(dec3)