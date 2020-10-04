import random
import string
from datetime import date


class ClassTemplate:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return "name: {}, attributes: {}".format(self.name, self.attributes)


class AttributeTemplate:
    def __init__(self, name, attribute_type):
        self.name = name
        self.attribute_type = attribute_type

    def __str__(self):
        return "name: {}, type: {}".format(self.name, self.attribute_type)


ATTRIBUTES_TYPE = ["string", "integer", "boolean", "datetime"]


def get_random_string(size):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(size))


def get_random_integer(max_value):
    return random.randint(0, max_value)


def get_random_boolean():
    return random.randint(0, 1)


def get_date():
    return date.today()


def generate_random_class(attributes_quantity):
    attributes = []
    for i in range(0, attributes_quantity):
        attributes.append(AttributeTemplate(get_random_string(10), ATTRIBUTES_TYPE[get_random_integer(3)]))
    return ClassTemplate(get_random_string(15), attributes)
