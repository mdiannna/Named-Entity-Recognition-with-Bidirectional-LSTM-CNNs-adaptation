from ner import Parser

p = Parser()

p.load_models("models/")

# TODO: train the NN on other with -O- label
print(p.predict("Steve Went to Paris"))
print(p.predict("email@test.con"))


print(p.predict("tammiecrawford@davis.info "))
print(p.predict("001-867-476-3479" ))
# print(p.predict("1352 Emily Rest Apt. 617, Richardsside, NV 61791" ))
print(p.predict("kyle18@henderson.com "))
print(p.predict("+1-158-972-3283x792 "))
print(p.predict("+1-158-972-3283x792 "))
print(p.predict("USNS Foley, FPO AA 00997 "))
print(p.predict("allenrodney@mcdonald.com "))
print(p.predict("+1-527-999-8972" ))
# print(p.predict("91562 Julie Extension Apt. 085, Heathview, IN 71341"))
print(p.predict("wchan@gmail.com"))

print(p.predict("+41 31 370 85 85"))
print(p.predict("+41 31 370 85 82"))
