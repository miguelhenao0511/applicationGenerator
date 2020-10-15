from django.shortcuts import render
from django.http import HttpResponse
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
from distutils.dir_util import copy_tree
from applicationGenerator.utils.classTemplate import ClassTemplate, AttributeTemplate, generate_random_class, \
    get_random_string, get_random_integer, get_random_boolean, get_date
import os

BASE_DIRECTORY = os.getcwd() + "/resources/base_application/application"
OUT_DIRECTORY = os.getcwd() + "/resources/out_application/application"
BASE_APP_DIRECTORY = token_dictionary()["base_app"]["path"]
BASE_APPLICATION_DIRECTORY = token_dictionary()["application"]["path"]


# Create your views here.
def create_application(request):
    copy_tree(BASE_DIRECTORY, OUT_DIRECTORY)

    user_class = ClassTemplate("Usuario", [
        AttributeTemplate("nombre", "string"),
        AttributeTemplate("apellido", "string"),
        AttributeTemplate("email", "string"),
        AttributeTemplate("password", "string")
    ])
    product_class = ClassTemplate("Producto", [
        AttributeTemplate("nombre", "string"),
        AttributeTemplate("descripcion", "string"),
        AttributeTemplate("valor", "integer"),
        AttributeTemplate("disponible", "boolean"),
        AttributeTemplate("fecha_publicacion", "datetime")
    ])
    random_class_1 = generate_random_class(3)
    random_class_2 = generate_random_class(3)
    random_class_3 = generate_random_class(5)

    create_app(user_class)
    create_app(product_class)
    create_app(random_class_1)
    create_app(random_class_2)
    create_app(random_class_3)

    return HttpResponse(
        "copy application from: {} to: {}".format(BASE_DIRECTORY, OUT_DIRECTORY))


def create_app(random_class):

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

    new_app_template_all_directory = new_app_template_directory + \
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_all"]["path"]
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

    new_app_template_one_directory = new_app_template_directory + \
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["path"]
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
    print("Define template one table fields values: {}".format(new_app_template_one_directory))
    print("")

    # Modify template get one back button
    replace_data_in_file(
        new_app_template_one_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_one"]["back_button"],
        create_template_one_back_button(random_class)
    )
    print("Define template get one back button: {}".format(new_app_template_one_directory))
    print("")

    new_app_template_create_directory = new_app_template_directory + \
                                        token_dictionary()["templates"]["base_app_templates"]["base_app_create"]["path"]
    # Modify template create title
    replace_data_in_file(
        new_app_template_create_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_create"]["template_title"],
        create_template_create_title(random_class)
    )
    print("Define template create title: {}".format(new_app_template_create_directory))
    print("")

    # Modify template create form fields
    replace_data_in_file(
        new_app_template_create_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_create"]["form_fields"],
        create_template_create_form_fields(random_class)
    )
    print("Define template create form fields: {}".format(new_app_template_create_directory))
    print("")

    # Modify template create back button
    replace_data_in_file(
        new_app_template_create_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_create"]["back_button"],
        create_template_create_back_button(random_class)
    )
    print("Define template create back button: {}".format(new_app_template_create_directory))
    print("")

    new_app_template_edit_directory = new_app_template_directory + \
                                      token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]["path"]
    # Modify template edit title
    replace_data_in_file(
        new_app_template_edit_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]["template_title"],
        create_template_edit_title(random_class)
    )
    print("Define template edit title: {}".format(new_app_template_edit_directory))
    print("")

    # Modify template edit form fields
    replace_data_in_file(
        new_app_template_edit_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]["form_fields"],
        create_template_edit_form_fields(random_class)
    )
    print("Define template edit form fields: {}".format(new_app_template_edit_directory))
    print("")

    # Modify template edit back button
    replace_data_in_file(
        new_app_template_edit_directory,
        token_dictionary()["templates"]["base_app_templates"]["base_app_edit"]["back_button"],
        create_template_edit_back_button(random_class)
    )
    print("Define template edit back button: {}".format(new_app_template_edit_directory))
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

    # Add views create
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_create(random_class)
    )
    print("Define create view in: {}".format(new_app_views_directory))
    print("")

    # Add views store
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_store(random_class)
    )
    print("Define store object in: {}".format(new_app_views_directory))
    print("")

    # Add views edit
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_edit(random_class)
    )
    print("Define edit view in: {}".format(new_app_views_directory))
    print("")

    # Add views update
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_update(random_class)
    )
    print("Define update object in: {}".format(new_app_views_directory))
    print("")

    # Add views delete
    replace_data_in_file(
        new_app_views_directory,
        token_dictionary()["base_app"]["views"]["methods"],
        create_views_methods_delete(random_class)
    )
    print("Define delete object in: {}".format(new_app_views_directory))
    print("")

    application_urls_directory = OUT_DIRECTORY + BASE_APPLICATION_DIRECTORY + token_dictionary()["application"]["urls"][
        "path"]
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

    # Add urls create pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_create_patterns_path(random_class, "create")
    )
    print("Define url pattern to create view in: {}".format(application_urls_directory))
    print("")

    # Add urls store pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_store_patterns_path(random_class, "store")
    )
    print("Define url pattern to store view in: {}".format(application_urls_directory))
    print("")

    # Add urls get one pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_get_one_patterns_path(random_class, "get_one")
    )
    print("Define url pattern to get one view in: {}".format(application_urls_directory))
    print("")

    # Add urls edit pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_edit_patterns_path(random_class, "edit")
    )
    print("Define url pattern to edit view in: {}".format(application_urls_directory))
    print("")

    # Add urls update pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_update_patterns_path(random_class, "update")
    )
    print("Define url pattern to update view in: {}".format(application_urls_directory))
    print("")

    # Add urls delete pattern
    replace_data_in_file(
        application_urls_directory,
        token_dictionary()["application"]["urls"]["url_patterns_path"],
        create_urls_delete_patterns_path(random_class, "delete")
    )
    print("Define url pattern to delete view in: {}".format(application_urls_directory))
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
    return "from {}.models import {}\n{}".format(class_object.name, class_object.name,
                                                 token_dictionary()["application"]["settings"]["installed_local_apps"])


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


