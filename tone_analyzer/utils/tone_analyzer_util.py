from utils.pinyin_utils import (
    chars_to_pinyin,
    char_to_pinyin
)

from utils.table_generator import generate

def create_table(line_endings_by_verse):
    #print(line_endings)
    rows = []
    totals = dict.fromkeys(['1', '2', '3', '4', 'Neutral 1', 'Neutral 2', 'English', 'Falling Contours', 'Total'], 0)
    for line_endings_this_verse in line_endings_by_verse:
        table = dict.fromkeys(['1', '2', '3', '4', 'Neutral 1', 'Neutral 2', 'English', 'Falling Contours', 'Total'], 0)
        for char in line_endings_this_verse:
            if char[-1].isdigit():
                table[char[-1]] += 1
                totals[char[-1]] += 1
            # jank english detection
            elif len(char) > 6:
                table['English'] += 1
                totals['English'] += 1
            else:
                table['Neutral 1'] += 1
                totals['Neutral 1'] += 1
        table['Falling Contours'] = table['3'] + table['4'] + table['Neutral 1'] + table['English']
        table['Total'] = len(line_endings_this_verse)
        totals['Total'] += len(line_endings_this_verse)
        rows.append(table)
    totals['Falling Contours'] = totals['3'] + totals['4'] + totals['Neutral 1'] + totals['English']
    rows.append(totals)
    # make percents
    percents = dict.fromkeys(['1', '2', '3', '4', 'Neutral 1', 'Neutral 2', 'English', 'Falling Contours', 'Total'], 0)
    for key, value in totals.items():
        percents[key] = value / totals['Total']
    rows.append(percents)
    return rows

def separate_verses(lyrics):
    def find_chorus(lines):
        # for each line
        # look for any matches in the remaining lines
        # write down the line number of every "base"
        # if there's no matches, we're done
        # else, for each base
        # extend by 1 line, then look for matches
        # the longest match is our chorus

        done = False
        while not done:
            done = True
            matches = []
            for i in range(len(lines)):
                base = lines[i]
                for j in range(i + 1, len(lines)):
                    if base == lines[j] and base not in matches:
                        #match found
                        print(base)
                        print(lines[j])
                        done = False
                        matches.append(i)
            length = 2
            change_made = True
            print(matches)
            while(len(matches) > 1 and change_made):
                change_made = False
                new_matches = []
                for line_num in matches:
                    to_match = lines[line_num:line_num + length]
                    for i in range(line_num + length, len(lines), length):
                        if to_match == lines[i:i + length]:
                            print(to_match)
                            print(lines[i:i + length])
                            new_matches.append(line_num)
                            change_made = True
                matches = new_matches
                length += 1
            return (matches[i], length)
                  
    verses = []
    lines = lyrics.splitlines()

    start, length = find_chorus(lines)
    for i in range(start, start + length):
        print(lines[i])

    # for line in lines:

    #     print(line)
    return verses

def load_and_convert():
    curPinyin = []
    line_endings_by_verse = []
    # generate("", [])
    print("Input number of verses:")
    num_verses = int(input())
    for i in range(num_verses):
        line_endings_this_verse = []
        print("Enter lyrics for verse" + str(i+1) + ", and 'Next' when done:")
        # take lines until the user says 'Next'
        # that makes 1 verse
        user_input = input()
        while user_input != "Next":
            # need way to find english words
            cleaned_input = filter_chinese_specific_punctuation(user_input)
            pinyin = chars_to_pinyin(cleaned_input, 2, as_list=True)
            curPinyin += pinyin
            if pinyin:
                line_endings_this_verse.append(pinyin[-1])
            user_input = input()
        # print("hi")
        line_endings_by_verse.append(line_endings_this_verse)
        # print(line_endings_by_verse)

    print("Enter lyrics for chorus/hook, and Analyze when done:")
    user_input = input()
    line_endings_this_verse = []
    while user_input[:7] != "Analyze":
        # need way to find english words
        cleaned_input = filter_chinese_specific_punctuation(user_input)
        pinyin = chars_to_pinyin(cleaned_input, 2, as_list=True)
        curPinyin += pinyin
        if pinyin:
            line_endings_this_verse.append(pinyin[-1])
        user_input = input()
    line_endings_by_verse.append(line_endings_this_verse)
    # print(line_endings_by_verse)
    params = user_input[8:]
    # print(create_table(line_endings))
    table = create_table(line_endings_by_verse)
    col_heads = ['1', '2', '3', '4', 'Neutral 1', 'Neutral 2', 'English', 'Falling Contours', 'Total']
    data = [
        col_heads
    ]
    for i in range(len(table)):
        new_row = list(table[i].values())
        print(new_row)
        # print(new_row)
        if i + 1 == len(table):
            new_row = ["Percentages"] + new_row
        elif i + 2 == len(table):
            new_row = ["Total"] + new_row
        elif i + 3 == len(table):
            new_row = ["Hook"] + new_row
        else:
            name = "Verse " + str((i+1))
            new_row = [name] + new_row
        data.append(new_row)
        # for (key, value) in row.items():
        #     row.append(value)
        # data.append(row)
    
    generate(params, data)

    # while True:
    #     try:
    #         user_input = input()
    #         if user_input[:7] == "Analyze":
    #             params = user_input[8:]
    #             # print(create_table(line_endings))
    #             table = create_table(line_endings)
    #             col_heads = []
    #             row = ["Count"]
    #             for (key, value) in table.items():
    #                 col_heads.append(key)
    #                 row.append(value)
    #             data = [
    #                 col_heads,
    #                 row
    #             ]
    #             generate(params, data)
    #         else:
    #             cleaned_input = filter_chinese_specific_punctuation(user_input)
    #             pinyin = chars_to_pinyin(cleaned_input, 2, as_list=True)
    #             curPinyin += pinyin
    #             if pinyin:
    #                 line_endings.append(pinyin[-1])
    #             # print(curPinyin)
    #             # print(line_endings)
    #     except EOFError:
    #         break