from inspect import isclass

class Dto(object):
    pass

def make_tuple(object):
    return_list = []
    if type(object) == list:
        for element in object:
            return_element = {}
            if hasattr(element, '__dict__') or type(element) == list:
                for key in element.__dict__:
                    value = element.__dict__[key]
                    if hasattr(value, '__dict__') or type(value) == list:
                        return_element[key] = make_tuple(value)
                    else:
                        return_element[key] = value
                return_list.append(return_element)
            else:
                return_list.append(element)
    elif type(object) == dict:
        return object
    elif hasattr(object, '__dict__'):
        for key in object.__dict__:
            value = object.__dict__[key]
            if hasattr(value, '__dict__') or type(value) == list:
                return_list.append({key: make_tuple(value)})
            else:
                return_list.append({key: value})

    return tuple(return_list)