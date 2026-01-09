import os
import subprocess

# 你的数据集路径
DATASET = "./datasets/virtual_stain"


# 构建训练命令
cmd = [

    "python", "train.py",
    "--dataroot", DATASET,
    "--name", "kidney_contrastive_pix2pix",
    "--CUT_mode", "CUT",
    "--dataset_mode", "aligned", 
    "--model", "cut", 
    "--direction", "AtoB", 
    "--lambda_NCE", "1.0", 
    "--batch_size", "4",
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
    "--lambda_L1", "10.0",         # 建议从 10.0 开始，如果颜色不准再加到 50.0
    "--print_freq", "1000"         # 每1000个batch打印一次日志
]


print("开始训练 contrastive_pix2pix 虚拟染色模型...")
subprocess.run(cmd)
print("训练完成，模型已保存在 ./checkpoints/virtual_" \
"stain_pix2pix/")

