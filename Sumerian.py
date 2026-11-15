
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Sumerian Language Quiz",
    page_icon="𒀭",
    layout="centered"
)

# --------------------------------------------------
# TITLE AND INTRODUCTION
# --------------------------------------------------

st.title("𒀭 Sumerian Language Quiz")
st.subheader("Test your knowledge of the world's earliest recorded written language!")

st.markdown("""
### Welcome to the Sumerian Quiz!

This quiz evaluates your knowledge of:

- **Sumerian vocabulary and meanings**
- **Cuneiform sign recognition**
- **Sumerian numbers**
- **Basic grammar and linguistic concepts**
- **Ancient Mesopotamian writing**

There are **15 questions**. Each correct answer earns one point.
""")

st.info("Choose the correct answer for each question. Good luck!")

st.markdown("---")

# --------------------------------------------------
# QUIZ QUESTIONS
# --------------------------------------------------

questions = [

    {
        "question": "1. What does the Sumerian word 'dingir' mean?",
        "options": ["King", "God / deity", "Water", "House"],
        "answer": "God / deity",
        "explanation": "Dingir means god or deity. Its cuneiform sign is 𒀭."
    },

    {
        "question": "2. Which cuneiform sign represents 'AN'?",
        "options": ["𒂍", "𒀭", "𒆠", "𒈗"],
        "answer": "𒀭",
        "explanation": "𒀭 is the sign AN, meaning heaven or sky. It can also function as a divine determinative."
    },

    {
        "question": "3. What does the Sumerian word 'é' mean?",
        "options": ["Water", "House / temple", "Sun", "Man"],
        "answer": "House / temple",
        "explanation": "É means house or temple. Its cuneiform sign is 𒂍."
    },

    {
        "question": "4. Which cuneiform sign represents 'LUGAL' (king)?",
        "options": ["𒈗", "𒀭", "𒊩", "𒌓"],
        "answer": "𒈗",
        "explanation": "𒈗 is the cuneiform sign LUGAL, meaning king."
    },

    {
        "question": "5. What is the meaning of the Sumerian word 'ki'?",
        "options": ["Earth / place", "Fire", "King", "Moon"],
        "answer": "Earth / place",
        "explanation": "KI means earth, ground or place. Its sign is 𒆠."
    },

    {
        "question": "6. Which cuneiform sign represents 'UD' (sun / day)?",
        "options": ["𒌓", "𒂍", "𒀭", "𒈗"],
        "answer": "𒌓",
        "explanation": "𒌓 is the sign UD, associated with the sun and day."
    },

    {
        "question": "7. What does 'lugal' mean in Sumerian?",
        "options": ["Priest", "King", "Farmer", "Scribe"],
        "answer": "King",
        "explanation": "LUGAL means king and is written 𒈗."
    },

    {
        "question": "8. Which cuneiform sign represents 'A' (water)?",
        "options": ["𒀀", "𒂍", "𒆠", "𒌓"],
        "answer": "𒀀",
        "explanation": "𒀀 is the sign A, meaning water."
    },

    {
        "question": "9. What does the Sumerian word 'ama' mean?",
        "options": ["Father", "Mother", "Son", "Daughter"],
        "answer": "Mother",
        "explanation": "AMA means mother in Sumerian."
    },

    {
        "question": "10. Which cuneiform sign represents 'DUMU' (child / son)?",
        "options": ["𒌉", "𒀭", "𒈗", "𒊩"],
        "answer": "𒌉",
        "explanation": "𒌉 is the sign DUMU, meaning child or son."
    },

    {
        "question": "11. What is the Sumerian word for 'woman'?",
        "options": ["LU₂", "NIN", "MUNUS", "DUMU"],
        "answer": "MUNUS",
        "explanation": "MUNUS means woman or female. Its sign is 𒊩."
    },

    {
        "question": "12. Which sign represents the Sumerian word 'NIN' (lady / queen)?",
        "options": ["𒊩𒌆", "𒂍", "𒀀", "𒆠"],
        "answer": "𒊩𒌆",
        "explanation": "𒊩𒌆 is a conventional cuneiform spelling of NIN, meaning lady or queen."
    },

    {
        "question": "13. What is the value of the Sumerian numeral sign 𒐕?",
        "options": ["1", "5", "10", "60"],
        "answer": "5",
        "explanation": "𒐕 is the cuneiform numeral sign for five."
    },

    {
        "question": "14. What does the cuneiform sequence 𒀭𒈗 represent?",
        "options": [
            "God and king",
            "House of the king",
            "King of heaven",
            "Water and earth"
        ],
        "answer": "God and king",
        "explanation": "𒀭 represents DINGIR (god), and 𒈗 represents LUGAL (king). The sequence can be read as DINGIR LUGAL; context determines the exact interpretation."
    },

    {
        "question": "15. Which writing system was primarily used to record Sumerian?",
        "options": [
            "Phoenician alphabet",
            "Greek alphabet",
            "Cuneiform",
            "Latin alphabet"
        ],
        "answer": "Cuneiform",
        "explanation": "Sumerian was recorded using the cuneiform writing system, developed in ancient Mesopotamia."
    }

]

