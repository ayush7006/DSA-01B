import requests
import json
import base64
import hashlib
import time
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from pprint import pprint

def generate_signature(method, url, body, app_id, private_key_path):
    method_str = method.upper()
    url_str = url
    timestamp = str(int(time.time()))
    nonce_str = hashlib.md5(timestamp.encode()).hexdigest()
    body_str = body
    if body :
        to_sign = f"{method_str}\n{url_str}\n{timestamp}\n{nonce_str}\n{body_str}"
    else:
        to_sign = f"{method_str}\n{url_str}\n{timestamp}\n{nonce_str}"
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    signature = private_key.sign(
        to_sign.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    signature_base64 = base64.b64encode(signature).decode()
    auth_header = f"TAMS-SHA256-RSA app_id={app_id},nonce_str={nonce_str},timestamp={timestamp},signature={signature_base64}"
    return auth_header

def ai_make():
    url_pre = "https://ap-east-1.tensorart.cloud"
    url = "/v1/jobs"
    app_id = "nuOE-lCiT"
    private_key_path = "/Users/ayushgurjar/Downloads/DSA-01B/tests/private_key.pem"
    data = {
        "request_id":  hashlib.md5(str(int(time.time())).encode()).hexdigest(),
    "stages": [
        {
            "type": "INPUT_INITIALIZE",
            "inputInitialize": {
                "seed": 8989898989,
                "count": 2
            }
        },
        {
            "type": "DIFFUSION",
            "diffusion": {
                "width": 512,
                "height": 512,
                "prompts": [
                    {
                        "text": "school girl"
                    }
                ],
                "steps": 15,
                "sd_model": "600423083519508503",
                "clip_skip": 4,
                "cfg_scale": 10
                }
            }
        ]
    }
    body = json.dumps(data)
    # auth_header = generate_signature("POST", url, body, app_id, private_key_path)
    # print(auth_header)
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Accept': 'application/json',
    #     'Authorization': auth_header
    # }
    # response = requests.post(f"{url_pre}{url}", json=data, headers=headers)
    # '{"job":{"id":"696405183276690015","status":"CREATED"}}'
    jobId = "696405183276690015"
    body = None
    url ='/v1/jobs/'
    auth_header = generate_signature("GET", url, body, app_id, private_key_path)
    print(auth_header)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': auth_header
    }
    # headers =  {'Date': 'Thu, 15 Feb 2024 12:10:39 GMT', 'Content-Type': 'application/json', 'Content-Length': '54', 'Connection': 'keep-alive', 'x-echo-pattern': '/tams_api.TamsApiV1Service/CreateJob', 'x-echo-traceid': 'a2aaa9ecf9ef6e3bd035b76fd4238053', 'x-tams-nonce': 'B1pxul0V3mdahEzu', 'x-tams-signature': 'dNo3S0fqHEJUP8RAK1Nl4WXPTj6c0mowWNhN8mS0Jq45d1bnyve7hJWCMf/g+9jDX79b82Kpg0vNCyteqJgcUHCkhnNQ71gsjgE2uQ2/iNcS0/z6BOaL9L/AN2ezdH7mSBBkDQtmBnQiKSXWEGeuhwJT7RLpOkV9W2QyzLZtBFzgqdXLPtVCgZVOx8aP0kbY8iP5Wd26arx++gvgtmPiqX7/edODkFXaAZNAqT+aY4lOgkuXX9M37Cw2AGisRbHyNncKAoVqpxShLLFtaa7XLL/RUZX3u0lZ8nJllsQ6eLOLwdRUGvxAdjKQ0a5sVJTayK78O/w/Ypaoix166VtLbA==', 'x-tams-timestamp': '1707999039', 'x-envoy-upstream-service-time': '44'}
    response = requests.get(f'{url_pre}{url}{int(jobId)}', headers=headers)
    pprint(f"{response.text =}")
    print(response.status_code, response.headers)
ai_make()

# url_ojjj= "https://tensor-sf-sig.7022ae40757f8d53295a57619de9b364.r2.cloudflarestorage.com/workspace/generation/694346566785550153/2024-02-15/c43718c6-30d7-4821-a180-42afad0d1394.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0bef8a003dc93fc4d7030c9da79271ff%2F20240215%2F%2Fs3%2Faws4_request&X-Amz-Date=20240215T125127Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=1cb2181754a72f7aecdff82d4a1280f642c2c4390d111ec1321fec4cabd9ea57"
# response = requests.get(url_ojjj)
# from PIL import Image
# from io import BytesIO
# # Sample image data
# if response.status_code == 200:
#     image_data = response.content
#     image = Image.open(BytesIO(image_data))
#     image.save("ai_1234.jpg")
#     print('ok')
# else:
#     print(f'Error: Unable to download the image. Status code: {response.status_code}')
    

