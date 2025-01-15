### **README.md**

```markdown
# UI Design Assistant

The UI Design Assistant is a web application powered by OpenAI's GPT models. It allows users to generate React components dynamically by describing them in plain language. This project serves as a practical demonstration of integrating AI with front-end development.

---

## Features

- Generate React components from natural language descriptions.
- Live code preview for generated components.
- Export the generated code for direct use in your projects.
- A sleek, modern UI with responsive design.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (v16 or later)
- [Python](https://www.python.org/) (v3.7 or later)
- [Git](https://git-scm.com/)

---

## Installation

Follow these steps to set up and run the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/<Your-GitHub-Username>/UI-Design-Assistant.git
cd UI-Design-Assistant
```

### **2. Set Up the Backend**
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   env\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI ChatGPT secret key:
   - Create a `.env` file in the `backend` directory:
     ```bash
     touch .env
     ```
   - Add the following line to the `.env` file:
     ```
     OPENAI_API_KEY=your-secret-key
     ```
   - Replace `your-secret-key` with your OpenAI API key. You can generate an API key by following [these instructions](https://platform.openai.com/account/api-keys).

5. Start the backend server:
   ```bash
   flask run
   ```

   By default, the backend will run on `http://127.0.0.1:5000`.

---

### **3. Set Up the Frontend**
1. Navigate back to the root directory and then to the `frontend` folder:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will run on `http://127.0.0.1:5173` by default.

---

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5173`.
2. Enter a description of the component you want to generate in the input box (e.g., "Create a search bar with a submit button").
3. Click the **Generate Component** button.
4. View the generated code in the preview section. You can also export the code for use in your projects.

---

## Environment Variables

The application requires the following environment variable to function correctly:

| Key               | Description                              |
|--------------------|------------------------------------------|
| `OPENAI_API_KEY`  | Your OpenAI API key for GPT integration. |

You can obtain an API key by visiting the [OpenAI API Key Management](https://platform.openai.com/account/api-keys) page.

---

## Screenshots

### Main Interface

<img width="1556" alt="Screenshot 2025-01-15 at 10 37 11 AM" src="https://github.com/user-attachments/assets/832c0284-7542-4aff-aa3e-022ec6209572" />


---

## Troubleshooting

### **Common Issues**
- **Push Rejected by GitHub:**
  If your API key is accidentally pushed to the repository, follow [these steps](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) to remove it and generate a new key.

- **CORS Errors:**
  Ensure the backend server is running and accessible at `http://127.0.0.1:5000`.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or additions.

---

