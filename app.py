import streamlit as st

# Page Configuration
st.set_page_config(page_title="Divyanshu Singh | AI Core Engine", page_icon="🤖", layout="wide")

# Custom Cyber CSS for Background, Robot Glowing FX and Split Screen
st.markdown("""
    <style>
    .stApp {
        background-color: #05070f;
        color: #e2e8f0;
        font-family: 'Courier New', Courier, monospace;
    }
    .robot-glow {
        font-size: 5rem;
        text-align: center;
        animation: pulse 2s infinite;
        text-shadow: 0 0 20px #00f3ff, 0 0 40px #00f3ff;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .speech-bubble {
        background: rgba(0, 243, 255, 0.05);
        border: 2px solid #00f3ff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
        font-size: 1.2rem;
        color: #00f3ff;
        font-weight: bold;
    }
    .content-box {
        background: rgba(255, 0, 127, 0.03);
        border: 1px dashed rgba(255, 0, 127, 0.4);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .badge-card {
        background: rgba(0, 243, 255, 0.03);
        border: 1px solid #00f3ff;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
    .cert-card {
        background: white;
        color: black;
        padding: 20px;
        border-radius: 8px;
        border-top: 10px solid #1d4ed8;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State for the Interactive Steps
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def reset_system():
    st.session_state.step = 0

# --- STAGE 1: Full Screen Welcome Robot ---
if st.session_state.step == 0:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="robot-glow">🤖</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="speech-bubble" style="text-align: center; max-width: 700px; margin: 0 auto;">
        "SYSTEM INITIALIZED... GREETINGS USER. I AM THE CENTRAL AI PROTOCOL FOR DIVYANSHU SINGH. 
        ACCESSING SECURE DATA REPOSITORY NOW. CLICK BELOW TO INITIATE SPLIT-SCREEN OVERVIEW."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        st.button("INITIALIZE CORE PROTOCOL ⚡", on_click=next_step, use_container_width=True)

# --- STAGE 2+: Split Screen Mode Enabled ---
else:
    # Creating Half-and-Half Layout (PC Split Screen)
    col_robot, col_data = st.columns([1, 1], gap="large")
    
    with col_robot:
        st.markdown('<div class="robot-glow" style="font-size: 4rem; text-align: left;">🤖 [ONLINE]</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Dynamic speech text depending on the current line step
        if st.session_state.step == 1:
            st.markdown('<div class="speech-bubble">"Analyzing developer profile... Divyanshu Singh is a 9th-grade Software Architect with 2 years of production experience in localized automation networks."</div>', unsafe_allow_html=True)
        elif st.session_state.step == 2:
            st.markdown('<div class="speech-bubble">"Scanning Core Shipped Deployments... System has verified the absolute completion of Jarvis ADA (Autonomous Voice Agent) and PropLoom CRM."</div>', unsafe_allow_html=True)
        elif st.session_state.step == 3:
            st.markdown('<div class="speech-bubble">"CRITICAL CREDENTIAL DETECTED! Fetching Global Validation Node from the Blue Ocean Student Entrepreneurs Competition..."</div>', unsafe_allow_html=True)
        elif st.session_state.step == 4:
            st.markdown('<div class="speech-bubble">"NEW ARCHIVE DEPLOYED... Pulling newly verified credential node: Microsoft AI Skills Fest 2026. Auto-accept active. Status: Public."</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="speech-bubble">"Data streaming complete. Core portfolio infrastructure is fully loaded and operational."</div>', unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Control Buttons under the Robot
        if st.session_state.step <= 4:
            st.button("NEXT LINE PROTOCOL ➡️", on_click=next_step, use_container_width=True)
        else:
            st.button("REBOOT PROTOCOL RUN 🔄", on_click=reset_system, use_container_width=True)

    with col_data:
        st.markdown('<h3 style="color: #ff007f; letter-spacing: 2px;">⚡ LIVE DATA STREAM</h3>', unsafe_allow_html=True)
        
        # Right Side dynamic content block based on current step
        if st.session_state.step == 1:
            st.markdown("""
            <div class="content-box">
                <h2 style='color:#00f3ff; margin-top:0;'>🧬 Developer Identity</h2>
                <p><b>Name:</b> Divyanshu Singh</p>
                <p><b>Status:</b> 9th Grade Software Developer</p>
                <p><b>Experience:</b> 2 Years in Production & AI Tooling</p>
                <hr style='border-color:rgba(0,243,255,0.2)'>
                <p style='color:#ff007f;'><i>Target Focus: High-Velocity SaaS & Global Business Ventures.</i></p>
            </div>
            """, unsafe_allow_html=True)
            
        elif st.session_state.step == 2:
            st.markdown("""
            <div class="content-box">
                <h2 style='color:#00f3ff; margin-top:0;'>🔥 Active Shipped Systems</h2>
                <h4 style='color:#ff007f; margin-bottom:2px;'>🤖 Jarvis ADA</h4>
                <p style='font-size:0.9rem; margin-top:0;'>Autonomous AI Voice Assistant integrated with LLM processing nodes for custom local executions.</p>
                <h4 style='color:#ff007f; margin-bottom:2px;'>🏠 PropLoom CRM</h4>
                <p style='font-size:0.9rem; margin-top:0;'>Real Estate Enterprise Suite managing high-fidelity leads, smart data routing, and virtual layouts.</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif st.session_state.step == 3:
            st.markdown("<b style='color:#00f3ff;'>🎖️ VERIFIED VALIDATION NODE:</b>", unsafe_allow_html=True)
            try:
                st.image("628f3cec-96f1-47ec-8d48-ee9045f5d411.png", caption="Blue Ocean Competition Verified Completion Node")
            except:
                st.markdown("""
                <div class="cert-card">
                    <h3 style="color: #1d4ed8; margin:0; font-family:sans-serif;">BLUE OCEAN COMPETITION</h3>
                    <p style="font-size:1.2rem; font-weight:bold; margin-top:10px; border-bottom:1px solid #ccc; padding-bottom:5px;">Certificate of Completion</p>
                    <p style="font-size:0.9rem; color:#555;">Proudly awarded to</p>
                    <h2 style="color:black; margin:5px 0;">Divyanshu singh</h2>
                    <p style="font-size:0.8rem; color:#444;">For successfully completing the Blue Ocean Student Entrepreneurs Mini-Course.</p>
                    <p style="font-size:0.75rem; color:#777; margin-top:20px;"><b>Date:</b> 2026-05-30<br><b>Serial Number:</b> 628f3cec-96f1-47ec-8d48-ee9045f5d411</p>
                </div>
                """, unsafe_allow_html=True)
                
        elif st.session_state.step >= 4:
            st.markdown("<b style='color:#ff007f;'>🛡️ MICROSOFT ACCREDITATION NODE:</b>", unsafe_allow_html=True)
            st.markdown("""
            <div class="content-box" style="border-color: #00f3ff;">
                <h3 style="color: #00f3ff; margin-top:0;">🎖️ AI Skills Fest 2026 Badge</h3>
                <p style="font-size: 0.85rem; color: #a0aec0;">Issued by: <b>Microsoft</b> | Date: June 19, 2026</p>
                <p style="font-size: 0.95rem;">Demonstrated expertise in foundational & applied AI systems to solve complex, real-world development pipelines.</p>
                <div class="badge-card">
                    <span style="color:#ff007f; font-weight:bold;">Verified Core Competencies:</span><br>
                    ⚡ Prompt Engineering | ⚙️ Workflow Automation | 🔒 Responsible AI | 🧠 Applied Artificial Intelligence
                </div>
                <p style="font-size:0.8rem; color:#00f3ff; margin-top:10px;">🟢 <i>Auto-Accept Verified: All future Microsoft credentials sync automatically.</i></p>
            </div>
            """, unsafe_allow_html=True)