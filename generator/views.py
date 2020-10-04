from django.shortcuts import render
from django.http import HttpResponse
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
from distutils.dir_util import copy_tree
from applicationGenerator.utils.classTemplate import ClassTemplate, AttributeTemplate, generate_random_class, get_random_string, get_random_integer, get_random_boolean, get_date
import os

BASE_DIRECTORY = os.getcwd() + "/resources/base_application/application"
OUT_DIRECTORY = os.getcwd() + "/resources/out_application/application"
BASE_APP_DIRECTORY = token_dictionary()["base_app"]["path"]
BASE_APPLICATION_DIRECTORY = token_dictionary()["application"]["path"]


# Create your views here.
def copy_application(request):
    copy_tree(BASE_DIRECTORY, OUT_DIRECTORY)

    return HttpResponse(
        "copy application from: {} to: {}".format(BASE_DIRECTORY, OUT_DIRECTORY))


def create_app(request):
    #random_class = generate_random_class(5)

    product_class = ClassTemplate("Producto", [
        AttributeTemplate("nombre", "string"),
        AttributeTemplate("descripcion", "string"),
        AttributeTemplate("valor", "integer"),
        AttributeTemplate("disponible", "boolean"),
        AttributeTemplate("fecha_publicacion", "datetime")
    ])

    user_class = ClassTemplate("Usuario", [
        AttributeTemplate("nombre", "string"),
        AttributeTemplate("apellido", "string"),
        AttributeTemplate("email", "string"),
        AttributeTemplate("password", "string")
    ])

    random_class = product_class
    #random_class = user_class

    new_app_directory = OUT_DIRECTORY + "/" + random_class.name
    # Create app
    copy_tree(OUT_DIRECTORY + BASE_APP_DIRECTORY, new_app_directory)
    print("Create new app in: {}".format(new_app_directory))
    print("")

    new_app_models_directory = new_app_directory + token_dictionary()["base_app"]["models"]["path"]
    # Create model
    # Define model class
    replace_data_in_file(
        new_app_models_directory,
        token_dictionary()["base_app"]["models"]["class"],
        create_model_class_definition(random_class.name)
    )
    print("Define new model in: {}".format(new_app_models_directory))
    print("")

    # Define model attributes
    replace_data_in_file(
        new_app_models_directory,
        token_dictionary()["base_app"]["models"]["attributes"],
        create_model_attributes_definition(random_class.attributes)
    )
    print("Define new attributes in: {}".format(new_app_models_directory))
    print("")

    application_settings_directory = OUT_DIRECTORY + BASE_APPLICATION_DIRECTORY + \
                                     token_dictionary()["application"]["settings"]["path"]
    # Add installed app to settings
    replace_data_in_file(
        application_settings_directory,
        token_dictionary()["application"]["settings"]["installed_local_apps"],
        create_settings_installed_local_app_definition(random_class.name)
    )
    print("Define new app installed in: {}".format(application_settings_directory))
    print("")

    new_app_template_directory = OUT_DIRECTORY + "/templates/{}_templates".format(random_class.name)
    # Create templates
    copy_tree(OUT_DIRECTORY + "/templates/base_app_templates", new_app_template_directory)
    print("Create new template in: {}".format(new_app_template_directory))
    print("")

    new_app_template_all_directory = new_app_template_directory + token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["path"]
    # Modify template all title
    replace_data_in_file(
        new_app_template_all_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["template_title"],
        create_template_all_title(random_class)
    )
    print("Define template all title: {}".format(new_app_template_all_directory))
    print("")

    # Modify template all link to create item
    replace_data_in_file(
        new_app_template_all_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["link_to_create_item"],
        create_template_all_link_to_create_item(random_class)
    )
    print("Define template all link to create item: {}".format(new_app_template_all_directory))
    print("")

    # Modify template all table fields headers
    replace_data_in_file(
        new_app_template_all_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["table_field_header"],
        create_template_all_table_fields_headers(random_class)
    )
    print("Define template all table fields headers: {}".format(new_app_template_all_directory))
    print("")

    # Modify template all table field values
    replace_data_in_file(
        new_app_template_all_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["table_field_value"],
        create_template_all_table_fields_values(random_class)
    )
    print("Define template all table fields values: {}".format(new_app_template_all_directory))
    print("")

    new_app_template_one_directory = new_app_template_directory + token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["path"]
    # Modify template one title
    replace_data_in_file(
        new_app_template_one_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["template_title"],
        create_template_one_title(random_class)
    )
    print("Define template one title: {}".format(new_app_template_one_directory))
    print("")

    # Modify template one table fields values
    replace_data_in_file(
        new_app_template_one_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["table_field_value"],
        create_template_one_table_fields_values(random_class)
    )
    print("Define template one table fields values: {}".format(new_app_template_all_directory))
    print("")

    # Modify template one back button
    replace_data_in_file(
        new_app_template_one_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["back_button"],
        create_template_one_back_button(random_class)
    )
    print("Define template one back button: {}".format(new_app_template_all_directory))
    print("")

    new_app_views_directory = new_app_directory + token_dictionary()["base_app"]["views"]["path"]
    # Modify view methods
    # Add views import
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["import"],
        create_views_import(random_class)
    )
    print("Define imports to view in: {}".format(new_app_views_directory))
    print("")

    # Add views get all
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_get_all(random_class)
    )
    print("Define get all objects to view in: {}".format(new_app_views_directory))
    print("")

    # Add views get one
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_get_one(random_class)
    )
    print("Define get one object to view in: {}".format(new_app_views_directory))
    print("")

    application_urls_directory = OUT_DIRECTORY + BASE_APPLICATION_DIRECTORY + token_dictionary()["application"]["urls"]["path"]
    # Add urls import
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["import"],
        create_urls_import(random_class)
    )
    print("Define import to get all view in: {}".format(application_urls_directory))
    print("")

    # Add urls get all pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_get_all_patterns_path(random_class, "get_all")
    )
    print("Define url pattern to get all view in: {}".format(application_urls_directory))
    print("")

    # Add urls get one pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_get_one_patterns_path(random_class, "get_one")
    )
    print("Define url pattern to get one view in: {}".format(application_urls_directory))
    print("")

    application_nav_directory = OUT_DIRECTORY + "/templates" + token_dictionary()["templates"]["nav"]["path"]
    # Add nav item
    replace_data_in_file(
        application_nav_directory,
        token_dictionary()["templates"]["nav"]["nav_item"],
        create_nav_item(random_class)
    )
    print("Define new nav item in: {}".format(application_nav_directory))
    print("")

    return HttpResponse("Create class {}".format(random_class))


