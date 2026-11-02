def build_prompt(query, retrieved_results):
    instruction = "Answer the question using only the context below. If you don't know, say so."    
    context = ''
    for result in retrieved_results:
        source_name = result['source']
        chunk = result['chunk']
        context += (f'SOURCE: {source_name} , CHUNK: {chunk}\n\n')
    final_prompt = f'{instruction} {context} QUESTION: {query}'
    return final_prompt