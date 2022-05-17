import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

'''
Connect to InfluxDB Cloud python3, using token
'''

token = os.environ.get("INFLUXDB_TOKEN")
org = "wulicheneason@gmail.com"
url = "https://us-west-2-2.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
'''
Write into InfluxDB cloud 2.0
'''
bucket = "smap_test"

write_api = client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    point = (
        Point("measurement1")
            .tag("tagname1", "tagvalue1")
            .field("field1", value)
    )
    write_api.write(bucket=bucket, org="wulicheneason@gmail.com", record=point)
    time.sleep(1)  # separate points by 1 second

'''
Simple query
'''

query_api = client.query_api()

query = """from(bucket: "<BUCKET>")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="wulicheneason@gmail.com")

for table in tables:
  for record in table.records:
    print(record)


