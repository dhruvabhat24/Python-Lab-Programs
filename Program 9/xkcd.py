import requests
import os
url= https://xkcd.com/info.0.json
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    img_url=data['img']
    tile=data['title']
    comic_number=data['num']
    download_folder = 'xkcd_comics'
    os.makedirs(download_folder, exist_ok=True)
    image_path = os.path.join(download_folder, os.path.basename(img_url))
    with open(image_path, 'wb') as f:
        f.write(requests.get(img_url).content)
    print(f"Downloaded {tile} comic number {comic_number} to {image_path}")
else:
    print("Error occurred while downloading the image")
