
import streamlit as st
from llm import llm
from prompts import prompt
from schema import ReviewAnalyzer

st.set_page_config(
    page_title="AI Review Analyzer",
    page_icon="⭐"
)

st.title("⭐ AI Review Analyzer")

review = st.text_area(
    "Paste the customer review here",
    height=250
)

if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        structured_llm = llm.with_structured_output(ReviewAnalyzer)

        formatted_prompt = prompt.invoke(
            {
                "review": review
            }
        )
        try:
           result = structured_llm.invoke(formatted_prompt)
           st.write(result)
        except Exception as e:
           st.exception(e)
        result = structured_llm.invoke(formatted_prompt)

        st.success("Analysis Complete")

        st.subheader("Summary")
        st.write(result.summary)

        st.subheader("Sentiment")
        st.write(result.sentiment)

        st.subheader("Rating")
        st.write(f"⭐ {result.rating} / 5")

        st.subheader("Confidence")
        st.progress(result["confidence"])
        st.write(result.confidence)

        st.subheader("Positive Points")
        for point in result.positive_points:
            st.success(point)

        st.subheader("Negative Points")
        for point in result.negative_points:
            st.error(point)

        st.subheader("Recommendation")
        st.info(result.recommendation)
