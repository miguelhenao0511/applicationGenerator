from django.http import HttpResponse
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
from applicationGenerator.utils.tokens import generate_json_structure
from generator.codeReplaces.models import define_models
from generator.codeReplaces.settings import define_settings
from generator.codeReplaces.views.views import define_views
from generator.codeReplaces.urls import define_urls
from generator.codeReplaces.templates.templates import define_templates
from distutils.dir_util import copy_tree
from applicationGenerator.utils.classTemplate import ClassTemplate, AttributeTemplate
import shutil
import os

BASE_DIRECTORY = os.getcwd() + "/resources/base_application/application"
OUT_DIRECTORY = os.getcwd() + "/resources/out_application/application"
BASE_APP_DIRECTORY = token_dictionary()["base_app"]["path"]
BASE_APPLICATION_DIRECTORY = token_dictionary()["application"]["path"]


# Create your views here.
def create_application(request):
    if os.path.exists(os.getcwd() + '/resources/out_application'):
        shutil.rmtree(os.getcwd() + '/resources/out_application')

    # Generate out application folder
    copy_tree(BASE_DIRECTORY, OUT_DIRECTORY)

    # Read json
    file = request.FILES["bpmn_file"]
    json = generate_json_structure(file)

    for class_json in json:

        if "CREAR " in class_json["name"]:
            class_object = ClassTemplate(class_json["name"].replace("CREAR ", "").replace(" ", "_").lower(), [])

            for attribute in class_json["attributes"]:
                attribute_object = AttributeTemplate(attribute["name"].replace(" ", "_").lower(),
                                                     attribute["attribute_type"])
                if "operation" in attribute and attribute["operation"] is not None:
                    attribute_object.operation = attribute["operation"]

                class_object.attributes.append(attribute_object)

            create_app(class_object)

    return HttpResponse("copy application from: {} to: {}".format(BASE_DIRECTORY, OUT_DIRECTORY))


def create_app(class_object):
    new_app_directory = OUT_DIRECTORY + "/" + class_object.name
    # Create app
    copy_tree(OUT_DIRECTORY + BASE_APP_DIRECTORY, new_app_directory)
    print("Create new app in: {}".format(new_app_directory))
    print("")

    new_app_template_directory = OUT_DIRECTORY + "/templates/{}_templates".format(class_object.name)
    # Create templates
    copy_tree(OUT_DIRECTORY + "/templates/base_app_templates", new_app_template_directory)
    print("Create new template in: {}".format(new_app_template_directory))
    print("")

    define_models(class_object)
    define_settings(class_object)
    define_views(class_object)
    define_urls(class_object)
    define_templates(class_object)
