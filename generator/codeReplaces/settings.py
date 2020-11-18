import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

settings_token = token_dictionary()["application"]["settings"]


def define_settings(class_object):
    settings_directory = constants.OUT_DIRECTORY + constants.BASE_APPLICATION_DIRECTORY + settings_token["path"]
    # Add installed app to settings
    replace_data_in_file(
        settings_directory,
        settings_token["installed_local_apps"],
        create_settings_installed_local_app_definition(class_object.name)
    )
    print("Define new app installed in: {}".format(settings_directory))
    print("")


def create_settings_installed_local_app_definition(app_name):
    return "'{}',\n\t{}".format(app_name, settings_token["installed_local_apps"])