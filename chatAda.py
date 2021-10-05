name = input("Wie heißt du, Bruder?\n")
print(f"{name.title()}, könnte ja besser sein...\n")
age = input("Wie alt bist du?\n")
if int(age)<20:
    print("Ooo, noch voller Kraft\n")
else:
    print("Genug\n")
question = input("Trinkst du freitags Vodka oder Bier?\n")
if question.lower() == "vodka":
    print("Klingt ernst\n")
if question.lower() == "bier":
    print("Gut\n")
if question.lower() == "beides":
    print("Ich auch!\n")
question2 = input("Könntest du mir bitte 2 Euro ausleihen?\n")
if question2.lower() == "ja":
    print("DANKE!\n")
if question2.lower() == "nein":
    print("warum\n")
prompt = "Okay, darf ich schon gehen?\n"
prompt += "\nTippe 'Ja' bitte\n"
question3 = input(prompt)
if question3.lower() == "ja":
    print("Tschüss")
if question3.lower() == "nein":
    print("warum")
