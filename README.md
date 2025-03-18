1) Создать и активировать виртуальное окружение python (Python 3.10.4).
2) pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
3) pip install ultralytics
4) Файл train.py и all_dataset/dataset.yaml:
   Заменить полный путь на актуальный.
5) Файл train.py: раскомментировать "Оптимальные параметры для RTX 4060"
6) Файл check.py:
   Правильный вывод:
   <x.x.x>+cu118
   <x.x.x>+cu118
   True
7) Запустить файл train.py
8) Нейронка будет сохранена по пути, который будет указан в терминале.
9) best.pt - обученная нейросеть по датасету (на слабом GPU)