def create_model_class_definition(model_name):
    print("model class definition created")
    return "class {}(models.Model):\n{}".format(model_name, token_dictionary()["base_app"]["models"]["class"])


def create_model_attributes_definition(attributes):
    response = "{}\n".format(token_dictionary()["base_app"]["models"]["attributes"])
    for attribute in attributes:
        print("model attribute definition created")
        response = response + "\t{} = models.{}\n".format(attribute.name, create_model_attribute_type_definition(
            attribute.attribute_type))
    return response


def create_model_attribute_type_definition(attribute_type):
    if attribute_type == "integer":
        return "IntegerField()"
    elif attribute_type == "boolean":
        return "BooleanField()"
    elif attribute_type == "datetime":
        return "DateTimeField()"
    else:
        return "CharField(max_length=255)"


def create_settings_installed_local_app_definition(app_name):
    return "'{}',\n\t{}".format(app_name, token_dictionary()["application"]["settings"]["installed_local_apps"])


def create_views_import(class_object):
    return "from {}.models import {}\n{}".format(class_object.name, class_object.name, token_dictionary()["application"]["settings"]["installed_local_apps"])


def create_views_methods_get_all(class_object):
    return """
def get_all(request):
    app_objects = {}.objects.all()
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_all.html', {})
{}""".format(class_object.name, "{'app_objects': app_objects}", token_dictionary()["base_app"]["views"]["methods"])


def create_views_methods_get_one(class_object):
    return """
def get_one(request, id):
    app_object = {}.objects.get(id=id)
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_one.html', {})
{}""".format(class_object.name, "{'app_object': app_object}", token_dictionary()["base_app"]["views"]["methods"])


def create_urls_import(class_object):
    return "import {}.views as {}_views\n{}".format(class_object.name, class_object.name,
                                                     token_dictionary()["application"]["urls"]["import"])


def create_urls_get_all_patterns_path(class_object, method):
    return "path('{}/', {}_views.{}, name='{}'),\n\t{}".format(class_object.name, class_object.name, method, class_object.name,
                                           token_dictionary()["application"]["urls"]["url_patterns_path"])


def create_urls_get_one_patterns_path(class_object, method):
    return "path('{}/<slug:id>/', {}_views.{}, name='{}'),\n\t{}".format(class_object.name, class_object.name, method, class_object.name,
                                           token_dictionary()["application"]["urls"]["url_patterns_path"])


def create_template_all_title(class_object):
    return "{} all items\n{}".format(class_object.name,
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_all"][
                                         "template_title"])


def create_template_one_title(class_object):
    return "{} item\n{}".format(class_object.name,
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_one"][
                                         "template_title"])


def create_template_all_link_to_create_item(class_object):
    return "<a href='{}'>".format("#")


def create_template_all_table_fields_headers(class_object):
    response = ""
    for attribute in class_object.attributes:
        response = response + "<th>{}<th>\n".format(attribute.name)
    return response


def create_template_all_table_fields_values(class_object):
    response = ""
    for attribute in class_object.attributes:
        app_object = "{{" + "app_object.{}".format(attribute.name) + "}}"
        response = response + "<td>{}<td>\n".format(app_object)
    return response + create_template_all_action_buttons(class_object)


def create_template_one_table_fields_values(class_object):
    response = ""
    for attribute in class_object.attributes:
        app_object = "{{" + "app_object.{}".format(attribute.name) + "}}"
        response = response + "<tr>\n<td>{}:<td>\n<td>{}<td>\n</tr>\n".format(attribute.name, app_object)
    return response


def create_template_all_action_buttons(class_object):
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
    """.format("{" + "% url '{}' id=app_object.id %".format(class_object.name) + "}", "#", "#")


def create_template_one_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format("{" + "% url '{}' %".format(class_object.name) + "}")


def create_nav_item(class_object):
    return """
<li class="nav-item mr-2 ml-2">
    <a href="{}">
        {}
    </a>
</li>
{}
    """.format("{" + "% url '{}' %".format(class_object.name) + "}", class_object.name, token_dictionary()["templates"]["nav"]["nav_item"])


def replace_data_in_file(file_path, old_data, new_data):
    file = open(file_path, 'r')
    fileContent = file.readlines()
    file.close()

    fileContentAsString = "".join(fileContent)
    fileContentAsString = fileContentAsString.replace(old_data, new_data)
    print("file data replace {} to {}".format(old_data, new_data))

    file = open(file_path, 'w')
    file.write(fileContentAsString)
    file.close()


def get_random_value_attribute(attribute_type):
    if attribute_type == "string":
        return get_random_string(20)
    elif attribute_type == "integer":
        return get_random_integer(999999)
    elif attribute_type == "boolean":
        return get_random_boolean()
    else:
        return get_date()
