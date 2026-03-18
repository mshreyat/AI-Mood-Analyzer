import streamlit as st
import plotly.express as px
import pandas as pd
from sentiment import analyze_mood_advanced
from storage import initialize_csv, save_entry, load_data

st.set_page_config(page_title="Pro Mood Analytics", layout="wide")
initialize_csv()

st.title("📊 Enterprise Mood & Screen Analytics")

# --- DATA INPUT ---
with st.sidebar:
    st.header("Daily Log")
    user_text = st.text_area("Detailed Entry:", height=150, placeholder="Describe your day...")
    screen_time = st.slider("Screen Time (Hours):", 0.0, 16.0, 5.0)
    
    if st.button("Run Advanced Analysis", use_container_width=True):
        if user_text:
            cat, emoji, specific, conf = analyze_mood_advanced(user_text)
            save_entry(user_text, cat, screen_time)
            st.success(f"Analysis Complete!")
            st.metric("Detected Emotion", specific)
            st.metric("AI Confidence", f"{conf:.1%}")
        else:
            st.error("Please enter text.")

# --- ANALYTICS DASHBOARD ---
df = load_data()

if not df.empty:
    # Key Metrics Row
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Entries", len(df))
    m2.metric("Avg Screen Time", f"{df['ScreenTime'].mean():.1f}h")
    m3.metric("Top Mood", df['Mood'].mode()[0])

    # Interactive Plots
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Mood Share")
        fig_pie = px.pie(df, names='Mood', color='Mood',
                         color_discrete_map={'Positive':'#00CC96','Negative':'#EF553B','Neutral':'#636EFA'},
                         hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Mood vs. Screen Time Trend")
        fig_scatter = px.scatter(df, x="ScreenTime", y="Mood", 
                                 size=[10]*len(df), color="Mood",
                                 hover_data=['Text'],
                                 title="How Screen Time Impacts Mood")
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Detailed History")
    st.table(df.tail(5))