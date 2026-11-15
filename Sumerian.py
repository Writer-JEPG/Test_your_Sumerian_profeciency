
import streamlit as st

# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="Sumerian Language Quiz",
    page_icon="𒀭",
    layout="centered"
)

# 2. TRANSLATIONS

translations = {
    "English": {
        "title": "𒀭 Sumerian Language Quiz",
        "subtitle": "Test your knowledge of the Sumerian language and cuneiform!",
        "welcome": "Welcome to the Sumerian Quiz!",
        "description": """
### Test your knowledge!

This quiz evaluates your knowledge of:

- **Sumerian vocabulary and meanings**
- **Cuneiform sign recognition**
- **Sumerian numbers**
- **Basic grammar and linguistic concepts**

There are **15 questions**. Each correct answer earns one point.
""",
        "language": "Select Application Language",
        "instructions": "Choose one answer for each question. Good luck!",
        "participant": "Participant Information",
        "name": "Enter participant's name:",
        "level": "Select your Sumerian knowledge level:",
        "levels": ["Beginner", "Intermediate", "Advanced"],
        "questions": "The 15 Questions",
        "choose": "Choose your answer:",
        "confidence": "How confident are you about your Sumerian knowledge?",
        "feedback": "Comments or suggestions about this quiz:",
        "submit": "Submit Quiz",
        "missing_name": "Please enter the participant's name.",
        "missing_answers": "Please answer all 15 questions before submitting.",
        "results": "𒀭 Quiz Results",
        "score": "Final Score",
        "excellent": "Excellent! You have demonstrated excellent knowledge of Sumerian and cuneiform!",
        "very_good": "Very good! You have a good understanding of Sumerian language and writing.",
        "fair": "Fair result. Further study of Sumerian is recommended.",
        "poor": "Keep studying! Your knowledge of Sumerian and cuneiform needs improvement.",
        "review": "Detailed Answer Review",
        "correct": "Correct!",
        "incorrect": "Incorrect",
        "your_answer": "Your answer",
        "correct_answer": "Correct answer",
        "thank_you": "Thank you for participating in the Sumerian Language and Cuneiform Quiz!",
        "feedback_received": "Participant feedback",
        "confidence_result": "Confidence",
        "level_result": "Knowledge level",
        "name_result": "Participant",
        "info": "Select your answers and submit the quiz to discover your score.",
        "percent": "Percentage"
    },

    "العربية": {
        "title": "𒀭 اختبار اللغة السومرية",
        "subtitle": "اختبر معرفتك باللغة السومرية والكتابة المسمارية!",
        "welcome": "مرحباً بك في اختبار اللغة السومرية!",
        "description": """
### اختبر معلوماتك!

يقيس هذا الاختبار معرفتك في المجالات التالية:

- **المفردات السومرية ومعانيها**
- **التعرّف على العلامات المسمارية**
- **الأعداد السومرية**
- **القواعد والمفاهيم اللغوية الأساسية**

يتضمن الاختبار **15 سؤالاً**. تحصل على نقطة واحدة لكل إجابة صحيحة.
""",
        "language": "اختر لغة التطبيق",
        "instructions": "اختر إجابة واحدة لكل سؤال. نتمنى لك التوفيق!",
        "participant": "معلومات المشارك",
        "name": "أدخل اسم المشارك:",
        "level": "اختر مستوى معرفتك باللغة السومرية:",
        "levels": ["مبتدئ", "متوسط", "متقدم"],
        "questions": "الأسئلة الخمسة عشر",
        "choose": "اختر إجابتك:",
        "confidence": "ما مدى ثقتك بمعرفتك باللغة السومرية؟",
        "feedback": "ملاحظاتك أو اقتراحاتك حول الاختبار:",
        "submit": "إرسال الاختبار",
        "missing_name": "يرجى إدخال اسم المشارك.",
        "missing_answers": "يرجى الإجابة عن الأسئلة الخمسة عشر قبل الإرسال.",
        "results": "𒀭 نتائج الاختبار",
        "score": "النتيجة النهائية",
        "excellent": "ممتاز! لقد أظهرت معرفة ممتازة باللغة السومرية والكتابة المسمارية!",
        "very_good": "جيد جداً! لديك معرفة جيدة باللغة السومرية وكتابتها.",
        "fair": "نتيجة مقبولة. ننصحك بمواصلة دراسة اللغة السومرية.",
        "poor": "واصل الدراسة! تحتاج إلى تحسين معرفتك باللغة السومرية والكتابة المسمارية.",
        "review": "مراجعة الإجابات بالتفصيل",
        "correct": "إجابة صحيحة!",
        "incorrect": "إجابة خاطئة",
        "your_answer": "إجابتك",
        "correct_answer": "الإجابة الصحيحة",
        "thank_you": "شكراً لمشاركتك في اختبار اللغة السومرية والكتابة المسمارية!",
        "feedback_received": "ملاحظات المشارك",
        "confidence_result": "مستوى الثقة",
        "level_result": "مستوى المعرفة",
        "name_result": "المشارك",
        "info": "اختر إجاباتك وأرسل الاختبار لمعرفة نتيجتك.",
        "percent": "النسبة المئوية"
    }
}

