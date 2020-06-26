from ner import Parser

p = Parser()

p.load_models("models/")

print(p.predict("Steve Went to Paris"))