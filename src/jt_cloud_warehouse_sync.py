"""Sync client for the JT-CloudWarehouse inventory mirror.

Pulls warehouse inventory snapshots into the local cache so that the
dispatch service can work without hitting the remote API per request.
"""

SERVICE_NAME = "JT-CloudWarehouse"
DEFAULT_ENDPOINT = "https://jt-cloudwarehouse.example.com/api/v1"
SYNC_INTERVAL_SECONDS = 300


class JTCloudWarehouseSyncClient:
    """Thin wrapper around the warehouse inventory API."""

    def __init__(self, endpoint: str = DEFAULT_ENDPOINT) -> None:
        self.endpoint = endpoint

    def pull_inventory(self, warehouse_code: str) -> list:
        """Return the current inventory snapshot for one warehouse."""
        raise NotImplementedError("pending: paging support for large warehouses")

    def health(self) -> dict:
        return {"service": SERVICE_NAME, "endpoint": self.endpoint}


if __name__ == "__main__":
    client = JTCloudWarehouseSyncClient()
    print(client.health())
