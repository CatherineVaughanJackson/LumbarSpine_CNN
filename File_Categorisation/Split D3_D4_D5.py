import os
import shutil

path = r"C:\Users\cathe\Documents\Deep learning\Label_Images"
dir_list = os.listdir(path)

print("files in", path, ":")
print(dir_list)

D3_files = []
D4_files = []
D5_files = []

for filename in dir_list:
    if "D3" in filename:
        D3_files.append(filename)
    elif "D4" in filename:
        D4_files.append(filename)
    elif "D5" in filename:
        D5_files.append(filename)


def move_file(Disc_files, folder_name):

    for filename in Disc_files:
        in_path = os.path.join(path, filename)
        #print(in_path)
        out_dir = os.path.join(path, folder_name)
        out_path = os.path.join(out_dir, filename)
        #print(out_path)
        shutil.move(in_path, out_path)

move_file(D3_files, "Disc_3")
move_file(D4_files, "Disc_4")
move_file(D5_files, "Disc_5")