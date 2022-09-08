import requests

# sending sms function
def sending_sms(phone_number,message):
    send_sms_success = False
    try:
        url = f"http://66.45.237.70/api.php?username=care71&password=care71@12&number={phone_number}&message={message}"
        payload  = {}
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        send_sms_success = True
    except:
        send_sms_success = False
    return send_sms_success