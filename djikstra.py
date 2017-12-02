from queue import Queue
import pprint
pp = pprint.PrettyPrinter(indent=4)


def build_graph():
    return [
        {
            "label": "home",
            "edges": [("a", 3), ("b", 2), ("c", 5)],
            "distance": 0,
            "visited": True,
        },
        {
            "label": "a",
            "edges": [("home", 3), ("d", 3)],
            "distance": None,
            "visited": False,

        },
        {
            "label": "b",
            "edges": [("d", 1), ("home", 2), ("e", 6)],
            "distance": None,
            "visited": False,
        },
        {
            "label": "c",
            "edges": [("home", 5), ("e", 2)],
            "distance": None,
            "visited": False,
        },
        {
            "label": "d",
            "edges": [("b", 1), ("a", 3), ("f", 4)],
            "distance": None,
            "visited": False,
        },
        {
            "label": "e",
            "edges": [("b", 6), ("c", 2), ("f", 1), ("university", 4)],
            "distance": None,
            "visited": False,
        },
        {
            "label": "f",
            "edges": [("d", 4), ("e", 1), ("university", 2)],
            "distance": None,
            "visited": False,
        },
        {
            "label": "university",
            "edges": [("f", 2), ("e", 4)],
            "distance": None,
            "visited": False,
        }
    ]


def get_unvisited(graph):
    return [x for x in graph if x["visited"] == False]


def get_closest_node(graph):
    minimum_node = None
    minimum_distance = None
    for node in graph:
        if node.get("distance") and (not minimum_distance or node["distance"] < minimum_distance):
            minimum_node = node
            minimum_distance = node["distance"]
    return minimum_node

def traverse(unvisited_set, current_node):
    pp.pprint("Visiting:")
    pp.pprint(current_node)
    pp.pprint("Checking:")

    for edge in current_node["edges"]:
        node = next((x for x in unvisited_set if x["label"] == edge[0]), None)
        if node:
            if not node.get("distance") or node.get("distance") > current_node["distance"] + edge[1]:
                node["distance"] = current_node["distance"] + edge[1]
            pp.pprint(node)

    current_node["visited"] = True

    if current_node["label"] == "university":
        return
    else:
        unvisited_set = get_unvisited(unvisited_set)
        current_node = get_closest_node(unvisited_set)
        traverse(unvisited_set, current_node)

# Initial setup.
graph = build_graph()
root_node = next(x for x in graph if x["label"] == "home")

# Go!
graph = traverse(get_unvisited(graph), root_node)
