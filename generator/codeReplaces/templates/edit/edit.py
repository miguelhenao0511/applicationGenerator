import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary

edit_template_token = token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]
edit_template_path_token = token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]["path"]
edit_template_directory = ""


def define_edit_template(class_object):
    global edit_template_directory
    edit_template_directory = constants.OUT_DIRECTORY + "/templates/{}_templates".format(class_object.name) + edit_template_path_token

    define_title(class_object)
    define_form_fields(class_object)
    define_back_button(class_object)


def define_title(class_object):
    # Modify template edit title
    replace_data_in_file(
        edit_template_directory,
        edit_template_token["template_title"],
        create_title(class_object)
    )
    print("Define template edit title: {}".format(edit_template_directory))
    print("")


def define_form_fields(class_object):
    # Modify template edit form fields
    replace_data_in_file(
        edit_template_directory,
        edit_template_token["form_fields"],
        create_form_fields(class_object)
    )
    print("Define template edit form fields: {}".format(edit_template_directory))
    print("")


def define_back_button(class_object):
    # Modify template edit back button
    replace_data_in_file(
        edit_template_directory,
        edit_template_token["back_button"],
        create_back_button(class_object)
    )
    print("Define template edit back button: {}".format(edit_template_directory))
    print("")


def create_title(class_object):
    return "{} edit item\n{}".format(class_object.name, edit_template_token["template_title"])


def create_form_fields(class_object):
    response = "<form action='{}' method='POST' class='form-control'>\n{}\n".format(
        "{% url " + "'{}-update'".format(class_object.name) + " id=app_object.id %}",
        "{% csrf_token %}")

    for attribute in class_object.attributes:
        response += create_form_field(attribute, "{{" + "app_object.{}".format(attribute.name) + "}}")

    response += """
<div class="form-group">
    <input type="submit" class="btn btn-success form-control" value="Save">
</div>
    """

    return response + "\n</form>"


def create_form_field(attribute, value=""):
    response = "<div class='form-group'>\n<label>{}</label>\n".format(attribute.name)
    response += create_form_input(attribute, value)
    return response + "</div>\n"


def create_form_input(attribute, value):
    attribute_type = "text"
    if attribute.attribute_type == "integer":
        attribute_type = "number"
    elif attribute.attribute_type == "datetime":
        attribute_type = "date"
    elif attribute.attribute_type == "boolean":
        attribute_type = "checkbox"
    return "<input type='{}' class='form-control' name='{}' value='{}' />".format(attribute_type, attribute.name, value)


def create_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format(
        "{" + "% url '{}' %".format(class_object.name) + "}")