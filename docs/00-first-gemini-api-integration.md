# First Gemini API Integration with Python

## 1. Objective

The objective of this exercise was to integrate Google's Gemini Large Language Model (LLM) API into a Python application.

Through this implementation, I learned how to:

- Generate an API key using Google AI Studio.
- Configure environment variables in Python.
- Use the official Google GenAI Python SDK.
- Initialize a Gemini client.
- Send prompts to an LLM.
- Receive and display AI-generated responses.

## 2. Prerequisites

The following tools and technologies were used:

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Visual Studio Code | Code editor |
| Google Gemini API | LLM service |
| Google GenAI SDK | Python integration library |
| python-dotenv | Loading environment variables |
| Git | Version control |

## 3. Project Setup

### Step 1: Create a project directory

Create a directory named `ai-learning` and open it in VS Code.

### Step 2: Create a Python virtual environment

Run:

```powershell
py -3.13 -m venv .venv
```

This creates an isolated Python environment inside the project.

A virtual environment keeps project dependencies separate from globally installed Python packages.

### Step 3: Activate the virtual environment

Run in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After successful activation, the terminal displays `(.venv)`.

### Step 4: Install dependencies

Run:

```powershell
python -m pip install google-genai python-dotenv
```

The two packages serve different purposes:

- `google-genai`: Official Google GenAI SDK used to communicate with Gemini.
- `python-dotenv`: Loads configuration values from a `.env` file.

## 4. Generate a Gemini API Key

1. Open [Google AI Studio](https://aistudio.google.com/).
2. Sign in using your Google account.
3. Navigate to the API key section.
4. Create an API key.
5. Copy the generated key and store it securely.

**Security note:** Never share your API key publicly or commit it to GitHub.

API availability and usage quotas depend on the model and your account's applicable limits.

## 5. Configure Environment Variables

Create a `.env` file in the root directory.

Add the following entry:

```dotenv
GEMINI_API_KEY=your_actual_gemini_api_key
```

Replace the placeholder with your actual key.

### Why use a `.env` file?

We should not hardcode API keys inside Python source code.

Instead, environment variables allow us to separate application configuration from application logic.

This makes the application easier to maintain and safer to share.

## 6. Protect Sensitive Files

Create or update `.gitignore` in the project root:

```gitignore
.venv/
.env
__pycache__/
*.py[cod]
.vscode/
```

This prevents Git from tracking the virtual environment, API key file, Python cache files, and local IDE settings.

## 7. Implement Gemini API Integration

Create `main.py` and add:

```python
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured")

# Step 3: Create Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send a prompt to Gemini
print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Apache Kafka in simple terms with a real-life example."
)

# Step 5: Display the response
print("Response received successfully!")
print(response.text)
```

**Note:** `gemini-3.8-flash` is the model identifier used successfully in this learning environment. Model availability can change. If it is unavailable for another developer, they should select a currently supported model from Google AI Studio documentation.

## 8. Understand the Implementation

### Step 1: Import libraries

```python
import os
from dotenv import load_dotenv
from google import genai
```

- `os`: Provides access to operating-system functionality, including environment variables.
- `load_dotenv`: Loads variables from the `.env` file.
- `genai`: Provides the Google GenAI SDK.

### Step 2: Load environment variables

```python
load_dotenv()
```

This reads the `.env` file and makes its configuration available through environment variables.

### Step 3: Read the API key

```python
api_key = os.getenv("GEMINI_API_KEY")
```

`os.getenv()` retrieves the value associated with the specified environment variable.

### Step 4: Validate the API key configuration

```python
if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured")
```

This prevents the application from proceeding when the API key is missing.

### Step 5: Initialize the Gemini client

```python
client = genai.Client(api_key=api_key)
```

This creates a client object configured to communicate with the Gemini API.

The SDK handles the underlying authentication and HTTP communication.

### Step 6: Send the prompt

```python
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Apache Kafka in simple terms with a real-life example."
)
```

- `client.models.generate_content()`: Sends a content-generation request.
- `model`: Specifies the LLM to use.
- `contents`: Contains the input prompt.
- `response`: Stores the result returned by Gemini.

### Step 7: Display the response

```python
print(response.text)
```

The generated text is extracted from the API response and displayed in the terminal.

## 9. Run the Application

Ensure that:

- The virtual environment is activated.
- The `.env` file exists.
- The Gemini API key is configured.
- The required packages are installed.

Run:

```powershell
python main.py
```

Expected output:

```text
Sending request to Gemini...
Response received successfully!
[Gemini-generated response]
```

The exact response will depend on the prompt and model output.

## 10. High-Level Architecture

The integration follows this flow:

1. Python application starts.
2. Environment configuration is loaded.
3. Gemini API key is retrieved.
4. Gemini client is initialized.
5. Application sends a prompt to Gemini.
6. Gemini processes the prompt.
7. Generated response is returned.
8. Python displays the response.

## 11. Errors Encountered During Implementation

### OpenAI API billing error

The initial OpenAI API experiment failed because the available API credit balance was zero.

**Resolution:** Switched to Google Gemini for continued learning.

### Gemini model not found

The initial model identifier `gemini-2.5-flash` returned a 404 error in the user's environment.

**Resolution:** Changed to `gemini-3.8-flash`, which worked successfully in that environment.

### Missing API key

If `GEMINI_API_KEY` is not configured, the application raises a `ValueError`.

**Resolution:** Verify that `.env` exists in the project root and contains the correct variable name.

## 12. Key Learnings

Through this implementation, I learned:

- How to integrate an external LLM API into a Python application.
- How to use a Python SDK instead of manually implementing HTTP communication.
- How to manage API credentials using environment variables.
- How to initialize an API client.
- How to send prompts and process model responses.
- Why sensitive configuration files must be excluded from Git.

## 13. Next Learning Objectives

- Understand what an LLM is and how it works.
- Learn tokens and tokenization.
- Understand context windows and model parameters.
- Explore prompt engineering.
- Learn structured outputs.
- Build more advanced applications using Gemini APIs.