def create_views_methods_create(class_object):
    return """
def create(request):
    return render(request, '{}_templates/base_app_create.html')
{}""".format(class_object.name, token_dictionary()["base_app"]["views"]["methods"])


def create_views_methods_store(class_object):
    return """
def store(request):
    app_object = {}.objects.create({})
    """.format(class_object.name, create_views_object_attributes(class_object.attributes)) + """
    redirectTo = '/{}/' + str(app_object.id)
    return HttpResponseRedirect(redirectTo)
{}""".format(class_object.name, token_dictionary()["base_app"]["views"]["methods"])


def create_views_methods_edit(class_object):
    return """
def edit(request, id):
    app_object = {}.objects.get(id=id)
    """.format(class_object.name) + """
    return render(request, '{}_templates/base_app_edit.html', {})
{}""".format(class_object.name, "{'app_object': app_object}", token_dictionary()["base_app"]["views"]["methods"])


def create_views_methods_update(class_object):
    return """
def update(request, id):
    app_object = {}.objects.get(id=id)
    """.format(class_object.name) + """
    app_object.__dict__.update({})""".format(create_views_object_attributes(class_object.attributes)) + """
    app_object.save()
    
    redirectTo = '/{}/' + str(app_object.id)
    return HttpResponseRedirect(redirectTo)
{}""".format(class_object.name, token_dictionary()["base_app"]["views"]["methods"])


def create_views_methods_delete(class_object):
    return """
def delete(request, id):
    {}.objects.filter(id=id).delete()
    """.format(class_object.name) + """
    return HttpResponseRedirect('/{}')
{}""".format(class_object.name, class_object.name, token_dictionary()["base_app"]["views"]["methods"])


def create_views_object_attributes(attributes):
    response = []
    for attribute in attributes:
        if attribute.attribute_type == "boolean":
            response.append("{}='{}' in request.POST".format(attribute.name, attribute.name))
        else:
            response.append("{}=request.POST['{}']".format(attribute.name, attribute.name))
    return ",".join(response)


def create_urls_import(class_object):
    return "import {}.views as {}_views\n{}".format(class_object.name, class_object.name,
                                                    token_dictionary()["application"]["urls"]["import"])


def create_urls_get_all_patterns_path(class_object, method):
    return "path('{}/', {}_views.{}, name='{}'),\n\t{}".format(class_object.name, class_object.name, method,
                                                               class_object.name,
                                                               token_dictionary()["application"]["urls"][
                                                                   "url_patterns_path"])


def create_urls_get_one_patterns_path(class_object, method):
    return "path('{}/<slug:id>/', {}_views.{}, name='{}-details'),\n\t{}".format(class_object.name, class_object.name,
                                                                                 method,
                                                                                 class_object.name,
                                                                                 token_dictionary()["application"][
                                                                                     "urls"][
                                                                                     "url_patterns_path"])


def create_urls_create_patterns_path(class_object, method):
    return "path('{}/create/', {}_views.{}, name='{}-create'),\n\t{}".format(class_object.name, class_object.name,
                                                                             method,
                                                                             class_object.name,
                                                                             token_dictionary()["application"]["urls"][
                                                                                 "url_patterns_path"])


def create_urls_store_patterns_path(class_object, method):
    return "path('{}/store/', {}_views.{}, name='{}-store'),\n\t{}".format(class_object.name, class_object.name, method,
                                                                           class_object.name,
                                                                           token_dictionary()["application"]["urls"][
                                                                               "url_patterns_path"])


