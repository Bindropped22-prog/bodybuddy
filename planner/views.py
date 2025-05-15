import os
from django.shortcuts import render
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Build the prompt
def build_prompt(user_info, choice_type):
    if choice_type == "diet":
        return (
            f"Create a highly personalized diet plan for a {user_info['age']} year old {user_info['gender']}, "
            f"{user_info['height']} ft tall, {user_info['weight']} lbs. "
            f"Their current daily routine: {user_info['activity']}. "
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
            f"They prefer working out at: {user_info['workout_location']}. "
            f"Design a weekly schedule (5 days of training), and specify exercises, sets, and reps for each day."
        )


# Call OpenAI
def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a highly personalized fitness and nutrition assistant. Provide detailed and specific plans. Take into account all user input."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=800
    )
    return response['choices'][0]['message']['content'].strip()

# Main view
def index(request):
    if request.method == "POST":
        user_info = {
            "age": request.POST.get("age"),
            "gender": request.POST.get("gender"),
            "height": request.POST.get("height"),
            "weight": request.POST.get("weight"),
            "activity": request.POST.get("activity"),
            "diet": request.POST.get("diet"),
            "goal": request.POST.get("goal"),
            "fitness_level": request.POST.get("fitness_level"),
            "workout_location": request.POST.get("workout_location"),
        }
       
        diet_prompt = build_prompt(user_info, "diet")
        workout_prompt = build_prompt(user_info, "workout")

        diet_response = chat_with_ai(diet_prompt)
        workout_response = chat_with_ai(workout_prompt)

        return render(request, "planner/result.html", {
            "diet_response": diet_response,
            "workout_response": workout_response
        })


    # For GET request, send data ranges to the template
    return render(request, "planner/index.html", {
        "age_range": range(13, 76),
        "weight_range": range(90, 351, 1),
        "height_feet": range(4, 8),
        "height_inches": range(0, 12)
    })
