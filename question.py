# this file contains all the question related to the covid-19 checker"


#Q0 = "Are you in Africa or Nigeria territory right now ?\n"
Q0 = {
    "text": "Are you in Africa or Nigeria territory right now ?"
}

QOA = {"text": "Where in the Nigeria or which Nigeria territory are you currently located?"}

Q34 = {"text": "What is your ZIP code?"}


Q4 = {
    "text": " Are you answering for yourself or someone else ?",
    "options": {
        "a": "Self",
        "b": "Someone else"}
}

Q39 = {
    "text":
    "Are you fully vaccinated against COVID-19? (You are considered fully vaccinated 2 weeks after your second dose in a two-shot series like Pfizer or Moderna vaccines, or 2 weeks after a single-dose\
        vaccine such as Janssen (Johnson & Johnson) vaccine.)",
    "options": {
        "a": "Yes",
        "b": "No"}
}
Q2 = {
    "text": "What is your Age?",
    "options": {
        "a": "Younger than 2 years old",
        "b": "2 - 4 years",
        "c": "5 - 9",
        "d": "10 - 12",
        "e": "13-17",
        "f": "18-29",
        "g": " 30-39",
        "h": "40-49",
        "i": "50-59",
        "j": "60-64",
        "k": "65-69",
        "l": "70-79",
        "m": "80"
    }
}

Q5 = {"text", "What sex were you assigned at birth, on your birth original birth ceritificate"}
Q35 = {"text": "How do you currently describe yourself"}
Q36 = {"text": "Are you of Hispanic, Latino, or of Spanish origin?"}
Q37 = {"text": "What is your race ? "}


Q1 = {
    "text":
    """Do you have any of these life-threatening symptoms?

                • Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone
                • Severe and constant pain or pressure in the chest
                • Difficulty breathing (such as gasping for air, being unable to walk or talk without catching your breath, severe wheezing,
                nostrils flaring, grunting, or ribs or stomach moving in and out deeply and rapidly as you breathe)
                • New disorientation (acting confused)
                • Unconscious or very difficult to wake up
                • Slurred speech or difficulty speaking (new or worsening)
                • New or worsening seizures\n 
                • Signs of low blood pressure (too weak to stand, dizziness,lightheaded, feeling cold, pale, clammy skin)\n
                • Dehydration (dry lips and mouth, not urinating much, sunken eyes)""",
        "options": {
            "a": "Yes",
            "b": "No"}
}

Q3 = {
    "text": "Are you feeling sick?",
    "options": {
            "a": "Yes",
            "b": "No"}
}


Q6 = {
    "text": """In the two weeks before you felt sick, have you been in close contact with someone who has COVID-19 ?
                You have been in close contact if you have
                a. been within 6 feet of someone who has COVID-19 for a combined total of 15 minutes or more over a 24 hour period or
                b. provided care at home to someone who is sick with COVID-19 or 
                c. had direct physical contact (hugged or kissed) with someone who has COVID-19 or
                d. shared eating or drinking utensils with someone who has COVID-19 or
                e. been sneezed on or coughed on by someone who has COVID-19 """,
    "options":
    {"a": "Yes",
     "b": "No",
     "c": "I Don't Know"}
}


Q25 = {
    "text": """In the last two weeks, have you been in close contact with someone who has COVID-19? — excluding people who have had COVID-19 within the past 3 months.
                You have been in close contact if you have
                a. been within 6 feet of someone who has COVID-19 for a combined total of 15 minutes or more over a 24 hour period or
                b. provided care at home to someone who is sick with COVID-19 or 
                c. had direct physical contact (hugged or kissed) with someone who has COVID-19 or
                d. shared eating or drinking utensils with someone who has COVID-19 or 
                e. been sneezed on or coughed on by someone who has COVID-19""",
    "options": {
        "a": "Yes",
        "b": "No",
        "c": "I Don't Know"}
}

Q31 = {
    "text": "In the last 10 days, have you been tested for the coronavirus that causes COVID-19?",

    "options": {
            "a": "have been tested in the last 10 days, and my result was positive.",
            "b": "I have been tested in the last 10 days, and my result was negative",
        "c": "I have been tested in the last 10 days and i am waiting for my result.",
        "d": "I have not been tested",
        "e": "I have been tested, but it has been more than 10 days since my last test"
    }
}

Q38 = {"text":
       "In the last 14 days, have you been tested for the coronavirus that causes COVID-19 ?",
       "options":
       {
           "a": "I have been tested in the last 14 days, and my result was positive",
           "b": "I have been tested in the last 14 days and my result was negative.",
                "c": "I have been tested in the last 14 days and i am waiting for my results.",
                "d": "I have not been tested.",
                "e": "I have been tested, but it has been more than 14 days since my last test."
       }
       }

