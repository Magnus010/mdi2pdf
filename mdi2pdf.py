import os
from subprocess import Popen, PIPE


def mdi2tif_function(__file_name__):
    mdi2tif = "C:/Program Files (x86)/modiconv/MDI2TIF.exe"

    source_parameter = "-source"
    old_file_name = os.path.basename(__file_name__)
    dest_parameter = "-dest"
    new_file_name = os.path.basename(os.path.splitext(__file_name__)[0]) + '.tif'
    path = os.path.dirname(__file_name__)
    log_parameter = "-log"
    log_file_name = "mdi2tif.log"
    print("Converting \'" + old_file_name + "\' to \'" + new_file_name + "\'")
    output = Popen([mdi2tif, source_parameter, os.path.join(path, old_file_name), log_parameter,
                    log_file_name, dest_parameter, os.path.join(path, new_file_name)], stdout=PIPE)
    print output.stdout.read()


def tif2pdf_function(__file_name__):
    tif2pdf = "C:/Program Files/ImageMagick-7.0.6-Q16/magick.exe"

    os.chdir(os.path.dirname(tif2pdf))

    old_file_name = os.path.basename(os.path.splitext(__file_name__)[0]) + '.tif'
    new_file_name = os.path.basename(os.path.splitext(__file_name__)[0]) + '.pdf'
    path = os.path.dirname(__file_name__)
    print("Converting \'" + old_file_name + "\' to \'" + new_file_name + "\'")
    output = Popen([tif2pdf, os.path.join(path, old_file_name), os.path.join(path, new_file_name)], stdout=PIPE)
    print output.stdout.read()

if __name__ == "__main__":
    home_folder = "c:/test"
    file_list = []

    for root, dirs, files in os.walk(home_folder):
        for name in files:
            if name.endswith(".mdi"):
                file_list.append(os.path.join(root, name))

    for file_name in file_list:
        mdi2tif_function(file_name)
        tif2pdf_function(file_name)
