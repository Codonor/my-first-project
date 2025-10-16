"""
QUESTION THREE: 
Feature Flags (App Settings) 
Scenario: Enable/disable simple app features. 


Data: 
flags = {"dark_mode": True, "notifications": False, "beta_banner": True} 


Tasks: 
a) Count how many features are enabled. 
b) Turn notifications on. 
c) List all feature names. 
"""

# Data
flags = {"dark_mode": True, "notifications": False, "beta_banner": True}
# a) Count how many features are enabled.
enabled_count = sum(flags.values())
print(f"Number of enabled features: {enabled_count}")

# b) Turn notifications on.
flags["notifications"] = True
print(f"Updated flags: {flags}")

# c) List all feature names.

def list_feature_names(data):
    feature_names = []
    for key in data:
        feature_names.append(key)
    return feature_names

print(list_feature_names(flags))

"""
QUESTION FOUR: 
Library Loans 
Scenario: Track book availability. 
Data: 
books = {"Dune": "available", "1984": "borrowed", "Neuromancer": "available"} 


Tasks: 
a) Mark "1984" as returned (now available). 
b) Count how many books are available. 
c) Get a sorted list of all book titles. 

"""
books = {"Dune": "available", "1984": "borrowed", "Neuromancer": "available"}

# a) Mark "1984" as returned (now available).

books["1984"] = "available"
print(books)

# b) Count how many books are available. 

def available_count(data):
    available_list = []
    for k, v in data.items():
        if v == "available":
            available_list.append(k)

    return available_list

print(len(available_count(books)))

#c) Get a sorted list of all book titles.

book_titles = [k for k in books]
print(book_titles)


print(sorted(book_titles))

"""
QUESTION FIVE: 
Gym Set Tracker (Basics) 
Scenario: You logged weights for a single exercise. 
Data: 
sets = [40, 42.5, 42.5, 45, 45] # kg 
Tasks: 
a) Find the heaviest set and the lightest set. 
b) Compute the average weight lifted across sets. 
"""

sets = [40, 42.5, 42.5, 45, 45] # kg 

#a) Find the heaviest set and the lightest set. 
print(f"the heaviest set was {max(sets)}kg")
print(f"the lightest set was {min(sets)}kg")

# b) Compute the average weight lifted across sets. 
print(dir(list))

def find_average(data):
    total = sum(data)
    avg = total / len(data)
    return avg
print(find_average(sets))

"""
QUESTION SIX: 
Tiny Marks Register 
Scenario: Record marks for three students. 
Data: 
marks = {"Amir": 74, "Bea": 81, "Chen": 68} 


Tasks: 
a) Compute the class average. 
b) Increase Amir’s mark by 3 bonus points and recompute average. 
c) Get the highest and lowest mark values.

"""
marks = {"Amir": 74, "Bea": 81, "Chen": 68} 

# a) Compute the class average. 

mark_values = [v for k, v in marks.items()]
print(mark_values)

avg_mark = sum(mark_values) / len(mark_values)
print(f"the average mark is {avg_mark}")

# improved, cleaner version from chatGPT

avg_mark = sum(marks.values()) / len(marks)
print(f"The average mark is {avg_mark:.2f}")

print(marks.values())

# b) Increase Amir’s mark by 3 bonus points and recompute average.

marks["Amir"] += 3
print(marks)

avg_mark = sum(marks.values()) / len(marks)
print(f"the average mark is now {avg_mark:.2f}")

# c) Get the highest and lowest mark values.

marks_values = marks.values()
print(f"the lowest mark is {min(marks_values)} and the highest mark is {max(marks_values)}")

"""
QUESTION SEVEN: 
Quick Currency Note 
Scenario: Convert a couple of GBP amounts to EUR with a fixed rate. 
Data: 
rate = 1.16 # EUR per GBP amounts_gbp = [12.50, 3.20] 

Tasks: 
a) Convert both amounts to EUR (store in a new list). 
b) Compute the total EUR across those items.
"""
rate = 1.16 # EUR per GBP amounts_gbp = [12.50, 3.20] 

