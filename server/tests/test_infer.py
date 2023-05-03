import pytest
import requests
import json
from services.infer import InferService


@pytest.fixture()
def mock_response(monkeypatch):
    def mock_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, content):
                self.status_code = status_code
                self.content = content

            def json(self):
                return json.loads(self.content)

        return MockResponse(200, '{"bug_type": "syntax error"}')

    monkeypatch.setattr(requests, "post", mock_post)


def test_infer_service_classify(mock_response):
    infer_service = InferService()
    bugged_code = 'def foo():\n    print("Hello, World!"\n'
    bug_type = infer_service.classify(bugged_code)
    assert bug_type == "syntax error"
