import ollama

response = ollama.chat(model='deepscaler', messages=[{'role': 'user', 'content': 'Solve 3x + 5 = 20'}])
print(response['message'])
