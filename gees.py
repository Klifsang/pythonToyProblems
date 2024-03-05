# Breakout Room 3
# Jane Rotich
# Lamech Omwega
# Sang Wicklife

# Filter out the Geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    #your code here
        # for x in geese:
        #     if x in birds:
        #         birds.remove(x)
        return [bird for bird in birds if bird not in geese]
print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))

# Reversed Words

def reverse_words(s):
    words = s.split(" ")
    # for word in words:
    #     newwords.insert(0,word)
    newwords = [word for word in reversed(words)]
    return " ".join(newwords)

reverse_words("hello all")



# Dictionary from Two Lists

def create_dict(keys, values):
    """
    Write your code here.
    """
    # result_dict = {}
    return {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}

    # Iterate through indices of keys
    # for i in range(len(keys)):
    #     # If there are corresponding values, assign them
    #     if i < len(values):
    #         result_dict[keys[i]] = values[i]
    #     # If there are additional keys without values, set their values to None
    #     else:
    #         result_dict[keys[i]] = None

    # return result_dict