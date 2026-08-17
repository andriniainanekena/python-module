def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def helper(i: int) -> None:
        if i > n:
            print("Harvest time!")
            return
        print(f"Day {i}")
        helper(i + 1)

    helper(1)
