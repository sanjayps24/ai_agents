from dotenv import load_dotenv
load_dotenv()
from email_sender import send_email

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

def isprime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
         return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
)

agent = create_agent(
    model=model,
    tools=[get_weather,isprime,send_email],
    system_prompt="You are a helpful assistant",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf and is 2001 is prime;send an email to 4mh23cs180@gmil.com with content about the weather and result of prime and content 'Hello \\ This email was sent using python!' "}]}
)

# Print only the final AI response
final_msg = response["messages"][-1]
if isinstance(final_msg.content, list):
    for block in final_msg.content:
        if isinstance(block, dict) and block.get("type") == "text":
            print(block["text"])
else:
    print(final_msg.content)