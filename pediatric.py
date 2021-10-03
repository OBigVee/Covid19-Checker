Q5_PED = {"text": "What sex were you assigned at birth, on your original birth certificate?",
          "options": {
              "a": "Male",
              "b": "Female",
              "c": "I prefer not to say",
              "d": "I don’t know"
          }
          }

Q35_PED = {"text": "How do you currently describe yourself?",
           "options": {
               "a": "Male",
               "b": "Female",
               "c": "Transgender",
               "d": "I prefer not to say"
           }}

Q37_PED = {"text": "What is your race ?",
           "options": {
               "a": "white",
               "b": "Black or African American",
               "c": "American Indian or Alaska Native",
               "d": "Asian",
               "e": "Native Hawaiian or Other Pacific Islander",
               "f": "I prefer not to say"
           }}

Q1_PED = {"text": """
            Do you have any of these life-threatening symptoms?
                • Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone
                • Severe and constant pain or pressure in the chest
                • Difficulty breathing (such as gasping for air, being unable to walk or talk without catching your breath, severe wheezing,\
                    nostrils flaring, grunting,or ribs or stomach moving in and out deeply and rapidly as you breathe)
                • Disoriented (acting confused or very irritable)
                • Unconscious or very difficult to wake up
                • New or worsening seizures
                • Signs of low blood pressure (too weak to stand, dizziness, lightheaded,feeling cold, pale, clammy skin)
                • Dehydration (dry lips and mouth, not urinating much, sunken eyes) 
                • Refusing to drink liquids 
                • Frequent vomiting 
            """,
          "options": {
              "a": "Yes",
              "b": "No"}
          }

Q3_PED = {"text": "Are you feeling Sick ?",
          "options": {
              "a": "Yes",
              "b": "No"
          }}

Q6_PED = {"text": """In the two weeks before you felt sick, have you been in close contact with someone who has COVID-19? —excluding people who have had COVID-19\ 
                within the past 3 months.
                You have been in close contact if you have
                1. been within 6 feet of someone who has COVID-19 for a combined total of 15 minutes or more
                over a 24 hour period or \n
                2. provided care at home to someone who is sick with COVID-19 or
                3. had direct physical contact (hugged or kissed) with someone who has COVID-19 or
                4. shared eating or drinking utensils with someone who has COVID-19 or
                5. been sneezed on or coughed on by someone who has COVID-19""",

          "options": {
              "a": "Yes",
              "b": "No",
              "c": "I Don't Know"}}


Q31_PED = {"text": "In the last 10 day, have you tested positive for the coronavirus that causes COVID-19?",
           "options": {
               "a": "Yes, tested positive",
               "b": "No, tested negative",
               "c": "No, waiting for results",
               "d": "No, not tested"
           }}

Q7_PED = {"text":
          " In the last 10 days, have you experienced any of the symptoms listed below? (check all that apply)",
          "options": {
              "a": "Fever or feeling feverish (such as chills, sweating)",
              "b": "Cough",
              "c": "Mild or moderate difficulty breathing (breathing slightly faster than normal, feeling like you can’t inhale or exhale, or wheezing,\
                especially during exhaling or breathing out)",
              "d": "Sore throat",
              "e": "Muscle aches or body aches",
              "f": "Headache",
              "g": "Diarrhea",
              "h": "Nausea or vomiting",
              "i": "Stomach ache or pain in abdomen",
              "j": "New loss of taste or smell",
              "k": "New rash",
              "l": "Red eyes",
              "m": "Congestion or runny nose",
              "n": "Other symptoms",
          }
          }
Q8_PED = {"text": "Do you live in a group home or other setting with others (pediatric skilled nursing facility, behavioral health center, \
        juvenile detention center, or homeless shelter)?"}

Q9_PED = {"text": "In the last two weeks, have you attended or spent time in a group setting (for example school, dormitory, child care,\
         sporting event)?"}


Q10_PED = """ 
        Do any of these apply to you? (check any)\n
            a. Lung disease, such as moderate to severe asthma or cystic fibrosis\n
            b. Born premature\n
            c. Serious heart condition, such as congenital heart defect\n
            d. Weakened immune system or taking medications that may cause immune suppression\n
            e. Obesity\n
            f. Diabetes, kidney disease, or liver disease\n
            g. Cancer\n
            h. HIV\n
            i. Blood disorder, such as sickle cell disease or thalassemia\n
            j. Neurologic condition, such as cerebral palsy\n
            k. Smoking\n
            l. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If female/other gender is selected and\ 
                age is ≥12 and <60 years,then include question on pregnancy\n
            m. None of the above\n
            n. Down syndrome or Down’s syndrome\n
        """

Q11_PED = {"text": "Do you live in a group home or other setting with others (pediatric skilled nursing facility, behavioral health center,\
             juvenile detention center, or homeless shelter)?"}

Q12_PED = {"text": "In the last two weeks, have you attended or spent time in a group setting (for example school, dormitory, child care, \
            sporting)?"}

