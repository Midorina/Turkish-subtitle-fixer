import os

replacements = {
    "Ý": "İ",
    "ý": "ı",

    "ð": "ğ",
    "Ð": "Ğ",

    "þ": "ş",
    "Þ": "Ş"
}

allowed_file_formats = ("srt", "sub", "sbv", "ass")

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for file in files:
    file_format = file.split(".")[-1]
    if file_format not in allowed_file_formats:
        files.remove(file)
        print(f"removed {file} from the file list that will be processed.")

for f in files:
    print(f"opening file {f}")
    with open(f, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        for replacement in replacements:
            if replacement in lines[i]:
                print(f"changed {replacement} with {replacements[replacement]} in file {f} at line {i+1}")
                lines[i] = lines[i].replace(replacement, replacements[replacement])

    with open(f, "w", encoding="utf-8") as file:
        file.writelines(lines)

print("Done.")
