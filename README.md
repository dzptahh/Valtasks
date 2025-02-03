# Valorant Agents Info App

## 🎯 Overview
The **Valorant Agents Info App** is a sleek and interactive web application that provides detailed information about Valorant agents, including their roles, abilities, and health stats. Built with a modern UI, it allows users to explore agents dynamically in a **scrollable and seamless** experience.

## 🚀 Features
- **🕵️ Agent List:** Browse through a collection of Valorant agents with their images.
- **📜 Detailed View:** Click on an agent to see their **abilities, role, and stats**.
- **🎨 Modern UI:** Responsive and clean design with **smooth scrolling**.
- **⚡ Fast & Lightweight:** Uses FastAPI for backend and React.js for frontend.

## 🛠️ Tech Stack
### **Frontend**
- ⚛️ **React.js** – Component-based UI for an interactive experience.
- 🎨 **CSS** – Styled for a clean, modern look with flexbox and responsive design.
- ⚡ **Vite** – Fast development server.

### **Backend**
- 🐍 **FastAPI** – High-performance backend serving agent data.
- 📦 **Static Files** – Hosts agent images for seamless integration.

## 🎮 How to Run the App
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/valorant-agents-app.git
cd valorant-agents-app
```

### **2️⃣ Install Dependencies**
#### **Backend (FastAPI)**
```bash
cd backend
pip install -r requirements.txt
```

#### **Frontend (React.js + Vite)**
```bash
cd frontend
npm install
```

### **3️⃣ Run the App**
#### **Start Backend Server**
```bash
uvicorn backend:app --reload
```

#### **Start Frontend**
```bash
npm run dev
```

### **4️⃣ Open in Browser**
Navigate to: [http://localhost:5173](http://localhost:5173)

## 📌 API Endpoints
| Method | Endpoint        | Description           |
|--------|----------------|-----------------------|
| GET    | `/agents/`      | Fetch all agents      |
| GET    | `/agents/{id}`  | Fetch a specific agent |



## 🤝 Contribution
Feel free to contribute by **submitting issues** or **pull requests**. 🚀


