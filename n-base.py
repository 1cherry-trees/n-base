#https://en.wikipedia.org/wiki/Polybius_square
#https://cryptii.com/
#https://v2.cryptii.com/text/select
#http://www.unit-conversion.info/texttools/

#conversion  of custom polybious square
convertTo = {
    "A" : "11",
    "B" : "12",
    "C" : "13",
    "D" : "14",
    "E" : "15",
    "F" : "16",
    "G" : "21",
    "H" : "22",
    "I" : "23",
    "J" : "24",
    "K" : "25",
    "L" : "26",
    "M" : "31",
    "N" : "32",
    "O" : "33",
    "P" : "34",
    "Q" : "35",
    "R" : "36",
    "S" : "41",
    "T" : "42",
    "U" : "43",
    "V" : "44",
    "W" : "45",
    "X" : "46",
    "Y" : "51",
    "Z" : "52",
    "0" : "53",
    "1" : "54",
    "2" : "55",
    "3" : "56",
    "4" : "61",
    "5" : "62",
    "6" : "63",
    "7" : "64",
    "8" : "65",
    "9" : "66"
}
convertFrom = {
    '1': {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F'
    },
    '2': {
        '1': 'G',
        '2': 'H',
        '3': 'I',
        '4': 'J',
        '5': 'K',
        '6': 'L'
    },
    '3': {
        '1': 'M',
        '2': 'N',
        '3': 'O',
        '4': 'P',
        '5': 'Q',
        '6': 'R'
    },
    '4': {
        '1': 'S',
        '2': 'T',
        '3': 'U',
        '4': 'V',
        '5': 'W',
        '6': 'X'
    },
    '5': {
        '1': 'Y',
        '2': 'Z',
        '3': '0',
        '4': '1',
        '5': '2',
        '6': '3'
    },
    '5': {
        '1': '4',
        '2': '5',
        '3': '6',
        '4': '7',
        '5': '8',
        '6': '9'
    },
}
textFrom = "42-15-41-42"
textTo = "TEST"

tempvar = ""
ending_text = ""

if 0:
    for i in textTo:
        ending_text += convertTo[i.capitalize()] + "-"
    ending_text = ending_text[:-1]
else:
    tempvar = textFrom.split("-")
    for i in range(len(tempvar)):
        ending_text += convertFrom[tempvar[i][0]][tempvar[i][1]]



print(ending_text)
