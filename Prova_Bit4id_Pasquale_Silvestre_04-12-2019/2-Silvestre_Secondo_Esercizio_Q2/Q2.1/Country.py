class Country():
    def __init__(self, nation, population, surface, continent, lang='EN'):
        self.nation = nation                        # string
        self.population = population                # int
        self.surface = surface                      # float (km**2)
        self.continent = continent                  # string
        self.lang = lang                            # EN or FR

    def __str__(self):
        return f"{self.nation}, {self.continent}, {self.lang}"