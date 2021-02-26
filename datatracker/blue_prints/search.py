class Search:  # able to search for a game and see a data visualization of the number of copies sold per console
    def __init__(self, platform, globalSales, name):
        self.platform = platform
        self.globalSales = globalSales
        self.name = name

    @staticmethod
    def search_results(obj):

        game_list = [] # list of games that have the same name a search_by_game_name
        for game in obj:
            game_list.append(Search(game.platform, game.globalSales, game.name))

        return game_list
