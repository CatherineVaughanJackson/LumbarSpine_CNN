import os
import shutil
import random
import numpy as np

main_path=r"C:\Users\cathe\Documents\Deep learning\Label_Images"


def shuffle_filnames(main_folder_path, secondary_folder_path):

    file_path = os.path.join(main_path, main_folder_path)
    in_file_path = os.path.join(file_path, secondary_folder_path)

    filename_IDs = os.listdir(in_file_path)
    random.shuffle(filename_IDs)

    return filename_IDs

All_Healthy_comb = shuffle_filnames("Combined_D4_D5", "Healthy_Images")
All_Unhealthy_comb = shuffle_filnames("Combined_D4_D5", "Unhealthy_Images")
D4_Healthy_comb = shuffle_filnames("Disc_4", "Healthy_D4")
D4_Unhealthy_comb = shuffle_filnames("Disc_4", "Unhealthy_D4")
D5_Healthy_comb = shuffle_filnames("Disc_5", "Healthy_D5")
D5_Unhealthy_comb = shuffle_filnames("Disc_5", "Unhealthy_D5")



def move_files(ID_list, main_folder_name, secondary_folder_name, train_folder_name, test_folder_name, out_folder_cond):

    folder_length = len(ID_list)
    train_length = np.floor(folder_length*0.8)

    main_file_path = os.path.join(main_path, main_folder_name)
    in_file_path = os.path.join(main_file_path, secondary_folder_name)

    if out_folder_cond == "Healthy":
        train_name = "Healthy Train"
        test_name = "Healthy Test"
    elif out_folder_cond == "Unhealthy":
        train_name = "Unhealthy Train"
        test_name = "Unhealthy Test"

    #train
    for filename in ID_list[0:int(train_length)]:

        in_path = os.path.join(in_file_path, filename)
        #print(in_path)

        out_path = os.path.join(main_file_path, train_folder_name)
        out_path = os.path.join(out_path, train_name)
        out_path = os.path.join(out_path, filename)
        try:
            shutil.move(in_path, out_path)
        except:
            print("image", filename, "doesn't exist")

    #test
    for filename in ID_list[int(train_length):]:

        in_path = os.path.join(in_file_path, filename)

        out_path = os.path.join(main_file_path, test_folder_name)
        out_path = os.path.join(out_path, test_name)
        out_path = os.path.join(out_path, filename)
        #print(out_path)
        try:
            shutil.move(in_path, out_path)
        except:
            print("image", filename, "doesn't exist")

#organise combined files
move_files(All_Healthy_comb, "Combined_D4_D5", "Healthy_Images", "Train", "Test", "Healthy")
move_files(All_Unhealthy_comb, "Combined_D4_D5", "Unhealthy_Images", "Train", "Test", "Unhealthy")

#organise D4 files
move_files(D4_Healthy_comb, "Disc_4", "Healthy_D4", "Train_D4", "Test_D4", "Healthy")
move_files(D4_Unhealthy_comb, "Disc_4", "Unhealthy_D4", "Train_D4", "Test_D4", "Unhealthy")

#organise D5 files
move_files(D5_Healthy_comb, "Disc_5", "Healthy_D5", "Train_D5", "Test_D5", "Healthy")
move_files(D5_Unhealthy_comb, "Disc_5", "Unhealthy_D5", "Train_D5", "Test_D5", "Unhealthy")