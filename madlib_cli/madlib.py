
test_path = '../assets/dark_and_stormy_night_template.txt'
true_path = '../assets/make_me_a_video_game_template.txt'
new_path = '../assets/user_madlibs.txt'

print(f"""
Welcome, User.
Madlibs is a fun word where you are asked to input words of a specific word class such as an adjective or noun.
Once you've finished entering the requisite terms, a whimsical story will be presented back to you filled with
your custom input.

Please check the prompt and enter the corresponding word type.

""")


def read_template(template):
    """"This opens a text file and returns the contents as a list"""
    with open(template) as file:
        contents = file.read()
    return contents  # returns string


def parse_template(txt):
    """this strips the word classes and stores them in a global array and returns the stripped text"""
    stripped = txt  # original string from read_template()
    stripped_char = ""
    temp_list = []
    parts_list = []
    counter = 0

    for counter in range(len(txt)):

        if txt[counter] == "{":  # search for opening {
            stripped_char += txt[counter]

            while txt[counter] != "}":
                counter += 1
                stripped_char += txt[counter]  # stores string without curlies

        elif txt[counter] == "}":  # search for ending }
            stripped = stripped.replace(stripped_char, "{}", 1)  # searches for word class, replaces with {} once
            temp_list.append(stripped_char)
            stripped_char = ""

    for i in temp_list:
        word_class = ""

        for j in range(1, len(i)-1):
            word_class += i[j]  # concatenates letters of word class to rebuild string without {}

        parts_list.append(word_class)  # and saves them to this list for later reference

    return stripped, parts_list  # returns string with empty {} curly braces to fill and parts list


def user_input(parts):
    """shows user word type, asks for input and store/return the list"""
    user_list = []
    for i in parts:
        user_list.append(input(f"Dear User, please input a {i}.\n > "))

    return user_list


def merge(parsed, input_list):
    """takes the template string with empty {}, fills with values from user list, writes to file"""
    user_list = input_list
    parsed_template = parsed

    for i in user_list:
        parsed_template = parsed_template.replace("{}", i, 1)

    return parsed_template


if __name__ == "__main__":

    results = read_template(true_path)
    parsed_template = parse_template(results)
    users_input = user_input(parsed_template[1])
    merged_madlib = merge(parsed_template[0], users_input)

    print(merged_madlib)

    with open(new_path, "w") as file:
        file.write(merged_madlib)

