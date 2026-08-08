# VibeHire Agent: Universal Predictive AI Interview Assistant

### 🌐 Live Platform: [vibehire-agent](https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/)
**Track:** ViCoDATHON Track 2 — The Interview Agent  
**Development Framework:** Jupyter Notebook & AI-Assisted Pair Programming

---

## 1. Project Overview

VibeHire Agent is an automated technical evaluation system designed to optimize screening workflows for ViCoDATHON Track 2. Rather than forcing candidates through a static list of rigid, hardcoded question fields, this platform initializes a **live, interactive multi-turn AI interview session**. By tracking conversation strings dynamically inside active memory, the agent adapts questions on the fly, mimics human recruiting exchanges, and isolates technical tracking focuses contextually based on historical candidate milestones.

Crucially, the project is designed for universal accessibility. While it processes pre-configured records from a central database, it features an end-to-end self-onboarding pathway. External users can visit the application live, input their unique profile parameters, select completed or skipped nodes along an interactive learning curriculum, and immediately engage with the automated evaluation loop.

---

## 2. Project Objectives

* **Eliminate Scripted Interviewing**: Replace rigid static questioning arrays with dynamic, history-aware, multi-turn interview chat pipelines that adapt naturally to candidate inputs.
* **Isolate Real-Time Knowledge Gaps**: Map and test candidate blind spots contextually by targeting uncompleted curriculum nodes inside the live chat matrix.
* **Deliver Responsive Operational Feedback**: Compute immediate diagnostic dashboards, metric insights, and downloadable scorecard streams without manual grading overhead upon interview termination.
* **Optimize Scalability & Performance**: Utilize high-efficiency O(1) hash map retrieval data layers to maintain instantaneous system render and response tracks during heavy traffic scaling.

---

## 3. Automation Technologies & Tools Used

### Core Frameworks & Deployment
* **Exploratory Data Analysis & Prototyping:** Jupyter Notebook (`interview_agent_dev.ipynb`) was used to experiment with data shapes, run sandbox processing tests, verify dictionary indexing, and structure the question loops step-by-step.
* **Frontend UI Framework:** Streamlit (Configured with native `st.chat_message` components for message thread presentation, `st.chat_input` for conversational entry, and explicit `st.rerun()` interface boundaries to completely control background script evaluations and eliminate infinite rendering loop locks.)
* **Environment Manifest Environment:** Python Standard Libraries (Native system tools prioritized to maintain zero external package dependencies outside the web layer).

### Helper & Automation Modules
* **Data Processing Layer:** json (Utilized to manage high-speed parsing across nested tracking arrays and curriculum modules).
* **Path Routing Automation:** os (Engineered with absolute workspace wrappers to prevent pathing configuration failures when transitioning from local notebook folders to cloud environments).
* **State Serialization Engine:** pickle (Deployed to translate active assessment parameters into high-security binary `.pkl` streams for local report downloads).

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
* **Curriculum Completion Ratio**: A calculated telemetry value mapping total completed modules against the global curriculum denominator to output an interactive progress percentage bar.
* **Mode Scaffolding Triggers**: Background conditionals that actively evaluate specific module parameters (`passed == True` vs. `skipped == True`). Instead of dumping static question arrays on screen, these triggers cleanly feed topic tokens right into the initial chatbot greeting string to scaffold custom-targeted conversational starting points instantly.

---

## 6. Target Labels & Evaluation Rules

Instead of predicting abstract values, the model maps telemetry inputs directly to programmatic output actions using strict logical parameters:

| Input Telemetry Signal | Trigger Evaluation Rule | Final Output Action Target |
| :--- | :--- | :--- |
| `passed == True` & Single Attempt | Qualifies as an established technical competency node. | Triggers high-level, advanced conceptual engineering questions. Appends to Strengths log. |
| `passed == False` or `skipped == True` | Qualifies as a potential knowledge gap or unverified threshold. | Triggers foundational theory questions combined with a Production Readiness Follow-up Query. Appends to Weaknesses log. |
| Active Session Complete | Compiles state answers and system analytics. | Generates a binary `.pkl` session state scorecard containing an automated Mentorship Blueprint download handle. |

---


## Application
<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1599" height="763" alt="image" src="https://github.com/user-attachments/assets/18951778-8321-49c7-8ec0-5294dd3149f6" />
</a>

<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1600" height="758" alt="image" src="https://github.com/user-attachments/assets/106d41af-8f86-4e07-ae4d-15159f5a3d96" />
</a>


## Result
<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1600" height="758" alt="image" src="https://github.com/user-attachments/assets/420ed2fb-5fec-4df7-8190-db01fb979b1a" />
</a>

<a href="https://vibehire-agent-eqsfyo8cmodrzixsz6gjtx.streamlit.app/">
<img width="1599" height="763" alt="image" src="https://github.com/user-attachments/assets/e63605be-93b8-414d-908b-0a63b47b0047" />
</a>


*Built for the ABTalks Hackathon - VibeHire Agent Project*
