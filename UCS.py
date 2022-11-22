# Matin Rezania 983112057
# کنترل تکراری بودن در هنگام بسط دادن هم انجام شده، در خط‌های 36، 52، 68 و 84
class UCS:

    def __init__(self):
        self.current_node = {"position": {"x": 1, "y": 1},
                             "path": [[1, 1]], "gn": 0, "parent_node": None}
        self.queue = []

    def get_input(self):
        '''
        input() takes a string as input. "1 2 3"
        split() splits the string by whitespaces and returns a
        list of strings. ["1", "2", "3"]
        list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
        All these steps are done row times and these lists are stored in another list.[[1, 2, 3], [4, 5, 6], [7, 8, 9]], row = 3
        '''
        matrix = [list(map(int, input().split())) for row in range(8)]

        self.horizontal_matrix = matrix[0:4]
        self.vertical_matrix = matrix[4:8]

    def sort_according_to_gn(self, item):
        return item["gn"]

    def search(self):
        while True:

            # MOVE RIGHT
            new_node = {"position": {"x": self.current_node["position"]["x"], "y": self.current_node["position"]["y"]+1},
                        "path": [*self.current_node["path"], [self.current_node["position"]["x"], self.current_node["position"]["y"]+1]],
                        "gn": self.current_node["gn"]+1,
                        "parent_node": self.current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the right of the current node
            if new_node["position"]["y"] != 6 and new_node not in self.queue and self.vertical_matrix[self.current_node["position"]["y"]-1][self.current_node["position"]["x"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not self.current_node["parent_node"]:
                    self.queue.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != self.current_node["parent_node"]["position"]:
                    self.queue.append(new_node)

            # MOVE LEFT
            new_node = {"position": {"x": self.current_node["position"]["x"], "y": self.current_node["position"]["y"]-1},
                        "path": [*self.current_node["path"], [self.current_node["position"]["x"], self.current_node["position"]["y"]-1]],
                        "gn": self.current_node["gn"]+1,
                        "parent_node": self.current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the left of the current node
            if new_node["position"]["y"] != 0 and new_node not in self.queue and self.vertical_matrix[self.current_node["position"]["y"]-2][self.current_node["position"]["x"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not self.current_node["parent_node"]:
                    self.queue.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != self.current_node["parent_node"]["position"]:
                    self.queue.append(new_node)

            # MOVE UP
            new_node = {"position": {"x": self.current_node["position"]["x"]-1, "y": self.current_node["position"]["y"]},
                        "path": [*self.current_node["path"], [self.current_node["position"]["x"]-1, self.current_node["position"]["y"]]],
                        "gn": self.current_node["gn"]+3,
                        "parent_node": self.current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the top of the current node
            if new_node["position"]["x"] != 0 and new_node not in self.queue and self.horizontal_matrix[self.current_node["position"]["x"]-2][self.current_node["position"]["y"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not self.current_node["parent_node"]:
                    self.queue.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != self.current_node["parent_node"]["position"]:
                    self.queue.append(new_node)

            # MOVE DOWN
            new_node = {"position": {"x": self.current_node["position"]["x"]+1, "y": self.current_node["position"]["y"]},
                        "path": [*self.current_node["path"], [self.current_node["position"]["x"]+1, self.current_node["position"]["y"]]],
                        "gn": self.current_node["gn"]+3,
                        "parent_node": self.current_node}

            # check for constrains:(respectively) if it exceeds the grid, if it's already visited, if there's a obstacle to the bottom of the current node
            if new_node["position"]["x"] != 6 and new_node not in self.queue and self.horizontal_matrix[self.current_node["position"]["x"]-1][self.current_node["position"]["y"]-1] == 0:
                # this case is only for start node, which doesn't have a parent node so no need to check if the next node is the parent of the current node
                if not self.current_node["parent_node"]:
                    self.queue.append(new_node)

                # for all nodes other which do have parents so we should check iff the next node is the parent of the current node for each of them
                elif new_node["position"] != self.current_node["parent_node"]["position"]:
                    self.queue.append(new_node)

            # Check if there isn't any move left and yet goal is not found either so it breaks the while loop and end the search. This is the
            # case where goal is not reachable
            if self.queue == []:
                break

            # Sort the queue according to the g(n) of the nodes, which is the cost up to that node.
            self.queue.sort(key=self.sort_according_to_gn)

            # The following get the best choice according to UCS algorithm which is the node with the lowest cost and then delete the
            choice = self.queue[0]
            del self.queue[0]

            # Updating the current node
            self.current_node = choice

            # GOAL TEST: If it reaches the cell with x and y equal to 5, then the search should end
            if self.current_node["position"] == {"x": 5, "y": 5}:
                break

    def print_result(self):
        for node in self.current_node["path"]:
            if node == self.current_node["path"][len(self.current_node["path"])-1]:
                print(node)
            else:
                print(node, end=" ")
        print(self.current_node["gn"])


graph = UCS()
graph.get_input()
graph.search()
graph.print_result()
