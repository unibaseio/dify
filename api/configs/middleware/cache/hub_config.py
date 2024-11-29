from pydantic import Field
from pydantic_settings import BaseSettings


class HubConfig(BaseSettings):
    """
    Configuration settings for HUB connection
    """

    HUB_ENDPOINT: str = Field(
        description="Hostname or IP address of the HUB server",
        default="http://localhost:8080",
    )

