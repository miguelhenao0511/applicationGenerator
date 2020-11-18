import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary


views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_get_all_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add get all method
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_get_all_method(class_object)
    )
    print("Define get all method in: {}".format(views_directory))
    print("")


def create_get_all_method(class_object):
    return """
def get_all(request):
    app_objects = {}.objects.all()
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_all.html', {})
{}""".format(class_object.name, "{'app_objects': app_objects}", views_methods_token)