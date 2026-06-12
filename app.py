
import streamlit as st
import pandas as pd
import joblib

# Load the necessary files
@st.cache_resource
def load_data():
    df = joblib.load('model_data.pkl')
    cosine_sim = joblib.load('cosine_sim_matrix.pkl')
    return df, cosine_sim

df, cosine_sim = load_data()

# App Interface
st.title("📚 Which book should you read?")

# Widgets
selected_book = st.selectbox("Select a book you liked:", df['title'].unique())
num_recs = st.slider("How many recommendations?", 1, 5, 3)

# Logic
def get_recommendations(title, num):
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices[title]
    target_cluster = df.loc[idx, 'cluster']

    cluster_indices = df[df['cluster'] == target_cluster].index
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = [s for s in sim_scores if s[0] in cluster_indices and s[0] != idx]

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[:num]

    return df['title'].iloc[[i[0] for i in sim_scores]]

if st.button("Recommend me a book!"):
    st.subheader(f"If you liked '{selected_book}', you might enjoy:")
    recommendations = get_recommendations(selected_book, num_recs)
    for book in recommendations:
        st.success(f"✅ {book}")
