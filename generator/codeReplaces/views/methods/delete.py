import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary


views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_delete_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add views delete
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_delete_method(class_object)
    )
    print("Define delete method in: {}".format(views_directory))
    print("")


def create_delete_method(class_object):
    return """
def delete(request, id):
    {}.objects.filter(id=id).delete()
    """.format(class_object.name) + """
    return HttpResponseRedirect('/{}')
{}""".format(class_object.name, views_methods_token)