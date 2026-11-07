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
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Apache Kafka in simple terms with a real-life example."
)

# Step 5: Display the response
print(response.text)