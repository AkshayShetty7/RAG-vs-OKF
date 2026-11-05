
from pathlib import Path
import yaml

from src.common.document_schema import Document


FOLDER_TYPES = {
    "01_patient_records": "patient_record",

    "02_diseases_guidelines": "disease_guideline",
    "02_diseases_clinical_guidelines": "disease_guideline",

    "03_medications_pharmacy": "medication_pharmacy",

    "04_laboratory_diagnostics": "laboratory_diagnostic",

    "05_hospital_operations": "hospital_operation",
}

def normalize_folder(value: str) -> str:
    folder = str(value).strip().lower()

    aliases = {
        "01_patient_records": "01_patient_records",
        "02_diseases_clinical_guidelines": "02_diseases_guidelines",
        "02_diseases_guidelines": "02_diseases_guidelines",
        "03_medications_pharmacy": "03_medications_pharmacy",
        "04_laboratory_diagnostics": "04_laboratory_diagnostics",
        "05_hospital_operations": "05_hospital_operations",
    }

    return aliases.get(folder, folder)


def parse_markdown_file(file_path: Path) -> Document:
    text = file_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError(f"Missing YAML frontmatter: {file_path}")

    parts = text.split("---", 2)

    if len(parts) != 3:
        raise ValueError(f"Invalid YAML frontmatter: {file_path}")

    metadata = yaml.safe_load(parts[1]) or {}
    content = parts[2].strip()

    if not isinstance(metadata, dict):
        raise ValueError(f"Frontmatter must be a YAML mapping: {file_path}")

    # Support both Claude's doc_id and the original document_id field.
    document_id = metadata.get("document_id") or metadata.get("doc_id")

    if not document_id:
        raise ValueError(f"Missing doc_id/document_id: {file_path}")

    for field in ["title", "folder", "version"]:
        if field not in metadata:
            raise ValueError(f"Missing field '{field}': {file_path}")

    # Accept integral versions such as 1 or 1.0.
    version_value = metadata["version"]

    if isinstance(version_value, bool) or not isinstance(version_value, (int, float)):
        raise ValueError(f"Invalid version: {file_path}")

    if not float(version_value).is_integer():
        raise ValueError(f"Version must be a whole number: {file_path}")

    version = int(version_value)

    # Normalize Claude's folder naming to the project convention.
    folder = normalize_folder(metadata["folder"])

    if folder not in FOLDER_TYPES:
        raise ValueError(
            f"Unknown folder '{metadata['folder']}' in {file_path}"
        )

    # Infer document type from its approved source folder.
    document_type = metadata.get(
        "document_type",
        FOLDER_TYPES[folder]
    )

    sections = []
    current_section = "Introduction"
    section_lines = []
    section_start = 1

    for line_number, line in enumerate(content.splitlines(), start=1):
        if line.startswith("#"):
            if section_lines:
                sections.append({
                    "title": current_section,
                    "start_line": section_start,
                    "end_line": line_number - 1,
                    "text": "\n".join(section_lines).strip(),
                })

            current_section = line.lstrip("#").strip()
            section_lines = [line]
            section_start = line_number
        else:
            section_lines.append(line)

    if section_lines:
        sections.append({
            "title": current_section,
            "start_line": section_start,
            "end_line": len(content.splitlines()),
            "text": "\n".join(section_lines).strip(),
        })

    return Document(
        document_id=str(document_id),
        title=str(metadata["title"]),
        folder=folder,
        document_type=str(document_type),
        version=version,
        content=content,
        file_path=str(file_path),
        sections=sections,
    )


def load_documents(root_dir: str) -> list[Document]:
    root = Path(root_dir)

    if not root.exists():
        raise FileNotFoundError(
            f"Source directory does not exist: {root}"
        )

    documents = []

    for file_path in sorted(root.rglob("*.md")):
        documents.append(parse_markdown_file(file_path))

    return documents
