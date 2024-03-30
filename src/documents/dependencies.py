from fastapi import File, HTTPException, UploadFile


async def validate_file_extension(file: UploadFile = File(...)):
    allowed_mimes = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]
    if file.content_type not in allowed_mimes:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    return file
