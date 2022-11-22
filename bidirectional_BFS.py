# Matin Rezania 983112057
# کنترل تکراری بودن در هنگام بسط دادن هم انجام شده، در خط‌های 44، 59، 74 و 91
class BidirectionalBFS:
    def get_input(self):
        '''
        input() takes a string as input. "1 2 3"
        split() splits the string by whitespaces and returns a
        list of strings. ["1", "2", "3"]
        list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
        All these steps are done row times and these lists are stored in another list.[[1, 2, 3], [4, 5, 6], [7, 8, 9]], row = 3
        '''
        matrix = [list(map(int, input().split())) for x in range(8)]

        self.horizontal_matrix = matrix[0:4]
        self.vertical_matrix = matrix[4:8]

    def __init__(self):
        self.forward_currnet_node = {"position": {"x": 1, "y": 1},
                                     "path": [[1, 1]], "gn": 0, "parent_node": None}
        self.backward_current_node = {"position": {"x": 5, "y": 5},
                                      "path": [[5, 5]], "gn": 0, "parent_node": None}
        self.goal_found = False
        self.forward_queue = []
        self.backward_queue = []

    def sort_function(self, item):
        return item["gn"]

    def BFS(self, direction):
        if not self.goal_found:
            if direction == "forward":
                current_node = self.forward_currnet_node
                queue_nodes = self.forward_queue
            else:
                current_node = self.backward_current_node
                queue_nodes = self.backward_queue
            # MOVE RIGHT
            new_node = {"position": {"x": current_node["position"]["x"], "y": current_node["position"]["y"]+1},
                        "path": [*current_node["path"], [current_node["position"]["x"], current_node["position"]["y"]+1]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the right of the current node
            if new_node["position"]["y"] != 6 and new_node not in queue_nodes and self.vertical_matrix[current_node["position"]["y"]-1][current_node["position"]["x"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)
            # MOVE LEFT
            new_node = {"position": {"x": current_node["position"]["x"], "y": current_node["position"]["y"]-1},
                        "path": [*current_node["path"], [current_node["position"]["x"], current_node["position"]["y"]-1]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the left of the current node
            if new_node["position"]["y"] != 0 and new_node not in queue_nodes and self.vertical_matrix[current_node["position"]["y"]-2][current_node["position"]["x"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            # MOVE UP
            new_node = {"position": {"x": current_node["position"]["x"]-1, "y": current_node["position"]["y"]},
                        "path": [*current_node["path"], [current_node["position"]["x"]-1, current_node["position"]["y"]]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the up of the current node
            if new_node["position"]["x"] != 0 and new_node not in queue_nodes and self.horizontal_matrix[current_node["position"]["x"]-2][current_node["position"]["y"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            # MOVE DOWN
            new_node = {"position": {"x": current_node["position"]["x"]+1, "y": current_node["position"]["y"]},
                        "path": [*current_node["path"], [current_node["position"]["x"]+1, current_node["position"]["y"]]],
                        "gn": current_node["gn"]+1,
                        "parent_node": current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the bottom of the current node
            if new_node["position"]["x"] != 6 and new_node not in queue_nodes and self.horizontal_matrix[current_node["position"]["x"]-1][current_node["position"]["y"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not current_node["parent_node"]:
                    queue_nodes.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != current_node["parent_node"]["position"]:
                    queue_nodes.append(new_node)

            # Check if there isn't any move left and yet goal is not found either so it breaks the while loop and end the search. This is the
            # case where goal is not reachable
            if queue_nodes == []:
                self.goal_found = True
                print("answer not found")

            # Sort the queue according to the g(n) of the nodes, which is the cost up to that node and for every step to the right, left, up and bottom is 1
            queue_nodes.sort(key=self.sort_function)

            # The following get the best choice according to UCS algorithm which is the node with the lowest cost and then delete the
            choice = queue_nodes[0]
            del queue_nodes[0]

            # Updating the current node
            current_node = choice
            if direction == "forward":
                self.forward_currnet_node = current_node
                self.forward_queue = queue_nodes
            else:
                self.backward_current_node = current_node
                self.backward_queue = queue_nodes

            self.intersect()

    def intersect(self):
        # GOAL TEST: If it reaches the if there is a node in forward searching with the same position as a node in the backward searching, then that's a goal!
        if [self.backward_current_node["position"]["x"], self.backward_current_node["position"]["y"]] in self.forward_currnet_node["path"]:
            self.goal_found = True

    def search(self):
        while not self.goal_found:
            self.BFS(direction="forward")
            self.BFS(direction="backward")
        self.build_goal_path()

    def build_goal_path(self):
        # To find the goal path
        self.backward_current_node["path"].reverse()
        path = [*self.forward_currnet_node["path"],
                *self.backward_current_node["path"]]
        # To remove duplicate nodes in goal path
        self.goal_path = []
        [self.goal_path.append(node)
         for node in path if node not in self.goal_path]

    def print_result(self):
        for node in graph.goal_path:
            if node == graph.goal_path[len(graph.goal_path)-1]:
                print(node)
            else:
                print(node, end=" ")


graph = BidirectionalBFS()
graph.get_input()
graph.search()
graph.print_result()
