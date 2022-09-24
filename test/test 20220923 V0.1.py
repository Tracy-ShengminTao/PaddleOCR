import paddlehub as hub
import requests
import json
import cv2
import base64
# '''terminal 运行
# hub serving start -m ch_pp-ocrv3
# '''
def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tostring()).decode('utf8')

# 发送HTTP请求
data = {'images':[cv2_to_base64(cv2.imread("E:\\dasein_py\\PaddleOCR\\tax\\1.png"))]}
headers = {"Content-type": "application/json"}
url = "http://192.168.1.7:8866/predict/ch_pp-ocrv3"
r = requests.post(url=url, headers=headers, data=json.dumps(data))

# 打印预测结果
print(r.json()["results"])

with open("../json2excel/json_txt/test_20220923 V0.1.txt", "w") as fp:
    fp.write(json.dumps(r.json()["results"],indent=4, ensure_ascii=False))

