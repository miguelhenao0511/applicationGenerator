from applicationGenerator.utils.tokensDictionary import get_token as token_dictionary
import os

BASE_DIRECTORY = os.getcwd() + "/resources/base_application/application"
OUT_DIRECTORY = os.getcwd() + "/resources/out_application/application"
BASE_APP_DIRECTORY = token_dictionary()["base_app"]["path"]
BASE_APPLICATION_DIRECTORY = token_dictionary()["application"]["path"]
