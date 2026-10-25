from atlas.pipeline import search_document

def main():
    file_path = input("Enter the path to your .txt file: ").strip().strip('"')
    query = input("Enter your search query: ").strip()

    try:
        chunk_size = int(input("Enter chunk size (words): "))
        if chunk_size <= 0:
            print("Chunk size must be greater than zero.")
            return

        result = search_document(file_path, query, chunk_size)

        if result is None:
            print("File not found or could not be read.")
            return

        print("\nStatistics:")
        print(result["statistics"])

        print("\nSearch results:")
        for score, chunk in result["results"]:
            print(f"Score: {score} | {chunk}")

    except ValueError:
        print("Chunk size must be a valid integer.")

if __name__ == "__main__":
    main()