from fastapi import HTTPException, status



TodoDoesNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Todo doesn't exist"
)

TodoDoesNotUpdated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Todo missing required"
)

TodoDoesNotUpdated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Todo missing required"
)