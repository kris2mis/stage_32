from player import FootballPlayer


class Manager:

    def give_golden_ball(players):
        if isinstance(players, (list, tuple)):
            max_goals = 0
            for player in players:

                if player._goal > max_goals:
                    max_goals = player._goal
                # elif player._goal == max_goals:
                #     if player._assist > max_goals:
                #         max_goals = player._assist
                return max_goals





            # total = 1
            # for player in players:
            #     if player._goal > total:
            #         total = player._goal
            #     elif player._goal == total:
            #         if player._assist > total:
            #             total = player._assist
            # return total

            #     if isinstance(player, FootballPlayer):
            #         max_goals = 1
            # return max_goals

            # max_goal = 1
            # for goal in players:
            #     if goal > max_goal:
            #         max_goal = goal
            # return max_goal
