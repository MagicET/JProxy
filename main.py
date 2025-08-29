from openai import OpenAI, OpenAIError
from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://janitorai.com"],
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/proxy")
async def callApi(reqest: Request, url: str, Authorization: str = Header("None")):
    def openai_stream_caller(data, url, key):
        try:
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
            
            return completion
        except OpenAIError as e:
            raise HTTPException(status_code=e.status_code, detail=str(e.body))
    
    def completion_generator(completion):
        for chunk in completion:
                yield "data: " + chunk.json() + "\n\n"

    data = await reqest.json()

    key = Authorization.replace("Bearer ", "")

    try:
        completion = openai_stream_caller(data, url, key)
    except HTTPException as e:
        raise e
    else:
        return StreamingResponse(completion_generator(completion), media_type="text/event-stream")