Q7 = {"text":
      "In the last 10 days, have you experienced any of the symptoms listed below? (check all that apply)",
      "options": {
          "a": "Fever or feeling feverish (such as chills, sweating)",
          "b":  "Cough",
          "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal, feeling like you can’t inhale or exhale, or wheezing, especially during exhaling or breathing out)",
          "d": "Sore throat",
          "e": "Muscle aches or body aches",
          "f": "Unusual fatigue",
          "g": "Headache",
          "h": "New loss of taste or smell",
          "i": "Congestion or runny nose",
          "j": "Nausea or vomiting",
          "k": "Diarrhea",
          "l": "Other symptoms"
      }
      }
Q8 = {"text":
      "Do you live in a long-term care facility, nursing home, or homeless shelter?",
      "options":
      {"a": "Yes",
       "b": "No"
       }
      }

Q9 = {"text":
      "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? Healthcare facilities\
                        include a hospital, medical or dental clinic, long-term care facility, or nursing home.",
      "options": {
          "a": "Yes",
          "b": "No"}
      }

Q10 = {"text":
       """ Do any of these apply to you ?
                        1. Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease), cystic fibrosis, or pulmonary fibrosis\n
                        2. Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart\n
                        3. Weakened immune system or taking medications that may cause immune suppression\n
                        4. Obesity\n
                        5. Diabetes, chronic kidney disease, or liver disease\n
                        6. High blood pressure\n
                        7. Cancer\n
                        8. HIV\n
                        9. Blood disorder, such as sickle cell disease or thalassemia\n
                        10. Cerebrovascular disease or neurologic condition, such as stroke or dementia\n
                        11. Smoking\n
                        12. Down syndrome or Down’s syndrome""",
       "options": {
           "a": "Yes",
           "b": "None of the Above"}
       }

Q10_Pregnacy = {"text":
                """ Do any of these apply to you ?
                        1. Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease), cystic fibrosis, or pulmonary fibrosis\n
                        2. Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart\n
                        3. Weakened immune system or taking medications that may cause immune suppression\n
                        4. Obesity
                        5. Diabetes, chronic kidney disease, or liver disease
                        6. High blood pressure
                        7. Cancer
                        8. HIV
                        9. Blood disorder, such as sickle cell disease or thalassemia
                        10. Cerebrovascular disease or neurologic condition, such as stroke or dementia
                        11. Smoking
                        12. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)
                        13. Down syndrome or Down’s syndrome""",

                "options": {
                    "a": "Yes",
                    "b": "None of the Above"}
                }

Q11 = {
    "text":
    "Do you live in a long-term care facility, nursing home, or homeless shelter?"
}

Q12 = {"text": "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? Healthcare facilities\
     include a hospital, medical or dental clinic, long-term care facility, or nursing home."}

Q13 = {"text":
       "Do any of these apply to you? (check any)",
       "options": {
           "a": "Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive\
                        pulmonary disease), cystic fibrosis, or pulmonary fibrosis",
           "b": "Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart",
           "c": "Weakened immune system or taking medications that may cause immune suppression",
           "d": "Obesity",
           "e": "Diabetes, chronic kidney disease, or liver disease",
           "f": "High blood pressure",
           "g": "Cancer",
           "h": "HIV",
           "i": "Blood disorder, such as sickle cell disease or thalassemia",
           "j": "Cerebrovascular disease or neurologic condition, such as stroke or dementia",
           "k": "Smoking",
           "l": "Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If\
                                        female/other gender is selected and age is ≥12 and <60 years, then include question on\
                                        pregnancy",
           "m": "None of the above",
           "n": "Down syndrome or Down’s syndrome"}
       }

Q14 = {"text":
       "In the last 10 days, have you experienced any of the symptoms listed below? (check all that apply)",
       "options": {
           "a": "Fever or feeling feverish (such as chills, sweating)",
           "b": "Cough",
           "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal, feeling like you can’t inhale or exhale, or wheezing, especially during exhaling or\
                                breathing out)",
           "d": "Sore throat",
           "e": "Muscle aches or body aches",
           "f": "Unusual fatigue",
           "g": "Headache",
           "h": "New loss of taste or smell",
           "i": "Congestion or runny nose",
           "j": "Nausea or vomiting",
           "k": "Diarrhea",
           "l": "Other symptoms"
       }
       }

Q15 = {"text":
       "Do you live in a long-term care facility, nursing home, or homeless shelter?"}

