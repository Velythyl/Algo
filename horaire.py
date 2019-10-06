# t_list est la liste des temps de forme [p, c, d]
# Exemple: [[31,2,2], [20, 3, 4], [10,10,2], [21,21,21], [10, 21,2], [40, 20, 20]]
def horaire(t_list):
    scores = [sum(pcd) * (pcd[0]) for pcd in t_list]

    def take_second(elem):
        return elem[1]

    return [item[0] for item in sorted(enumerate(scores), key=take_second, reverse=True)]
