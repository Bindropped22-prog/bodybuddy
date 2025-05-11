import os
from django.shortcuts import render
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Load your API key from a .env file

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to build the prompt for OpenAI API
def build_prompt(user_info, choice_type):
    if choice_type == "diet":
        return (
            f"Create a highly personalized diet plan for a {user_info['age']} year old {user_info['gender']}, "
            f"{user_info['height']} ft tall, {user_info['weight']} lbs, "
            f"who is {user_info['activity']} active. "
            f"Their goal is to {user_info['goal']}. "
            f"Dietary preferences: {user_info['diet']}. "
            f"Provide a detailed breakfast, lunch, dinner, and snack plan for one day, "
            f"with estimated calories per meal."
        )
    elif choice_type == "workout":
        return (
            f"Create a {user_info['fitness_level']} workout routine for a {user_info['age']} year old {user_info['gender']}, "
            f"{user_info['height']} ft tall, {user_info['weight']} lbs. "
            f"Their goal is to {user_info['goal']}, with an activity level of {user_info['activity']}. "
            f"Design a weekly schedule (5 days of training), "
            f"and specify exercises, sets, and reps for each day."
        )

# Function to interact with the OpenAI API
def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or the latest model like "gpt-4"
        messages=[
            {"role": "system", "content": "You are a highly personalized fitness and nutrition assistant. Provide detailed and specific plans."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500  # Adjust the number of tokens as needed
    )
    return response['choices'][0]['message']['content'].strip()

# View function for handling form and API interaction
def index(request):
    if request.method == "POST":
        # Get user input data from the form
        user_info = {
            "age": request.POST.get("age"),
            "gender": request.POST.get("gender"),
            "height": request.POST.get("height"),
            "weight": request.POST.get("weight"),
            "activity": request.POST.get("activity"),
            "diet": request.POST.get("diet"),
            "goal": request.POST.get("goal"),
            "fitness_level": request.POST.get("fitness_level"),
        }
        plan_type = request.POST.get("plan_type")

        # Build the prompt for OpenAI API based on user input
        prompt = build_prompt(user_info, plan_type)

        # Get the AI response
        ai_response = chat_with_ai(prompt)

        # Return the result to the result.html page with the response
        return render(request, "planner/result.html", {"ai_response": ai_response})

    # If it's a GET request, render the index.html page with the form
    return render(request, "planner/index.html")
