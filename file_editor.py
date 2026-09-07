import os

directory_path = r"C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen\TestOrdner"

def main():

    print("starting")
    add_image_view()
    print("finished")

def add_image_view():
    for f in os.scandir(directory_path):
        if f.is_file():
            with open(f.path, "r") as file:
                file_contents = file.readlines()

            with open(f.path, "w") as file:
                for i in range(len(file_contents)):
                    if file_contents[i].strip("\n").startswith("cover: "):
                        image_str = "![[" + file_contents[i].strip("\n").strip("cover: ") + ".jpg]]\n\n"
                        file.write(file_contents[i])
                    if file_contents[i].startswith("---") and file_contents[i-1].startswith("bewertung:") and i > 0:
                        file.write(file_contents[i])
                        file.write(image_str)
            

    
    
    
    
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
                    if line.strip("\n").startswith(line_before_new_text):
                        file.write(line)
                        file.write(text_to_add)
                    else:
                        file.write(line)

def add_text_if_missing(text_before_missing, missing_text, text_to_add):
        for f in os.scandir(directory_path):
            if f.is_file():
                with open(f.path, "r") as file:
                    file_contents = file.readlines()

                with open(f.path, "w") as file:
                    for i in range(len(file_contents)):
                        if file_contents[i].strip("\n").startswith(text_before_missing) and not file_contents[i+1].startswith(missing_text):
                            file.write(file_contents[i])
                            file.write(text_to_add)
                        else:
                            file.write(file_contents[i])

main()