import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Madhusudan Ambulkar | Portfolio Dashboard",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL CUSTOM CSS ---
st.markdown("""
    <style>
    /* Absolute Midnight Canvas Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #030307 !important;
    }
    
    /* Premium Cyan-Purple Gradient text for Name */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00B2FE 0%, #4F46E5 50%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem;
        display: inline-block;
    }
    .subtitle {
        font-size: 1.35rem;
        color: #00B2FE; /* Electric Cyan for crisp contrast */
        font-weight: 500;
        margin-bottom: 1.5rem;
        letter-spacing: 0.5px;
    }
    
    /* Section Headers with a Subtle Gradient Line Accent */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #FFFFFF; 
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        position: relative;
        padding-bottom: 0.6rem;
    }
    .section-header::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, #00B2FE 0%, #8B5CF6 50%, transparent 100%);
    }
    
    .job-title {
        font-weight: bold;
        font-size: 1.25rem;
        color: #00B2FE;
    }
    
    /* Custom Tight Spacing Block for Education Layout */
    .edu-container {
        margin-bottom: 1rem;
    }
    .edu-degree {
        font-size: 1.25rem;
        font-weight: 700;
        color: #FAFAFA;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    .edu-uni {
        font-size: 1.05rem;
        color: #CBD5E1;
        margin: 2px 0 0 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    .gpa-text {
        font-size: 0.95rem;
        color: #FAFAFA; /* Updated to complete crisp white */
        font-weight: 600;
        margin: 2px 0 0 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    
    .company-date {
        color: #64748B;
        font-style: italic;
        text-align: right;
        line-height: 1.3;
    }
    
    /* Minimalist Sidebar Links (No Bubbles/Cards) */
    .sidebar-link-container {
        margin-bottom: 12px;
        font-size: 1rem;
    }
    .sidebar-link-container a {
        color: #E2E8F0 !important;
        text-decoration: none !important;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .sidebar-link-container a:hover {
        color: #00B2FE !important;
    }
    .sidebar-email {
        color: #94A2B8;
        font-size: 0.95rem;
        margin-top: 4px;
    }

    /* Premium Midnight Skills Container Elements */
    .skill-category {
        font-size: 1.2rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-top: 1.8rem;
        margin-bottom: 0.8rem;
    }
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 1.5rem;
    }
    .skill-badge {
        background-color: #0B0B14; 
        color: #E2E8F0; 
        padding: 8px 16px;
        border-radius: 6px; 
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid #1E1E30; 
        transition: all 0.25s ease;
    }
    .skill-badge:hover {
        background-color: #121225;
        border-color: #8B5CF6; 
        color: #FFFFFF;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.2);
    }
    
    /* Project Tech Badges with Hover Gradient Accents */
    .proj-badge {
        background: linear-gradient(135deg, #0B0B14 0%, #121225 100%);
        color: #00B2FE;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #1E3A8A;
        margin-right: 6px;
        margin-bottom: 6px;
        display: inline-block;
        transition: all 0.3s ease;
    }
    .proj-badge:hover {
        background: linear-gradient(90deg, #00B2FE 0%, #8B5CF6 100%);
        color: #FFFFFF;
        border-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONTACT & DOWNLOADS ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Madhusudan Abhay Ambulkar")
    st.markdown("### 📍 Frankfurt am Main, Germany")
    st.write("---")
    
    st.markdown("""
        <div class="sidebar-link-container">
            <span>🔗</span> <a href="https://www.linkedin.com/" target="_blank">LinkedIn</a>
        </div>
        <div class="sidebar-link-container">
            <span>💻</span> <a href="https://github.com/" target="_blank">GitHub</a>
        </div>
        <div class="sidebar-link-container" style="margin-top: 15px;">
            <span>📧</span> <span style="font-weight:500; color:#E2E8F0;">Email:</span>
            <div class="sidebar-email">madhusudanambulkar@gmail.com</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    try:
        with open("sample_resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Download Full PDF Resume",
            data=PDFbyte,
            file_name="Madhusudan_Ambulkar_Resume.pdf",
            mime="application/octet-stream",
            use_container_width=True
        )
    except FileNotFoundError:
        st.download_button(
            label="📥 Download Full PDF Resume",
            data="Placeholder content",
            file_name="Resume_Placeholder.pdf",
            mime="text/plain",
            disabled=True,
            help="Upload your sample_resume.pdf to the repository to enable downloading.",
            use_container_width=True
        )

# --- MAIN HERO SECTION ---
st.markdown('<div class="main-title">Madhusudan Abhay Ambulkar</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">GenAI & AI Agents | Computer Vision (YOLO) | Distributed Data Pipelines</div>', unsafe_allow_html=True)

st.markdown("""
I am a Master's student specializing in **High Integrity Systems**, passionate about bridging the gap between raw data intelligence and robust, distributed systems. My background spans building optimized automation pipelines, training heavy-duty computer vision models, and scaling resilient backend infrastructure.
""")

st.write("---")

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📋 Experience & Education", "🛠️ Technical Skills", "💻 Projects Portfolio"])

# ==========================================
# TAB 1: EXPERIENCE & EDUCATION
# ==========================================
with tab1:
    st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<span class="job-title">Software Specialist (Data & Systems Engineering)</span>', unsafe_allow_html=True)
        st.markdown("""
        *   Engineered, explored, and optimized relational databases connecting directly to MySQL infrastructures to write complex ad-hoc queries, profile schemas, and ensure absolute data integrity across critical healthcare data sets.
        *   Diagnosed, performance-tuned, and resolved 300+ advanced database bottlenecks and system anomalies, driving overall operational pipeline efficiency up by 20% within an agile engineering sprint framework.
        *   Architected and standardized technical Standard Operating Procedures (SOPs), cutting down data system integration incident response latencies by 15% across functional engineering layers.
        *   Partnered with Product Analysis teams to design and build end-to-end data pipelines and visualization layers in Power BI, SQL, and Excel, translating complex relational analytics into strategic visual systems.
        """)
    with col2:
        st.markdown('<div class="company-date">eClinicalWorks, Mumbai<br>July 2022 – Aug 2024</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
    
    # Entry 1: Master's Degree (Tight layout, margins zeroed to completely drop layout gaps)
    edu1_col1, edu1_col2 = st.columns([3, 1])
    with edu1_col1:
        st.markdown("""
            <div class="edu-container">
                <p class="edu-degree">MS in High Integrity Systems (AI & Data Science)</p>
                <p class="edu-uni">Frankfurt University of Applied Sciences</p>
            </div>
        """, unsafe_allow_html=True)
    with edu1_col2:
        st.markdown('<div class="company-date" style="padding-top: 2px;">Frankfurt am Main, Germany<br>October 2024 – Present</div>', unsafe_allow_html=True)
        
    # Entry 2: Bachelor's Degree (Tight layout, margins zeroed to completely drop layout gaps)
    edu2_col1, edu2_col2 = st.columns([3, 1])
    with edu2_col1:
        st.markdown("""
            <div class="edu-container">
                <p class="edu-degree">Bachelor of Science in Information Technology</p>
                <p class="edu-uni">University of Mumbai</p>
                <p class="gpa-text">GPA: 1.3 / 4.0</p>
            </div>
        """, unsafe_allow_html=True)
    with edu2_col2:
        st.markdown('<div class="company-date" style="padding-top: 2px;">Mumbai, India<br>2019 – 2022</div>', unsafe_allow_html=True)

# ==========================================
# TAB 2: TECHNICAL SKILLS
# ==========================================
with tab2:
    st.markdown('<div class="section-header">Core Competencies & Tech Stack</div>', unsafe_allow_html=True)
    
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.markdown('<div class="skill-category">📊 Data & Analytics</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <span class="skill-badge">Power BI (DAX)</span>
                <span class="skill-badge">SQL</span>
                <span class="skill-badge">Data Mining</span>
                <span class="skill-badge">Data Cleaning & Transformation</span>
                <span class="skill-badge">Statistics</span>
                <span class="skill-badge">ETL Pipelines</span>
                <span class="skill-badge">Streamlit</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="skill-category">🤖 Gen AI & AI Agents</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <span class="skill-badge">YOLO (Object Detection)</span>
                <span class="skill-badge">Edge Deployment</span>
                <span class="skill-badge">LLM APIs (Claude, OpenAI)</span>
                <span class="skill-badge">RAG</span>
                <span class="skill-badge">LangChain</span>
                <span class="skill-badge">Prompt Engineering</span>
                <span class="skill-badge">Power Automate</span>
            </div>
        """, unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="skill-category">🔧 Programming & Tools</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <span class="skill-badge">Python (Pandas, NumPy, scikit-learn)</span>
                <span class="skill-badge">Excel (VBA/Macros)</span>
                <span class="skill-badge">Jupyter Notebook</span>
                <span class="skill-badge">Git / GitHub</span>
                <span class="skill-badge">VS Code</span>
                <span class="skill-badge">Google Colab</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="skill-category">📋 Dashboards, Reporting & Collaboration</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <span class="skill-badge">SOP Writing</span>
                <span class="skill-badge">Atlassian JIRA</span>
                <span class="skill-badge">MS Office Suite</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="skill-category">🗣️ Languages</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <span class="skill-badge">🗣️ English (C1 - IELTS 7.0)</span>
                <span class="skill-badge">🇩🇪 German (A1.2, actively improving)</span>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 3: PROJECTS PORTFOLIO
# ==========================================
with tab3:
    st.markdown('<div class="section-header">Key Architectures & Implementations</div>', unsafe_allow_html=True)
    
    # Project 1: Refructured Complete Sentences without Small Headings
    with st.container():
        st.markdown("### 👁️ AI-Driven Object Detection System (Distributed Infrastructure Context)")
        st.markdown("""
            <div>
                <span class="proj-badge">YOLOv8n</span>
                <span class="proj-badge">Roboflow</span>
                <span class="proj-badge">Raspberry Pi</span>
                <span class="proj-badge">PXE Network Boot</span>
                <span class="proj-badge">MQTT Broker</span>
                <span class="proj-badge">Kubernetes</span>
                <span class="proj-badge">Python</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        *   Formulated and deployed an end-to-end edge computer vision workflow by sourcing, augmenting, and preprocessing a custom dataset of over 34,000 images within the Roboflow development ecosystem.
        *   Trained and compiled a localized YOLOv8n core network architecture that successfully produced an optimal evaluation performance metric of 0.758 mAP targeted specifically for safety security operations.
        *   Optimized and performance-tuned deep learning execution parameters to achieve minimized system inference latency overheads when deployed directly onto physical hardware edge constraint nodes.
        *   Collaborated tightly within an 8-person project team infrastructure environment to integrate live model inference streams across centralized PXE network boot workers, MQTT data brokers, and Kubernetes orchestrations.
        """)
        st.write("---")
        
    # Project 2: Air Quality Telemetry Pipeline
    with st.container():
        st.markdown("### 🍃 Real Time Air Quality Monitoring System")
        st.markdown("""
            <div>
                <span class="proj-badge">Python</span>
                <span class="proj-badge">Zephyr RTOS</span>
                <span class="proj-badge">Streamlit</span>
                <span class="proj-badge">ETL Pipelines</span>
                <span class="proj-badge">IoT Sensors</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        *   Engineered a hardware-to-cloud telemetry layout utilizing **Zephyr RTOS** to stream raw industrial environmental metrics into a high-performance **6-stage ETL pipeline**.
        *   Maintained absolute continuous data streaming integrity, achieving a **99.8% packet ingestion rate** with an end-to-end telemetry system latency of **29.7ms**.
        *   Embedded threshold automation compliance engines matching international **ASHRAE 62.1 and WHO guidelines**, instantly isolating and classifying air toxicity flags into distinct emergency tiers.
        *   Developed an interactive analytics dashboard in Python **Streamlit**, mapping fused timeseries data streams into instantaneous visual frameworks for non-technical stakeholders.
        """)
        st.write("---")

    # Project 3: Power BI ATM Dashboard
    with st.container():
        st.markdown("### 📊 ATM Transaction Performance Dashboard")
        st.markdown("""
            <div>
                <span class="proj-badge">Power BI</span>
                <span class="proj-badge">DAX Formulas</span>
                <span class="proj-badge">Time Intelligence</span>
                <span class="proj-badge">Data Visualization</span>
                <span class="proj-badge">Excel</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        *   Developed a dynamic **Power BI** commercial analytics engine analyzing critical multi-tier ATM execution variables, tracking revenue patterns, operational overheads, and hardware uptime metrics.
        *   Automated comparative time-series reporting cycles using specialized **DAX measures** and time intelligence formulas, enabling instantaneous detection of underperforming network systems.
        *   Designed high-contrast interactive layout graphs to consolidate transaction data flows, effectively lowering manual diagnostic processing durations by **30%**.
        """)