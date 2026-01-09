import os
import subprocess

# 数据集路径
DATASET = "./datasets/virtual_stain"
# 你的实验名称 (必须与 checkpoints 下的文件夹一致)
EXPERIMENT_NAME = "kidney_contrastive_pix2pix"

cmd = [
    "python", "test.py",
    "--dataroot", DATASET,
    "--name", EXPERIMENT_NAME,
    "--model", "cut",
    
    # --- ✅ 关键修改在这里 ---
    # 改为 unaligned，它会自动加载 testA 和 testB
    "--dataset_mode", "unaligned", 
    
    # 强制不打乱顺序，按文件名排序读取 (对后期拼接很重要)
    "--serial_batches",  
    
    # 尺寸设置 (与你切片时的 1024 保持一致)
    "--load_size", "1024",
    "--crop_size", "1024",
    "--preprocess", "none",
    
    # 测试数量 (设大一点以覆盖所有切片)
    "--num_test", "50000",
    
    # 确保进入评估模式
    "--eval"
]

print(f"🚀 开始测试模型 (使用 unaligned 模式读取双域数据)...")
subprocess.run(cmd)
print(f"✅ 测试完成！请查看 ./results/{EXPERIMENT_NAME}/test_latest/images/")