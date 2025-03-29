from fastapi import APIRouter, Depends, HTTPException
from app.auth import authenticate_user, create_access_token, SECRET_KEY, ALGORITHM
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services import process_query
from app.auth import oauth2_scheme
from pydantic import BaseModel
from jose import JWTError, jwt

class QueryRequest(BaseModel):
    query: str

router = APIRouter()

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/query")
async def query_data(request: QueryRequest, token: str = Depends(verify_token)):
    try:
        result = process_query(request.query)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/explain")
async def explain_query(request: QueryRequest, token: str = Depends(verify_token)):
    result = process_query(request.query)
    return {"explanation": f"Query converted to: {result['pseudo_sql']}"}

@router.post("/validate")
async def validate_query(request: QueryRequest, token: str = Depends(verify_token)):
    if not request.query:
        return {"valid": False, "reason": "Empty query"}
    return {"valid": True, "reason": "Query is processable"}