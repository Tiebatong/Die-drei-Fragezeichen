import os

directory_path = r"C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen\TestOrdner"

def main():

    print("==============================")
    add_text_inbetween("### Personen\n","### Orte")
    print("==============================")

def delete_text(text_to_delete):
    for f in os.scandir(directory_path):
        if f.is_file():
            with open(f.path, "r") as file:
                file_contents = file.readlines()

            with open(f.path, "w") as file:
                for line in file_contents:
                    if line.strip("\n") != text_to_delete:
                        file.write(line)

def add_text_inbetween(text_to_add, line_before_new_text):
    for f in os.scandir(directory_path):
        if f.is_file():
            with open(f.path, "r") as file:
                file_contents = file.readlines()

            with open(f.path, "w") as file:
                for line in file_contents:
                    if line.strip("\n") == line_before_new_text:
                        file.write(line)
                        file.write(text_to_add)
                    else:
                        file.write(line)

main()