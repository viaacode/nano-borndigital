import pytest


@pytest.fixture
def mock_ftp(monkeypatch):
    def mock_connect(self):
        print(f"Connecting to host.")
        pass

    def mock_put(self, content_bytes, destination_path, destination_filename):
        print(f"Putting {destination_filename} to {destination_path} on {self.host}")
        pass

    from meemoo.helpers import FTP

    monkeypatch.setattr(FTP, "put", mock_put)
    monkeypatch.setattr(FTP, "_FTP__connect", mock_connect)


@pytest.fixture
def mock_organisations_api(monkeypatch):
    def mock_get_organisation(self, or_id):
        print(f"getting name for {or_id}")
        return {"cp_name_mam": "UNITTEST"}

    from meemoo.services import OrganisationsService

    monkeypatch.setattr(OrganisationsService, "get_organisation", mock_get_organisation)


@pytest.fixture
def mock_events(monkeypatch):
    def mock_init(self, name, ctx):
        print(f"Initiating Rabbit connection.")
        pass

    def mock_publish(self, message, correlation_id):
        print(f"Publish message: {message}")
        pass

    from meemoo.events import Events

    monkeypatch.setattr(Events, "__init__", mock_init)
    monkeypatch.setattr(Events, "publish", mock_publish)


@pytest.fixture
def mock_mediahaven_api(monkeypatch):
    def mock_get_token(self):
        print("Getting token.")
        return {"access_token": "bearer, bear with me"}

    def mock_get_fragment(self, query_params):
        print("Get fragment")
        return {
            "MediaDataList": [
                {"Dynamic": {"PID": "pid"}, "Internal": {"FragmentId": "ID"}}
            ]
        }

    def mock_update_metadata(self, fragment_id: str, sidecar: str):
        print("Update metadata")
        pass

    from meemoo.services import MediahavenService

    monkeypatch.setattr(MediahavenService, "_MediahavenService__get_token", mock_get_token)
    monkeypatch.setattr(MediahavenService, "get_fragment", mock_get_fragment)
    monkeypatch.setattr(MediahavenService, "update_metadata", mock_update_metadata)
