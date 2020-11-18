import generator.utils.constants as constants
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
    app_object = {}.objects.create({})
    """.format(class_object.name, define_object_attributes(class_object.attributes)) + """
    redirectTo = '/{}/' + str(app_object.id)
    return HttpResponseRedirect(redirectTo)
{}""".format(class_object.name, views_methods_token)


def define_object_attributes(attributes):
    response = []
    for attribute in attributes:
        if attribute.attribute_type == "boolean":
            response.append("{}='{}' in request.POST".format(attribute.name, attribute.name))
        else:
            response.append("{}=request.POST['{}']".format(attribute.name, attribute.name))
    return ",".join(response)