Q16 = {"text": "In the last two weeks, have you worked or volunteered in any healthcare facility or as a first responder?\
         Healthcare facilities include a hospital, medical or dental clinic, long-term care facility, or nursing home"}

Q17 = {"text":
       "Do any of these apply to you? (check any)",
       "options": {
           "a": "Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease),\
                                        cystic fibrosis, or pulmonary fibrosis",
           "b": "Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart",
           "c": "Weakened immune system or taking medications that may cause immune suppression",
           "d": "Obesity",
           "e": "Diabetes, chronic kidney disease, or liver disease",
           "f": "High blood pressure",
           "g": "Cancer",
           "h": "HIV",
           "i": "Blood disorder, such as sickle cell disease or thalassemia",
           "j": "Cerebrovascular disease or neurologic condition, such as stroke or dementia",
           "k": "Smoking",
           "l": "Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If\
                                female/other gender is selected and age is ≥12 and <60 years, then include question on\
                                pregnancy",
           "m": "None of the above",
           "n": "Down syndrome or Down’s syndrome"
       }
       }

Q18 = {"text": "Do you live in a long-term care facility, nursing home, or homeless shelter?"}
Q19 = {"text": "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder?\
         Healthcare facilities include a hospital, medical or dental clinic, long-term care facility, or nursing home."}
Q20 = {"text": "Do any of these apply to you? (check any)",
       "options": {
           "a": "Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive\
                pulmonary disease), cystic fibrosis, or pulmonary fibrosis",
           "b": "Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart",
           "c":  "Weakened immune system or taking medications that may cause immune suppression",
                "d": "Obesity",
                "e": "Diabetes, chronic kidney disease, or liver disease",
                "f": "High blood pressure",
                "g": "Cancer",
                "h": "HIV",
                "i": "Blood disorder, such as sickle cell disease or thalassemia",
                "j": "Cerebrovascular disease or neurologic condition, such as stroke or dementia",
                "k": "Smoking",
                "l": "Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If\
                        female/other gender is selected and age is ≥12 and <60 years, then include question on pregnancy",
                "m": "None of the above",
                "n": "Down syndrome or Down’s syndrome"}
       }

Q21 = {"text": "Do you live in a long-term care facility, nursing home or homeless shelter?"}

Q22 = {"text": "In the last two weeks, have you worked or volunteered in any healthcare facility or as a first responder? \
        Healthcare facilities include a hospital, other medical setting (including dental care setting), long-term care facility,\
                 or nursing home"}
Q23 = {"text":
       "Do any of these apply to you? (check any)",
       "options": {
           "a": "Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive\
                        pulmonary disease), cystic fibrosis, or pulmonary fibrosis",
           "b": "Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart",
                "c": "Weakened immune system or taking medications that may cause immune suppression",
                "d": "Obesity",
                "e": "Diabetes, chronic kidney disease, or liver disease",
                "f": "High blood pressure",
                "g": "Cancer",
                "h": "HIV",
                "i": "Blood disorder, such as sickle cell disease or thalassemia",
                "j": "Cerebrovascular disease or neurologic condition, such as stroke or dementia",
                "k": "Smoking",
                "l": "Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If\
                female/other gender is selected and age is ≥12 and <60 years, then include question on pregnancy",
                "m": "None of the above",
                "n": "Down syndrome or Down’s syndrome"
       }
       }

Q201 = {"text":
        "What was the result of your test?",
        "options": {
            "a": "The test showed that I did have COVID-19 (positive test)",
            "b": "The test showed that I did not have COVID-19 (negative test)"
        }
        }

Q202 = {"text": "How long has it been since your most recent test for COVID-19?",
        "options": {
            "a": "less than 1 month",
            "b": "at least 1 month but less than 3 months",
            "c": "at least 3 months but less than 6 months",
            "d": "at least 6 months but less than 1 year",
            "e": "1 year or more"
        }
        }

Q203 = {"text":
        "What symptoms, if any, have you had since testing positive for COVID-19?",
        "options": {
            "a": "Fever or feeling feverish (such as chills, sweating)",
            "b": "Cough",
            "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal,feeling like you can’t inhale or exhale,\
                        or wheezing, especially during exhaling or breathing out)",
            "d": "Sore throat",
            "e": "Muscle aches or body aches",
            "f": "Headache",
            "g": "Vomiting or diarrhea",
            "h": "Loss of taste or smell",
            "i": "Congestion or runny nose",
            "j": "New rash",
            "k": "Unusual fatigue",
            "l": "Joint pain",
            "m": "Tightness in the chest or unusual chest pain",
            "n": "Difficulty thinking or concentrating (sometimes referred to as “brain fog”)",
            "o": "Depression, anxiety, changes in mood",
            "p": "Fast-beating or pounding heart (also known as heart palpitations)",
            "q": "Other symptoms",
            "r": "No symptoms"
        }
        }
