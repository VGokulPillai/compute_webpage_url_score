import requests
import json


class EntityRecognitionLinking:

    class APIError(Exception):

        def __init__(self, status):
            self.status = status

        def __str__(self):
            return "APIError: status={}".format(self.status)

    def entityRecogLink(self, text):

        # Base URL for Spotlight API
        base_url = "http://api.dbpedia-spotlight.org/en/annotate"
        params = {"text": text, "confidence": 0.35}
        headers = {'accept': 'application/json'}
        res = requests.get(base_url, params=params, headers=headers)
        if res.status_code != 200:
            # Something went wrong
            raise APIError(res.status_code)
        print(json.dumps(json.loads(res.text), sort_keys=True, indent=4))
        return json.loads(res.text)
