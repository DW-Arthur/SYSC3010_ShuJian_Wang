import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3" # Put your API Key here
group = "l3-T-1"
email = "danielwang6@cmail.carleton.ca"
identifier = "d"

def labtest():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        params = urllib.parse.urlencode({'field1': group,'field2': email , 'field3': identifier, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (group)
            print (email)
            print (identifier)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        labtest()
 
