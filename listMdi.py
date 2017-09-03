import os

if __name__ == "__main__":
    home_folder = os.getcwd()
    file_list = []

    for root, dirs, files in os.walk(home_folder):
        for name in files:
            if name.endswith(".mdi"):
                file_list.append(os.path.join(root, name))

    for file_name in file_list:
        print(file_name)
