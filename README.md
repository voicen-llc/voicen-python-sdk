# Voicen Python SDK

## Documentation

This is Python SDK to use Speech-to-text service of Voicen. To see more about
API visit to [API Documentation](https://voicen.com/en/api/). You are free to
develop your own SDK for different languages using Voicen API documentation.

## Installation

You can install SDK direct from pip repository running this command:

    pip install --upgrade voicen-python-sdk

You can also install from source code:

    python setup.py install --user

### Requirements

- Python 2.7+ or Python 3.4+

## Usage

Before using this SDK you must have an Access Token. To get Access Token visit
to [API Token](https://voicen.com/en/user/api/) page. There is an Access Token
generated for you. Use this Access Token to create your client:

```python
from voicen import vcnclient
# create your client
voicen_client = vcnclient.VoicenClient('ACCESS_TOKEN')
```

### Sending a file

Once you have set up your client with your Access Token you can send a file to
transcribe. You also must specify language of speech.

```python
#send a file to transcribe
job = voicen_client.create_job_with_local_file('PATH_TO_FILE', 'LANGUAGE')
```

### Sending media url

Once you have set up your client with your Access Token you can send a media URL
to transcribe. For example you can use youtube URL as a media URL. You also must
specify language of speech.

```python
#send a media URL to transcribe
job = voicen_client.create_job_with_media_url('MEDIA_URL', 'LANGUAGE')
```

### Checking status of job

You can check status of job using its `id`

```python
#get job details
job_details = voicen_client.get_job(job.id)
```

### Getting list of jobs

You can get list of jobs.

```python
#get list of jobs
jobs = voicen_client.get_jobs()

#limit number of jobs in the list
jobs = voicen_client.get_jobs(limit=50)

#get jobs starting after the certain job id
jobs = voicen_client.get_jobs(start_after=1203)
```

### Deleting job

You can delete job using its `id`

```python
#delete job
voicen_client.delete_job(job.id)
```

### Getting your transcription

You can get your transcription in these formats:

- json
- text
- srt(SubRip Text)
- Microsoft Word

```python
#get your transcription as a json
#returns Transcription object
transcription = voicen_client.get_transcription(job.id)

#get your transcription as a text
#return string
transcription_text = voicen_client.get_transcription_as_text(job.id)

#get your transcription as a srt
#returns string
transcription_srt = voicen_client.get_transcription_as_srt(job.id)

#get your transcription as ms word
#returns byte array
transcription_msword = voicen_client.get_transcription_as_msword(job.id)
```

### Getting account details

You can get you account email and balance in seconds.

```python
#get account
account = voicen_client.get_account()
```

### Getting payment details

You can get your payment details.

```python
#get payment details
payment = voicen_client.get_payments()
```