# 3. SIDEBAR LANGUAGE SELECTOR

st.sidebar.title("🌐 Language / اللغة")

language = st.sidebar.radio(
    "Select language / اختر اللغة",
    ["English", "العربية"],
    index=0
)

t = translations[language]

st.sidebar.markdown("---")
st.sidebar.info(t["info"])


# 4. QUIZ QUESTIONS


questions = [
    {
        "en": "1. What does the Sumerian word 'dingir' mean?",
        "ar": "1. ماذا تعني الكلمة السومرية «دينغير» (dingir)؟",
        "options_en": ["King", "God / deity", "Water", "House"],
        "options_ar": ["ملك", "إله / معبود", "ماء", "بيت"],
        "answer": "God / deity",
        "explanation_en": "DINGIR means god or deity. Its sign is 𒀭.",
        "explanation_ar": "تعني DINGIR إلهاً أو معبوداً، وعلامتها المسمارية هي 𒀭."
    },
    {
        "en": "2. Which cuneiform sign represents AN?",
        "ar": "2. أي علامة مسمارية تمثل AN؟",
        "options_en": ["𒂍", "𒀭", "𒆠", "𒈗"],
        "options_ar": ["𒂍", "𒀭", "𒆠", "𒈗"],
        "answer": "𒀭",
        "explanation_en": "𒀭 is the sign AN, meaning heaven or sky.",
        "explanation_ar": "𒀭 هي علامة AN وتعني السماء."
    },
    {
        "en": "3. What does the Sumerian word 'é' mean?",
        "ar": "3. ماذا تعني الكلمة السومرية «إي» (é)؟",
        "options_en": ["Water", "House / temple", "Sun", "Man"],
        "options_ar": ["ماء", "بيت / معبد", "شمس", "رجل"],
        "answer": "House / temple",
        "explanation_en": "É means house or temple. Its sign is 𒂍.",
        "explanation_ar": "تعني É البيت أو المعبد، وعلامتها 𒂍."
    },
    {
        "en": "4. Which sign represents LUGAL (king)?",
        "ar": "4. أي علامة مسمارية تمثل LUGAL (ملك)؟",
        "options_en": ["𒈗", "𒀭", "𒊩", "𒌓"],
        "options_ar": ["𒈗", "𒀭", "𒊩", "𒌓"],
        "answer": "𒈗",
        "explanation_en": "𒈗 is LUGAL, meaning king.",
        "explanation_ar": "𒈗 هي علامة LUGAL وتعني الملك."
    },
    {
        "en": "5. What does the Sumerian word 'ki' mean?",
        "ar": "5. ماذا تعني الكلمة السومرية KI؟",
        "options_en": ["Earth / place", "Fire", "King", "Moon"],
        "options_ar": ["الأرض / المكان", "النار", "الملك", "القمر"],
        "answer": "Earth / place",
        "explanation_en": "KI means earth, ground or place. Its sign is 𒆠.",
        "explanation_ar": "تعني KI الأرض أو المكان، وعلامتها 𒆠."
    },
    {
        "en": "6. Which sign represents UD (sun / day)?",
        "ar": "6. أي علامة تمثل UD (الشمس / النهار)؟",
        "options_en": ["𒌓", "𒂍", "𒀭", "𒈗"],
        "options_ar": ["𒌓", "𒂍", "𒀭", "𒈗"],
        "answer": "𒌓",
        "explanation_en": "𒌓 is UD, associated with the sun and day.",
        "explanation_ar": "𒌓 هي علامة UD وترتبط بالشمس والنهار."
    },
    {
        "en": "7. What does LUGAL mean?",
        "ar": "7. ماذا تعني كلمة LUGAL؟",
        "options_en": ["Priest", "King", "Farmer", "Scribe"],
        "options_ar": ["كاهن", "ملك", "مزارع", "كاتب"],
        "answer": "King",
        "explanation_en": "LUGAL means king and is written 𒈗.",
        "explanation_ar": "تعني LUGAL الملك وتكتب بالعلامة 𒈗."
    },
    {
        "en": "8. Which sign represents A (water)?",
        "ar": "8. أي علامة مسمارية تمثل A (الماء)؟",
        "options_en": ["𒀀", "𒂍", "𒆠", "𒌓"],
        "options_ar": ["𒀀", "𒂍", "𒆠", "𒌓"],
        "answer": "𒀀",
        "explanation_en": "𒀀 is the sign A, meaning water.",
        "explanation_ar": "𒀀 هي علامة A وتعني الماء."
    },
    {
        "en": "9. What does AMA mean?",
        "ar": "9. ماذا تعني كلمة AMA؟",
        "options_en": ["Father", "Mother", "Son", "Daughter"],
        "options_ar": ["أب", "أم", "ابن", "ابنة"],
        "answer": "Mother",
        "explanation_en": "AMA means mother in Sumerian.",
        "explanation_ar": "تعني AMA الأم باللغة السومرية."
    },
    {
        "en": "10. Which sign represents DUMU (child / son)?",
        "ar": "10. أي علامة تمثل DUMU (طفل / ابن)؟",
        "options_en": ["𒌉", "𒀭", "𒈗", "𒊩"],
        "options_ar": ["𒌉", "𒀭", "𒈗", "𒊩"],
        "answer": "𒌉",
        "explanation_en": "𒌉 is DUMU, meaning child or son.",
        "explanation_ar": "𒌉 هي علامة DUMU وتعني الطفل أو الابن."
    },
    {
        "en": "11. Which Sumerian word means woman?",
        "ar": "11. ما الكلمة السومرية التي تعني امرأة؟",
        "options_en": ["LU₂", "NIN", "MUNUS", "DUMU"],
        "options_ar": ["LU₂", "NIN", "MUNUS", "DUMU"],
        "answer": "MUNUS",
        "explanation_en": "MUNUS means woman or female. Its sign is 𒊩.",
        "explanation_ar": "تعني MUNUS المرأة أو الأنثى، وعلامتها 𒊩."
    },
    {
        "en": "12. Which sign is conventionally used for NIN (lady)?",
        "ar": "12. أي علامة تُستخدم تقليدياً لكتابة NIN (السيدة)؟",
        "options_en": ["𒊩𒌆", "𒂍", "𒀀", "𒆠"],
        "options_ar": ["𒊩𒌆", "𒂍", "𒀀", "𒆠"],
        "answer": "𒊩𒌆",
        "explanation_en": "𒊩𒌆 is a conventional spelling of NIN, meaning lady.",
        "explanation_ar": "𒊩𒌆 كتابة مسمارية تقليدية لـ NIN وتعني السيدة."
    },
    {
        "en": "13. What is the Unicode name of 𒐕?",
        "ar": "13. ما الاسم الرسمي لعلامة العدد المسمارية 𒐕 في يونيكود؟",
        "options_en": ["One GESH2", "Five ASH", "One GESHU", "Two GESH2"],
        "options_ar": ["One GESH2", "Five ASH", "One GESHU", "Two GESH2"],
        "answer": "One GESH2",
        "explanation_en": "𒐕 is CUNEIFORM NUMERIC SIGN ONE GESH2 (U+12415).",
        "explanation_ar": "𒐕 هي العلامة المسمارية العددية ONE GESH2 ورمزها يونيكود U+12415."
    },
    {
        "en": "14. What are the sign values in 𒀭𒈗?",
        "ar": "14. ما القيم الصوتية للعلامتين في التسلسل 𒀭𒈗؟",
        "options_en": [
            "AN and LUGAL",
            "E2 and KI",
            "A and UD",
            "DUMU and MUNUS"
        ],
        "options_ar": [
            "AN و LUGAL",
            "E2 و KI",
            "A و UD",
            "DUMU و MUNUS"
        ],
        "answer": "AN and LUGAL",
        "explanation_en": "The signs have the values AN and LUGAL respectively.",
        "explanation_ar": "تحمل العلامتان القيمتين AN و LUGAL على التوالي."
    },
    {
        "en": "15. Which writing system was used to record Sumerian?",
        "ar": "15. ما نظام الكتابة الذي استُخدم لتدوين اللغة السومرية؟",
        "options_en": [
            "Phoenician alphabet",
            "Greek alphabet",
            "Cuneiform",
            "Latin alphabet"
        ],
        "options_ar": [
            "الأبجدية الفينيقية",
            "الأبجدية اليونانية",
            "الكتابة المسمارية",
            "الأبجدية اللاتينية"
        ],
        "answer": "Cuneiform",
        "explanation_en": "Sumerian was recorded using cuneiform in ancient Mesopotamia.",
        "explanation_ar": "دُوّنت اللغة السومرية باستخدام الكتابة المسمارية في بلاد الرافدين القديمة."
    }
]

