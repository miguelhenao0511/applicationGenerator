import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

all_template_token = token_dictionary()["templates"]["base_app_templates"]["base_app_all"]
all_template_path_token = token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["path"]
all_template_directory = ""


def define_all_template(class_object):
    global all_template_directory
    all_template_directory = constants.OUT_DIRECTORY + "/templates/{}_templates".format(class_object.name) + all_template_path_token

    define_title(class_object)
    define_link_to_create_item(class_object)
    define_table_field_header(class_object)
    define_table_field_value(class_object)


def define_title(class_object):
    # Modify template all title
    replace_data_in_file(
        all_template_directory,
        all_template_token["template_title"],
        create_title(class_object)
    )
    print("Define template all title: {}".format(all_template_directory))
    print("")


def define_link_to_create_item(class_object):
    # Modify template all link to create item
    replace_data_in_file(
        all_template_directory,
        all_template_token["link_to_create_item"],
        create_link_to_create_item(class_object)
    )
    print("Define template all link to create item: {}".format(all_template_directory))
    print("")


def define_table_field_header(class_object):
    # Modify template all table fields headers
    replace_data_in_file(
        all_template_directory,
        all_template_token["table_field_header"],
        create_table_fields_headers(class_object)
    )
    print("Define template all table fields headers: {}".format(all_template_directory))
    print("")


def define_table_field_value(class_object):
    # Modify template all table field values
    replace_data_in_file(
        all_template_directory,
        all_template_token["table_field_value"],
        create_table_fields_values(class_object)
    )
    print("Define template all table fields values: {}".format(all_template_directory))
    print("")


def create_title(class_object):
    return "{} all items\n{}".format(class_object.name, all_template_token["template_title"])


def create_link_to_create_item(class_object):
    return "<a href='{}'>".format("{% url " + "'{}-create'".format(class_object.name) + " %}")


def create_table_fields_headers(class_object):
    response = ""
    for attribute in class_object.attributes:
        if attribute.attribute_type in "string,integer,boolean,date,calculated":
            response = response + "<th>{}<th>\n".format(attribute.name)
    return response


def create_table_fields_values(class_object):
    response = ""
    for attribute in class_object.attributes:
        if attribute.attribute_type in "string,integer,boolean,date,calculated":
            object = "{{" + "app_object.{}".format(attribute.name) + "}}"
            response = response + "<td>{}<td>\n".format(object)
    return response + create_action_buttons(class_object)


def create_action_buttons(class_object):
    return """    
<td>
    <a href="{}">
        <i class="fa fa-eye mr-1 ml-1"></i>
    </a>
    <a href="{}">
        <i class="fas fa-edit mr-1 ml-1""></i>
    </a>
    <a href="{}">
        <i class="fas fa-trash mr-1 ml-1""></i>
    </a>
</td>
    """.format(
        "{" + "% url '{}-details' id=app_object.id %".format(class_object.name) + "}",
        "{" + "% url '{}-edit' id=app_object.id %".format(class_object.name) + "}",
        "{" + "% url '{}-delete' id=app_object.id %".format(class_object.name) + "}"
    )