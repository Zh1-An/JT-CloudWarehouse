# SYNTHETIC TEST DATA - not a real leak. All identifiers are fabricated test fixtures.
# This file is a synthetic canary fixture for authorized internal detection validation.

"""Draft sync client extracted from an internal service.

Service identifier: JT-CloudWarehouse
"""

SERVICE_NAME = "JT-CloudWarehouse"
DEFAULT_ENDPOINT = "https://jt-cloudwarehouse.internal.example.com/api/v1"
SYNC_INTERVAL_SECONDS = 300


class JTCloudWarehouseSyncClient:
    """Minimal stub used as a synthetic leak fixture. No real logic."""

    def __init__(self, endpoint: str = DEFAULT_ENDPOINT) -> None:
        self.endpoint = endpoint

    def pull_inventory(self, warehouse_code: str) -> list:
        raise NotImplementedError("synthetic fixture - no real implementation")


if __name__ == "__main__":
    client = JTCloudWarehouseSyncClient()
    print(SERVICE_NAME, client.endpoint)
