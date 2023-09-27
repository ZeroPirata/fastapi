from settings.config import settings, start_application
import uvicorn

app = start_application()

@app.get("/")
def inidex():
    return { "message" : f"Wellcome to {settings.PROJECT_NAME} in version {settings.PROJECT_VERSION}" }

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")