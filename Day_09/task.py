programming_dictionary = {"bug": "An Error that prevents programs from running.",
                          "function": "A block of code that you can run over and over again",
                          "loop": "An action of doing something over and over again"
                         }

# print(programming_dictionary["bug"])

programming_dictionary["middleware"] = "A function written to provide security layer before accessing any route."

# print(programming_dictionary)

#loop
# for key in programming_dictionary:
#     print(key)
#     print(key + ": " + programming_dictionary[key])


capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm"
}

# travel_log = {
#     "France": ["Île-de-France", "Notre-Dame", "Louvre", "Basillique du Sacre-Cœour de Montmartre"],
#     "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt am Main", "Stuttgrat"]
# }

# print(travel_log["Germany"][1])

nested_list =["A", "B", ["C", "D"]];
print(nested_list[2][0])

travel_log = {
    "France": {
        "num_times_visited" : 8,
        "cities_visited" : ["Île-de-France", "Notre-Dame", "Louvre", "Basillique du Sacre-Cœour de Montmartre"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited" : ["Berlin", "Munich", "Hamburg", "Frankfurt am Main", "Stuttgrat"]
    },
}

print(travel_log["Germany"]["cities_visited"][4])