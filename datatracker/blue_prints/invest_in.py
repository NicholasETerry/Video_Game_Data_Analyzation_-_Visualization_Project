class Invest:
    def __init__(self, platform, year, globalSales):
        self.platform = platform
        self.year = year
        self.globalSales = globalSales



    @staticmethod
    def invest_results(obj):
        year_in_name_list = []  # year key is none but year appears in game title
        none_list = []  # year key is none
        year_list = []
        invest_list = []
        for game in obj:
            invest_list.append(Invest(game.platform, game.year, game.globalSales))
        for game in obj:
            if str(game.year) == "None":
                none_list.append(game)
        for game in none_list:
            if "19" in game.name or "20" in game.name:
                year_in_name_list.append(game)



        return invest_list
