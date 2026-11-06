from atlas.pipeline import search_document
from atlas.llm_client import OllamaClient

def main():
    file_path = input("Enter the path to your .txt file: ").strip().strip('"')
    
    search_keyword = input('Enter a keyword to search the document: ')
    question = input("Enter your full question for Atlas: ").strip()
    
    try:
        chunk_size = int(input("Enter chunk size (words): "))
        if chunk_size <= 0:
            print("Chunk size must be greater than zero.")
            return

        result = search_document(file_path, question, chunk_size)

        if result is None:
            print("File not found or could not be read.")
            return
        
        print(f'\nAnalyzing: {result['source']}')
        print(f'Stats: {result['statistics']}')

        chunks_for_llm = []
        for score, chunk in result["results"]:
            chunks_for_llm.append(chunk)
        
        if not chunks_for_llm:
            print(f'Could not find any passages containing the word \'{search_keyword}\'')
        
        top_chunks = chunks_for_llm[:3]
        print(f'\nSending top {len(top_chunks)} chunks to Llama 3... (Waiting for Local CPU)')
        client = OllamaClient()
        prompt = client.build_prompt(question, chunks_for_llm)
        answer = client.generate(prompt)
        print('\n' * 50)
        print('AI Answer:')
        print('='*50)
        print(answer)

    except ValueError:
        print("Chunk size must be a valid integer.")
    except RuntimeError as e:
        print(f"\nAI Error {e}")

if __name__ == "__main__":
    main()