
import streamlit as st
import json
import os
import pickle

# 1. Setup clean web layout configuration
st.set_page_config(page_title="VibeHire Agent", page_icon="🎤", layout="wide")

# 2. Reliable data retrieval utilities using portable os path rules
def load_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    curr_path = os.path.join(base_path, "curriculum.json")
    cand_path = os.path.join(base_path, "candidates.json")
    
    if not os.path.exists(curr_path):
        curr_path = "curriculum.json"
        cand_path = "candidates.json"
        
    with open(curr_path, "r", encoding="utf-8") as f:
        curriculum = json.load(f)
    with open(cand_path, "r", encoding="utf-8") as f:
        candidates_data = json.load(f)
        
    return curriculum, candidates_data["candidates"]

# 3. Core Adaptive Question Selection Matrix (Advanced vs Fundamentals)
def generate_interview_questions(candidate, curriculum, num_questions=6):
    questions = []
    missions = candidate["missions"]
    
    # Mode A: Passed topics -> Advanced technical questions
    for m in missions:
        if m.get("passed") and len(questions) < num_questions // 2:
            day_info = next((d for d in curriculum["days"] if d["day"] == m["day"]), None)
            if day_info and day_info.get("objectives"):
                obj = day_info["objectives"]
                questions.append(f"Advanced Q on {day_info['title']}: {obj}")
                
    # Mode B: Skipped/Failed topics -> Fundamental core questions + follow-ups
    for m in missions:
        if (m.get("skipped") or m.get("passed") is False) and len(questions) < num_questions:
            day_info = next((d for d in curriculum["days"] if d["day"] == m["day"]), None)
            if day_info and day_info.get("objectives"):
                obj = day_info["objectives"]
                q = f"Fundamental Q on {day_info['title']}: {obj}"
                follow_up = f"Follow-up Q: Why is {day_info['title']} critical for production-ready AI systems?"
                
                questions.append(q)
                if len(questions) < num_questions:
                    questions.append(follow_up)
                    
    return questions[:num_questions]

# 4. Evaluation Reporting Mechanical Engine Loop
def generate_feedback(candidate, curriculum, answers):
    strengths = []
    weaknesses = []
    
    for m in candidate["missions"]:
        day_info = next((d for d in curriculum["days"] if d["day"] == m["day"]), None)
        m_title = day_info["title"] if day_info else f"Day {m['day']} Module"
        
        if m.get("passed") and m.get("attempts", 1) == 1:
            strengths.append(m_title)
        elif m.get("skipped") or m.get("passed") is False:
            weaknesses.append(m_title)
            
    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "tips": "Focus on skipped/failed topics to strengthen fundamentals. Practice monitoring, logging, and observability for production readiness.",
        "answers": answers
    }

# Asset activation trigger
try:
    curriculum, profiles = load_data()
except Exception as e:
    st.error("Data tracking configuration assets are missing or corrupt.")
    st.stop()

# 5. Interactive UI Roster Setup Panels
st.title("🎤 VibeHire Agent")
st.markdown("### Universal Predictive AI Interview Assistant")

st.sidebar.title("🛠️ Mode Selection")
app_mode = st.sidebar.radio("Choose Input Method:", ["Select from Database", "Input Custom Candidate"])

if app_mode == "Select from Database":
    names = [c["member"]["name"] for c in profiles]
    choice = st.sidebar.selectbox("Select Candidate", names)
    cand = next(c for c in profiles if c["member"]["name"] == choice)
    
