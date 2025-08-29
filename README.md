# JProxy
This is a proxy server for JanitorAI to bypass CORS errors of strict LLM APIs like NVIDIA NIM and Vercel AI Gateway.

# How to use (NVIDIA NIM for example)
1. Go to https://build.nvidia.com/ and follow the instruction of getting API key.

2. Choose the model you use.
    - Recommendations: deepseek-ai/deepseek-v3.1, qwen/qwen3-235b-a22b, mistralai/mistral-medium-3-instruct, openai/gpt-oss-120b (censored)

4. Go to JanitorAI, add a new proxy configuration.

5. Insert the informations
    - ![IMG_2467](https://github.com/user-attachments/assets/39e59e94-a1b7-401f-aa92-4aa3070d2bff)
    - Configuration Name: As you want
    - Model Name: One of the model names I said above or from the official page
    - **Proxy URL: https://jproxy.onrender.com/proxy?url=https://integrate.api.nvidia.com/v1**
        - This is the most important part, insert the URL of the API service after `?url=`, and `/chat/completions` is not needed
    - API Key: Your API key from the service
    - Custom Prompt: pls someone tell me a good custom prompt

That's it. All you need is use the weird proxy URL. This will basically work for any API services.

Reddit Account if you want to contact: https://www.reddit.com/user/Magicet-12/

Built with Render.com. Thanks!
