import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

models_token = token_dictionary()["base_app"]["models"]

models_directory = ""


def define_models(class_object):
    global models_directory
    models_directory = constants.OUT_DIRECTORY + "/" + class_object.name + models_token["path"]

    # Create model
    # Define model class
    replace_data_in_file(
        models_directory,
        models_token["class"],
        create_model_class_definition(class_object.name)
    )
    print("Define new model in: {}".format(models_directory))
    print("")

    # Define model attributes
    replace_data_in_file(
        models_directory,
        models_token["attributes"],
        create_model_attributes_definition(class_object.attributes)
    )
    print("Define new attributes in: {}".format(models_directory))
    print("")


    # Define model str function
    #replace_data_in_file(
    #    models_directory,
    #    models_token["str_function"],
    #    create_str_function(class_object)
    #)
    #print("Define new str function in: {}".format(models_directory))
    #print("")



def define_import_model(model_name):
    # Define model attributes
    replace_data_in_file(
        models_directory,
        models_token["import"],
        create_import_model(model_name)
    )
    print("Define new attributes in: {}".format(models_directory))
    print("")


def create_str_function(class_object):
    return """def __str__(self):
        return "{}".format({})    
    """.format(create_str_template(class_object), create_str_values(class_object))


def create_str_template(class_object):
    response = []
    for attribute in class_object.attributes:
        if attribute.attribute_type in "string,integer":
            response.append("{}: {}".format(attribute.name, "{}"))
    if len(response) == 0:
        response.append("id: {}, class_of: {}")
    response = ", ".join(response)
    return "{"+response+"}"


def create_str_values(class_object):
    response = []
    for attribute in class_object.attributes:
        if attribute.attribute_type in "string,integer":
            response.append("self.{}".format(attribute.name))
    if len(response) == 0:
        response.append("self.id, '{}'".format(class_object.name))
    response = ", ".join(response)
    return response


def create_import_model(model_name):
    print("model class import model created")
    return "from {}.models import {}\n{}".format(model_name, model_name, models_token["class"])


def create_model_class_definition(model_name):
    print("model class definition created")
    return "class {}(models.Model):\n{}".format(model_name, models_token["class"])


def create_model_attributes_definition(attributes):
    response = "{}\n".format(models_token["attributes"])
    for attribute in attributes:
        print("model attribute definition created")
        response = response + "\t{} = models.{}\n".format(attribute.name, create_model_attribute_type_definition(
            attribute.attribute_type))
    return response


def create_model_attribute_type_definition(attribute_type):
    if attribute_type == "integer" or attribute_type == "calculated":
        return "IntegerField(blank = True, null=True)"
    elif attribute_type == "boolean":
        return "BooleanField(blank = True, null=True)"
    elif attribute_type == "datetime":
        return "DateTimeField(blank = True, null=True)"
    elif attribute_type == "string":
        return "CharField(max_length=255, blank = True, null=True)"
    else:
        if "[]" in attribute_type:
            define_import_model(attribute_type.replace("[]", ""))
            return "ManyToManyField({}, blank = True, null=True)".format(attribute_type.replace("[]", ""))
        else:
            define_import_model(attribute_type)
            return "ForeignKey({}, on_delete=models.CASCADE, blank = True, null=True)".format(attribute_type)
