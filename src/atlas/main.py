from atlas.multipipeline import build_index, search_index
from atlas.llm_client import OllamaClient

def main():
    while True:
        print("\n=== Project Atlas ===")
        print("1. Build/Update Knowledge Base (Index Documents)")
        print("2. Chat with Atlas (Search & Ask)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            folder_path = input("Enter the path to your document folder: ").strip().strip('"')
            try:
                chunk_size = int(input("Enter chunk size (words): "))
                build_index(folder_path, chunk_size)
            except ValueError:
                print("Chunk size must be a valid integer.")
                
        elif choice == "2":
            question = input("\nAsk Atlas a question: ").strip()
            
            # Instantly search the pre-built JSON index
            results = search_index(question, top_k=3)
            
            if not results:
                continue
                
            chunks_for_llm = []
            print("\n--- Top Relevant Matches ---")
            for i, result in enumerate(results):
                score_pct = round(result['score'] * 100, 2)
                print(f"Match {i+1} ({score_pct}%) from [{result['source']}]:")
                print(f"\"{result['chunk'][:100]}...\"\n")
                chunks_for_llm.append(result["chunk"])

            print("Sending context to Llama 3... (Waiting for Local CPU)")
            client = OllamaClient()
            prompt = client.build_prompt(question, chunks_for_llm)
            
            try:
                answer = client.generate(prompt)
                print('\n' + '=' * 50)
                print('AI Answer:')
                print('=' * 50)
                print(answer)
            except RuntimeError as e:
                print(f"\nAI Error: {e}")
                
        elif choice == "3":
            print("Shutting down Atlas...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()