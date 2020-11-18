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
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_edit.html', {})
{}""".format(class_object.name, "{'app_object': app_object}", views_methods_token)