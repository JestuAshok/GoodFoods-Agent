# GoodFoods
Agentic AI restaurant reservation system using Grok(Llama 3), FastAPI backend, and Streamlit UI with tool-based execution and guardrails.


```markdown
# 🍽️ GoodFoods Reservation System (Agentic AI using Groq + LLaMA)

## 🚀 Overview

GoodFoods is a conversational AI reservation assistant that helps users discover restaurants and book tables across Bangalore.

The system uses **Groq’s ultra-fast LLaMA inference** to power an Agentic AI workflow that can:

- 🔍 Search restaurants based on cuisine/location
- 🧠 Decide when to use backend tools
- 📅 Collect reservation details
- ✅ Validate party size constraints
- 🎟️ Confirm bookings instantly

This project demonstrates a full end-to-end **Agentic AI architecture** integrating:

- ⚡ Groq (LLaMA model)
- 🧠 Tool-calling agent loop
- ⚙️ FastAPI backend (execution layer)
- 💬 Streamlit chat UI
- 📂 JSON-based prototype database

---

## 🏗️ System Architecture

```

User (Streamlit UI)
↓
Conversation Engine (Groq LLaMA + Tools)
↓
FastAPI Backend (Execution Layer)
↓
JSON Data Store (Restaurants + Bookings)

```

### 🔄 Agent Loop

1. User sends message via Streamlit
2. LLaMA model plans response and may generate a tool call
3. Tool executes through FastAPI
4. Tool result is appended to conversation
5. Model generates final assistant response

This two-step reasoning loop prevents hallucination and ensures grounded execution.

---

## 📂 Repository Structure

```

GoodFoods/

│
├── app_goodfoods.py              # Streamlit frontend UI

├── start.py                      # One-command launcher

│
├── agent/

│   ├── conversation_engine.py    # Core agent logic

│   ├── toolkit.py                # Tool schemas

│   └── prompt_library.py         # System prompt + guardrails

│
├── data/

│   ├── service_api.py            # FastAPI backend

│   ├── restaurant_list.json      # Restaurant catalog

│   └── bookings_list.json        # Reservation storage

│
├── requirements.txt

└── README.md

````

---

## 🛠️ Tools (Function-Calling Style)

### 1️⃣ lookup_dining_options

Search restaurants by:
- name
- location
- cuisine

Returns ranked restaurant matches.

---

### 2️⃣ confirm_table_booking

Create reservation using:
- restaurant_id
- orderer_name
- orderer_contact
- party_size
- reservation_date
- reservation_time

Includes:
- Capacity validation guardrail
- Order ID generation
- Booking persistence

---

## 🧠 Prompt Engineering Strategy

- Clear role definition (GoodFoods Bangalore Assistant)
- Step-by-step task flow: discover → collect details → confirm
- Tool usage guidance
- Guardrails against hallucination
- Friendly conversational tone
- Structured behavior for missing information

---

## 📊 Business Problem

Manual reservation workflows are:
- Slow
- Expensive
- Inconsistent

### 💡 Solution

An AI-powered reservation assistant that:
- Automates discovery
- Collects booking details conversationally
- Validates constraints
- Confirms instantly

### 📈 Business Value

- Increased booking conversion
- Reduced staffing costs
- Faster time-to-book
- 24/7 automation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd GoodFoods
````

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5️⃣ Run the application

```bash
python start.py
```

This launches:

* FastAPI backend
* Streamlit frontend

---

## 🔌 API Endpoints

### POST /restaurants/search

Search restaurant catalog by filters.

### POST /reservations

Create reservation with validation.

---

## 🧩 Limitations

* JSON-based prototype storage
* No cancellation or modification of reservations
* No advanced time-slot validation
* Sequential tool execution only
* No authentication layer

---

## 🚀 Future Enhancements

* PostgreSQL database integration
* Parallel multi-tool planning
* Reservation modification & cancellation
* Menu-level RAG integration
* Authentication & rate limiting
* Docker + Cloud deployment

---

## 🧠 Technologies Used

* Python 3.9+
* Groq API (LLaMA model)
* FastAPI
* Streamlit
* Pydantic
* Requests
* Uvicorn

---

## 🎯 Why This Project Matters

This project demonstrates:

* Agentic AI system design
* Tool-calling architecture
* LLM + backend integration
* Guardrail implementation
* Modular scalable architecture
* Real-world business workflow modeling

