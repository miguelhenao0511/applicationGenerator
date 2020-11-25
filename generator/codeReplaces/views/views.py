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
views_directory = ""


def define_views(class_object):
    global views_directory
    views_directory = constants.OUT_DIRECTORY + "/" + class_object.name + views_token["path"]
    define_import(class_object)
    define_attributes_import(class_object)

    define_get_all_method(class_object)
    define_get_one_method(class_object)
    define_create_method(class_object)
    define_store_method(class_object)
    define_edit_method(class_object)
    define_update_method(class_object)
    define_delete_method(class_object)


def define_import(class_object):
    # Add views import
    replace_data_in_file(
        views_directory,
        views_token["import"],
        create_import(class_object)
    )
    print("Define imports to view in: {}".format(views_directory))
    print("")


def define_attributes_import(class_object):
    for attribute in class_object.attributes:
        if attribute.attribute_type not in "string,integer,double,boolean,date,calculated":
            # Add views import
            replace_data_in_file(
                views_directory,
                views_token["import"],
                create_attributes_import(attribute.name.replace("[]", ""))
            )
            print("Define imports to view in: {}".format(views_directory))
            print("")


def create_import(class_object):
    return "from {}.models import {}\n{}".format(class_object.name, class_object.name, views_token["import"])


def create_attributes_import(class_name):
    return "from {}.models import {}\n{}".format(class_name, class_name, views_token["import"])