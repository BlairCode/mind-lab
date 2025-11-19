import requests
import os
from PIL import Image
from io import BytesIO

if __name__ == "__main__":
    # 浏览器中打开网站HTML，找到PPT图片的URL, 复制到下面的base_url中, 删去最后的数字和文件格式
    base_url = "https://yxdoc.zhihuishu.com/doc/20870572/757101/kYvhzFPy/thumbnail/"
    save_dir = os.path.join(os.path.curdir, "OS_PPT", "6")
    os.makedirs(save_dir, exist_ok=True)

    num =  127 # The number of ppt sliders
    images = []
    for i in range(1, num+1):
        img_url = f"{base_url}{i}.jpg"
        
        try:
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGB")
            images.append(img)
        except Exception as e:
            print(e)

    pdf_path = os.path.join(save_dir, "ppt.pdf")
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    