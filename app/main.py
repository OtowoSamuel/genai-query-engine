import os  # <-- Add this import at the top
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="GenAI Query Engine")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # <-- Critical Railway compatibility
    uvicorn.run(
        app,
        host="0.0.0.0",  # Required for Docker/Railway
        port=port,        # Now handles both local and production
        reload=True if os.getenv("DEV") == "1" else False  # Optional: Auto-reload in dev
    )