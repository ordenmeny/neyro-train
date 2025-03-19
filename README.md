1) Создать и активировать виртуальное окружение python (Python 3.10.4). py -3.9 -m venv venv
2) .\venv\Scripts\activate
3) pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
4) pip install ultralytics
5) Файл train.py и all_dataset/dataset.yaml:
   Заменить полный путь на актуальный.
6) Файл train.py: раскомментировать "Оптимальные параметры для RTX 4060"
7) Файл check.py:
   Правильный вывод:
   <x.x.x>+cu118
   <x.x.x>+cu118
   True
8) Запустить файл train.py
9) Нейронка будет сохранена по пути, который будет указан в терминале.
10) best.pt - обученная нейросеть по датасету (на слабом GPU)
