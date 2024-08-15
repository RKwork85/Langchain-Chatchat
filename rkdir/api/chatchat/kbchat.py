base_url = "http://127.0.0.1:7861/chat"

data = {'messages': [{'role': 'user', 'content': '介绍一下李白'}], 'model': 'qwen2-instruct', 'stream': True, 'tools': ['search_local_knowledgebase'], 'tool_choice': 'search_local_knowledgebase', 'extra_body': {'metadata': None, 'chat_model_config': {'preprocess_model': {'glm4-chat': {'temperature': 0.05, 'max_tokens': 4096, 'history_len': 100, 'prompt_name': 'default', 'callbacks': False}}, 'llm_model': {'glm4-chat': {'temperature': 0.9, 'max_tokens': 4096, 'history_len': 10, 'prompt_name': 'default', 'callbacks': True}, 'qwen2-instruct': {}}, 'action_model': {'glm4-chat': {'temperature': 0.01, 'max_tokens': 4096, 'prompt_name': 'ChatGLM3', 'callbacks': True}}, 'postprocess_model': {'glm4-chat': {'temperature': 0.01, 'max_tokens': 4096, 'prompt_name': 'default', 'callbacks': True}}, 'image_model': {'sd-turbo': {'size': '256*256'}}}, 'conversation_id': '1d4daf6b82bb4d9e816236d5077f5ad6', 'tool_input': {'database': 'samples', 'query': '介绍一下李白'}}}
# data = {'messages': [{'role': 'user', 'content': '李白什么时候去世的'}], 'model': 'qwen2-instruct', 'stream': True, 'tools': ['search_local_knowledgebase'], 'tool_choice': 'search_local_knowledgebase', 'extra_body': {'metadata': None, 'chat_model_config': {'preprocess_model': {'glm4-chat': {'temperature': 0.05, 'max_tokens': 4096, 'history_len': 100, 'prompt_name': 'default', 'callbacks': False}}, 'llm_model': {'glm4-chat': {'temperature': 0.9, 'max_tokens': 4096, 'history_len': 10, 'prompt_name': 'default', 'callbacks': True}, 'qwen2-instruct': {}}, 'action_model': {'glm4-chat': {'temperature': 0.01, 'max_tokens': 4096, 'prompt_name': 'ChatGLM3', 'callbacks': True}}, 'postprocess_model': {'glm4-chat': {'temperature': 0.01, 'max_tokens': 4096, 'prompt_name': 'default', 'callbacks': True}}, 'image_model': {'sd-turbo': {'size': '256*256'}}}, 'conversation_id': '1d4daf6b82bb4d9e816236d5077f5ad6'}}



# 方式一
# import requests
# response = requests.post(f"{base_url}/chat/completions", json=data, stream=True)
# for line in response.iter_content(None, decode_unicode=True):
#     print(line)

# 方式二：使用 openai sdk
import openai
client = openai.Client(base_url=base_url, api_key="EMPTY")
resp = client.chat.completions.create(**data)
for chunk in resp:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

