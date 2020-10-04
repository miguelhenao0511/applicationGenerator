token_dictionary = {
    "application": {
        "path": "/application",
        "settings": {
            "path": "/settings.py",
            "installed_local_apps": "#@application_settings_installed_local_apps",
        },
        "urls": {
            "path": "/urls.py",
            "import": "#@application_urls_imports",
            "url_patterns_path": "#@application_urls_patterns_path",
        },
    },
    "base_app": {
        "path": "/base_app",
        "models": {
            "path": "/models.py",
            "import": "#@base_app_model_import",
            "class": "#@base_app_model_class",
            "attributes": "#@base_app_model_attributes",
        },
        "views": {
            "path": "/views.py",
            "import": "#@base_app_views_import",
            "methods": "#@base_app_views_methods",
        },
        "urls": {
            "path": "/urls.py",
            "import": "#@base_app_urls_imports",
            "url_patterns_path": "#@base_app_urls_patterns_path"
        }
    },
    "templates": {
        "path": "/templates",
        "base_app_templates": {
            "path": "/base_app_templates",
            "base_app_all": {
                "path": "/base_app_all.html",
                "template_title": "<!--#@templates_base_app_all_template_title-->",
                "link_to_create_item": "<!--#@templates_base_app_all_link_to_create_item-->",
                "table_field_header": "<!--#@templates_base_app_all_table_field_header-->",
                "table_field_value": "<!--#@templates_base_app_all_table_field_value-->",
            },
            "base_app_one": {
                "path": "/base_app_one.html",
                "template_title": "<!--#@templates_base_app_one_template_title-->",
                "table_field_value": "<!--#@templates_base_app_one_table_field_value-->",
                "back_button": "<!--#@templates_base_app_one_back_button-->",
            },
            "base_app_create": {
                "path": "/base_app_create.html",
            },
            "base_app_edit": {
                "path": "/base_app_edit.html",
            },
        },
        "base_app_template": {
            "path": "/base_app_template.html",
        },
        "nav": {
            "path": "/nav.html",
            "nav_item": "<!--#@templates_nav_item-->",
        },
    },
}


def get_token():
    return token_dictionary
