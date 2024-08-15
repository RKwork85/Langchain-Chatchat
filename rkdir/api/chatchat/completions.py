
base_url = "http://127.0.0.1:7861/chat"
data = {
    "model": "qwen2-instruct",
    "messages": [
        {"role": "user", "content": "你好"},
    ],
    "stream": True,
    "temperature": 0.7,
    "tool_choice": "search_local_knowledgebase",

}

# 方式一：使用 requests
import requests
response = requests.post(f"{base_url}/chat/completions", json=data, stream=True)
for line in response.iter_content(None, decode_unicode=True):
    print(line, end="", flush=True)

# 方式二：使用 openai sdk
# import openai
# client = openai.Client(base_url=base_url, api_key="EMPTY")
# resp = client.chat.completions.create(**data)
# for chunk in resp:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")



# base_url = "http://127.0.0.1:7861/chat"
# data = {
#     "messages": [
#         {"role": "user", "content": "众承教育董事长是谁"},
#     ],
#     "model": "qwen2-instruct",
#     "tool_choice": "search_local_knowledgebase",
#     "stream": True,
# }

# import requests
# response = requests.post(f"{base_url}/chat/completions", json=data, stream=True)
# for line in response.iter_content(None, decode_unicode=True):
#     print(line)