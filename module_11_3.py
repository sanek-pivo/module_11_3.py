from pprint import pprint #  импорт функции pprint из модуля pprint
import inspect # импорт Интроспекции
from pathlib import Path #  делает класс Path доступным для программы

a = {} # присваиваем словарик

def introspection_info(obj): #  функцию introspection_info(obj), которая принимает объект obj
    a['type'] = type(obj) # Тип объекта
    a['attributes'] = [method for method in dir(obj) if not callable(getattr(obj, method))] # Атрибуты объекта
    a['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))] #  Методы объекта
    a['module'] = obj.__class__.__module__ # Модуль, к которому объект принадлежит
    a['id'] = [method for method in dir(obj)] # ID -идентификатора (адреса в памяти) объекта

    return a

number_info = introspection_info(42)
pprint(number_info)
print()
str_info = introspection_info('pear')
pprint(str_info)
signature = inspect.signature(introspection_info) # inspect.signature помогает в отладке элементов, связанных с сигнатурой функции
pprint(signature)
print(Path(inspect.getfile(introspection_info)).resolve()) # Здесь мы просто ищем местоположение (файл) функции