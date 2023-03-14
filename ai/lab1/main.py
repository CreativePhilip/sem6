import parse_csv
from a_star import a_star


def basic_heuristic(node, adj_list):
    return 1


def main():
    adj_list = parse_csv.load_csv()

    a_star(adj_list, basic_heuristic)


if __name__ == '__main__':
    main()
