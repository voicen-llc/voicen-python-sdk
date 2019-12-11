from enum import Enum

class JobStatus(Enum):
	WAITING = -1
	PREPARING = 0
	PROCESSING = 1
	TRANSCRIBING = 2
	READY = 3
	FAILED = 4

	def to_string(self):
		return self.name.lower()

	@classmethod
	def from_string(cls, status):
		return cls[status.upper()]
