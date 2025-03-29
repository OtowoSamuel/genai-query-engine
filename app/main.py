import os  
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="GenAI Query Engine")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(
        app,
        host="0.0.0.0",  
        port=port,        
        reload=True if os.getenv("DEV") == "1" else False  
    )