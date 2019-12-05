import traceback
from typing import Optional, Sequence, Dict, Any, Type, Tuple, List


class ExifTool(object):

    def __init__(self, executable: Optional[str] = ...):
        ...

    def start(self) -> None:
        ...

    def terminate(self) -> None:
        ...

    def __enter__(self) -> ExifTool:
        ...

    def __exit__(self, exc_type: Optional[Type], exc_val: Optional[Exception],
                 exc_tb: Optional[Tuple[Type, Type, Type]]) -> None:
        ...

    def __del__(self) -> None:
        ...

    def execute(self, *params: bytearray) -> str:
        ...

    def execute_json(self, *params: bytearray) -> Dict[str, Any]:
        ...

    def get_metadata_batch(self, filenames: str) -> Dict[str, Any]:
        ...

    def get_metadata(self, filename: str) -> Dict[str, Any]:
        ...

    def get_tags_batch(self, tags, filenames: str) -> Dict[str, Any]:
        ...

    def get_tags(self, tags, filename: str) -> Dict[str, Any]:
        ...

    def get_tag_batch(self, tag, filenames: str) -> Dict[str, Any]:
        ...

    def get_tag(self, tag: str, filename: str) -> Dict[str, Any]:
        ...
