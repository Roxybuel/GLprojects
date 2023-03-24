# has a template for the cover letter (make sure you define the template)

import os
import openai

openai.api_key = "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"

#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
def generate_cover_letter(job_title, years_of_experience, profession, company_name, full_name, skill_1, skill_2):
    introduction = f"Dear Hiring Manager, \n\nI am excited to apply for the position of {job_title} at " \
                   f"{company_name}, and I am writing to express my interest in the role. With my experience and" \
                   f" qualifications, I believe I am uniquely qualified to be an excellent {job_title} at " \
                   f"your company.\n\n"

    body = f"I have {years_of_experience} years of experience in {profession}, an extensive knowledge of {skill_1}" \
           f" and {skill_2}, and have worked in a variety of {profession} jobs. I am an excellent communicator and " \
           f"team player, and believe I can bring those qualities to the role."

    conclusion = f"I am confident that I can make a positive contribution to {company_name} and help it achieve its " \
                 f"goals. I am thrilled for the opportunity to become a part of your team and am eager to learn more " \
                 f"about the position."

    closing = f"Thank you for your time and consideration. I look forward to hearing from you soon. \n\nSincerely, \n\n {full_name}"

    return introduction + body + conclusion + closing


job_title = input("Which job position do you want to apply for?: ")
years_of_experience = input("How many years of work experience do you have?: ")
company_name = input("What is the name of the company that you would like to work for?: ")
full_name = input("What is your full name?: ")
profession = input("What is the general name of your profession?: ")
skill_1 = input("Name a skill you have?: ")
skill_2 = input("Name another skill that you have?: ")

cover_letter = generate_cover_letter(job_title, years_of_experience, profession, company_name, full_name, skill_1,
                                     skill_2)

print(cover_letter)
