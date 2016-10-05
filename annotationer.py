import socket
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='POST Events to Graphite API')
parser.add_argument('-ip', nargs='+', default=None, required=True, help='IP address(es) to the Graphite host(s).')
parser.add_argument('-w', default=None, required=True, help='What is this event about?')
parser.add_argument('-t', nargs='+', default=None, required=True, help='Descriptive and whitespace seperated tags that will be searchable.')
args = parser.parse_args()

graphitehosts = args.ip
jsondict = {}

def connectTest(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, 80))
        s.close()
        return True
    except Exception as e:
        print e.message
        return False

def buildPayload(key, value):
    jsondict[str(key)] = str(value)
    return jsondict

def sendAnnotation(payload):
    for host in graphitehosts:
        if connectTest(host):
            headers = {'content-type': 'application/json'}
            url = 'http://' + host + '/events/'
            r = requests.post(url, data = json.dumps(payload), headers = headers)
            if r.status_code == 200:
                print '200 OK'
            else:
                print r.status_code

# Main
if __name__ == "__main__":
    buildPayload('what', args.w)
    buildPayload('tags', ' '.join(args.t))

    sendAnnotation(jsondict)
