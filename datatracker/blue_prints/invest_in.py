class Invest:
    def __init__(self, platform, year, globalSales):
        self.platform = platform
        self.year = year
        self.globalSales = globalSales

    @staticmethod
    def invest_results(obj):

        invest_list = []
        for game in obj:
            if str(game.year) != "None" and game.year > 2012:
                invest_list.append(Invest(game.platform, game.year, game.globalSales))

        g = len(invest_list)
        return invest_list
