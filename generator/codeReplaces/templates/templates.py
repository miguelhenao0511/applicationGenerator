import generator.utils.constants as constants
from generator.utils.fileUtils import replace_data_in_file
from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
from generator.codeReplaces.templates.all.all import define_all_template
from generator.codeReplaces.templates.one.one import define_one_template
from generator.codeReplaces.templates.create.create import define_create_template
from generator.codeReplaces.templates.edit.edit import define_edit_template

templates_token = token_dictionary()["templates"]
nav_token = token_dictionary()["templates"]["nav"]


def define_templates(class_object):

    define_all_template(class_object)
    define_one_template(class_object)
    define_create_template(class_object)
    define_edit_template(class_object)

    define_nav_item(class_object)


def define_nav_item(class_object):
    nav_directory = constants.OUT_DIRECTORY + "/templates" + nav_token["path"]
    # Add nav item
    replace_data_in_file(
        nav_directory,
        nav_token["nav_item"],
        create_nav_item(class_object)
    )
    print("Define new nav item in: {}".format(nav_directory))
    print("")


def create_nav_item(class_object):
    return """
<li class="nav-item mr-2 ml-2">
    <a href="{}">
        {}
    </a>
</li>
{}
    """.format("{" + "% url '{}' %".format(class_object.name) + "}", class_object.name,
               nav_token["nav_item"])