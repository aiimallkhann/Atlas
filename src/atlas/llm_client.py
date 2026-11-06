import httpx
import json

class OllamaClient:
    def __init__(self, host_url= 'http://localhost:11434', model_name='llama3'):
        self.host_url = host_url
        self.model_name = model_name
        self.client = httpx.Client()
        
    def build_prompt(self, query: str, context_chunks: list[str]) ->str:
        joined_chunks = '\n\n'.join(context_chunks)
        instructions = f'Background Information:\n{joined_chunks}\n\nQuestion:\n\n{query}' 
        return instructions
    def generate(self, prompt: str) -> str:
        payload = {
            'model': self.model_name,
            'prompt': prompt,
            'stream': False
        }
        r = self.client.post(self.host_url + '/api/generate', json=payload, timeout=60.0)
        parsed_json = r.json()
        
        # Proper Error Handling
        if 'error' in parsed_json:
            raise RuntimeError(f"Ollama API Error: {parsed_json['error']}")
            
        return parsed_json['response']

if __name__ == "__main__":
    client = OllamaClient()
    
    # Dummy data
    query = "What is DBMS?"
    chunks = ["Paris is the capital and most populous city of France."]
    
    # Run the pipeline
    prompt = client.build_prompt(query, chunks)
    answer = client.generate(prompt)
    
    print(answer)