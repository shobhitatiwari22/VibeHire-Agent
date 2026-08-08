import streamlit as st
import json
import pickle

# -------------------------------
# Load curriculum and candidates
# -------------------------------
with open("curriculum.json") as f:
    curriculum = json.load(f)

with open("candidates.json") as f:
    data = json.load(f)

profiles = data["candidates"]

# -------------------------------
# Helper functions
# -------------------------------
def generate_interview_questions(candidate, curriculum, num_questions=8):
    questions = []
    missions = candidate["missions"]

    # Passed topics → advanced questions
    for m in missions:
        if m.get("passed") and len(questions) < num_questions//2:
            day_info = next(d for d in curriculum["days"] if d["day"] == m["day"])
            q = f"Advanced Q on {day_info['title']}: {day_info['objectives'][0]}"
            questions.append(q)

    # Skipped/failed topics → fundamentals + follow-up
    for m in missions:
        if (m.get("skipped") or m.get("passed") is False) and len(questions) < num_questions:
            day_info = next(d for d in curriculum["days"] if d["day"] == m["day"])
            q = f"Fundamental Q on {day_info['title']}: {day_info['objectives'][0]}"
            follow_up = f"Follow-up Q: Why is {day_info['title']} critical for production-ready AI systems?"
            questions.append(q)
            if len(questions) < num_questions:
                questions.append(follow_up)

    return questions[:num_questions]

def generate_feedback(candidate, answers):
    strengths = []
    weaknesses = []
    for m in candidate["missions"]:
        if m.get("passed") and m.get("attempts") == 1:
            strengths.append(m["title"])
        elif m.get("skipped") or m.get("passed") is False:
            weaknesses.append(m["title"])

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "tips": "Focus on skipped/failed topics to strengthen fundamentals. Practice monitoring, logging, and observability for production readiness.",
        "answers": answers
    }

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="VibeHire Agent", page_icon="🎤", layout="wide")

st.title("🎤 VibeHire Agent")
st.markdown("### Adaptive AI Interview Agent for ABTalks Hackathon")

# Sidebar for candidate selection
names = [c["member"]["name"] for c in profiles]
choice = st.sidebar.selectbox("Select Candidate", names)

cand = next(c for c in profiles if c["member"]["name"] == choice)

# Candidate summary
st.subheader("📋 Candidate Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Name", cand["member"]["name"])
col2.metric("Role", cand["member"]["jobRole"])
col3.metric("Experience", f"{cand['member']['yearsExperience']} yrs")

st.write("🎓 Education:", cand["member"]["education"])
st.write("📊 Missions Completed:", cand["signals"]["missionsCompleted"])
st.write("⚡ First-Try Success:", cand["signals"]["missionsFirstTry"])

# Interview questions
st.subheader("📝 Adaptive Interview Questions")
qs = generate_interview_questions(cand, curriculum)

answers = {}
for i, q in enumerate(qs, 1):
    st.markdown(f"**Q{i}:** {q}")
    ans = st.text_area(f"Your Answer to Q{i}", key=f"ans{i}")
    answers[f"Q{i}"] = ans

# Feedback
if st.button("Generate Feedback"):
    feedback = generate_feedback(cand, answers)
    st.subheader("📈 Structured Feedback")
    st.success("**Strengths:** " + ", ".join(feedback["strengths"]))
    st.error("**Weaknesses:** " + ", ".join(feedback["weaknesses"]))
    st.info("**Tips:** " + feedback["tips"])

    # Save interview session with pickle
    with open("session.pkl", "wb") as f:
        pickle.dump(feedback, f)
    st.download_button("⬇️ Download Session Report", data=pickle.dumps(feedback), file_name="session.pkl")

# Unique UI design: add progress bar + theme
progress = len([m for m in cand["missions"] if m.get("passed")]) / len(cand["missions"])
st.progress(progress)

st.markdown("---")
st.caption("Built with ❤️ for ABTalks Hackathon · VibeHire Agent")
