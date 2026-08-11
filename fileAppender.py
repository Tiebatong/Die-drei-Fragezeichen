import os

directory_path = r"C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen\TestOrdner"

for f in os.scandir(directory_path):
    if f.is_file():
        with open(f.path, "r") as file:
            file_contents = file.readlines()

        with open(f.path, "w") as file:
            for line in file_contents:
                if line.strip("\n") != "TESTTESTTEST":
                    file.write(line)
