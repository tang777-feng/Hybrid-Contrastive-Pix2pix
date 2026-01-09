import os
import subprocess


DATASET = "./datasets/virtual_stain"
EXPERIMENT_NAME = "kidney_contrastive_pix2pix"

cmd = [
    "python", "test.py",
    "--dataroot", DATASET,
    "--name", EXPERIMENT_NAME,
    "--model", "cut",
    "--dataset_mode", "unaligned", 
    "--serial_batches",  
    "--load_size", "1024",
    "--crop_size", "1024",
    "--preprocess", "none",    
    "--num_test", "9999999",
    "--eval"
]

