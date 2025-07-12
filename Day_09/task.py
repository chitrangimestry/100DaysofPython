programming_dictionary = {"bug": "An Error that prevents programs from running.",
                          "function": "A block of code that you can run over and over again",
                          "loop": "An action of doing something over and over again"
                         }

print(programming_dictionary["bug"])

programming_dictionary["middleware"] = "A function written to provide security layer before accessing any route."

print(programming_dictionary)

#loop
for key in programming_dictionary:
    print(key)
    print(key + ": " + programming_dictionary[key])