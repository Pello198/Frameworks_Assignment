import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- Load data ---
@st.cache_data
def load_data(path="metadata.csv"):
    df = pd.read_csv(path, low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda s: len(str(s).split()))
    return df

df = load_data()

# --- Layout ---
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# --- Sidebar filters ---
years = df['year'].dropna().unique()
years = sorted([int(y) for y in years if y > 1900])
year_range = st.sidebar.slider("Select year range", min(years), max(years), (2019, 2021))

journals = df['journal'].fillna('Unknown').unique().tolist()
selected_journal = st.sidebar.selectbox("Filter by Journal", ["All"] + sorted(journals))

# --- Apply filters ---
df_filtered = df[df['year'].between(year_range[0], year_range[1])]
if selected_journal != "All":
    df_filtered = df_filtered[df_filtered['journal'].fillna('Unknown') == selected_journal]

# --- Metrics ---
st.metric("Total Papers", len(df_filtered))
st.metric("Unique Journals", df_filtered['journal'].nunique())

# --- Publications by Year ---
year_counts = df_filtered['year'].value_counts().sort_index()
plt.figure(figsize=(8,4))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
st.pyplot(plt)
plt.close()

# --- Top Journals ---
journal_counts = df_filtered['journal'].fillna('Unknown').value_counts().head(15)
plt.figure(figsize=(8,4))
journal_counts.sort_values().plot(kind='barh')
plt.title("Top Journals")
st.pyplot(plt)
plt.close()

# --- Word Cloud ---
text = " ".join(df_filtered['title'].fillna("").tolist())
wc = WordCloud(width=800, height=400, collocations=False).generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)
plt.close()

# --- Show sample data ---
st.subheader("Sample Data")
st.dataframe(df_filtered.head(100))
