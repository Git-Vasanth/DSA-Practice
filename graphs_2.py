def build_weighted_graph(roads: list[tuple[str, str, int]]) -> dict[str, list[tuple[str, int]]]:

    adj_list = {}

    for city_1  , city_2 , distance in roads:

        if city_1 not in adj_list:
            adj_list[city_1] = []

        if city_2 not in adj_list:
            adj_list[city_2] = []

        adj_list[city_1].append((city_2 , distance))
        adj_list[city_2].append((city_1 , distance)) 

    return adj_list


roads = [
    ("A", "B", 5),
    ("A", "C", 10),
    ("B", "C", 3),
    ("B", "D", 2)
]

result = build_weighted_graph(roads=roads)

print(result)