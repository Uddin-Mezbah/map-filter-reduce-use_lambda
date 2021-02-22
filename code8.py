#'''''''''''''without lambda''''''''''
'''def start_with_A(s):
    return s[0] == "A"

fruit = ["Apple","Banana","Pear","Apricot","Orange"]
filter_object = filter(start_with_A, fruit)

print(list(filter_object))'''

#'''''''''''with lambda''''''''''''

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))

