# LumbarSpine_CNN
CNN model to classify disc herniation of the lumbar spine.

Dataset Cited from Sudirman, Sud; Al Kafri, Ala; natalia, friska; Meidia, Hira; Afriliana, Nunik; Al-Rashdan, Wasfi; Bashtawi, Mohammad; Al-Jumaily, Mohammed (2019), 
“Label Image Ground Truth Data for Lumbar Spine MRI Dataset”, Mendeley Data, V2, doi: 10.17632/zbf6b4pttk.2

LumbarSpine_CNN
|
|___ File_Categorisation
|      |___ Split D3_D4_D5.py
|      |___ Split_test_train.py
|      |___ categorise_files.py
|
|___ final_mri_classification.ipynb


File in the folder File_Categorisation refer to the process of moving image files into appropriate folders determined by whether images present hernation and 
what disc space the image is take from 

If you wish to use GPU configuration GPU used Tesla P100-PCIE-16GB
To configure GPU inside Juypter Notebook you will need: 

NVIDIA driver 
Visual Studio 2019, Microsoft visual C++
CUDA : 11.2
CuDNN : 8.1.0
Python : 3.8
Anaconda :4.13.0
Juypter Notebook :6.4.5

Module installation : 

Tensorflow : 2.80
pandas : 1.3.4 
numpy : 1.20.3

other modules (random, os, matplotlib, seaborn, sklearn)
