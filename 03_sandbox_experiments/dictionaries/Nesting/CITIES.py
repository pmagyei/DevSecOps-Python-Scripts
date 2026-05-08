

cities = {
    'London': { 'country': 'United Kingdon',
                'population': 'Over 10 million',
                'fact': 'GB left the EU in 2016',
    },
    'Roma': { 'country': 'Italy',
                'population': 'Unknown',
                'fact': 'Julius Caesar used to rule over Rome',
    },
    'Madrid':{ 'country': 'Spain',
               'population': 'I dont know',
               'fact': 'Spanish is the predominant language'
   },
}

for city, info in cities.items():
    print(f"\n{city}")

    country_info = f"{info['country']}'s population: {info['population']}"
    facts = info['fact']

    print(country_info)
    print(f"Interesting fact: {facts}")