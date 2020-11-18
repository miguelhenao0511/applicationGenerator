import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary


views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_edit_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add views edit
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_edit_method(class_object)
    )
    print("Define edit method in: {}".format(views_directory))
    print("")


def create_edit_method(class_object):
    return """
def edit(request, id):
    app_object = {}.objects.get(id=id)
{}
    """.format(class_object.name, create_call_list_items(class_object)) + """
    return render(request, '{}_templates/base_app_edit.html', {})
{}""".format(class_object.name, create_parameters_to_send_view(class_object), views_methods_token)


def create_call_list_items(class_object):
    response = ""
    for attribute in class_object.attributes:
        if attribute.attribute_type not in "string,integer,boolean,date,calculated":
            response += """
    {}_list = {}.objects.all()
""".format(attribute.name, attribute.name)

    return response


def create_parameters_to_send_view(class_object):
    response = "{'app_object': app_object"
    for attribute in class_object.attributes:
        if attribute.attribute_type not in "string,integer,boolean,date,calculated":
            response += ", '{}_list': {}_list".format(attribute.name, attribute.name)

    return response + '}'