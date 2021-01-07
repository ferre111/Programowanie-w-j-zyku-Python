import numpy as np

file_names = ["przykladowy_tekst_1.txt", "przykladowy_tekst_2.txt", "przykladowy_tekst_4.txt"]
words = {
    "i": "oraz",
    "oraz": "i",
    "nigdy": "prawie nigdy",
}

for file_name in file_names:
    new_text = []
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            new_line = []
            line = line.split()
            for word in line:
                word = " " + word + " "
                new_line.append(word)
            line = new_line

            flag_tab = np.zeros((len(line),), dtype=int)
            i = 0
            for lword in line:
                for word in words:
                    tmp_lword = lword
                    if flag_tab[i] == 0:
                        tmp_lword = tmp_lword.replace(" " + word + " ", " " + words[word])
                        tmp_lword = tmp_lword.replace(" " + word + ",", " " + words[word] + ",")
                        tmp_lword = tmp_lword.replace(" " + word + ".", " " + words[word] + ".")

                    if tmp_lword != lword:
                        flag_tab[i] = 1

                    lword = tmp_lword
                i = i + 1
                new_text.append(lword)
            new_text.append("\n")
        new_text = "".join(new_text)

    with open(file_name, 'w', encoding='utf8') as file:
        file.write(new_text)
