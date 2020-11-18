import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
from generator.codeReplaces.views.methods.getAll import define_get_all_method
from generator.codeReplaces.views.methods.getOne import define_get_one_method
from generator.codeReplaces.views.methods.create import define_create_method
from generator.codeReplaces.views.methods.store import define_store_method
from generator.codeReplaces.views.methods.edit import define_edit_method
from generator.codeReplaces.views.methods.update import define_update_method
from generator.codeReplaces.views.methods.delete import define_delete_method

views_token = token_dictionary()["base_app"]["views"]


def define_views(class_object):
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_token["path"]
    # Add views import
    replace_data_in_file(
        views_directory,
        views_token["import"],
        create_views_import(class_object)
    )
    print("Define imports to view in: {}".format(views_directory))
    print("")

    define_get_all_method(class_object)
    define_get_one_method(class_object)
    define_create_method(class_object)
    define_store_method(class_object)
    define_edit_method(class_object)
    define_update_method(class_object)
    define_delete_method(class_object)


def create_views_import(class_object):
    return "from {}.models import {}\n{}".format(class_object.name, class_object.name, views_token["import"])