else:
    st.sidebar.markdown("---")
    st.sidebar.subheader("👤 New Profile Attributes")
    custom_name = st.sidebar.text_input("Candidate Name", "Jane Doe")
    custom_role = st.sidebar.text_input("Target Job Role", "Machine Learning Engineer")
    custom_exp = st.sidebar.number_input("Years of Experience", min_value=0, max_value=40, value=5)
    custom_edu = st.sidebar.text_input("Education Background", "M.S. Data Science")
    
    st.sidebar.markdown("**Select Cleared Curriculum Modules:**")
    custom_missions = []
    
    for day_info in curriculum["days"]:
        cleared = st.sidebar.checkbox(f"Day {day_info['day']}: {day_info['title']}", value=True, key=f"c_m_{day_info['day']}")
        custom_missions.append({
            "day": day_info["day"],
            "title": day_info["title"],
            "passed": cleared,
            "attempts": 1 if cleared else 0
        })
        
    cand = {
        "member": {
            "name": custom_name,
            "jobRole": custom_role,
            "yearsExperience": custom_exp,
            "education": custom_edu
        },
        "signals": {
            "missionsCompleted": len([m for m in custom_missions if m["passed"]]),
            "missionsFirstTry": len([m for m in custom_missions if m["passed"]])
        },
        "missions": custom_missions
    }

# Render profile summaries dashboard template cards
st.subheader("📋 Candidate Summary Profile")
col1, col2, col3 = st.columns(3)
col1.metric("Name", cand["member"]["name"])
col2.metric("Role", cand["member"]["jobRole"])
col3.metric("Experience", f"{cand['member']['yearsExperience']} Yrs")

st.write(f"🎓 **Education:** {cand['member']['education']}")
st.write(f"🚀 **Missions Completed:** {cand['signals'].get('missionsCompleted', len([m for m in cand['missions'] if m.get('passed')]))}")

# Roadmap timeline layout visualization component
st.write("**Curriculum Completion Roadmap Metric:**")
progress = len([m for m in cand["missions"] if m.get("passed")]) / len(cand["missions"])
st.progress(progress)

st.divider()
st.subheader("💬 Adaptive Interview Questions")

qs = generate_interview_questions(cand, curriculum)
answers = {}

if "chat_history" not in st.session_state:
    first_q = qs[0] if isinstance(qs, list) and len(qs) > 0 else "your general technical milestones"
    st.session_state.chat_history = [
        {"role": "assistant", "content": f"Hello! Let's kick off your adaptive interview. Can you talk about your hands-on implementation details regarding: {first_q}?"}
    ]

# 1. Render active conversational chat history logs
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 2. Track chat interaction values via input field
if user_reply := st.chat_input("Type your technical response here..."):
    st.session_state.chat_history.append({"role": "user", "content": user_reply})
    with st.chat_message("user"):
        st.write(user_reply)
        
    # 3. Simulate an intelligent, contextual AI follow-up response loop
    with st.chat_message("assistant"):
        with st.spinner("Analyzing responses and mapping framework concepts..."):
            follow_up = "Understood. Based on that implementation, how would you design a recovery plan if the pipeline crashes or encounters data drift in production?"
            st.write(follow_up)
            st.session_state.chat_history.append({"role": "assistant", "content": follow_up})

# 4. Generate Performance Feedback action trigger using the dynamic chat logs
st.divider()
if st.button("Generate Performance Feedback", type="primary"):
    st.session_state.feedback_report = generate_feedback(cand, curriculum, {"logs": str(st.session_state.chat_history)})
# ----------------------------------------------

if "feedback_report" in st.session_state:
    report = st.session_state.feedback_report
    st.subheader("📊 Structured Assessment Performance Feedback")
    st.success(f"**Strengths:** " + ", ".join(report["strengths"][:6]) if report["strengths"] else "None flagged")
    st.error(f"**Weaknesses:** " + ", ".join(report["weaknesses"][:6]) if report["weaknesses"] else "None flagged")
    st.info(f"**Mentorship Recommendation Blueprint:** " + report["tips"])
    
    # Export system generating serialization blocks dynamically (.pkl stream)
    serialized_bytes = pickle.dumps(report)
    st.download_button(
        label="📥 Download Session Report Asset (.pkl)",
        data=serialized_bytes,
        file_name=f"vibe_session_{cand['member']['name'].replace(' ', '_').lower()}.pkl",
        mime="application/octet-stream"
    )

st.markdown("---")
st.caption("Built with ❤️ for ABTalks Hackathon - VibeHire Agent")
