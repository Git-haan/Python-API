from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

# To run the server, use the following command:
# uvicorn main:app --reload

app = FastAPI()

class Athlete(BaseModel):
    name: str
    favorite: bool
    rank: Optional[int] = None

class UpdateAthlete(BaseModel):
    name: Optional[str] = None
    favorite: Optional[bool] = None
    rank: Optional[int] = None

inventory = {
    # 1: {
    #     "player": "Novak Djokovic",
    #     "favorite": False,
    #     "rank": "1"
    # }
}


# GET
@app.get("/get-player/{player_id}")
# Uses A Path Parameter
def get_player(player_id: int = Path(..., description="The ID of the player you want to view")):
    if player_id not in inventory:
        raise HTTPException(status_code=404, detail="Player ID does not exists")
    else:
        return inventory[player_id]

@app.get("/get-name")
# Uses A Query Parameter
def get_name(name: str = Query(None, title="Name", description="Name of the player")):
    for player_id in inventory:
        if inventory[player_id].name == name:
            return inventory[player_id]
    
    raise HTTPException(status_code=404, detail="Player not found")


# POST
@app.post("/create-player/{player_id}")
def create_item(player_id: int, player: Athlete):
    if player_id in inventory:
        raise HTTPException(status_code=400, detail="Player ID already exists")
    
    inventory[player_id] = player
    return inventory[player_id]


# PUT
@app.put("/update-player/{player_id}")
def update_player(player_id: int, player: UpdateAthlete):
    if player_id not in inventory:
        raise HTTPException(status_code=404, detail="Player ID does not exists")
    
    if player.name != None:
        inventory[player_id].name = player.name
    if player.favorite != None:
        inventory[player_id].favorite = player.favorite
    if player.rank != None:
        inventory[player_id].rank = player.rank
    return inventory[player_id]


# DELETE
@app.delete("/delete-player/{player_id}")
def delete_player(player_id: int):
    if player_id not in inventory:
        raise HTTPException(status_code=404, detail="Player ID does not exists")
    
    del inventory[player_id]
    return {"Message": "Player has been deleted"}