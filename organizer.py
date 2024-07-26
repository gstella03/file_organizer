import os
import shutil
import logging
from datetime import datetime

def organize_files(directory, method):
    if not os.path.isdir(directory):
        raise ValueError("La directory non esiste.")
    if method == 'Extension':
        organize_by_extension(directory)
    elif method == 'Date':
        organize_by_date(directory)
    elif method == 'Size':
        organize_by_size(directory)

def organize_by_extension(directory):
    try:
        list_file = os.listdir(directory)
        for file_name in list_file:
            file_path = os.path.join(directory,file_name)
            if os.path.isfile(file_path):
                extension = file_name.split('.')[-1]
                target_dir = os.path.join(directory, extension)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.move(file_path, target_dir)
                logging.debug(f"Moved file {file_name} to {target_dir}")
    except Exception as e:
        logging.error(f"Error organizing by extension: {e}")
        raise ValueError(f"Error organizing by extension: {e}")

def organize_by_date(directory):
    try:
        list_file = os.listdir(directory)
        for file_name in list_file:
            file_path = os.path.join(directory,file_name)
            if os.path.isfile(file_path):
                file_time = os.path.getctime(file_path)
                date = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d')
                target_dir = os.path.join(directory, date)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.move(file_path, target_dir)
                logging.debug(f"Moved file {file_name} to {target_dir}")
    except Exception as e:
        logging.error(f"Error organizing by date: {e}")
        raise ValueError(f"Error organizing by date: {e}")



def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size} {unit}"
        size //= 1024

def organize_by_size(directory):
    try:
        list_file = os.listdir(directory)
        for file_name in list_file:
            file_path = os.path.join(directory,file_name)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                str_file_size=format_size(file_size)
                target_dir = os.path.join(directory, str_file_size)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.move(file_path, target_dir)
                logging.debug(f"Moved file {file_name} to {target_dir}")
    except Exception as e:
        logging.error(f"Error organizing by size: {e}")
        raise ValueError(f"Error organizing by size: {e}")