Q204 = {"text":
        "How are you feeling now?",
        "options": {
            "a": "I have recovered, and I no longer have symptoms.",
            "b": "I am feeling better, but I still have symptoms.",
            "c": "I am not feeling better, and I have new symptoms."
        }
        }

Q205 = {"text": "Do you live in a long-term care facility, nursing home, or homeless shelter?"}

Q206 = {"text": "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? Healthcare facilities\
        include a hospital, medical or dental clinic, long-term care facility, or nursing home."}

Q208 = {"text": " How long has it been since your most recent test for COVID-19?",
        "options": {
            "a": "less than 1 month",
                "b": "at least 1 month but less than 3 months",
                "c": "at least 3 months but less than 6 months",
                "d": "at least 6 months but less than 1 year",
                "e":  "1 year or more",
        }
        }

Q209 = {"text":
        "What symptoms, if any, have you had since testing negative for COVID-19(check all that apply)",
        "options": {
            "a": "Fever or feeling feverish (such as chills, sweating)",
            "b": "Cough",
            "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal, feeling like you can’t inhale or exhale, or wheezing, especially during exhaling or breathing out)",
            "d": "Sore throat",
            "e": "Muscle aches or body aches",
            "f": "Headache",
            "g":  "Vomiting or diarrhea",
            "h": "Loss of taste or smell",
            "i": "Congestion or runny nose",
            "j": "New rash",
            "k": "Unusual fatigue",
            "l": "Joint pain",
            "m": "Tightness in the chest or unusual chest pain",
            "n": "Difficulty thinking or concentrating (sometimes referred to as “brain fog”)",
            "o": "Depression, anxiety, changes in mood",
            "p": "Fast-beating or pounding heart (also known as heart palpitations)",
            "q": "Other symptoms",
            "r": "No symptoms"
        }
        }

Q210 = {"text":"How are you feeling now?",
"options":{
                "a": "I have recovered, and I no longer have symptoms",
                "b" : "I am feeling better, but I still have symptoms.",
                "c" :"I am not feeling better, and I have new symptoms."
}}
Q211 = {"text":"Do you live in a long-term care facility, nursing home, or homeless shelter"}

Q212 = {"text"
        :"In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? \
        Healthcare facilities include a hospital, medical or dental clinic, long-term care facility, or nursing home."}

Q214 = {"text": "What was the result of your test?",
"options":{
        "a":"The test showed that I did have COVID-19 (positive test).",
        "b": "The test showed that I did not have COVID-19 (negative test)"
}}

Q26 = {"text": "Do you live in a long-term care facility, nursing home, or homeless shelter?",
"options":{
        "a": "Yes",
        "b": "No"}}

Q27 = {"text":"In the last two weeks, have you worked or volunteered in any healthcare facility or as a first responder? Healthcare facilities\
        include a hospital, medical or dental clinic, long-term care facility, or nursing home.",
        "options":{
        "a" :"Yes",
        "b": "No"}}

Q28 = {"text":"Did you wear personal protective equipment (gown, mask or respirator, goggles or face shield, and gloves) while working or volunteering \
        at the healthcare facility?",
         "options":{
        "a" :"Yes",
        "b" :"No"
         }}

Q40 = {"text":"What is your age?",
"options":{
                "a": "12-15",
                "b": "16-17",
                "c" :"18-29",
                "d": "30-39",
                "e": "40-49",
                "f": "50-59",
                "g": "60-64",
                "h": "65-69",
                "i": "70-79",
                "j": "80+"}}

Q41 = {"text" :"What sex were you assigned at birth, on your original birth certificate?",
"options":{
        "a" :"Male",
        "b" :"Female",
        "c" : "I prefer not to say",
        "d" : "I don’t know"}}

Q42 = {"text":"How do you currently describe yourself?",
"options":{
        "a": "Male",
        "b": "Female",
        "c" :"Transgender",
        "d":"I prefer not to say"
}}

Q43 = {"text":
                "Are you of Hispanic, Latino, or of Spanish origin?",
                "options":{

        "a": "Yes",
        "b" :"No",
        "c": "I Prefer not to say"}}

Q44 = {"text":
"What is your race ?",
"options":{
                "a":  "White",
                "b":  "Black or African American",
                "c":  "American Indian or Alaska Native",
                "d": "Asian",
                "e":  "Native Hawaiian or Other Pacific Islander",
                "f":  "I prefer not to say",
}}

