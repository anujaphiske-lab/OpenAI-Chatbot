## Enterprise Q&A Chatbot with LangChain & OpenAI
This repository contains a professional-grade Q&A Chatbot built with LangChain, Streamlit, and OpenAI. It features a dynamic user interface that allows users to swap models, adjust creativity parameters, and monitor performance via LangSmith.

🌟 Key Features
- Multi-Model Support: Users can toggle between various OpenAI models (e.g., GPT-5 variants) directly from the UI.
- Dynamic Parameter Tuning: Includes interactive sidebar sliders to control Temperature and Max Tokens in real-time.
- Secure Authentication: Implements a password-protected API key input to ensure user credentials are handled securely and never hardcoded.
- Production Observability: Integrated with LangSmith for full-trace logging, allowing for detailed debugging of the prompt-to-output chain.

🛠️ Tech Stack
- Orchestration: LangChain
- LLM Provider: OpenAI
- Frontend: Streamlit
- Observability: LangSmith
- Environment Management: Python-dotenv
