from fastapi import FastAPI

from controllers.hello_controller import router as hello_router


app = FastAPI()

app.include_router(hello_router, prefix="")


if __name__ == "__main__":
    # Minimal local runner for quick checks; use uvicorn for production/dev server
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
