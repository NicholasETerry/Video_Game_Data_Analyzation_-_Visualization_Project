class Details:

    def usable_games(games):

        usable_list = []
        for game in games:
            if str(game.year) != "None":
                usable_list.append(game)

        return usable_list

    @staticmethod
    def game_details(game):

        detail_list = [game.name, game.platform, game.year, game.genre, game.publisher, game.naSales, game.euSales,
                       game.jpSales, game.otherSales, game.globalSales, game.rank, game._id ]