# 5. APPLICATION HEADER

st.title(t["title"])
st.subheader(t["subtitle"])

st.markdown(t["description"])

st.info(t["instructions"])

st.markdown("---")

# 6. PARTICIPANT INFORMATION

st.markdown(f"### {t['participant']}")

name = st.text_input(t["name"])

level_index = st.selectbox(
    t["level"],
    range(3),
    format_func=lambda x: t["levels"][x]
)

st.markdown("---")

# 7. DISPLAY THE 15 QUESTIONS

st.markdown(f"### {t['questions']}")

user_answers = []

for i, q in enumerate(questions):

    question_text = q["en"] if language == "English" else q["ar"]
    options = q["options_en"] if language == "English" else q["options_ar"]

    st.write(f"**{question_text}**")

    answer = st.radio(
        t["choose"],
        options,
        index=None,
        key=f"question_{i}"
    )

    user_answers.append(answer)

    st.markdown("---")

# 8. ADDITIONAL WIDGETS

confidence = st.slider(
    t["confidence"],
    min_value=0,
    max_value=100,
    value=50,
    format="%d%%"
)

feedback = st.text_area(t["feedback"])

# 9. SUBMIT BUTTON AND SCORE CALCULATION

if st.button(t["submit"], type="primary"):

    if not name.strip():

        st.error(t["missing_name"])

    elif None in user_answers:

        st.warning(t["missing_answers"])

    else:

        score = 0

        for i, q in enumerate(questions):

            options = q["options_en"] if language == "English" else q["options_ar"]

            correct_index = q["options_en"].index(q["answer"])
            correct_answer = options[correct_index]

            if user_answers[i] == correct_answer:
                score += 1

        percentage = (score / 15) * 100

        # DISPLAY RESULTS

        st.markdown("---")
        st.header(t["results"])

        st.write(f"**{t['name_result']}:** {name}")
        st.write(f"**{t['level_result']}:** {t['levels'][level_index]}")
        st.write(f"**{t['confidence_result']}:** {confidence}%")

        st.metric(
            label=t["score"],
            value=f"{score}/15",
            delta=f"{percentage:.1f}%"
        )

        # RESULT MESSAGE

        if score >= 13:
            st.success(t["excellent"])

        elif score >= 9:
            st.success(t["very_good"])

        elif score >= 6:
            st.warning(t["fair"])

        else:
            st.error(t["poor"])

        # ANSWER REVIEW

        st.markdown("---")
        st.subheader(t["review"])

        for i, q in enumerate(questions):

            options = q["options_en"] if language == "English" else q["options_ar"]
            correct_index = q["options_en"].index(q["answer"])
            correct_answer = options[correct_index]

            explanation = (
                q["explanation_en"]
                if language == "English"
                else q["explanation_ar"]
            )

            if user_answers[i] == correct_answer:

                st.success(f"Question {i+1}: {t['correct']}")

            else:

                st.error(
                    f"Question {i+1}: {t['incorrect']} | "
                    f"{t['your_answer']}: {user_answers[i]} | "
                    f"{t['correct_answer']}: {correct_answer}"
                )

            st.caption(explanation)

        # FEEDBACK

        if feedback.strip():
            st.info(f"{t['feedback_received']}: {feedback}")

        st.markdown("---")
        st.write(t["thank_you"])
