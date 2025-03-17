import torch
import torchvision

print(torch.__version__)

print(torchvision.__version__)

print(torch.cuda.is_available())  # True

# import os
# print(os.path.exists(r"F:\projectNeyro\all_dataset\dataset.yaml"))  # Должно быть True
# print(os.path.exists(r"F:\projectNeyro\all_dataset\train\images"))  # Должно быть True
# print(os.path.exists(r"F:\projectNeyro\all_dataset\train\labels"))  # Должно быть True
