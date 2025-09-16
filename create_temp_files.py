import os

for root, dirs, files in os.walk("."):
    for d in dirs:
        folder_path = os.path.join(root, d)
        temp_file = os.path.join(folder_path, "temp_file.txt")
        if not os.path.exists(temp_file):
            with open(temp_file, "w") as f:
                f.write("placeholder")