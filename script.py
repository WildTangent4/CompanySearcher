import os
import requests

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
    "Reading",
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

API_KEY = os.environ.get("GOOGLE_SEARCH_API_KEY", "set the environment variable GOOGLE_SEARCH_API_KEY to your project's API key")
search_engine_ID= "5287871e9271b4d4d"
search_region = "countryUK"
all_generated_searches = []

for field in fields:
    for location in locations:
        for search_term in search_terms:
            all_generated_searches.append(
                field + " " + search_term + " in " + location
            )

cached_results = []



start = int(input("start from search number: "))-1

search_by_region = input("type y to search only for UK based sites (NOTE: reduces search quality, better at finding SMEs): ").lower()=="y"
if search_by_region:
    region = "&cr=" + search_region
else:
    region = ""

for i in range(start,len(all_generated_searches)):
    print("\n")
    search = all_generated_searches[i]
    print(search)
    response = requests.get("https://customsearch.googleapis.com/customsearch/v1?key="
                            +API_KEY
                            +"&cx="+search_engine_ID
                            +region
                            +"&q="+search
                            ).json()
    num_excluded = 0
    for item in response["items"]:
        if item["link"] not in cached_results:#dont bother outputting websites I have already seen this session
            cached_results.append(item["link"])
            print(item["title"])
            print(item["link"])
        else:
            num_excluded+=1
    if num_excluded>0:
        print("\nexcluded", str(num_excluded), " duplicates")

    input("end of search " + str(i+1) + ", press enter for next search")