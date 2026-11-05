
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Document:
    document_id: str
    title: str
    folder: str
    document_type: str
    version: int
    content: str
    file_path: str
    sections: list[dict] = field(default_factory=list)


@dataclass
class Evidence:
    document_id: str
    section: str
    start_line: int
    end_line: int
    text: str
    file_path: Optional[str] = None
