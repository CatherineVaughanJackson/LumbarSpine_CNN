import shutil
import os
import pandas as pd

main_path = r"C:\Users\cathe\Documents\Deep learning\Label_Images"
data = pd.read_csv("Radiologists Report.xlsx - Sheet1.csv")
#print(data.head())

print(data.columns)

#print(data['L4-L5'].isin(["1"]))
data.dropna(subset=['L4-L5'], inplace=True)
data.dropna(subset=['L5-S1'], inplace=True)
data = data.astype({"L4-L5": str})
data = data.astype({"L5-S1": str})

healthy_D4 = []
unhealthy_D4 = []
healthy_D5 = []
unhealthy_D5 = []

for index, row in data.iterrows():
    if "1" in row["L4-L5"]:
        #print(row['Patient ID'], row['L4-L5'])
        unhealthy_D4.append(row['Patient ID'])
        if "1" in row["L5-S1"]:
            unhealthy_D5.append(row['Patient ID'])
        elif "0" in row["L5-S1"]:
                healthy_D5.append(row['Patient ID'])
    elif "0" in row["L4-L5"]:
        #print(row['Patient ID'], row['L4-L5'])
        healthy_D4.append(row['Patient ID'])
        if "1" in row["L5-S1"]:
            unhealthy_D5.append(row['Patient ID'])
        elif "0" in row["L5-S1"]:
            healthy_D5.append(row['Patient ID'])


healthy_D4_filename = []
unhealthy_D4_filename = []
healthy_D5_filename = []
unhealthy_D5_filename = []

def create_filename(file, file_extention, new_list):
    for number in file:
        num = str(number).zfill(4)
        filename = "L1_" + num + file_extention
        new_list.append(filename)

create_filename(healthy_D4, "_D4.png", healthy_D4_filename)
create_filename(unhealthy_D4, "_D4.png", unhealthy_D4_filename)
create_filename(healthy_D5, "_D5.png", healthy_D5_filename)
create_filename(unhealthy_D5, "_D5.png", unhealthy_D5_filename)

def file_move(filename_list, start_folder, new_folder):

    for filename in filename_list:

        folder_path = os.path.join(main_path, start_folder)
        in_path = os.path.join(folder_path, filename)
        #print(in_path)
        out_folder_path =os.path.join(folder_path, new_folder)
        out_path = os.path.join(out_folder_path, filename)
        #print(out_path)
        try:
            shutil.move(in_path, out_path)
        except:
            print("image", filename, "doesn't exist")

file_move(healthy_D4_filename, "Disc_4", "Healthy_D4")
file_move(unhealthy_D4_filename, "Disc_4", "Unhealthy_D4")
file_move(healthy_D5_filename, "Disc_5", "Healthy_D5")
file_move(unhealthy_D5_filename, "Disc_5", "Unhealthy_D5")
