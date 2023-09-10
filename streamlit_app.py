import openai
openai.api_key = "{API_KEY}"  # Replace "{API_KEY}" with your OpenAI API key

def generate_business_ideas(capital, time_frame):
    # Generate business ideas using OpenAI's ChatGPT-3.5-turbo
    prompt = f"What are some profitable business ideas given an initial capital of ${capital} and an expected return timeframe of {time_frame} months?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=5,  # Generate 5 different business ideas
        stop=None,
        temperature=0.7,
        top_p=None,
        frequency_penalty=0.0
    )

    # Extract the generated business ideas from the response
    business_ideas = [choice['text'].strip() for choice in response['choices']]

    return business_ideas

# Get user input
api_key = input("Enter your OpenAI API key:")
capital = input("Enter your initial capital:")
time_frame = input("Enter the expected return timeframe in months:")

# Set the OpenAI API key
openai.api_key = api_key

# Generate business ideas
ideas = generate_business_ideas(capital, time_frame)

# Print the generated business ideas
print("Here are some profitable business ideas:")
for i, idea in enumerate(ideas, 1):
    print(f"Idea {i}: {idea}")
```
