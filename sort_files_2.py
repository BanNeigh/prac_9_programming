import os


def main():
    sort_files = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_type = filename.split('.')[-1]
        if file_type not in sort_files:
            category = input(f"What category would you like to sort {file_type} files into? ")
            sort_files[file_type] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, f"{sort_files[file_type]}/{filename}")


main()
