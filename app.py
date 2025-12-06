import streamlit as st
from dotenv import load_dotenv
from src.pipelines.pipeline import CartoonRecomendationPipeline


load_dotenv()

st.set_page_config(page_title="Anime Recommender", layout="wide")


@st.cache_resource()
def init_pipeline():
    return CartoonRecomendationPipeline()


pipeline = init_pipeline()

st.title("Anime Recommender System")
query = st.text_input(label="Type your anime preferences...")
if query:
    with st.spinner(f"Fetching recommendation for you!"):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)
