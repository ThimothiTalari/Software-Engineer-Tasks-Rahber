from collections import defaultdict

class VideoCoursePlatform:
    def __init__(self):
        self.graph = defaultdict(list)
        self.completed = set()

    def add_dependency(self, video, prerequisites):
        self.graph[video].extend(prerequisites)

    def topological_sort(self):
        sorted_order = []
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                raise ValueError("Circular dependency detected.")
            if node in visited:
                return
            visiting.add(node)
            for neighbor in self.graph[node]:
                dfs(neighbor)
            visiting.remove(node)
            visited.add(node)
            sorted_order.append(node)

        for node in self.graph:
            dfs(node)

        return sorted_order[::-1]

    def navigate_learning_path(self):
        sorted_order = self.topological_sort()
        for video in sorted_order:
            if all(prerequisite in self.completed for prerequisite in self.graph[video]):
                print(f"Now watching: {video}")
                self.completed.add(video)

# Example usage:
platform = VideoCoursePlatform()
platform.add_dependency("Module 1 Video 1", [])
platform.add_dependency("Module 1 Video 2", ["Module 1 Video 1"])
platform.add_dependency("Module 1 Video 3", ["Module 1 Video 2"])
platform.add_dependency("Module 2 Video 1", [])
platform.add_dependency("Module 2 Video 2", ["Module 2 Video 1"])
platform.add_dependency("Module 2 Video 3", ["Module 2 Video 2"])

platform.navigate_learning_path()
