import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary


views_methods_token = token_dictionary()["base_app"]["views"]["methods"]
views_path_token = token_dictionary()["base_app"]["views"]["path"]


def define_get_one_method(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_path_token
    # Add views get one
    replace_data_in_file(
        views_directory,
        views_methods_token,
        create_get_one_method(class_object)
    )
    print("Define get one method in: {}".format(views_directory))
    print("")


def create_get_one_method(class_object):
    return """
def get_one(request, id):
    app_object = {}.objects.get(id=id)
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_one.html', {})
{}""".format(class_object.name, "{'app_object': app_object}", views_methods_token)