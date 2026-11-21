from fastapi import FastAPI, HTTPException
from app.models import InventoryItem

# Initialize the FastAPI application
app = FastAPI(
    title="Player Inventory API",
    description="A microservice for managing game player inventories and assets.",
    version="1.0.0"
)

# Fake in-memory database to store inventories (player_id -> list of items)
fake_database: dict[str, list[InventoryItem]] = {}


@app.get("/")
async def root() -> dict:
    """Health check endpoint."""
    return {"status": "online", "message": "Player Inventory API is running."}


@app.post("/inventory/{player_id}/add")
async def add_item(player_id: str, item: InventoryItem) -> dict:
    """
    Adds a new item to a player's inventory.
    If the player doesn't exist, it creates a new inventory for them.
    """
    if player_id not in fake_database:
        fake_database[player_id] = []

    fake_database[player_id].append(item)
    return {"status": "success", "message": f"Item '{item.name}' added to player {player_id}."}


@app.get("/inventory/{player_id}")
async def get_inventory(player_id: str) -> list[InventoryItem]:
    """
    Retrieves the full inventory of a specific player.
    """
    if player_id not in fake_database:
        raise HTTPException(status_code=404, detail="Player inventory not found.")

    return fake_database[player_id]


@app.delete("/inventory/{player_id}/remove/{item_id}")
async def remove_item(player_id: str, item_id: str) -> dict:
    """
    Removes a specific item from a player's inventory.
    Demonstrates senior-level error handling.
    """
    # Tratamento de Erro 1: O jogador nem sequer existe
    if player_id not in fake_database:
        raise HTTPException(status_code=404, detail=f"Player '{player_id}' not found.")

    # Procurar o item específico no inventário do jogador
    inventory = fake_database[player_id]
    for index, item in enumerate(inventory):
        if item.item_id == item_id:
            # Remove o item e retorna mensagem de sucesso
            inventory.pop(index)
            return {"status": "success", "message": f"Item '{item_id}' removed from player {player_id}."}

    # Tratamento de Erro 2: O jogador existe, mas não tem este item
    raise HTTPException(status_code=404, detail=f"Item '{item_id}' not found in player '{player_id}' inventory.")