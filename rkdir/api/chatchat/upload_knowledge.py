'''
curl -X 'POST' \
  'http://127.0.0.1:7861/knowledge_base/upload_docs' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'to_vector_store=true' \
  -F 'override=false' \
  -F 'not_refresh_vs_cache=false' \
  -F 'chunk_size=250' \
  -F 'chunk_overlap=50' \
  -F 'zh_title_enhance=false' \
  -F 'files=@dufu.txt;type=text/plain' \
  -F 'knowledge_base_name=samples' \
  -F 'docs='
  '''

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# 定义文件路径和服务器端点
file_path = '/home/rkwork/work_place/project/rk_llm/project/Langchain-Chatchat/rkdir/rk_data/liyu.txt'
url = 'http://127.0.0.1:7861/knowledge_base/upload_docs'

# 创建一个MultipartEncoder实例来构建请求体
fields = {
    'to_vector_store': 'true',
    'override': 'false',
    'not_refresh_vs_cache': 'false',
    'chunk_size': '250',
    'chunk_overlap': '50',
    'zh_title_enhance': 'false',
    'files': (file_path, open(file_path, 'rb')),
    'knowledge_base_name': 'samples',
    'docs': '你的文档内容'  # 这里替换为实际的文档内容
}

# 使用MultipartEncoder来编码字段
multipart_data = MultipartEncoder(fields=fields)

# 发送POST请求
headers = {
    'accept': 'application/json',
    'Content-Type': multipart_data.content_type
}
response = requests.post(url, headers=headers, data=multipart_data)

# # 检查 'files' 是否在 fields 中，并且它的第二个元素是否是一个文件对象
# if 'files' in fields and isinstance(fields['files'][1], (io.IOBase,)):  # 使用 io.IOBase 作为文件对象的基类
#     fields['files'][1].close()  # 关闭文件

# 打印响应内容
print(response.text)