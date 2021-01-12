import os

import uvicorn
from fastapi import FastAPI

from app.api.v1.api_router import api_router


app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    debug: bool = True if os.getenv("ENV", "dev") == "dev" else False
    port: int = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=debug, debug=debug)
