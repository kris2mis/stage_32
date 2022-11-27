from player import FootballPlayer


class Manager:
    @staticmethod
    def give_golden_ball(players):
        if not isinstance(players, (list, tuple)):
            return

        iplayer = 0  # индекс игрока

        for index in range(1, len(players)):
            if isinstance(players[index], FootballPlayer):
                current = players[index].goal * 2 + players[index].assist
                max = players[iplayer].goal * 2 + players[iplayer].assist

                if ((current > max)
                        or (current == max and players[index].goal > players[iplayer].goal)):
                    iplayer = index

        return players[iplayer]
