def tower_of_hanoi(num_disks: int, source: str, aux: str, target: str) -> None:
    '''Runs a game of hanoi tower'''
    if num_disks > 0:
        tower_of_hanoi(num_disks - 1, source, target, aux)
        print(f"Переместить диск {num_disks} с {source} на {target}")
        tower_of_hanoi(num_disks - 1, aux, source, target)
tower_of_hanoi(2, "Source", "Auxiliary", "Target")
print("---")
tower_of_hanoi(4, "Source", "Auxiliary", "Target")