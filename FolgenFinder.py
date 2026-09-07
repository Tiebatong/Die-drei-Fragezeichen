import os
import Folge


directory_path = r"C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen"
#testfile_path = "C:\Users\Anwender\Documents\Obsidian Vault\Obsidian Vault\Die drei Fragezeichen\Folgen\015_und der rasende Löwe.md"


def main():
    
    print("started main")
    
    for f in os.scandir(directory_path):
        if f.is_file():
            with open(f.path, "r") as file:
                file_contents = file.readlines()

            if "Löwe" in f.name:
                print("succes")
    
                name = f.name.strip(".md")

                orte = ["x"] *10
                orte_idx = 0
                
                for i in range(len(file_contents)):
                    line = file_contents[i]
                    if line == "### Orte\n":                                                   
                        i += 1
                        line = file_contents[i]
                        while line.startswith("#") and not line.startswith("#", 1):

                            orte[orte_idx] = line.strip("#").strip("\n")
                            orte_idx += 1
                            i += 1
                            line = file_contents[i]
                            
                
                folge14 = Folge.Folge(name, orte)
                print(folge14.name)
                print(folge14.orte)
    
main()