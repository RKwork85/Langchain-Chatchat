# Langchain-Chatchat v 0.3.0 部署记录

前提：
>conda 安装完成 以及Nvidia驱动安装 cuda cudnn 计算资源可正常使用（确认GPU资源可用）

一 安装依赖：

conda create -n chatchat python=3.10

conda activate chatchat

pip install "langchain-chatchat[xinference]" -U

pip install "xinference[all]"

启动两个模型服务

XINFERENCE_MODEL_SRC=modelscope xinference-local --host 0.0.0.0 --port 9997


二 命令行修改配置文件：


```
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

```
三 测试及服务启动：

chatchat-kb -r

chatchat -a