#unwieldy first attempt
gbp_1250_in_eur = 12.50 * rate
print(gbp_1250_in_eur)
gbp_320_in_eur = 3.20 * rate
print(gbp_320_in_eur)

# cleaner code from chatGPT
rate = 1.16  # EUR per GBP
amounts_gbp = [12.50, 3.20]

for amount in amounts_gbp:
    amount_eur = amount * rate
    print(f"£{amount:.2f} = €{amount_eur:.2f}")

# Tasks: a) Convert both amounts to EUR (store in a new list). 

def convert_eur_list(data):
    eur_list = []
    for amount in data:
        eur_list.append(round(amount * rate, 2))
    return eur_list

amounts_eur = convert_eur_list(amounts_gbp)
print(amounts_eur)
# b) Compute the total EUR across those items.

print(sum(amounts_eur))

"""
QUESTION EIGHT: 
Email De-dupe Counter 
Scenario: You exported emails with repeats. 


Data: 
emails = ["a@x.com", "b@y.com", "a@x.com", "c@z.com", "b@y.com"] 


Tasks: 
a) Count total emails vs unique emails. 
b) Compute how many duplicates there are. 
c) Produce a sorted list of unique emails. 
"""

emails = ["a@x.com", "b@y.com", "a@x.com", "c@z.com", "b@y.com"]

# a) Count total emails vs unique emails. 
print(len(emails))
print(len(set(emails)))

# b) Compute how many duplicates there are.
print(f"there were {len(emails) - len(set(emails))} duplicates")

# c) Produce a sorted list of unique emails. 
sorted_list_non_dup = sorted(list(set(emails)))
print(sorted_list_non_dup)

"""
QUESTION TEN: 
Email Domain Counter 


Scenario: Count how many people use each email provider from a list of emails. 


Data: 
emails = ["john@gmail.com", "sarah@yahoo.com", "mike@gmail.com", "emma@outlook.com", "alex@gmail.com"] 


Tasks: 
a) Extract just the domain part (after @) from each email. 
b) Count how many times each domain appears (which data structure lets you store counts?). 
c) Which email provider is most popular? 
"""

emails = ["john@gmail.com", "sarah@yahoo.com", "mike@gmail.com", "emma@outlook.com", "alex@gmail.com"]

# a) Extract just the domain part (after @) from each email. 
# I needed some help from chatGPT on this

def domain_finder(email_list):
    domain_names = [email.split('@')[1] for email in email_list]
    return domain_names

domains_list = domain_finder(emails)
print(domains_list)
    
domain_count = {}
for domain in domains_list:
    domain_count[domain] = domain_count.get(domain, 0) + 1
print(domain_count)

# c) Which email provider is most popular?
# got help here and don't fully understand the logic. Dictionaries are difficult
most_popular = max(domain_count, key=domain_count.get)
print(most_popular)

"""
QUESTION ELEVEN: 
Recipe Ingredient Comparison 
Scenario: You want to make two recipes but see which ingredients overlap. 


Data: 
recipe1_ingredients = ["flour", "eggs", "milk", "sugar", "butter"] recipe2_ingredients = ["eggs", "milk", "cheese", "salt"] 


Tasks: 
a) Convert both lists to sets. 
b) Find ingredients that appear in both recipes. 
c) Find ingredients you need only for recipe1 (not in recipe2).
"""
    
recipe1_ingredients = ["flour", "eggs", "milk", "sugar", "butter"] 
recipe2_ingredients = ["eggs", "milk", "cheese", "salt"] 

# a)
recipe1_ingredients_set = set(recipe1_ingredients)
recipe2_ingredients_set = set(recipe2_ingredients)

#b)
print(dir(recipe1_ingredients_set))
print(recipe1_ingredients_set.intersection(recipe2_ingredients_set))

#c)
print(recipe1_ingredients_set.difference(recipe2_ingredients_set))