import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary


views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_update_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add views update
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_views_methods_update(class_object)
    )
    print("Define update method in: {}".format(views_directory))
    print("")


def create_views_methods_update(class_object):
    return """
def update(request, id):
    app_object = {}.objects.get(id=id)
    """.format(class_object.name) + """
    app_object.__dict__.update({})""".format(create_object_attributes(class_object.attributes)) + """
    app_object.save()

    redirectTo = '/{}/' + str(app_object.id)
    return HttpResponseRedirect(redirectTo)
{}""".format(class_object.name, views_methods_token)


def create_object_attributes(attributes):
    response = []
    for attribute in attributes:
        if attribute.attribute_type == "boolean":
            response.append("{}='{}' in request.POST".format(attribute.name, attribute.name))
        else:
            response.append("{}=request.POST['{}']".format(attribute.name, attribute.name))
    return ",".join(response)