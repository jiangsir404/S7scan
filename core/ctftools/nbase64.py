import base64

def nbase64(s):
	try:
		while True:
			s = base64.b64decode(s)
			print s
	except:
		print 'finish'

	
if __name__ == '__main__':
	nbase64('Vm0xd1NtUXlWa1pPVldoVFlUSlNjRlJVVGtOamJGWnlWMjFHVlUxV1ZqTldNakZIWVcxS1IxTnNhRmhoTVZweVdWUkdXbVZHWkhOWGJGcHBWa1paZWxaclpEUmhNVXBYVW14V2FHVnFRVGs9')
	nbase64('ZmxhZ3t5MHVkMWFueTFzMX0=')