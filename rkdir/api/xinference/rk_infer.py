
# 方式一 xinference 格式
# from xinference.client import RESTfulClient
# client = RESTfulClient("http://127.0.0.1:9997")
# model = client.get_model("qwen2-instruct")
# print(model.chat(
#     prompt="你好",
#     system_prompt="You are a helpful assistant.",
#     chat_history=[]
# ))

# 方式二 openai 格式
# from openai import OpenAI
# client = OpenAI(base_url="http://127.0.0.1:9997/v1", api_key="not used actually")

# response = client.chat.completions.create(
#     model="qwen2-instruct",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你好，创造一首200字现代诗，主题是阶级"}
#     ]
# )
# print(response)


# 方式二 openai 内容
# from openai import OpenAI
# client = OpenAI(base_url="http://127.0.0.1:9997/v1", api_key="not used actually")

# response = client.chat.completions.create(
#     model="qwen2-instruct",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你好，创造一首200字现代诗，主题是阶级"}
#     ]
# )
# print(response.choices[0].message.content)


# 方式三 python 流式输出
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:9997/v1", api_key="not used actually")

stream = client.chat.completions.create(
    model="rkllm",
    messages=[{"role": "user", "content": "你们公司董事长是谁"}],
    stream=True,
    
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")


# 方式三 node流式输出
# import OpenAI from "openai";

# const openai = new OpenAI();

# async function main() {
#     const stream = await openai.chat.completions.create({
#         model: "gpt-3.5-turbo",
#         messages: [{ role: "user", content: "Say this is a test" }],
#         stream: true,
#     });
#     for await (const chunk of stream) {
#         process.stdout.write(chunk.choices[0]?.delta?.content || "");
#     }
# }

# main();