# --------------------------------------------------
# USER INFORMATION
# --------------------------------------------------

st.markdown("### Participant Information")

name = st.text_input("Enter participant's name:")

level = st.selectbox(
    "Select your Sumerian knowledge level:",
    ["Beginner", "Intermediate", "Advanced"]
)

st.markdown("---")

# --------------------------------------------------
# DISPLAY QUESTIONS
# --------------------------------------------------

st.markdown("### The 15 Questions")

user_answers = []

for i, q in enumerate(questions):

    st.write(f"**{q['question']}**")

    answer = st.radio(
        "Select your answer:",
        q["options"],
        index=None,
        key=f"question_{i}"
    )

    user_answers.append(answer)

    st.markdown("---")

# --------------------------------------------------
# ADDITIONAL WIDGETS
# --------------------------------------------------

confidence = st.slider(
    "How confident are you about your Sumerian knowledge?",
    min_value=0,
    max_value=100,
    value=50,
    format="%d%%"
)

feedback = st.text_area(
    "Comments or suggestions about this quiz:"
)

# --------------------------------------------------
# SUBMIT AND CALCULATE SCORE
# --------------------------------------------------

if st.button("Submit Quiz", type="primary"):

    if not name.strip():

        st.error("Please enter the participant's name.")

    elif None in user_answers:

        st.warning("Please answer all 15 questions before submitting.")

    else:

        score = 0

        for i, q in enumerate(questions):

            if user_answers[i] == q["answer"]:
                score += 1

        percentage = (score / len(questions)) * 100

        st.markdown("---")
        st.header("𒀭 Quiz Results")

        st.write(f"**Participant:** {name}")
        st.write(f"**Knowledge level:** {level}")
        st.write(f"**Confidence:** {confidence}%")

        st.metric(
            label="Final Score",
            value=f"{score}/15",
            delta=f"{percentage:.1f}%"
        )

        # ------------------------------------------
        # SCORE EVALUATION
        # ------------------------------------------

        if score >= 13:

            st.success(
                f"Excellent, {name}! You have demonstrated "
                "excellent knowledge of Sumerian and cuneiform!"
            )

        elif score >= 9:

            st.success(
                f"Very good, {name}! You have a good understanding "
                "of Sumerian language and writing."
            )

        elif score >= 6:

            st.warning(
                f"Fair result, {name}. You have some knowledge "
                "of Sumerian, but further study is recommended."
            )

        else:

            st.error(
                f"Keep studying, {name}! Your knowledge of "
                "Sumerian and cuneiform needs improvement."
            )

        # ------------------------------------------
        # ANSWER REVIEW
        # ------------------------------------------

        st.markdown("---")
        st.subheader("Detailed Answer Review")

        for i, q in enumerate(questions):

            if user_answers[i] == q["answer"]:

                st.success(
                    f"Question {i+1}: Correct!"
                )

            else:

                st.error(
                    f"Question {i+1}: Incorrect. "
                    f"Your answer: {user_answers[i]}. "
                    f"Correct answer: {q['answer']}."
                )

            st.caption(q["explanation"])

        # ------------------------------------------
        # FINAL FEEDBACK
        # ------------------------------------------

        if feedback.strip():

            st.info(f"Participant feedback: {feedback}")

        st.markdown("---")

        st.write(
            "Thank you for participating in the "
            "Sumerian Language and Cuneiform Quiz!"
        )
