from atlas.multipipeline import search_documents_vector
from atlas.llm_client import OllamaClient

def main():
    print("=== Project Atlas (Vector Search Edition) ===")
    
    
    folder_path = input("Enter the path to your document folder (e.g., 'data'): ").strip().strip('"')
    
    
    search_keyword = input("Enter a search phrase/keyword to find the right text: ").strip()
    question = input("Enter your full question for Atlas: ").strip()

    try:
        chunk_size = int(input("Enter chunk size (words): "))
        if chunk_size <= 0:
            print("Chunk size must be greater than zero.")
            return
        
        results = search_documents_vector(folder_path, search_keyword, chunk_size, top_k=3)

        if not results:
            print("No documents found or no matching chunks could be generated.")
            return
        chunks_for_llm = []
        print("\n--- Top Relevant Matches ---")
        
        for i, result in enumerate(results):
            score_percentage = round(result['score'] * 100, 2)
            print(f"Match {i+1} (Similarity: {score_percentage}%) from [{result['source']}]:")
            print(f"\"{result['chunk'][:100]}...\"\n") 
            
            chunks_for_llm.append(result["chunk"])

        print(f"Sending the top {len(chunks_for_llm)} chunks to Llama 3... (Waiting for Local CPU)")
        
        client = OllamaClient()
        prompt = client.build_prompt(question, chunks_for_llm)
        answer = client.generate(prompt)
        
        print('\n' + '=' * 50)
        print('AI Answer:')
        print('=' * 50)
        print(answer)

    except ValueError:
        print("Chunk size must be a valid integer.")
    except RuntimeError as e:
        print(f"\nAI Error: {e}")

if __name__ == "__main__":
    main()