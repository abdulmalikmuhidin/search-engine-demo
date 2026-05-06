import os
from indexer import build_index

def search(query, index):
    words = query.lower().split()
    results = None

    for word in words:
        if word in index:
            if results is None:
                results = index[word]
            else:
                results = results.intersection(index[word])
        else:
            return []

    return list(results) if results else []


if __name__ == "__main__":
    # 👇 SAME LOGIC HERE
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, "documents")

    index = build_index(folder_path)

    while True:
        query = input("Search: ")
        results = search(query, index)

        if results:
            print("Results:", results)
        else:
            print("No results found")