import httpx
import json

class OllamaClient:
    def __init__(self, host_url= 'http://localhost:11434', model_name='llama3'):
        self.host_url = host_url
        self.model_name = model_name
        self.client = httpx.Client()
        
    def build_prompt(self, query: str, context_chunks: list[str]) ->str:
        rule = 'You are a strict research assistant for Project Atlas. Answer the question using only the provided Background Information.If the answer is not contained in the text, say \'I cannot answer based on this document.\' Do not guess.'
        joined_chunks = '\n\n'.join(context_chunks)
        instructions = f'{rule}\n\nBackground Information:\n{joined_chunks}\n\nQuestion:\n\n{query}' 
        return instructions
    def generate(self, prompt: str) -> str:
        payload = {
            'model': self.model_name,
            'prompt': prompt,
            'stream': False
        }
        r = self.client.post(self.host_url + '/api/generate', json=payload, timeout=300.0)
        r.raise_for_status()
        parsed_json = r.json()
        
        if 'error' in parsed_json:
            raise RuntimeError(f"Ollama API Error: {parsed_json['error']}")
            
        return parsed_json['response']

if __name__ == "__main__":
    client = OllamaClient()
    
    # Dummy data
    query = "What is 2+2?"
    chunks = ["Paris is the capital and most populous city of France."]
    
    # Run the pipeline
    prompt = client.build_prompt(query, chunks)
    answer = client.generate(prompt)
    
    print(answer)