import json


def add_word(word, container):
    with open("WordsAsLetters.json", "r") as jf:  # read only
        data = json.loads(jf.read())  # fetches text from JSON file and applies it to a variable
    jf.close()  # close document from read only

    if word not in data["words"][container]:  # edit datapoint
        data["words"][container].append(word)
        print(f"The word '{word}' was added to {container}")
    else:
        return print(f"The word '{word}' is already in {container}.")

    with open("WordsAsLetters.json", "w") as jf:  # write
        return json.dump(data, jf, indent=4)  # dumps entire file back in with edited datapoint


def delete_word(word, container):
    with open("WordsAsLetters.json", "r") as jf:
        data = json.loads(jf.read())
    jf.close()
    if word in data["words"][container]:
        data["words"][container].remove(word)
        print(f"The word '{word}' was deleted from {container}")
    else:
        return print(f"The word '{word}' is not in {container}.")

    with open("WordsAsLetters.json", "w") as jf:
        return json.dump(data, jf, indent=4)
