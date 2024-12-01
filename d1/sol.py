import argparse

def main() -> None:
    """O(nlogn)
    """
    parser = argparse.ArgumentParser(description="Solution of day 1 of Advent of Code 2024")
    parser.add_argument('input_file', type=str, help="Path to the input file, you need to download it from the website.")
    args = parser.parse_args()

    raw_input = args.input_file
    with open(raw_input, 'r') as file:
        data = file.read().strip()

    left: list[int] = []
    right: list[int] = []
    
    # counter of occurrences of right endpoints
    right_count: dict[int, int] = {}

    
    # O(n)
    # parsing the input data
    for line in data.split('\n'):
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
        if r in right_count:
            right_count[r] += 1
        else:
            right_count[r] = 1

    # O(nlogn)
    left.sort()
    right.sort()

    # O(n)
    part1 = 0
    # sum of absolute differences between sorted left and right endpoints
    for l, r in zip(left, right):
        part1 += abs(r - l)
    print("Part 1 result:", part1)

    # O(n)
    part2 = 0
    # multiply each left endpoint by its occurrence count in the right endpoint dictionary
    # like a weighted sum of left endpoints by their occurrence count in the right endpoints
    for l in left:
        part2 += l * right_count.get(l, 0)
    print("Part 2 result:", part2)

if __name__ == "__main__":
    main()
