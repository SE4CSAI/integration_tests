import requests
import base64
import json
def test():
    test_images = ['bird1.jpg', 'bug1.jpg', 'bird2.jpg', 'bird3.jpg', 'bug2.jpg']
    test_results = ['bird', 'insect', 'bird', 'bird', 'insect']
    actual_results = []
    for image in test_images:
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        response = requests.post("http://127.0.0.1:7860/run/predict", json={
            "data": [
                "data:image/jpg;base64,{}".format(encoded_string),
            ]})
        parsed = json.loads(json.loads(response.json()['data'][0]))
        actual_results.append(parsed['predicted_label'])
try:
    test()
    print("Passed.")
except:
    print("Error. Test failure or loading problem")