def create_urls_edit_patterns_path(class_object, method):
    return "path('{}/<slug:id>/edit', {}_views.{}, name='{}-edit'),\n\t{}".format(class_object.name, class_object.name,
                                                                                  method,
                                                                                  class_object.name,
                                                                                  token_dictionary()["application"][
                                                                                      "urls"][
                                                                                      "url_patterns_path"])


def create_urls_update_patterns_path(class_object, method):
    return "path('{}/<slug:id>/update', {}_views.{}, name='{}-update'),\n\t{}".format(class_object.name,
                                                                                      class_object.name,
                                                                                      method,
                                                                                      class_object.name,
                                                                                      token_dictionary()["application"][
                                                                                          "urls"][
                                                                                          "url_patterns_path"])


def create_urls_delete_patterns_path(class_object, method):
    return "path('{}/<slug:id>/delete', {}_views.{}, name='{}-delete'),\n\t{}".format(class_object.name,
                                                                                      class_object.name,
                                                                                      method,
                                                                                      class_object.name,
                                                                                      token_dictionary()["application"][
                                                                                          "urls"][
                                                                                          "url_patterns_path"])


def create_template_all_title(class_object):
    return "{} all items\n{}".format(class_object.name,
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_all"][
                                         "template_title"])


def create_template_one_title(class_object):
    return "{} item\n{}".format(class_object.name,
                                token_dictionary()["templates"]["base_app_templates"]["base_app_one"][
                                    "template_title"])


def create_template_create_title(class_object):
    return "{} create item\n{}".format(class_object.name,
                                       token_dictionary()["templates"]["base_app_templates"]["base_app_create"][
                                           "template_title"])


def create_template_edit_title(class_object):
    return "{} edit item\n{}".format(class_object.name,
                                     token_dictionary()["templates"]["base_app_templates"]["base_app_edit"][
                                         "template_title"])


def create_template_all_link_to_create_item(class_object):
    return "<a href='{}'>".format("{% url " + "'{}-create'".format(class_object.name) + " %}")


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


def create_template_create_form_fields(class_object):
    response = "<form action='{}' method='POST' class='form-control'>\n{}\n".format(
        "{% url " + "'{}-store'".format(class_object.name) + " %}",
        "{% csrf_token %}")

    for attribute in class_object.attributes:
        response += create_template_form_field(attribute)

    response += """
<div class="form-group">
    <input type="submit" class="btn btn-success form-control" value="Save">
</div>
    """

    return response + "\n</form>"


def create_template_edit_form_fields(class_object):
    response = "<form action='{}' method='POST' class='form-control'>\n{}\n".format(
        "{% url " + "'{}-update'".format(class_object.name) + " id=app_object.id %}",
        "{% csrf_token %}")

    for attribute in class_object.attributes:
        response += create_template_form_field(attribute, "{{" + "app_object.{}".format(attribute.name) + "}}")

    response += """
<div class="form-group">
    <input type="submit" class="btn btn-success form-control" value="Save">
</div>
    """

    return response + "\n</form>"


def create_template_form_field(attribute, value=""):
    response = "<div class='form-group'>\n<label>{}</label>\n".format(attribute.name)
    response += create_template_form_input(attribute, value)
    return response + "</div>\n"


def create_template_form_input(attribute, value):
    attribute_type = "text"
    if attribute.attribute_type == "integer":
        attribute_type = "number"
    elif attribute.attribute_type == "datetime":
        attribute_type = "date"
    elif attribute.attribute_type == "boolean":
        attribute_type = "checkbox"
    return "<input type='{}' class='form-control' name='{}' value='{}' />".format(attribute_type, attribute.name, value)


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
    """.format(
        "{" + "% url '{}-details' id=app_object.id %".format(class_object.name) + "}",
        "{" + "% url '{}-edit' id=app_object.id %".format(class_object.name) + "}",
        "{" + "% url '{}-delete' id=app_object.id %".format(class_object.name) + "}"
    )


def create_template_one_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format(
        "{" + "% url '{}' %".format(class_object.name) + "}")


def create_template_create_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format(
        "{" + "% url '{}' %".format(class_object.name) + "}")


def create_template_edit_back_button(class_object):
    return "<a href='{}' class='btn btn-secondary'>Back</a>".format(
        "{" + "% url '{}' %".format(class_object.name) + "}")


def create_nav_item(class_object):
    return """
<li class="nav-item mr-2 ml-2">
    <a href="{}">
        {}
    </a>
</li>
{}
    """.format("{" + "% url '{}' %".format(class_object.name) + "}", class_object.name,
               token_dictionary()["templates"]["nav"]["nav_item"])


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
