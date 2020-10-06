from fastapi import FastAPI
import uvicorn

from app.resources import users, DeleteApi, PutAPI, PostAPI, PatchAPI, FileUploadAPI, FileDownloadAPI

CONTEXT_PATH = "/myapp"

app = FastAPI(title="My Demo Project using Python FastAPI",
              description="This is an example project which uses Python FastAPI",
              version="1.0.0",
              )

app.include_router(users.router)
app.include_router(DeleteApi.router, prefix=CONTEXT_PATH)
app.include_router(PutAPI.router, prefix=CONTEXT_PATH)
app.include_router(PostAPI.router, prefix=CONTEXT_PATH)
app.include_router(PatchAPI.router, prefix=CONTEXT_PATH)
app.include_router(FileUploadAPI.router, prefix=CONTEXT_PATH)
app.include_router(FileDownloadAPI.router, prefix=CONTEXT_PATH)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
