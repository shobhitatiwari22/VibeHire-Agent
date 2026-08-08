# VibeHire Agent: Universal Predictive AI Interview Assistant

### 🌐 Live Platform: [vibehire-agent](https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/)
**Track:** ViCoDATHON Track 2 — The Interview Agent  
**Development Framework:** Jupyter Notebook & AI-Assisted Pair Programming

---

## 1. Project Overview
VibeHire Agent is an automated evaluation system designed to revolutionize technical recruiting. Instead of running candidates through a static list of hardcoded questions, this platform operates as an intelligent recruiter that dynamically adapts its interview flow based on a candidate’s past learning progress. 

Crucially, the project is designed for **universal accessibility**. While it processes pre-configured records from a central database, it features an end-to-end self-onboarding pathway. External users can visit the application live, input their unique profile parameters, select completed or skipped nodes along an interactive learning curriculum, and immediately engage with the automated evaluation loop.

---

## 2. Project Objectives
* **Eliminate Scripted Interviewing:** Replace static questioning arrays with dynamic, history-aware interview pipelines.
* **Isolate Real-Time Knowledge Gaps:** Map and test candidate blind spots by targeting uncompleted curriculum nodes.
* **Provide Instant Operational Feedback:** Deliver background evaluations, metric insights, and downloadable scorecard streams without manual grading overhead.
* **Support Seamless Public Self-Registration:** Decouple dependency on predefined server data, allowing immediate use by any visiting applicant.

---

## 3. Automation Technologies & Tools Used

### Core Frameworks & Deployment
* **Exploratory Data Analysis & Prototyping:** `Jupyter Notebook` (`Interview_agent_dev.ipynb` was used to experiment with data shapes, run sandbox processing tests, verify dictionary indexing, and structure the question loops step-by-step).
* **Frontend UI Framework:** `Streamlit` (Selected for fast execution, state persistence across interactive clicks, and clean data visualization panels).
* **Environment Manifest Environment:** `Python Standard Libraries` (Native system tools prioritized to maintain zero external package dependencies outside the web layer).

### Helper & Automation Modules
* **Data Processing Layer:** `json` (Utilized to manage high-speed parsing across nested tracking arrays and curriculum modules).
* **Path Routing Automation:** `os` (Engineered with absolute workspace wrappers to prevent pathing configuration failures when transitioning from local notebook folders to cloud environments).
* **State Serialization Engine:** `pickle` (Deployed to translate active assessment parameters into high-security binary `.pkl` streams for local report downloads).

### AI Collaboration Tooling
* **AI Coding Partner:** Leveraged as an interactive teammate to write cleaner loops, handle nested list comprehensions, optimize the Streamlit session state architecture, and generate professional software engineering documentation.

---

## 4. Dataset Information
The application operates on an interconnected multi-file data schema that feeds raw variables straight into the interview evaluation pipeline:

1. **`curriculum.json`**: The structural baseline containing the global education tracks. It documents daily operational modules, core titles, and learning objectives.
2. **`candidates.json`**: The core student repository documenting individual profile data structures, historical tracking arrays, and progress statuses.
3. **`technical-spec.md`**: The structural documentation reference containing reporting constraints and structural alignment layouts required by the evaluation scorecard.

---

## 5. Predictive Features & Telemetry Setup
The engine dynamically compiles raw user history data into active mathematical vectors and telemetry signals to structure the interview layout:

* **`signals.missionsCompleted`**: Calculated array tracking the exact quantity of milestones a candidate has successfully completed.
* **`signals.missionsFirstTry`**: Tracks structural execution efficiency by isolating how many modules were passed on the initial attempt.
* **Curriculum Completion Ratio:** A calculated telemetry value mapping total completed modules against the global curriculum denominator to output an interactive progress percentage bar.
* **Mode Scaffolding Triggers:** Conditional signals checking lookups across specific module parameters (`passed` == `True` vs. `skipped` == `True`) to dictate immediate question generation paths.

---

## 6. Target Labels & Evaluation Rules
Instead of predicting abstract values, the model maps telemetry inputs directly to programmatic output actions using strict logical parameters:

| Input Telemetry Signal | Trigger Evaluation Rule | Final Output Action Target |
| :--- | :--- | :--- |
| **`passed == True`** & Single Attempt | Qualifies as an established technical competency node. | Triggers high-level, advanced conceptual engineering questions. Appends to **Strengths** log. |
| **`passed == False`** or **`skipped == True`** | Qualifies as a potential knowledge gap or unverified threshold. | Triggers foundational theory questions combined with a *Production Readiness Follow-up Query*. Appends to **Weaknesses** log. |
| **Active Session Complete** | Compiles state answers and system analytics. | Generates a binary `.pkl` session state scorecard containing an automated Mentorship Blueprint download handle. |

---

## Application
<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1600" height="765" alt="image" src="https://github.com/user-attachments/assets/97349f86-767f-4067-95ed-cb8adf6700e1" />
</a>
<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1599" height="763" alt="image" src="https://github.com/user-attachments/assets/0b783df2-46cf-45ed-bf42-3036862d2fee" />
</a>


## Result
<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1600" height="768" alt="image" src="https://github.com/user-attachments/assets/989b297d-2d1c-48ef-afa4-4332aeb37ccd" />
</a>

<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1600" height="749" alt="image" src="https://github.com/user-attachments/assets/677ac4c1-379e-4bf2-9813-e4def279497e" />
</a>


*Built for the ABTalks Hackathon - VibeHire Agent Project*
