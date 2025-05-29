import time
import tracemalloc
from map import g 

def analyze_case(start, finish, case_name):
    print(f"\n--- {case_name} ---")
    tracemalloc.start()
    t0 = time.perf_counter()
    dist, path = g.dijkstra(start, finish)
    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Start: {start}")
    print(f"Finish: {finish}")
    print(f"Shortest path: {path}")
    print(f"Total distance: {dist[finish]}")
    print(f"Time taken: {(t1-t0)*1000:.3f} ms")
    print(f"Peak memory usage: {peak/1024:.2f} KB")

if __name__ == "__main__":
    analyze_case("Sociolla", "Elevatione", "Optimum Case")
    analyze_case("Sociolla", "Pandora", "Non-Optimum Case")