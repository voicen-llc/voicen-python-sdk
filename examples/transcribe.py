"""
Copyright 2019 Voicen LLC

Licensed under the Apache License, Version 2.0 (the “License”); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an “AS IS” BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License.
"""


import time
from voicen import vcnclient

access_token = 'YOUR_ACCESS_TOKEN'


#create voicen transcriber client
voicen_client = vcnclient.VoicenClient('79434977-3c62-4711-b26d-543f0b99a98f')

"""
Uploads english_test.wav and creates job and returns job details. This job details will be used for next operations.
The english test audio was used in example. Voicen currently supports four languages: english(en-EN), russian(ru-RU), turkish(tr-TR) and azerbaijani(az-AZ).
"""
job = voicen_client.create_job_with_local_file("/home/toghrul/Projects/voicen-asr-python/audio/example-az.wav", "az-AZ")

#lets check job status and wait for complete
while True:
	job_details = voicen_client.get_job(job.id)

	status = job_details.status.name

	print('Current status of job: {}'.format(status))

	if status == 'WAITING' or status == 'PREPARING' or status == 'PROCESSING' or status == 'TRANSCRIBING':
		time.sleep(3)
		continue
	elif status == 'FAILED':
		print('Job failed')
		break

	if status == 'READY':
		#obtaining result as JSON
		transcription = voicen_client.get_transcription(job.id)
		print(transcription.dump_json())

		#obtaining result as text
		transcription_text = voicen_client.get_transcription_as_text(job.id)
		print(transcription_text)

		#obtaining result as srt(SubRip Text)
		transcription_srt = voicen_client.get_transcription_as_srt(job.id)
		print(transcription_srt)

		#obtaining result as MS Word
		transcription_msword = voicen_client.get_transcription_as_msword(job.id)
		with open("./english_test.docx", "wb") as file:
			file.write(transcription_msword)
			file.close()

		break

print("Creating job and retrieving result finished.")