Q45 = {"text":
        """In the last two weeks, have you been in close contact with someone who has COVID-19? — excluding people who have had COVID-19\
                within the past 3 months.
                You have been in close contact if you have
                • been within 6 feet of someone who has COVID-19 for a combined total of 15 minutes or more over a 24-hour period or
                • provided care at home to someone who is sick with COVID-19 or
                • had direct physical contact (hugged or kissed) with someone who has COVID-19 or
                • shared eating or drinking utensils with someone who has COVID-19 or
                • been sneezed on or coughed on by someone who has COVID-19""",
       "options": {
           "a": "Yes",
           "b": "No"}}

Q52 = {"text":
       """Do you have any of these life-threatening symptoms?
                • Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone
                • Severe and constant pain or pressure in the chest
                • Difficulty breathing (such as gasping for air, being unable to walk or talk without catching your breath, severe wheezing, nostrils \
                  flaring, grunting, or ribs or stomach moving in and out deeply and rapidly as you breathe)
                • New disorientation (acting confused)
                • Unconscious or very difficult to wake up
                • Slurred speech or difficulty speaking (new or worsening)
                • New or worsening seizures
                • Signs of low blood pressure (too weak to stand, dizziness,lightheaded, feeling cold, pale, clammy skin)
                • Dehydration (dry lips and mouth, not urinating much, sunken eyes)
              
        """,
       "options": {
           "a": "Yes",
           "b": "No"}}
Q46 = {"text":
       "In the last 10 days, have you experienced any of the symptoms listed below? (check all that apply)",
       "options": {
           "a": "Fever or feeling feverish (such as chills, sweating)",
           "b": "Cough",
           "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal, feeling like you can’t inhale or exhale, or wheezing,\
                                especially during exhaling or breathing out)",
           "d": "Sore throat",
           "e": "Muscle aches or body aches",
           "f": "Headache",
           "g": "Vomiting or diarrhea",
           "h": "New loss of taste or smell",
           "i": "Congestion or runny nose",
           "j": "Nausea or vomiting",
           "k": "Diarrhea",
           "l": "Other symptoms",
           "m": "No symptoms"}
       }

Q47 = {"text": "Do you live in a long-term care facility, nursing home, or homeless shelter?",
       "options": {
           "a": "Yes",
           "b": "No"}}


Q48 = {"text":
       "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? Healthcare facilities\
                include a hospital, medical or dental clinic, long-term care facility, or nursing home.",
       "options": {
           "a": "Yes",
           "b": "No"}}

Q49 = {"text":
       """ Do you have, or have you had any of the following? (check all that apply)
                        1. Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease), cystic fibrosis, or pulmonary fibrosis\n
                        2. Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart
                        3. Weakened immune system or taking medications that may cause immune suppression
                        4. Obesity
                        5. Diabetes, chronic kidney disease, or liver disease
                        6. High blood pressure
                        7. Cancer
                        8. HIV
                        9. Blood disorder, such as sickle cell disease or thalassemia
                        10. Cerebrovascular disease or neurologic condition, such as stroke or dementia
                        11. Smoking
                        12. Down syndrome or Down’s syndrome""",
       "options": {
           "a": "Yes",
           "b": "None of the Above"}}

Q49_Pregnacy = {"text":
                """ Do you have, or have you had any of the following? (check all that apply)
                1. Chronic lung disease, such as moderate to severe asthma, COPD (chronic obstructive pulmonary disease), cystic fibrosis, or pulmonary fibrosis
                2. Serious heart condition, such as heart failure, cardiomyopathy, heart attack, or blocked arteries to the heart
                3. Weakened immune system or taking medications that may cause immune suppression
                4. Obesity
                5. Diabetes, chronic kidney disease, or liver disease
                6. High blood pressure
                7. Cancer
                8. HIV
                9. Blood disorder, such as sickle cell disease or thalassemia
                10. Cerebrovascular disease or neurologic condition, such as stroke or dementia
                11. Smoking
                12. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)
                13. Down syndrome or Down’s syndrome""",

                "options": {"a": "Yes",
                            "b": "None of the Above"

                            }}

Q50 = {"text":
       "Do you live in a long-term care facility, nursing home, or homeless shelter?",
       "options": {
           "a": "Yes",
           "b": "No"
       }
       }
Q51 = {"text":
       "In the last two weeks, have you worked or volunteered in a healthcare facility or as a first responder? Healthcare facilities \
                include a hospital, medical or dental clinic, long-term care facility, or nursing home",
       "options":
       {"a": "Yes",
        "b": "No"}
       }
