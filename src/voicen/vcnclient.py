import requests
from urllib.parse import urljoin
from urllib.parse import quote
from requests.exceptions import HTTPError
from .classes import Job
from .classes import Transcription
from .classes import Account
from .classes import Payment

class VoicenClient:
	#Current version voicen RESTful API
	api_version = "v1"

	#Base URL of API
	api_base_url = "https://api.voicen.com/speechtotext/{}/".format(api_version)
#	api_base_url = "http://127.0.0.1:8080/speechtotext/{}/".format(api_version)

	def __init__(self, voicen_access_token):
		if not voicen_access_token:
			raise ValueError("You must provide access token to use API.")

		self.default_headers = {
			"Authorization": "Bearer {}".format(voicen_access_token)
		}

	def create_job_with_media_url(self, media_url, language):
		"""
			Creates transcription job using media URL. After creating job downloads audio from media URL and transcribes it.

			:param media_url: web url of audio or video. Voicen currently supports transcribing of youtube.
			:param language: language of speech downloaded from media url
			:returns: new created job
			:raises: HTTPError
		"""
		#media url is important and must be included
		if not media_url:
			raise ValueError("You must provide media URL to create job.")

		#language of speech is also important and must be included
		if not language:
			raise ValueError("You must provide language of speech on media URL.")

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"
		
		payload = "lang={}&link={}".format(quote(language), quote(media_url))

		response = requests.request("POST", urljoin(self.api_base_url, "jobs/url"), data=payload, headers=headers)

		try:
			response.raise_for_status()
			return Job.parse_json(response.json())
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def create_job_with_local_file(self, local_file, language):
		"""
			Creates transcription job using local audio or video file. 
			Uploads local media file to the server.
			After creating job processes uploaded media file.

			:param local_file: local audio or video file to upload and transcribe
			:param language: language of speech of local audio or video file
			:returns: new created job
			:raises: HTTPError
		"""

		#media file is important and must be included
		if not local_file:
			raise ValueError("You must provide local video ro audio file to create job.")

		#language of speech is also important and must be included
		if not language:
			raise ValueError("You must provide language of speech of local video or audio file.")

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		#headers["Content-Type"] = "multipart/form-data"
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"
		#headers["content-Type"] = "multipart/form-data"
		
		
		payload = {"lang": language}

		try:
			files={'file':open(local_file, "rb")}
#			payload['file'] = local_file #open(local_file, "rb")
		except IOError as err:
			raise

		response = requests.request("POST", urljoin(self.api_base_url, "jobs/file"), data=payload, headers=headers, files = files)

		try:
			response.raise_for_status()
			return Job.parse_json(response.json())
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_job(self, job_id):
		"""
		Retrieves job details by id.

		:param: job_id: ID of job want to get details
		:returns: job
		:raises: HTTPError
		"""
		
		if not job_id:
			raise ValueError("You must provide valid job ID value.")

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"
		
		response = requests.request("GET", urljoin(self.api_base_url, "jobs/{}".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
			return Job.parse_json(response.json())
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_jobs(self, start_after = 0, limit = 100):
		"""
		Retrieves job list realtive to start_after and limit parameters.

		:param: start_after: the job ID that you retrieve job list which their id greater than it.
		:param: limit: max size of job list
		:returns: array of job
		:raises: HTTPError
		"""

		if start_after is None:
			raise ValueError("You must provide valid start_after param.")

		if limit is None:
			raise ValueError("You must provide valid limit param.")

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "jobs?start_after={}&limit={}".format(start_after, limit)), headers=headers)

		try:
			response.raise_for_status()
			return [Job.parse_json(job) for job in response.json()]
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def delete_job(self, job_id):
		"""
		Deletes job and it's all data by ID

		:param job_id: ID of job which will be deleted
		:raises: HTTPError
		:returns: None if job deleted successfully
		"""
		if not job_id:
			raise ValueError("You must provide valid job ID value.")

		headers = self.default_headers.copy()
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"

		response = requests.request("DELETE", urljoin(self.api_base_url, "jobs/{}".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

		return

	def get_transcription(self, job_id):
		"""
		Retrieves transcript by job ID

		:param: job_id: ID of job want to get transcript
		:returns:  job transcription
		:raises: HTTPError
		"""

		if not job_id:
			raise ValueError("You must provide valid job ID value.")
		headers = self.default_headers.copy()
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "jobs/{}/transcript?type=json".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
			return Transcription.parse_json(response.json())
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise


	def get_transcription_as_text(self, job_id):
		"""
		Retrieves transcript as text by job ID

		:param: job_id: ID of job want to get transcript as text
		:returns: job transcription as text
		:raises: HTTPError
		"""

		if not job_id:
			raise ValueError("You must provide valid job ID value.")

		headers = self.default_headers.copy()
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "jobs/{}/transcript?type=txt".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
			return response.text
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_transcription_as_srt(self, job_id):
		"""
		Retrieves transcription as srt by job ID

		:param: job_id: ID of job want to get transcription as srt
		:returns: job transcription as srt
		:raises: HTTPError
		"""

		if not job_id:
			raise ValueError("You must provide valid job ID value.")
		headers = self.default_headers.copy()
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "jobs/{}/transcript?type=srt".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
			return response.text
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_transcription_as_msword(self, job_id):
		"""
		Retrieves transcript as microsoft word by job ID

		:param: job_id: ID of job want to get transcript as text
		:returns: job transcription as microsoft word
		:raises: HTTPError
		"""

		if not job_id:
			raise ValueError("You must provide valid job ID value.")

		headers = self.default_headers.copy()
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "jobs/{}/transcript?type=doc".format(job_id)), headers=headers)

		try:
			response.raise_for_status()
			return response.content
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_account(self):
		"""
		Retrieves account details.

		:returns: account
		:raises: HTTPError
		"""

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "account"), headers=headers)

		try:
			response.raise_for_status()
			return Account.parse_json(response.json())
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise

	def get_payments(self):
		"""
		Retrieves account details.

		:returns: account
		:raises: HTTPError
		"""

		#copy of default HTTP headers to use additional headers
		headers = self.default_headers.copy()
		headers["Accept"] = "application/json"
		headers["Cache-Control"] = "no-cache"

		response = requests.request("GET", urljoin(self.api_base_url, "payments"), headers=headers)

		try:
			response.raise_for_status()
			return [Payment.parse_json(payment) for payment in response.json()]
		except HTTPError as err:
			if response.content:
				err.args = (err.args[0] + "; Server Response: \n{}".format(response.content.decode("utf-8")),)
			raise
