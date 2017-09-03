import os

if __name__ == "__main__":
    home_folder = os.getcwd()

    file_list = []

    for root, dirs, files in os.walk(home_folder):
        for name in files:
            if name.endswith("-conv.pdf"):
                file_list.append(os.path.join(root, name))

    for file_name in file_list:
        path = os.path.dirname(file_name)
        new_file_name = file_name.replace("-conv.pdf", ".pdf")
        if os.path.isfile(os.path.join(path, new_file_name)):
            print("Error, file already exists")
        else:
            print("Renaming \'" + os.path.basename(file_name) + "\' to \'" + new_file_name)
            os.rename(file_name, os.path.join(path, new_file_name))
        mdi_file_name = file_name.replace("-conv.pdf", ".mdi")
        if os.path.isfile(os.path.join(path, mdi_file_name)):
            print("Removing \'" + mdi_file_name + "\'")
            os.remove(os.path.join(path, mdi_file_name))
