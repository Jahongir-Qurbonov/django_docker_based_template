from typing import NotRequired, TypedDict


class SpectacularSettings(TypedDict):
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    SERVE_PERMISSIONS: list[str]
    SCHEMA_PATH_PREFIX: str
    SERVERS: NotRequired[list[dict[str, str]]]


class RestFrameworkSettings(TypedDict):
    DEFAULT_RENDERER_CLASSES: list[str]
    DEFAULT_SCHEMA_CLASS: str
    DEFAULT_PARSER_CLASSES: list[str]
    DEFAULT_PAGINATION_CLASS: str
    PAGE_SIZE: int
    DEFAULT_PERMISSION_CLASSES: list[str]
    DEFAULT_FILTER_BACKENDS: list[str]
    DEFAULT_AUTHENTICATION_CLASSES: NotRequired[list[str]]
