import boto3
from time import strftime, localtime

client = boto3.resource('dynamodb')
table = client.Table('my-ip')

items = table.scan()['Items']
lookup: dict[str, int] = {}

for item in items:
    ip = item['myip']
    if not ip:
        ip = item['ip4Only']
    if not ip:
        ip = item['ipify']

    timestamp = float(item['id'])
    if ip:
        if ip not in lookup or timestamp < lookup[ip]:
            lookup[ip] = timestamp


a = [[lookup[ip], ip] for ip in lookup]
a.sort(reverse=True)
a = list(filter(lambda tpl: tpl[0] > 1, a))

for r in a:
    print(f'Time: {strftime("%Y-%m-%d %H:%M:%S %Z", localtime(r[0]))}, IP: {r[1]}')
