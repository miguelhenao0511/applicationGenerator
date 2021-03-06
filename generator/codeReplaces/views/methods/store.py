import generator.utils.constants as constants
import re
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_store_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add views store
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_store_method(class_object)
    )
    print("Define store method in: {}".format(views_directory))
    print("")


def create_store_method(class_object):
    return """
def store(request):
    app_object = {}()
{}
    app_object.save()
    """.format(class_object.name, define_object_attributes(class_object.attributes)) + """
    redirectTo = '/{}/' + str(app_object.id)
    return HttpResponseRedirect(redirectTo)
{}""".format(class_object.name, views_methods_token)


def define_object_attributes(attributes):
    response = ""
    for attribute in attributes:
        if attribute.attribute_type == "boolean":
            response += ("""    app_object.{}='{}' in request.POST\n""".format(attribute.name, attribute.name))
        elif attribute.attribute_type in "string,date,integer,double":
            response += ("""    app_object.{}=request.POST['{}']\n""".format(attribute.name, attribute.name))
        elif attribute.attribute_type == "calculated":
            response += ("""    app_object.{}={}\n""".format(attribute.name, define_attribute_operation(attribute)))
        else:
            if "[]" in attribute.attribute_type:
                response += define_attribute_many_to_many(attribute)
            else:
                response += ("""    app_object.{}={}.objects.get(id=request.POST['{}'])\n""".format(attribute.name, attribute.name, attribute.name))

    return response


def define_attribute_operation(attribute):
    operation = attribute.operation
    regexExp = re.compile("\[+\w+\]")
    object_operands = regexExp.findall(attribute.operation)
    for object_operand in object_operands:
        operation = operation.replace(object_operand,
                                      "float(app_object.{})".format(object_operand.replace("[", "").replace("]", "")))
    return "{}".format(operation)


def define_attribute_many_to_many(attribute):
    return """
    app_object.save()
    for {}_id in request.POST.getlist('{}'):
        app_object.{}.add({}.objects.get(id={}_id))        
""".format(attribute.name, attribute.name, attribute.name, attribute.name, attribute.name)
