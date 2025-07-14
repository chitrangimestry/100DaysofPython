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


captials = {
    "France" : "Paris",
    "Germany" : "Berlin",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm"
}

travel_log = {
    "France": ["Île-de-France", "Notre-Dame", "Louvre", "Basillique du Sacre-Cœour de Montmartre"],
    "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt am Main", "Stuttgrat"]
}