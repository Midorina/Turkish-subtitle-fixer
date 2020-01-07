import os

replacements = {
    "Ý": "İ",
    "ý": "ı",

    "ð": "ğ",
    "Ð": "Ğ",

    "þ": "ş",
    "Þ": "Ş"
}

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for file in files:
    print(file)
    if not file.endswith(".srt"):
        files.remove(file)
        print(f"removed {file}")

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
