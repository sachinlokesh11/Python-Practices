# Given a lists of words, print all combinations of phrases that can be formed by picking one word from each list.

# Input:
# lists =
# [
# 	['John', 'Emma'],
# 	['Plays', 'Hates', 'Watches'],
# 	['Cricket', 'Soccer', 'Chess']
# ]

# Output:
# 	'John Plays Cricket',
# 	'John Plays Soccer',
# 	'John Plays Chess',
# 	'John Hates Cricket',
# 	'John Hates Soccer',
# 	'John Hates Chess',
# 	'John Watches Cricket',
# 	'John Watches Soccer',
# 	'John Watches Chess',
# 	'Emma Plays Cricket',
# 	'Emma Plays Soccer',
# 	'Emma Plays Chess',

def find_phrases1(lists):
    phrases = [i+" "+j+" "+k for i in lists[0] for j in lists[1] for k in lists[2]]
    for sentence in phrases:
        print(sentence)


def find_phrases2(lists):
    for words in lists[0]:
        for word in lists[1]:
            for wrd in lists[2]:
                print(words+" "+word+" "+wrd+" ")


if __name__ == "__main__":
    lists = [
        ['John', 'Emma'],
        ['Plays', 'Hates', 'Watches'],
        ['Cricket', 'Soccer', 'Chess']
    ]
    flag = True
    while flag:
        choice = int(input("Select 1.Method1 2.Method2.3.Exit\nEnter your choice: "))
        match choice:
            case 1:
                find_phrases1(lists)
            case 2:
                find_phrases2(lists)
            case 3:
                flag = False
