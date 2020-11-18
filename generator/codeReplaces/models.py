import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

models_token = token_dictionary()["base_app"]["models"]


def define_models(class_object):
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
    return ""


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
    if attribute_type == "integer":
        return "IntegerField()"
    elif attribute_type == "boolean":
        return "BooleanField()"
    elif attribute_type == "datetime":
        return "DateTimeField()"
    else:
        return "CharField(max_length=255)"
