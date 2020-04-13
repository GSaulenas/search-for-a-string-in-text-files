import argparse
from pathlib import Path
import os


def search_in_file(filename, path, relative_path, search_for):
    lines = []

    try:
        with open((path / filename), encoding="utf-8", errors='ignore') as f:
            count = 0

            for num, line in enumerate(f, 1):
                if search_for in line:
                    lines.append(num)
                    count += 1
            if count:
                print('Found in', filename, 'located', relative_path)
                print('Found at lines:', lines, '\n')

    except FileNotFoundError:
        print('File ', filename, ' was not found. Please check the filename \n')
        return
    except Exception:
        return


if __name__ == '__main__':
    files_checked = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("search_for")
    p = parser.parse_args()

    for root, subdirs, files in os.walk(p.path):
        opath_str = str(p.path)
        original_path = len(opath_str)
        current_path = len(root)
        rel_path = ''
        comp_paths = current_path - original_path

        if comp_paths:
            rel_path = root[original_path:current_path]

        for f in files:
            search_in_file(f, Path(root), rel_path, p.search_for)
            files_checked += 1

    print('Number of files that were checked', files_checked)