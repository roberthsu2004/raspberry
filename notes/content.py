import requests
import json

content = requests.get("https://raspberryfirebase.firebaseio.com/test/led.json", verify=False)
print("status code:",content.status_code);
print("json:",content.json());

newState = not content.json();
data={'led':newState};
requests.put("https://raspberryfirebase.firebaseio.com/test.json",data=json.dumps(data));
