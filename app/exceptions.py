from fastapi import HTTPException, status



TodoDoesNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="todo doesn't exist"
)

TodoDoesNotUpdated = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="todo missing required"
)