from models.base_response import BaseResponse

class InferResponse(BaseResponse):
    def __init__(self, payload:dict):
        super().__init__(id="infer", payload=payload)
        self._extract()

    def _extract(self):
        self._content = self._payload[self._id].replace("\\n", "\n")

    @property
    def content(self):
        return self._content

    @property
    def title(self):
        return self._title