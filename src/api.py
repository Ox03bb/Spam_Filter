import fastapi as api
from typing import Union
from pydantic import BaseModel
import numpy as np

import user

app = api.FastAPI()

class mail(BaseModel):
    data: str

@app.get("/")
def page():
    return {"message": "Hello World"}


@app.post("/test/")
async def read_item(txt: mail = None ):
   
    pred = int(user.predict(txt.data))
    proba= float(user.predict_proba(txt.data)[1])
   
    return {"predction": pred, "probability of spam": "{:.2f}".format(proba) }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)