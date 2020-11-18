import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

one_template_token = token_dictionary()["templates"]["base_app_templates"]["base_app_one"]
one_template_path_token = token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["path"]
one_template_directory = ""


def define_one_template(class_object):
    global one_template_directory
    one_template_directory = constants.OUT_DIRECTORY + "/templates/{}_templates".format(class_object.name) + one_template_path_token

    define_title(class_object)
    define_table_fields_values(class_object)
    define_back_button(class_object)


def define_title(class_object):
    # Modify template one title
    replace_data_in_file(
        one_template_directory,
        one_template_token["template_title"],
        create_title(class_object)
    )
    print("Define template one title: {}".format(one_template_directory))
    print("")


def define_table_fields_values(class_object):
    # Modify template one table fields values
    replace_data_in_file(
        one_template_directory,
        one_template_token["table_field_value"],
        create_table_fields_values(class_object)
    )
    print("Define template one table fields values: {}".format(one_template_directory))
    print("")


def define_back_button(class_object):
    # Modify template get one back button
    replace_data_in_file(
        one_template_directory,
        one_template_token["back_button"],
        create_back_button(class_object)
    )
    print("Define template get one back button: {}".format(one_template_directory))
    print("")


def create_title(class_object):
    return "{} item\n{}".format(class_object.name, one_template_token["template_title"])


def create_table_fields_values(class_object):
    response = ""
    for attribute in class_object.attributes:
        if "[]" in attribute.attribute_type:
            response += define_table_many_to_many_values(attribute)
        else:
            app_object = "{{" + "app_object.{}".format(attribute.name) + "}}"
            response = response + "<tr>\n<td>{}:<td>\n<td>{}<td>\n</tr>\n".format(attribute.name, app_object)
    return response


def define_table_many_to_many_values(attribute):
    response = "<tr>\n<td>{}</td>\n".format(attribute.name)
    response += "<td>\n{% for " + "{} in app_object.{}.all ".format(attribute.name, attribute.name) + "%}\n"
    response += "<p>{{ " + "{}".format(attribute.name) + " }}</p>\n"
    response += "{% endfor %}\n </td>\n </tr>"
    return response

def create_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format(
        "{" + "% url '{}' %".format(class_object.name) + "}")