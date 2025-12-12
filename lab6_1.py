import os
import json
import logging

class FileNotFound(Exception):
    pass

class FileCorrupted(Exception):
    pass

def logged(exception_type, mode="console"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e: 
                logger = logging.getLogger(func.__name__)
                logger.setLevel(logging.ERROR)
                if mode == "console":
                    handler = logging.StreamHandler()
                else:
                    handler = logging.FileHandler("events_log.txt", mode="a", encoding="utf-8")
                handler.setLevel(logging.ERROR)
                handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
                logger.addHandler(handler)
                logger.error(f"{type(e).__name__}: {str(e)}")
                logger.removeHandler(handler)
                raise e 
        return wrapper
    return decorator

class FileWorker: 

    @logged(FileNotFound, mode="file") 
    def __init__(self, file_path): 
        self.file_path = file_path 
        if not os.path.exists(self.file_path): 
            raise FileNotFound("Файл не існує!")

    @logged(FileCorrupted, mode="file") 
    def read(self): 
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file) 
        except Exception:
            raise FileCorrupted("Помилка читання JSON-файлу!")

    @logged(FileCorrupted, mode="file")
    def write(self, data):
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception:
            raise FileCorrupted("Помилка запису у JSON-файл!")

    @logged(FileCorrupted, mode="file")
    def append(self, data): 
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = json.load(file)
            if isinstance(content, list): 
                content.append(data) 
            else:
                content.update(data) 
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(content, file, ensure_ascii=False, indent=4)
        except Exception:
            raise FileCorrupted("Помилка дозапису у JSON-файл!")
        
if __name__ == "__main__":
    worker = FileWorker("data.json")

    print("Поточний JSON:")
    print(worker.read())

    worker.append({"newKey": "newValue"}) 

    print("Після допису:")
    print(worker.read())

    worker.write({"reset": True})

    print("Після повного перезапису:")
    print(worker.read())
