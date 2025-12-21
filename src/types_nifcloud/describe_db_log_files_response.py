"""Response type for DescribeDBLogFiles API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class DBLogFile(BaseModel):
    """DB log file information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    log_file_name: Optional[str] = None
    last_written: Optional[int] = None
    size: Optional[int] = None


class DescribeDBLogFilesResponse(BaseModel):
    """Response from DescribeDBLogFiles API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    db_log_files: Optional[list[DBLogFile]] = None
