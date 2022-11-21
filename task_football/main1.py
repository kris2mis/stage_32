from player import FootballPlayer
from manager import Manager


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Cristiano", "Ronaldo", 840, 300)
    alex = FootballPlayer("Alessandro", "Del Piero", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    print("List of players:")
    print(leo)
    print(cristiano)
    print(alex)
    print(ivan)

    players = (leo, cristiano, alex, ivan)

    best_player = Manager.give_golden_ball(players)
    print(f"\nBest player: {best_player}")


if __name__ == "__main__":
    main()