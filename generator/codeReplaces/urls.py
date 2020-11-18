import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

urls_token = token_dictionary()["application"]["urls"]


def define_urls(class_object):
    urls_directory = constants.OUT_DIRECTORY + constants.BASE_APPLICATION_DIRECTORY + urls_token["path"]
    # Add urls import
    replace_data_in_file(
        urls_directory,
        urls_token["import"],
        create_urls_import(class_object)
    )
    print("Define import to get all view in: {}".format(urls_directory))
    print("")

    # Add urls get all pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_get_all_patterns_path(class_object, "get_all")
    )
    print("Define url pattern to get all view in: {}".format(urls_directory))
    print("")

    # Add urls create pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_create_patterns_path(class_object, "create")
    )
    print("Define url pattern to create view in: {}".format(urls_directory))
    print("")

    # Add urls store pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_store_patterns_path(class_object, "store")
    )
    print("Define url pattern to store view in: {}".format(urls_directory))
    print("")

    # Add urls get one pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_get_one_patterns_path(class_object, "get_one")
    )
    print("Define url pattern to get one view in: {}".format(urls_directory))
    print("")

    # Add urls edit pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_edit_patterns_path(class_object, "edit")
    )
    print("Define url pattern to edit view in: {}".format(urls_directory))
    print("")

    # Add urls update pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_update_patterns_path(class_object, "update")
    )
    print("Define url pattern to update view in: {}".format(urls_directory))
    print("")

    # Add urls delete pattern
    replace_data_in_file(
        urls_directory,
        urls_token["url_patterns_path"],
        create_urls_delete_patterns_path(class_object, "delete")
    )
    print("Define url pattern to delete view in: {}".format(urls_directory))
    print("")


def create_urls_import(class_object):
    return "import {}.views as {}_views\n{}".format(class_object.name, class_object.name,
                                                    urls_token["import"])


def create_urls_get_all_patterns_path(class_object, method):
    return "path('{}/', {}_views.{}, name='{}'),\n\t{}".format(class_object.name, class_object.name, method,
                                                               class_object.name,
                                                               urls_token["url_patterns_path"])


def create_urls_get_one_patterns_path(class_object, method):
    return "path('{}/<slug:id>/', {}_views.{}, name='{}-details'),\n\t{}".format(class_object.name, class_object.name,
                                                                                 method,
                                                                                 class_object.name,
                                                                                 urls_token["url_patterns_path"])


def create_urls_create_patterns_path(class_object, method):
    return "path('{}/create/', {}_views.{}, name='{}-create'),\n\t{}".format(class_object.name, class_object.name,
                                                                             method,
                                                                             class_object.name,
                                                                             urls_token["url_patterns_path"])


def create_urls_store_patterns_path(class_object, method):
    return "path('{}/store/', {}_views.{}, name='{}-store'),\n\t{}".format(class_object.name, class_object.name, method,
                                                                           class_object.name,
                                                                           urls_token["url_patterns_path"])


def create_urls_edit_patterns_path(class_object, method):
    return "path('{}/<slug:id>/edit', {}_views.{}, name='{}-edit'),\n\t{}".format(class_object.name, class_object.name,
                                                                                  method,
                                                                                  class_object.name,
                                                                                  urls_token["url_patterns_path"])


def create_urls_update_patterns_path(class_object, method):
    return "path('{}/<slug:id>/update', {}_views.{}, name='{}-update'),\n\t{}".format(class_object.name,
                                                                                      class_object.name,
                                                                                      method,
                                                                                      class_object.name,
                                                                                      urls_token["url_patterns_path"])


def create_urls_delete_patterns_path(class_object, method):
    return "path('{}/<slug:id>/delete', {}_views.{}, name='{}-delete'),\n\t{}".format(class_object.name,
                                                                                      class_object.name,
                                                                                      method,
                                                                                      class_object.name,
                                                                                      urls_token["url_patterns_path"])