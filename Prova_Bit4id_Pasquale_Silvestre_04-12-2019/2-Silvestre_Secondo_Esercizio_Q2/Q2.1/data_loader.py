from Country import Country

filename1 = 'countries.txt'
with open(filename1, mode='r') as fileToRead:
    listCountries = fileToRead.readlines()

print(listCountries)
listCountriesObject = []

for country in listCountries:
    country.strip()
    print(country)
    countrySplit = country.split(sep=";")
    print(countrySplit)
    countryNow = Country(countrySplit[0], int(countrySplit[1]), float(countrySplit[2]), countrySplit[3], countrySplit[4].strip())
    listCountriesObject.append(countryNow)

for country in listCountriesObject:
    print(country)

print("------------------------------------------")
print("AVVIO QUERY COMMISSIONATE:\n")

def stampaNazioneEstesa():
    "Query per la stampa del territorio con superficie più estesa."
    print("Nazione con superficie più estesa:")
    nationExt = listCountriesObject[0]
    for nation in listCountriesObject[1:]:
        if nationExt.surface < nation.surface:
            nationExt = nation
    print(f"Nazione più estesa: {nationExt} con superficie pari a: {nationExt.surface}.")

stampaNazioneEstesa()                # USA, superficie volutamente esagerata per enfatizzare l'esito della query.
print()

def stampaNazioniConLangEN():
    "Stampa le nazioni in cui il linguaggio è 'EN'."
    for nation1 in listCountriesObject:
        if nation1.lang == 'EN':
            print("Paese con lingua EN:", nation1.nation, nation1.lang)

print("Query che stampa le nazioni con lingua 'EN':")
stampaNazioniConLangEN()

def nazioneMaggiorDensitaPopol():
    maxListaDenPop = max([nation.population / nation.surface for nation in listCountriesObject])      # density
    print(maxListaDenPop)
    for nation in listCountriesObject:
        if maxListaDenPop == nation.population/nation.surface:
            print("Popolazione con la maggior densità di popolazine:", nation.nation)

print("\nQuery che stampa la nazione con la maggior densità di popolazione::")
nazioneMaggiorDensitaPopol()

print("\nQuery continente percentuale EN FR:")
def continente_EN_FR(continente):
    try:
        continente = continente.capitalize()
        if continente not in [nation.continent for nation in listCountriesObject]:
            raise ValueError("Continente non esistente!")
        countENinContinent = 0
        for nation in listCountriesObject:
            if nation.continent == continente:
                if nation.lang == "EN":
                    countENinContinent += 1
        percentageENinContinent = (countENinContinent/len([nation for nation in listCountriesObject
                                                          if nation.continent == continente])) * 100
        print(f"Percentuale dei Paesi del continente {continente} che parlano 'EN': {percentageENinContinent}%.")
        print(f"Percentuale dei Paesi del continente {continente} che parlano 'FR': {100 - percentageENinContinent}%.")
    except ValueError:
        continente = input("Il continente da lei inserito non risulta ammissibile, reinserire:\n")
        continente_EN_FR(continente)

print("Per l'Europa:")
continente_EN_FR("Europa")
print("Per l'America:")
continente_EN_FR("America")
print("Prova con continente inesistente:")
continente_EN_FR("Africa")
