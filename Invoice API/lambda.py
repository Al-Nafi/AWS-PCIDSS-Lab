import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='lab-demo-invoices'

	invoice_data = {}
	invoice_data['invoiceId'] = '452321'
	invoice_data['type'] = 'PURCHASE'
	invoice_data['amount'] = 100
	invoice_data['customerId'] = 'CUST-ID-5343231'

	file_name = 'CUST-ID-5343231' + '.json'

	byte_stream = bytes(json.dumps(invoice_data).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=file_name, Body=byte_stream)

	print('Uploaded')
