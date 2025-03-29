from fastapi import APIRouter, Depends, HTTPException
from app.auth import authenticate_user, create_access_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services import process_query
from app.auth import oauth2_scheme
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/query")
async def query_data(request: QueryRequest, token: str = Depends(oauth2_scheme)):
    try:
        result = process_query(request.query)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/explain")
async def explain_query(request: QueryRequest, token: str = Depends(oauth2_scheme)):
    result = process_query(request.query)
    return {"explanation": f"Query converted to: {result['pseudo_sql']}"}

@router.post("/validate")
async def validate_query(request: QueryRequest, token: str = Depends(oauth2_scheme)):
    if not request.query:  # Note: access through request.query
        return {"valid": False, "reason": "Empty query"}
    return {"valid": True, "reason": "Query is processable"}