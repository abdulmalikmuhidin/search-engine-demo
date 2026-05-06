import os

def tokenize(text):
    return text.lower().split()

def build_index(folder_path):
    index = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as f:
            content = f.read()
            words = tokenize(content)

            for word in words:
                if word not in index:
                    index[word] = set()
                index[word].add(filename)

    return index


if __name__ == "__main__":
    # 👇 This is the important part
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, "documents")

    print("Using folder:", folder_path)  # debug

    index = build_index(folder_path)

    for word, files in index.items():
        print(word, ":", list(files))