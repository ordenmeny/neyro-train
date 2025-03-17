from ultralytics import YOLO
import torch

# Загружаем предобученную модель YOLOv8
model = YOLO("yolov8n.pt")  # nano-версия (самая лёгкая)

# Оптимальные параметры для слабого GPU
model.train(
    data=r"F:\projectNeyro\all_dataset\dataset.yaml",  # Указываем полный путь
    epochs=50,  # Можно уменьшить, если идёт слишком долго
    imgsz=320,  # Уменьшаем размер изображения (меньше VRAM)
    batch=1,  # Минимальная загрузка для слабой видеокарты
    device="cuda",  # Используем GPU (если падает - поменяй на "cpu")
    workers=0,  # Отключаем многопоточное чтение
    cache=False,  # Отключаем кэширование в RAM (не помогает на слабых GPU)
    single_cls=False,  # Если только 1 класс - ставь True
    amp=False  # Отключаем FP16
)

# Для быстрого GPU
# from ultralytics import YOLO
# import torch
#
# # Загружаем предобученную модель YOLOv8
# model = YOLO("yolov8n.pt")  # nano-версия (лёгкая и быстрая)
#
# # Оптимальные параметры для RTX 4060
# model.train(
#     data=r"F:\projectNeyro\all_dataset\dataset.yaml",  # Путь к датасету
#     epochs=50,  # Количество эпох
#     imgsz=640,  # Оптимальный размер изображений
#     batch=8,  # Можно увеличить до 16, если не вылетает по памяти
#     device="cuda",  # Используем видеокарту
#     workers=4,  # Включаем многопоточное чтение
#     cache="ram",  # Используем оперативную память для кэша (ускоряет обучение)
#     single_cls=False,  # Если только 1 класс - ставь True
#     amp=True  # Включаем FP16 для ускорения работы
# )

