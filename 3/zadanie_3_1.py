file_names = ["przykladowy_tekst_1.txt", "przykladowy_tekst_2.txt", "przykladowy_tekst_3.txt"]
words = ["się", "i", "oraz", "nigdy", "dlaczego"]

for file_name in file_names:
    new_text = []
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            for word in words:
                line = line.replace(" " + word + " ", " ")
                line = line.replace(" " + word + ",", ", ")
                line = line.replace(" " + word + ".", ". ")
            new_text.append(line)

    new_text = ''.join(new_text)
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(new_text)
