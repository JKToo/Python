#Name: Justin K Too
#Email: justin.too27@myhunter.cuny.edu
#This program takes userInput and replaces the verb / noun in the sentence

template = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

noun = input("")
template = template.replace("NOUN", noun)
verb1 = input("")
template = template.replace("VERB1", verb1)
verb2 = input("")
template = template.replace("VERB2", verb2)

print(template)
