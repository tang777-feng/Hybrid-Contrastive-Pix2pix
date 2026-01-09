import os
import subprocess


DATASET = "./datasets/virtual_stain"


cmd = [

    "python", "train.py",
    "--dataroot", DATASET,
    "--name", "kidney_contrastive_pix2pix",
    "--CUT_mode", "CUT",
    "--dataset_mode", "aligned", 
    "--model", "cut", 
    "--direction", "AtoB", 
    "--lambda_NCE", "1.0", 
    "--batch_size", "1",
    "--display_id", "0",
    "--n_epochs", "25",
    "--n_epochs_decay", "25",
    "--save_epoch_freq", "5",
    "--preprocess", "flip",
    "--load_size", "256",
    "--crop_size", "256",
    "--num_threads", "0",
    "--lambda_GAN", "1.0", 
    "--lambda_NCE", "1.0", 
    "--lambda_L1", "10.0",        
    "--print_freq", "1000"         
]


