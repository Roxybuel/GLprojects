# creates cover letters randomly

import os
import openai


file = open("my_api_key.txt","r")
api_key = file.read()
file.close()

openai.api_key = api_key

full_name = input("What is your full name?: ")
hiring_manager = input("What is the name of your hiring manager?: ")
job_title = input("Which job position are you applying for?: ")
years_of_experience = input("How many years of work experience do you have?: ")
company_name = input("What is the name of the company that you are applying to?: ")
profession = input("What is the general name of your profession?: ")
skill_1 = input("Name a skill you have relating to your position?: ")
skill_2 = input("Name another skill that you have relating to the workplace e.g communication?: ")
contact_info = input("What is your email address?: ")
education = input("What is the name of your University or College (if you attended)?: ")



completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user", "content": "Generate a cover letter using" + full_name + hiring_manager + job_title + years_of_experience + company_name + profession + skill_1 + skill_2 + contact_info + education}],

)


completion['choices'][0]['message']['content']
#tells chat gpt to use all the info I gave it to generate a cover letter
print(completion['choices'][0]['message']['content'])