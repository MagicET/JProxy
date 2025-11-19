from openai import OpenAI, OpenAIError
from fastapi import FastAPI, Request, Response, Header, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/")
async def root():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET"
    }
    with open("index.html", "r", encoding="utf-8") as html:
        return HTMLResponse(content=html.read(), headers=headers)

@app.get("/proxy")
async def redirect_to_root():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET"
    }
    return RedirectResponse(url="/", headers=headers)

@app.options("/proxy")
async def preflight_handler():
    headers = {
        "Access-Control-Allow-Origin": "https://janitorai.com",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Authorization, Content-Type",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Max-Age": "600"
    }
    return Response(headers=headers)

@app.post("/proxy")
async def callApi(request: Request, url: str, reasoning: str = "hidden", Authorization: str = Header("None")):
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
                stream=data.get("stream"),
                extra_body={"chat_template_kwargs": {"thinking":True}} if reasoning == "force" else {},
            )
            
            return completion
        except OpenAIError as e:
            raise HTTPException(status_code=e.status_code, detail=str(e.body))
    
    def completion_generator(completion):
        is_in_reasnoning = False

        for chunk in completion:
                if reasoning == "visible" or reasoning == "force":
                    if getattr(chunk.choices[0].delta, "reasoning_content", None) is not None:
                        if not is_in_reasnoning:
                            is_in_reasnoning = True
                            yield 'data: {"choices":[{"delta":{"content":" <think>"}}]}\n\n'
                        chunk.choices[0].delta.content = chunk.choices[0].delta.reasoning_content
                    else:
                        if is_in_reasnoning:
                            is_in_reasnoning = False
                            yield 'data: {"choices":[{"delta":{"content":" </think>"}}]}\n\n'
                yield "data: " + chunk.model_dump_json() + "\n\n"

    data = await request.json()

    key = Authorization.replace("Bearer ", "")

    headers = {
        "Access-Control-Allow-Origin": "https://janitorai.com",
        "Access-Control-Allow-Credentials": "true"
    }

    try:
        completion = openai_stream_caller(data, url, key)
    except HTTPException as e:
        e.headers = headers
        raise e
    else:
        return StreamingResponse(completion_generator(completion), media_type="text/event-stream", headers=headers)

@app.options("/proxy/blank")
async def blank_preflight_handler():
    return Response(
        headers = {
        "Access-Control-Allow-Origin": "https://janitorai.com",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Authorization, Content-Type",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Max-Age": "600"
        }
    )

@app.post("/proxy/blank")
async def returnBlank(request: Request, text: str = "placeholder"):
    def streaming_generator():
        yield 'data: {"choices":[{"delta":{"content":"' + text + '"}}]}\n\n'

    return StreamingResponse(
        content = streaming_generator(),
        media_type = "text/event-stream", 
        headers = {
            "Access-Control-Allow-Origin": "https://janitorai.com",
            "Access-Control-Allow-Credentials": "true"
        }
    )

