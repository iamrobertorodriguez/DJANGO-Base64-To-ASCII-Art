import os

def delete_temp_image(path):
    if os.path.exists(path):
        os.remove(path)