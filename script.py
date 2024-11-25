fields = [
    "Cyber security",
    "Science",
    "Engineering",
    "Infrastructure",
    "Software",
    "Energy",
    "Banking",
    "Games"
]

#note: since I am targeting SMEs which may not have good SEO, im using small regions
locations = [
    "North London",
    "London",
    "Midlands",
    "Nottingham",
    "Sheffield",
    "Leicester",
    "Exeter",
    "Manchester",
    "Liverpool",
    "Stockport",
    "Devon",
    "Didcot",
    "Cheltenham",
    "Gloucestershire",
    "UK" #might catch companies the smaller regions cant

]

search_terms = [
    "Start up",
    "Consultancy",
    "Goverment body",
    "Agency",
    "SME",
    "Company"
]

all_generated_searches = []

for field in fields:
    for location in locations:
        for search_term in search_terms:
            all_generated_searches.append(
                field + " " + search_term + " in " + location
            )


for search in all_generated_searches:
    print(search)