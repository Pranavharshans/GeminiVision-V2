import google.generativeai as genai
from pathlib import Path



import google.generativeai as genai
from pathlib import Path




# Insert your  API key here
api_key = ""
genai.configure(api_key=api_key)

# Configurations
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Model Instance
model = genai.GenerativeModel(
    model_name="gemini-pro-vision",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Image Input Function
def input_image_setup(file_loc):
    if not (img := Path(file_loc)).exists():
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [{"mime_type": "image/jpeg", "data": Path(file_loc).read_bytes()}]
    return image_parts

# Response Function
def generate_gemini_response(input_prompt, image_loc, question_prompt):
    image_prompt = input_image_setup(image_loc)
    prompt_parts = [input_prompt, image_prompt[0], question_prompt]
    response = model.generate_content(prompt_parts)
    return response.text


input_prompt = """You are an expert in understanding images and explaining what is in the image"""# change according to use case

image_loc = "image1.png"# image location

print("Enter question prompt for the image")
question_prompt = input()  # question to be asked to the image using Gemini Vision

result = generate_gemini_response(input_prompt, image_loc, question_prompt)
print(result)
