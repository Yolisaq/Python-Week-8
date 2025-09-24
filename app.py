# -----------------------------
# CORD-19 Data Explorer App (Memory-Safe Version)
# -----------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("🦠 CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers using the metadata dataset.")

# -----------------------------
# Part 1: Load Data (Sample for Memory Safety)
# -----------------------------
@st.cache_data
def load_data(sample_rows=10000):
    """
    Load a sample of metadata.csv to avoid memory errors.
    If 'metadata_sample.csv' exists, load it directly.
    """
    sample_file = "metadata_sample.csv"
    original_file = "metadata.csv"

    if os.path.exists(sample_file):
        df = pd.read_csv(sample_file)
        return df

    if not os.path.exists(original_file):
        st.error(f"❌ File '{original_file}' not found. Place it in the same folder as app.py.")
        return pd.DataFrame()

    # Load only a sample to avoid MemoryError
    df = pd.read_csv(original_file, nrows=sample_rows)
    df.to_csv(sample_file, index=False)  # Save sample for future use
    return df

df = load_data()

# -----------------------------
# Part 2: Data Cleaning
# -----------------------------
if not df.empty:
    # Handle missing values
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['title'] = df['title'].fillna("No Title")
    df['journal'] = df['journal'].fillna("Unknown")
    df['abstract'] = df['abstract'].fillna("")

    # Additional columns
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

if not df.empty:
    min_year = int(df['year'].min()) if pd.notnull(df['year'].min()) else 2019
    max_year = int(df['year'].max()) if pd.notnull(df['year'].max()) else 2022
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (2020, 2021))
    journal_options = ["All"] + sorted(df['journal'].dropna().unique().tolist())
    selected_journal = st.sidebar.selectbox("Select Journal", journal_options)

    # Apply filters
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    if selected_journal != "All":
        filtered_df = filtered_df[filtered_df['journal'] == selected_journal]

    st.write(f"### Dataset Preview ({len(filtered_df)} papers)")
    st.dataframe(filtered_df[['title', 'authors', 'journal', 'year', 'abstract']].head(50))

# -----------------------------
# Part 3: Analysis & Visualization
# -----------------------------
if not df.empty and not filtered_df.empty:
    st.write("### 📊 Publications by Year")
    year_counts = filtered_df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")
    st.pyplot(fig)

    st.write("### 🏆 Top Journals")
    top_journals = filtered_df['journal'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_journals.values, y=top_journals.index, palette="magma", ax=ax2)
    ax2.set_xlabel("Number of Publications")
    ax2.set_ylabel("Journal")
    st.pyplot(fig2)

    st.write("### ☁️ Word Cloud of Paper Titles")
    titles_text = " ".join(filtered_df['title'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
    fig3, ax3 = plt.subplots(figsize=(12,6))
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis('off')
    st.pyplot(fig3)

    st.write("### 📰 Source Distribution")
if 'source_x' in filtered_df.columns:
    source_counts = filtered_df['source_x'].value_counts().head(10)
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=source_counts.values, y=source_counts.index, palette="cool", ax=ax4)
    ax4.set_xlabel("Number of Papers")
    ax4.set_ylabel("Source")
    st.pyplot(fig4)
    plt.close(fig4)


# -----------------------------
# Part 4: Notes
# -----------------------------
st.write("""
---
### 📝 Notes:
- Dataset is loaded as a **sample** to avoid memory issues.
- Missing values are handled for key columns.
- Word cloud is generated from titles.
- Filters allow selection by year range and journal.
- Beginner-friendly exploratory analysis of CORD-19 papers.
""")
