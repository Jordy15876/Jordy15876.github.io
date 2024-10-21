import sys
from typing import Dict, List


class TowerOfHanoi:
    def __init__(self, num_disks: int):
        self.pegs: Dict[str, List[int]] = {
            'A': list(range(num_disks, 0, -1)),  # Source peg with disks stacked
            'B': [],  # Target peg
            'C': []   # Auxiliary peg
        }
        self.num_disks = num_disks

    def hanoi(self, num_disks: int, source: str, target: str, auxiliary: str):
        """Solve the Tower of Hanoi problem recursively."""
        if num_disks == 0:
            return

        # Move n - 1 disks from source to auxiliary peg
        self.hanoi(num_disks - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        self.pegs[target].append(self.pegs[source].pop())
        print(f"Move disk {num_disks} from {source} to {target}")
        self.print_pegs()

        # Move n - 1 disks from auxiliary to target peg
        self.hanoi(num_disks - 1, auxiliary, target, source)

    def print_pegs(self):
        """Print the current state of all pegs."""
        for peg_name, peg in self.pegs.items():
            print(f"{peg_name}: ", end="")
            for disk in peg:
                print(f"{disk * '*'} ", end="")
            print()

    def print_moves(self):
        """Calculate and print total moves required for the problem."""
        total_moves = 2 ** self.num_disks - 1
        print("\n---------------------------------------------")
        print(f"Recursion limit: {sys.getrecursionlimit()}")
        print(f"Total moves required: {total_moves} (calculated as 2^n - 1)")
        print("The recursion limit indicates the maximum depth of recursive calls.")
        print("Exceeding this limit can cause a stack overflow.")


def get_number_of_disks() -> int:
    """Get the number of disks from the user, ensuring valid input."""
    while True:
        try:
            num_disks = int(input("Enter the number of disks (must be a positive integer): "))
            if num_disks < 1:
                raise ValueError("Number of disks must be at least 1.")
            return num_disks
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    number_of_disks = get_number_of_disks()
    hanoi_solver = TowerOfHanoi(number_of_disks)

    print("Initial state:")
    hanoi_solver.print_pegs()
    hanoi_solver.hanoi(number_of_disks, 'A', 'B', 'C')
    hanoi_solver.print_moves()
