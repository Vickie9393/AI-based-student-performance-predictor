import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #58A6FF !important;
        font-weight: 700 !important;
    }
    
    /* Cards / Metrics container */
    div[data-testid="metric-container"] {
        background: rgba(33, 38, 45, 0.7);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #30363D;
        box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0px 12px 30px rgba(88, 166, 255, 0.2);
    }
    
    div[data-testid="metric-container"] > div {
        color: #8B949E !important;
    }
    div[data-testid="metric-container"] > div > div {
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #238636 0%, #2EA043 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(46, 160, 67, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2EA043 0%, #3FB950 100%);
        box-shadow: 0 6px 20px rgba(46, 160, 67, 0.5);
        transform: translateY(-2px);
    }
    
    /* Download Button Specific */
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #1F6FEB 0%, #388BFD 100%);
        box-shadow: 0 4px 15px rgba(56, 139, 253, 0.3);
    }
    [data-testid="stDownloadButton"] > button:hover {
        background: linear-gradient(135deg, #388BFD 0%, #58A6FF 100%);
        box-shadow: 0 6px 20px rgba(56, 139, 253, 0.5);
    }

    /* Inputs */
    .stSelectbox div[data-baseweb="select"], .stNumberInput input, .stTextInput input, .stSlider div {
        border-radius: 8px;
    }
    
    /* Dividers */
    hr {
        border-color: #30363D !important;
    }
    
    /* Dataframe / Tables */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #30363D;
    }

    /* Hero section specific to main app */
    .hero {
        background: linear-gradient(135deg, #1F6FEB 0%, #7C3AED 100%);
        padding: 50px 30px;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 15px 35px rgba(31, 111, 235, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        transform: rotate(30deg);
        pointer-events: none;
    }
    .hero h1 {
        color: white !important;
        font-size: 3.2rem !important;
        margin-bottom: 15px;
        text-shadow: 0 4px 15px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    .hero h4 {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 500;
        font-size: 1.3rem;
        position: relative;
        z-index: 1;
    }
    
    /* Adjust warning/success info boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
