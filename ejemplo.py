Import spacy
#carga el modulo pequeño en español 
Nlp = spacy.load(“es_core_newa_sm”)
#procesa un texto
Doc = nlp(“ella comio pizza”)
#itera sobre los tokens
For token in doc:
#imprime en pantalla el texto y part-of-speech tag predicho
Print(token.text, token.pos_:)
