"""
Base Pydantic model for all request/response models.

Usage:
    from lib.models.base import BaseSchema

    class CreateDocumentRequest(BaseSchema):
        author_id: str = Field(alias="authorId")
        name: str = Field(default_factory=lambda: f"doc_{uuid.uuid4()}")
"""

from json import JSONDecodeError
from typing import Any, Dict, List, Optional, TypeVar, Generic

from pydantic import BaseModel, ConfigDict, Field
from requests import Response



class BaseSchema(BaseModel):
    """
    Base model with common configuration for all API models.

    Features:
    - Serialization excludes None values by default
    - Supports both camelCase (API) and snake_case (Python) field names
    - Validates on assignment
    - Allows population by field name or alias
    """

    model_config = ConfigDict(
        # Allow population by both field name and alias
        populate_by_name=True,
        # Validate default values
        validate_default=True,
        # Allow extra fields (useful for API responses with unknown fields)
        extra="ignore",
        # Use enum values instead of enum objects
        use_enum_values=True,
        # Strip whitespace from strings
        str_strip_whitespace=True,
    )

    def to_dict(self, exclude_none: bool = False, by_alias: bool = True) -> Dict[str, Any]:
        """
        Convert model to dictionary for API requests.

        Args:
            exclude_none: Remove fields with None values (default: False)
            by_alias: Use field aliases (camelCase) in output (default: True)

        Returns:
            Dictionary representation of the model
        """
        return self.model_dump(exclude_none=exclude_none, by_alias=by_alias)

    def to_json(self, exclude_none: bool = False, by_alias: bool = True) -> str:
        """
        Convert model to JSON string for API requests.

        Args:
            exclude_none: Remove fields with None values (default: False)
            by_alias: Use field aliases (camelCase) in output (default: True)

        Returns:
            JSON string representation of the model
        """
        return self.model_dump_json(exclude_none=exclude_none, by_alias=by_alias)

    @classmethod
    def from_response(cls, data: Dict[str, Any]) -> "BaseSchema":
        """
        Create model instance from API response data.

        Args:
            data: Dictionary from API response

        Returns:
            Model instance
        """
        return cls.model_validate(data)


class BaseRequestSchema(BaseSchema):
    """Base model for API request payloads."""
    pass


class BaseResponseSchema(BaseSchema):
    """
    Base model for API response data.

    More lenient validation for handling various API response formats.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_default=True,
        extra="ignore",
        use_enum_values=True,
        # Don't fail on unknown types in responses
        arbitrary_types_allowed=True,
    )


T = TypeVar("T", bound=BaseResponseSchema)


class BaseResponseModel(BaseModel, Generic[T]):
    """
    Pydantic-based response model that wraps API responses.

    Usage:
        class LoginResponseModel(BaseResponseModel[LoginModel]):
            pass

        resp = api.post("/auth/login", json=payload)
        result = LoginResponseModel.from_response(resp)
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status_code: int
    reason: Optional[str]
    payload: Optional[Any] = None
    data: Optional[T] = None
    meta: Optional[Dict[str, Any]] = None
    linked: Optional[Dict[str, Any]] = None
    errors: Optional[Any] = None
    response_status: Optional[str] = None

    @classmethod
    def from_response(cls, resp: Response) -> "BaseResponseModel[T]":
        """Create model instance from requests.Response."""
        try:
            payload = resp.json()
        except JSONDecodeError:
            payload = resp.text

        data_raw = None
        meta = None
        linked = None
        errors = None
        response_status = None

        if isinstance(payload, dict):
            data_raw = payload.get("data")
            meta = payload.get("meta")
            linked = payload.get("linked")
            response_status = payload.get("responseStatus")
            errors = payload.get("errors") or payload.get("error")

        return cls(
            status_code=resp.status_code,
            payload=payload,
            reason=resp.reason,
            data=data_raw,
            meta=meta,
            linked=linked,
            errors=errors,
            response_status=response_status,
        )


class ListResponseModel(BaseModel, Generic[T]):
    """
    Pydantic-based response model for list responses.

    Usage:
        class LoginsResponseModel(ListResponseModel[LoginModel]):
            pass
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status_code: int
    payload: Optional[Any] = None
    data: Optional[List[T]] = None
    meta: Optional[Dict[str, Any]] = None
    linked: Optional[Dict[str, Any]] = None
    errors: Optional[Any] = None
    response_status: Optional[str] = None

    @classmethod
    def from_response(cls, resp: Response) -> "ListResponseModel[T]":
        """Create model instance from requests.Response."""
        try:
            payload = resp.json()
        except JSONDecodeError:
            payload = resp.text

        data_raw = None
        meta = None
        linked = None
        errors = None
        response_status = None

        if isinstance(payload, dict):
            data_raw = payload.get("data")
            meta = payload.get("meta")
            linked = payload.get("linked")
            response_status = payload.get("responseStatus")
            errors = payload.get("errors") or payload.get("error")

        return cls(
            status_code=resp.status_code,
            payload=payload,
            data=data_raw,
            meta=meta,
            linked=linked,
            errors=errors,
            response_status=response_status,
        )
