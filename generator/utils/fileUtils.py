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
