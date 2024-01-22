import requests

API_KEY = 'VF.DM.65929cdabb70aa0008e6c814.Z7B59nlaj2X1os09'
def api_data(prompt):

    url = 'https://general-runtime.voiceflow.com/knowledge-base/query'
    headers = {
        'Authorization': API_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {'question': prompt}

    response = requests.post(url, headers=headers, json=data)

    text = response.json().get('output')
    print(text)
    if text != None:
        return text
    else: return ""
