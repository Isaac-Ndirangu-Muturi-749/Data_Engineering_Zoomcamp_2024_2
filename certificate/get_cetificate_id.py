from hashlib import sha1

def compute_hash(email):
	return sha1(email.encode('utf-8')).hexdigest()

def compute_certificate_id(email):
	email_clean = email.lower().strip()
	return compute_hash(email_clean + '_')


cohort = 2024
course = 'dezoomcamp'
your_id = compute_certificate_id('never.give.up@gmail.com')
url = f"https://certificate.datatalks.club/{course}/{cohort}/{your_id}.pdf"
print(url)

def get_certificate_url(email='ndirangumuturi749@gmail.com'):
	cohort = 2024
	course = 'dezoomcamp'
	your_id = compute_certificate_id(email)
	url = f"https://certificate.datatalks.club/{course}/{cohort}/{your_id}.pdf"

	return url



'https://certificate.datatalks.club/dezoomcamp/2024/7fb6afbfb9a8a42c9c26bf1150a939e732315a6c.pdf'
