from .job_status import JobStatus

class Job():
	def __init__(
					self,
					job_id,
					name,
					language,
					duration,
					status,
					created,
					completed):
			"""
			:param job_id: unique identfication of job
			:param name: name of job
			:param language: language of speech
			:param duration: duration of speech
			:param status: current status of job. Can be one of: WAITING, PREPARING, PROCESSING, TRANSCRIBING, READY, FAILED
			:param created: creation time of job
			:param completion time of job
			"""

			self.id = job_id
			self.name = name
			self.language = language
			self.duration = duration
			self.status = status
			self.created = created
			self.completed = completed

	def dump_json(self):
		"""Makes JSON description of job"""
		json_desc = '{\n'
		json_desc += '\t\"id\": ' + str(self.id) + ',\n'
		json_desc += '\t\"name\": \"' + self.name + '\",\n'
		json_desc += '\t\"lamguage\": \"' + self.language + '\",\n'
		if self.duration is not None:
			json_desc += '\t\"duration\": ' + str(self.duration) + ',\n'
		json_desc += '\t\"status\": \"' + self.status.to_string() + '\",\n'
		json_desc += '\t\"created\": \"' + self.created
		if self.completed is not None:
			json_desc += '\",\n\t\"completed\": \"' + self.completed + '\"\n'
		else:
			json_desc += '\"\n'
		json_desc += "}"
		return json_desc

	@classmethod
	def parse_json(cls, json):
		"""Creates instance from JSON"""
		return cls(
			json["id"],
			json["name"],
			json["language"],
			json.get("duration"),
			JobStatus.from_string(json["status"]),
			json["created"],
			json.get("completed")
		)
