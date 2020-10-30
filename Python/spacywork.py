import spacy
nlp = spacy.load('en_core_web_sm')


# Named entity Recognitions
text = 'Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE'
doc = nlp(text)
for X in doc.ents:
    print((X.text,X.label_))

# Extract stop words list
print([x for x in doc if not x.is_stop])

