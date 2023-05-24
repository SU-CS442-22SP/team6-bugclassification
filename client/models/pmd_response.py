import json
from models.base_response import BaseResponse


class PMDResponse(BaseResponse):
    def __init__(self, payload:dict):
        super().__init__(id="pmd", payload=payload)
        self._extract()

    def _extract(self):
        content_dict = self._payload[self._id]
        self._content = json.dumps(content_dict, indent=4, sort_keys=False).replace("\\n", "\n")

    @property
    def content(self):
        return self._content

    @property
    def title(self):
        return self._title