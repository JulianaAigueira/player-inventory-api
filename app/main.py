from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="Player Inventory API",
    description="A microservice for managing game player inventories and assets.",
    version="1.0.0"
)

@app.get("/")
async def root() -> dict:
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "online", "message": "Player Inventory API is running."}