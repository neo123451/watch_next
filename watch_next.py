import spacy
nlp = spacy.load('en_core_web_md')

mt_lists = []
with open("movies.txt","r+") as file:
    for lines in file.readlines():
        mt_lists.append(lines)
    print(mt_lists)


def decrip(description):

    send_lists = []
    model_sentence = nlp(description)
    for sentence in mt_lists:
        similarity = nlp(sentence).similarity(model_sentence)
        send_lists.append(similarity)
        print(sentence + "-", similarity)
        print(f"This movie has the highest similarity: {max(send_lists)}\n")


    return model_sentence
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for 
            Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live
            in peace.Unfortunately, Hulk land on the planet sakaar where he is sold into slavery and trained as a gladiator."""

result = decrip(description)





