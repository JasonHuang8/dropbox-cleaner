from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/scrub")
async def scrub(file: UploadFile = File(...)):
    # Dummy passthrough – no real scrubbing here
    return {"filename": file.filename, "status": "scrubbed", "notes": "dummy response"}

# Optional: run directly via `python mock_scrubber/app.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mock_scrubber.app:app", host="127.0.0.1", port=8000, reload=True)
