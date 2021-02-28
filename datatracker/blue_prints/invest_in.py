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

        return invest_list


    @staticmethod
    def no_year(obj):  # this method is strictly for testing

        no_year_list = []
        for game in obj:
            if str(game.year) == "None":
                print(game.name)
                print(game.year)
                print(game._id)
                no_year_list.append(game)

        return no_year_list
