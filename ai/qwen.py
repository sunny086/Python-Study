import logging

from openai import OpenAI


class QwenClient:
    def __init__(self):
        self.client = OpenAI(
            # api_key=os.getenv("DASHSCOPE_API_KEY"),
            api_key="",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

    def parse_image(self, image_url: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model="qwen2.5-vl-72b-instruct",
                # 此处以qwen-vl-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
                messages=[{"role": "user", "content": [
                    {"type": "image_url",
                     "image_url": {"url": image_url}, },
                    {"type": "text", "text": "请详细描述这张图片的内容，包括场景、人物、物体及其关系。如果有明显的情感、动作或特殊元素，也请一并说明。"},
                ]}]
            )
            logging.info("QwenClient parse_image called with image_url: %s, info: %s", image_url,
                         completion.choices[0].message.content)
            return completion.choices[0].message.content
        except Exception as e:
            logging.error("Error calling Qwen API: %s", str(e))
            raise Exception(f"Qwen API调用失败: {str(e)}")


if __name__ == '__main__':
    client = QwenClient()
    res = client.parse_image("https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg")
    print(res)