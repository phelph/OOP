from dataclasses import dataclass, field


@dataclass
class Stats:
    values: dict = field(
        default_factory=lambda: {
            "Strength": 5,
            "Dexterity": 5,
            "Arcane": 5,
        }
    )
    spendable_points: int = 5

    def print_stats(self) -> None:
        print(f"Your current stats:\n")
        for index, (stat, value) in enumerate(self.values.items(), start=1):
            print(f"{index}. {stat.capitalize()}: {value}")

    def upgrade_stats(self) -> None:
        while self.spendable_points > 0:
            print(f"You have {self.spendable_points} spendable stat point(s) left.\n")
            self.print_stats()
            try:
                choice = int(
                    input(
                        "\nEnter the corresponding number of the stat you want to upgrade: "
                    )
                )
                chosen_stat = list(self.values.keys())[choice - 1]

                points_to_add = int(
                    input(
                        f"\nHow many points ({self.spendable_points} left) do you want to add to {chosen_stat}? "
                    )
                )
                if 0 < points_to_add <= self.spendable_points:
                    self.values[chosen_stat] += points_to_add
                    self.spendable_points -= points_to_add
                else:
                    print("Invalid number of points. Please try again.\n")
            except (IndexError, ValueError):
                print("Invalid selection. Please try again.\n")

        print("You have used all your spendable points.\n")
        self.print_stats()


if __name__ == "__main__":
    # Testing class
    player_stats = Stats()
    player_stats.upgrade_stats()
