# JProxy

This is a proxy server service for JanitorAI to bypass CORS error of strict LLM APIs like NVIDIA NIM or Vercel AI Gateway.

---

## How to use

### NVIDIA NIM

General Information:

* Limit: 40 requests per minute
* Can't be access directly from JanitorAI due to CORS error
* Free **for prototyping, research, development, testing, learning**, note that using for JAI is **outside the scope of the purpose**

Steps to use:

1.  Go to https://build.nvidia.com/, create an account and get the API key.
    1.  Press "Login" button and enter your Email id
    2.  Fill out the form, read ToS and Privacy Policy, finish the Email verification and create an account.
    3.  Press the account icon on the top right and go to [API Key](https://build.nvidia.com/settings/api-keys) page.
    4.  Press "Generate API Key" button, enter the name and the expiration.
    5.  Keep the key somewhere safely. You will use it in the next step.
2.  Choose the model you use.
    * You can browse for models in this page: https://build.nvidia.com/models
    * Model Recommendations: 

        * `deepseek-ai/deepseek-v3.1`
                                        [Model Page](https://build.nvidia.com/deepseek-ai/deepseek-v3_1/modelcard)
        * `qwen/qwen3-235b-a22b`
                                        [Model Page](https://build.nvidia.com/qwen/qwen3-235b-a22b/modelcard)
        * `mistralai/mistral-medium-3-instruct`
                                        [Model Page](https://build.nvidia.com/mistralai/mistral-medium-3-instruct/modelcard)
        * `openai/gpt-oss-120b` (censored)
                                        [Model Page](https://build.nvidia.com/openai/gpt-oss-120b/modelcard)
        * `moonshotai/kimi-k2-instruct`
                                        [Model Page](https://build.nvidia.com/moonshotai/kimi-k2-instruct/modelcard)
3.  Go to JanitorAI, add a new proxy configuration.
4.  Fill out the settings.
    * ![](https://github.com/user-attachments/assets/39e59e94-a1b7-401f-aa92-4aa3070d2bff)

    * Configuration Name: As you want
    * Model Name: One of the model names I said above or from the official page
    * **Proxy URL:**
                            `https://jproxy.onrender.com/proxy?url=https://integrate.api.nvidia.com/v1`

        * This is the most important part, insert the URL of the API service after `?url=`, and
                                        `/chat/completions` is not needed
    * API Key: Your API key from the service
    * Custom Prompt: pls someone tell me a good custom prompt
5.  Choose options. (optional)
    * You can add options to the Proxy URL.
        * `reasoning=force`

            * The `<think>` section will be visible. If you're using models with both reasoning and
                                                        non-reasoning modes like DeepSeek-V3.1, this option forces them to enable reasoning. To use it, add
                                                        `&reasoning=force` to the end of the Proxy URL.

            * The full URL will be like this:   
                `https://jproxy.onrender.com/proxy?url=https://integrate.api.nvidia.com/v1&reasoning=force`
        * `reasoning=visible`

            * The `<think>` section will be visible. Unlike `reasoning=force`, this option
                                                        doesn't force to enable reasoning. To use it, add
                                                        `&reasoning=visible` to the end of the Proxy URL.
            * The full URL will be like this:   
                `https://jproxy.onrender.com/proxy?url=https://integrate.api.nvidia.com/v1&reasoning=visible`

---

### Vercel AI Gateway

* Limit: monthly $5 credit
* Can't be access directly from JanitorAI due to CORS error
* You can test many proprietary flagship models singlehandedly

Steps to use:

1.  Go to https://vercel.com/, create an account and get the API key.
    * Create an account. You can use Google, Github, GitLab, or BitBucket.
    * Go to Dashboard, select AI Gateway, and press Create an API Key.
2.  Choose the model you use.
    * You can browse for models in this page: https://vercel.com/ai-gateway/models
    * Models for example: 

        * `deepseek/deepseek-v3.1`
                                        [Model Page](https://vercel.com/ai-gateway/models/deepseek-v3.1)
        * `google/gemini-2.5-pro`
                                        [Model Page](https://vercel.com/ai-gateway/models/gemini-2.5-pro)
        * `anthropic/claude-opus-4`
                                        [Model Page](https://vercel.com/ai-gateway/models/claude-opus-4)
        * `xai/grok-4`
                                        [Model Page](https://vercel.com/ai-gateway/models/grok-4)
3.  Go to JanitorAI, set up a new Proxy configuration.
    * The rest is the same.
    * Proxy URL: `https://jproxy.onrender.com/proxy?url=https://ai-gateway.vercel.sh/v1`
    * Don't forget not to write `/chat/completions`.

### Other Proxy Services

You can use other Proxy services as well. All you need is to use the URL: `https://jproxy.onrender.com/proxy?url=<Proxy service's URL>`

---

Thank you for using!

* My Reddit Account if you want to contact me: 
                https://www.reddit.com/user/Magicet-12/
* Create an issue if you find a bug or want to request a new feature: 
                https://github.com/MagicET/JProxy
* My other project, a browser extension to improve the experience of JanitorAI:
                https://github.com/MagicET/Custodian

    * Features

    * Light theme
    * Showing images from catbox.moe on bots' description
    * Hiding the header when chatting
    * Maximizing the textbox when chatting
    * Changing the color of the text when editing back to white

* Built with [Render.com](https://render.com/). Thanks!