'''Скрипт призначений для копіювання файлів і сортування їх за розширеннями'''
import os
import argparse
import shutil
import sys

def parse_args():
    '''Функція парсить аргументи командного рядка і вертає Namespace із ними'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-s", "--source", type=str, default=".", help="Шлях до директорії звідки копіювати")
    parser.add_argument("-d", "--dest", type=str, default="dist", help="Шлях до директорії куди копіювати")
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return parser.parse_args()

def copy_files(src: str, dest: str):
    '''
    Функція приймає два шляхи у файловій системі і копіює рекурсивно файли з одно до іншого.
    Файли у місці призначення сортуються відповідно до їх розширнння
    '''
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isdir(item_path):
            copy_files(item_path, dest)
        else:
            ext = os.path.splitext(item)[1][1:]
            if ext:
                dir_path = os.path.join(dest, ext)
                os.makedirs(dir_path, exist_ok=True)
                shutil.copy(item_path, dir_path)

def main():
    args = parse_args()
    try:
        copy_files(args.source, args.dest)
    except FileNotFoundError as e:
        print(f"Помилка: Шлях {e.filename} не існує")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")
    else:
        print(f"Файли скопійовано у призначення {args.dest}")

if __name__ == "__main__":
    main()
