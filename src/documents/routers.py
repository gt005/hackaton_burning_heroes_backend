import tempfile

from fastapi import APIRouter, Depends, UploadFile

from src.documents.utils import extract_text_from_docx, extract_text_from_pdf
from src.documents.dependencies import validate_file_extension


documents_v1_router = APIRouter(tags=['documents'])


@documents_v1_router.post('/')
async def create_text_from_document(file: UploadFile = Depends(validate_file_extension)) -> str:
    content_type = file.content_type

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = f"{temp_dir}/{file.filename}"

        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        if content_type == "application/pdf":
            text = extract_text_from_pdf(temp_file_path)
        else:
            text = extract_text_from_docx(temp_file_path)

    return text
