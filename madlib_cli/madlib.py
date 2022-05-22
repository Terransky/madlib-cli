
test_path = './dark_and_stormy_night_template.txt'
true_path = './make_me_a_video_game_template.txt'
new_path = './user_madlibs.txt'

print(f"""
Welcome, user.
Madlibs is a thing I'll explain in a future commit.
Use the following commands to play:
""")


def read_template(template):
    with open(template) as file:
        contents = file.read()
    return contents


results = read_template(test_path)
print(type(results), results)


def parse_template(txt):
    txt_list = txt.split()
    stripped = txt
    parts = []

    for i in txt_list:

        stripped_char = ""
        word_class = ""

        if i[0] == "{":
            for j in range(len(i)):
                stripped_char += i[j]
                if i[j] == "}":
                    break

            stripped = stripped.replace(stripped_char, "{}", 1)

            for j in range(1, len(i)-1):
                if i[j] == "}":
                    break
                word_class += i[j]

            parts.append(word_class)

    return stripped, parts


parsed_template = parse_template(results)
print(type(parsed_template[0]), parsed_template[0])
print(type(parsed_template[1]), parsed_template[1])
