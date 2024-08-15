# Langchain-Chatchat v 0.3.0 部署记录

前提：
1 conda 安装 以及Nvidia驱动安装 cuda cudnn 计算资源可正常使用（确认GPU资源可用）

一 安装依赖：

conda create -n chatchat python=3.10

conda activate chatchat

pip install "langchain-chatchat[xinference]" -U

pip install "xinference[all]"

启动两个模型服务

XINFERENCE_MODEL_SRC=modelscope xinference-local --host 0.0.0.0 --port 9997


二 命令行修改配置文件：

chatchat-config model --default_llm_model qwen2-instruct

chatchat-config model --set_model_platforms "[{
    \"platform_name\": \"xinference\",
    \"platform_type\": \"xinference\",
    \"api_base_url\": \"http://127.0.0.1:9997/v1\",
    \"api_key\": \"EMPT\",
    \"api_concurrencies\": 5,
    \"llm_models\": [
        \"qwen2-instruct\"
    ],
    \"embed_models\": [
        \"bge-large-zh-v1.5\"
    ],
    \"image_models\": [],
    \"reranking_models\": [],
    \"speech2text_models\": [],
    \"tts_models\": []
}]"

三 测试及服务启动：

chatchat-kb -r

chatchat -a


## 使用说明

全命令行操作：

基础操作

查看：

chatchat-config --help

chatchat-config model --help

chatchat-conifg basic --help

修改：

chatchat-config model --default_llm_model qwen2-instruct

chatchat-config model --set_model_platforms "[{
    \"platform_name\": \"xinference\",
    \"platform_type\": \"xinference\",
    \"api_base_url\": \"http://127.0.0.1:9997/v1\",
    \"api_key\": \"EMPT\",
    \"api_concurrencies\": 5,
    \"llm_models\": [
        \"qwen2-instruct\"
    ],
    \"embed_models\": [
        \"bge-large-zh-v1.5\"
    ],
    \"image_models\": [],
    \"reranking_models\": [],
    \"speech2text_models\": [],
    \"tts_models\": []
}]"

chatchat-kb -r

xinference 启动两个模型服务

Langchain-Chatchat服务启动


qwen2-instruct
bge-large-zh-v1.5 




## 项目记录

1 embedding模型接口配置文件 ln:121

/home/rkwork/anaconda3/envs/chatchat/lib/python3.10/site-packages/chatchat/configs/_model_config.py


2 我需要查找发送接口格式而不是服务接口

/home/rkwork/anaconda3/envs/chatchat/lib/python3.10/site-packages/chatchat/webui_pages/dialogue/dialogue.py

3 对话接口地址

http://127.0.0.1:7861/chat/chat/completions

4 接口封装格式
/home/rkwork/anaconda3/envs/chatchat/lib/python3.10/site-packages/openai/_base_client.py    ln： 1236

```
    def post(                                       ## Post接口格式
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        opts = FinalRequestOptions.construct(
            method="post", url=path, json_data=body, files=to_httpx_files(files), **options
        )
        return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))

```

5 post接口格式
/home/rkwork/anaconda3/envs/chatchat/lib/python3.10/site-packages/openai/resources/chat/completions.py      ln: 643
```
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

```
6 与自定义模型进行对话

1 先使用xinference代码进行模型注册，测试正常部署

2 修改chatchat配置文件

```
chatchat-config model --set_model_platforms "[{
    \"platform_name\": \"xinference\",
    \"platform_type\": \"xinference\",
    \"api_base_url\": \"http://192.168.1.246:9997/v1\",
    \"api_key\": \"EMPT\",
    \"api_concurrencies\": 5,
    \"llm_models\": [
        \"rkllm\"
    ],
    \"embed_models\": [
        \"bge-large-zh-v1.5\"
    ],
    \"image_models\": [],
    \"reranking_models\": [],
    \"speech2text_models\": [],
    \"tts_models\": []
}]"

chatchat-config model --default_llm_model rkllm
```
3 启动

chatchat -a
