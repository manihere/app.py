# Array Challenge
# Have the function ArrayChallenge (strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (11,12), where 11 represents a child node in a tree and the second integer 12 signifies that it is the parent of 11. For example: if strArr is I" (1,2)*. "(2,4)*. "(7,2)], then this forms the following tree:
# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed.
# If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
# Examples
# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", " (9,5)"]
# Output: true
# Input: ["(1,2)", "(1,3)"]
# Output: false

def ArrayChallenge(strArr):
    def is_valid_binary_tree(pairs):
        graph = {}
        for pair in pairs:
            child, parent = map(int, pair.strip("()").split(","))
            if parent in graph:
                graph[parent].append(child)
            else:
                graph[parent] = [child]

        def dfs(node, visited):
            if node not in graph:
                return True
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if not dfs(child, visited):
                    return False
            visited.remove(node)
            return True

        root_count = 0
        for parent in graph.keys():
            if parent not in sum(graph.values(), []):
                root_count += 1
                if root_count > 1:
                    return False
                if not dfs(parent, set()):
                    return False
        return True

    return is_valid_binary_tree(strArr)

# Test cases
print(ArrayChallenge(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))  # Output: true
print(ArrayChallenge(["(1,2)", "(1,3)"]))  # Output: false
