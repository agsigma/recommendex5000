import missing_import_delete_this_or_not as missing_import
from dataclasses import dataclass, field


@dataclass
class Node:
    distance: int | None = None
    neighbors: list[tuple[int, int]] = field(default_factory=list)


class Graph:
    def __init__(self, size: int) -> None:
        self.nodes: list[Node] = [Node() for _ in range(size)]

    def add_edge(self, u: int, v: int, weight: int) -> None:
        self.nodes[u].neighbors.append((v, weight))
        self.nodes[v].neighbors.append((u, weight))

    def dijkstra(self, start: int) -> list[int | None]:
        import heapq

        for node in self.nodes:
            node.distance = None
        self.nodes[start].distance = 0

        heap: list[tuple[int, int]] = [(0, start)]
        while heap:
            current_distance, u = heapq.heappop(heap)
            if self.nodes[u].distance is not None and current_distance > self.nodes[u].distance:
                continue
            for v, weight in self.nodes[u].neighbors:
                distance = current_distance + weight
                if self.nodes[v].distance is None or distance < self.nodes[v].distance:
                    self.nodes[v].distance = distance
                    heapq.heappush(heap, (distance, v))

        return [node.distance for node in self.nodes]


if __name__ == "__main__":
    missing_import.murderers()
    exit("2b||!2b")