Q13_PED = """Do any of these apply to you? (check any)\n
                a. Lung disease, such as moderate to severe asthma or cystic fibrosis\n
                b. Born premature\n
                c. Serious heart condition, such as congenital heart defect\n
                d. Weakened immune system or taking medications that may cause immune suppression\n
                e. Obesity\n
                f. Diabetes, kidney disease, or liver disease\n
                g. Cancer\n
                h. HIV\n
                i. Blood disorder, such as sickle cell disease or thalassemia\n
                j. Neurologic condition, such as cerebral palsy\n
                k. Smoking\n
                l. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If female/other gender is selected and age is ≥12\
                    and <60 years,then include question on pregnancy\n
                m. None of the above\n
                n. Down syndrome or Down’s syndrome\n
        """

Q14_PED = """
        In the last 10 days, have you experienced any of the symptoms listed below? (check all that apply)\n
        a. Fever or feeling feverish (such as chills, sweating)\n
        b. Cough\n
        c. Mild or moderate difficulty breathing (breathi breathing slightly faster than normal, feeling like you can’t inhale or exhale, \
            or wheezing, especially during exhaling or breathing out ng slightly faster than normal, using extra muscles around the chest to \
            help breathe)\n
        d. Sore throat\n
        e. Muscle aches or body aches\n
        f. Headache\n
        g. Diarrhea\n
        h. Nausea or vomiting\n
        i. Stomach ache or pain in abdomen\n
        j. New loss of taste or smell\n
        k. New rash\n
        l. Red eyes\n
        m. Congestion or runny nose\n
        n. Other symptoms\n
"""

Q15_PED = {"text": "Do you live in a group home or other setting with others (pediatric skilled nursing facility, behavioral health center, \
            juvenile detention center, or homeless shelter)?"}

Q16_PED = {"text": "In the last two weeks, have you attended or spent time in a group setting (for example school, dormitory, child care, \
            sporting event)?"}
Q17_PED = """ Do any of these apply to you? (check any)\n
                a. Lung disease, such as moderate to severe asthma or cystic fibrosis\n
                b. Born premature\n
                c. Serious heart condition, such as congenital heart defect\n
                d. Weakened immune system or taking medications that may cause immune suppression\n
                e. Obesity\n
                f. Diabetes, kidney disease, or liver disease\n
                g. Cancer\n
                h. HIV\n
                i. Blood disorder, such as sickle cell disease or thalassemia\n
                j. Neurologic condition, such as cerebral palsy\n
                k. Smoking\n
                l. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If female/other gender is selected and\
                    age is ≥12 and <60 years, then include question on pregnancy\n
                m. None of the above\n
                n. Down syndrome or Down’s syndrome\n
"""
Q18_PED = {"text": "Do you live in a group home or other setting with others (pediatric skilled nursing facility, behavioral health center,\
     juvenile detention center, or homeless shelter)?"}

Q19_PED = {"text": "In the last two weeks, have you attended or spent time in a group setting (for example school,dormitory, child care, sporting\
             event)?"}

Q20_PED = """Do any of these apply to you? (check any)\n
                a. Lung disease, such as moderate to severe asthma or cystic fibrosis\n
                b. Born premature\n
                c. Serious heart condition, such as congenital heart defect\n
                d. Weakened immune system or taking medications that may cause immune suppression\n
                e. Obesity\n
                f. Diabetes, kidney disease, or liver disease\n
                g. Cancer\n
                h. HIV\n
                i. Blood disorder, such as sickle cell disease or thalassemia\n
                j. Neurologic condition, such as cerebral palsy\n
                k. Smoking\n
                l. Pregnant or recently pregnant (for at least 42 days following end of pregnancy)** If female/other gender is selected and age is ≥12 \
                    and <60 years, then include question on pregnancy\n
                m. None of the above\n
                n. Down syndrome or Down’s syndrome\n
    """

Q25_PED = {"text":
           """In the last two weeks, have you been in close contact with someone who has COVID-19? —excluding people who have had COVID-19 within the past 3 months.\n
                    You have been in close contact if you have
                        1. been within 6 feet of someone who has COVID-19 for a combined total of 15 minutes or more over a 24 hour period or\n
                        2. provided care at home to someone who is sick with COVID-19 or 
                        3. had direct physical contact (hugged or kissed) with someone who has COVID-19 or
                        4. shared eating or drinking utensils with someone who has COVID-19 or
                        5. been sneezed on or coughed on by someone who has COVID-19""",
           "options": {
               "a": "Yes",
               "b": "No",
               "c": "I Don't Know",
           }}

Q26_PED = {"text": "Do you live in a group home or other setting with others (pediatric skilled nursing facility, behavioral health center,\
         juvenile detention center, or homeless shelter)?"}

Q27_PED = {"text": "In the last two weeks, have you attended or spent time in a group setting (for example school, dormitory, child care,\
             sporting event)?"}
Q28_PED = ""
