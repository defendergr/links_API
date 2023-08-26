import uvicorn

if __name__ == "__main__":
    uvicorn.run('Api.main:app', port=8030, reload=True)
