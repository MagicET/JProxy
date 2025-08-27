from openai import OpenAI
from fastapi import FastAPI, Request, Header
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://janitorai.com"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["authorization, content-type"],
)

def openai_stream_generator(data, url, key):
    client = OpenAI(
        base_url = url,
        api_key = key
    )

    completion = client.chat.completions.create(
        model=data.get("model"),
        messages=data.get("messages"),
        temperature=data.get("temperature"),
        stream=data.get("stream")
    )

    for chunk in completion:
        yield "data: " + chunk.json() + "\n\n"

@app.post("/proxy")
async def callApi(reqest: Request, url: str, Authorization: str = Header("None")):
    data = await reqest.json()
    
    key = Authorization.replace("Bearer ", "")

    return StreamingResponse(openai_stream_generator(data, url, key), media_type="text/event-stream")
