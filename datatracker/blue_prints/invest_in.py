class Invest:
    def __init__(self, platform, year, globalSales):
        self.platform = platform
        self.year = year
        self.globalSales = globalSales



    @staticmethod
    def invest_results(obj):
        year_list = []
        invest_list = []
        for game in obj:
            invest_list.append(Invest(game.platform, game.year, game.globalSales))
        for game in obj:
            if str(game.year) == "None":
                print(game.name)
                print(game._id)

        return invest_list
