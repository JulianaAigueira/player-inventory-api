from pydantic import BaseModel, Field

class InventoryItem(BaseModel):
    """
    Schema for an item in the player's inventory.
    Demonstrates strict typing and data validation.
    """
    item_id: str = Field(..., description="The unique identifier for the item (e.g., 'sword_01')")
    name: str = Field(..., description="The display name of the item")
    quantity: int = Field(default=1, ge=1, description="Quantity must be at least 1")
    category: str = Field(default="general", description="Category: weapon, armor, potion, or general")