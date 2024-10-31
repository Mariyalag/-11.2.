
import inspect
def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = []
    methods = []

    for attr in dir(obj):
        value = getattr(obj, attr)
        if callable(value):
            methods.append(attr)
        else:
            attributes.append(attr)

    if isinstance(obj, type):
        module = obj.__module__
    else:
        module = obj.__class__.__module__

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info

number_info = introspection_info(42)
print(number_info)























# # import requests
# # help(requests)
# # #help(requests.get)
#
# import requests
# from pprint import  pprint
# import
# some_string = 'i am a string'
# some_number = 42
# some_list = [some_string, some_number]
#
# def some_function(param, param_2='n/a'):
#     print('my params is', param, param_2)
#
# class SomeClass:
#     def __init__(self):
#         self.attribute_1 = 27
#
#     def some_class_method(self, value):
#         self.attribute_1 = value
#         print(self.attribute_1)
#
# # some_object = SomeClass()
# # func = some_function
# # print(some_function.__name__)
# # print(SomeClass.__name__)
# # print(requests.__name__)
# # print(func.__name__)
# #
# # print(type(some_number))
# # print(type(some_number) is int)
# # print(type(some_number) is list)
# # print(type(requests))
# # print(type(requests.get))
# #
# # # pprint(dir(some_number))
# # # pprint(dir(some_list))
# # # pprint(type(SomeClass))
# # # pprint(type(some_object)
# pprint(dir(requests))