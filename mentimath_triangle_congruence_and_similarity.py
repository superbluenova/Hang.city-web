import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp

# Set up page configuration
st.set_page_config(
    page_title="Interactive Tutorial: Introduction to Probabilistic Models",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Interactive Tutorial: Introduction to Probabilistic Models")
st.write("""
*Inspired by the clarity and insight of educators like Pierre René Deligne.*

This tutorial provides an interactive introduction to the fundamental concept of probability distributions. 
We will focus on the Normal (Gaussian) distribution as an example, exploring how adjusting parameters such as the mean and standard deviation changes its shape.
You will be able to visualize probability density functions, understand how they represent uncertainty, 
and test your understanding with a brief quiz.
""")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select a section:",
    ["Understanding Probability Distributions", "Interactive Normal Distribution", "Test Your Knowledge"]
)

def normal_pdf(x, mean, std):
    return (1/(std*sqrt(2*pi))) * exp(-0.5*(((x-mean)/std)**2))

if page == "Understanding Probability Distributions":
    st.header("What is a Probability Distribution?")
    st.write("""
    A probability distribution describes how probabilities are assigned to the possible values of a random variable. 
    Consider, for example, the height of adults in a population. Not everyone is the same height; some heights are more common than others. 
    The probability distribution summarizes this pattern, telling us the relative likelihood of different outcomes.
    
    The **Normal (Gaussian) distribution** is one of the most common and important probability distributions. 
    It is symmetric and bell-shaped, characterized completely by two parameters:
    - **Mean (μ):** The center or peak of the distribution.
    - **Standard Deviation (σ):** Measures how spread out the distribution is. A larger σ means that values spread more widely around the mean.
    
    Many real-world phenomena approximate a normal distribution, including measurement errors, test scores, and biological traits like height. 
    This makes understanding normal distributions a critical skill in statistics, data science, and many scientific fields.
    """)

    st.subheader("Key Properties of the Normal Distribution")
    st.write("""
    - **Symmetry:** The normal distribution is symmetric about its mean μ.
    - **Bell-shaped curve:** Most of the probability mass is concentrated around the mean. Values far from the mean are increasingly rare.
    - **The 68-95-99.7 Rule:** Approximately 68% of the area under the curve is within one standard deviation (σ) of the mean, 
      about 95% within two standard deviations, and about 99.7% within three standard deviations.
    """)
    
    st.write("""
    Before diving into the interactive portion, reflect on how changing μ and σ might affect the shape:
    - Increasing μ shifts the curve left or right.
    - Increasing σ stretches the curve, making it "shorter and wider."
    """)

elif page == "Interactive Normal Distribution":
    st.header("Explore the Normal Distribution")
    st.write("""
    Use the sliders below to adjust the **mean (μ)** and the **standard deviation (σ)** of a normal distribution. 
    Observe how the shape of the distribution changes in real-time. 
    This will help build your intuition about how these parameters control the distribution's location and spread.
    """)

    # Interactive controls
    mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, step=0.1)
    std = st.slider("Standard Deviation (σ)", 0.1, 3.0, 1.0, step=0.1)

    # Generate data and plot
    x = np.linspace(mean - 4*std, mean + 4*std, 400)
    y = [normal_pdf(val, mean, std) for val in x]

    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(x, y, color="blue", label=f"N(μ={mean}, σ={std})")
    ax.axvline(mean, color="red", linestyle="--", label="Mean (μ)")
    ax.set_title("Normal Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Probability Density")
    ax.legend()
    st.pyplot(fig)

    st.write("""
    The equation for the normal distribution's Probability Density Function (PDF) is:
    $$ f(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} \\exp\\left(-\\frac{1}{2}\\left(\\frac{x - \\mu}{\\sigma}\\right)^2\\right) $$
    """)

    st.write("""
    **Observations:**
    - Increasing μ shifts the peak left or right.
    - Increasing σ makes the distribution wider and shorter (the total area under the curve remains 1, as all probability distributions must integrate to 1).
    """)

elif page == "Test Your Knowledge":
    st.header("Test Your Knowledge")
    st.write("Answer the following questions to check your understanding of probability distributions and the normal distribution:")

    # We'll create a small quiz with a submit button
    questions = [
        {
            "question": "1. What does the mean (μ) of a normal distribution represent?",
            "options": [
                "How spread out the distribution is.",
                "The central peak of the distribution.",
                "The total area under the curve."
            ],
            "answer": "The central peak of the distribution."
        },
        {
            "question": "2. What does the standard deviation (σ) of a normal distribution represent?",
            "options": [
                "The central location of the distribution.",
                "The total number of samples.",
                "How spread out the distribution is."
            ],
            "answer": "How spread out the distribution is."
        },
        {
            "question": "3. Which of the following is true for all probability distributions?",
            "options": [
                "They must be symmetric and bell-shaped.",
                "Their total area under the curve is 1.",
                "They always represent real-world phenomena accurately."
            ],
            "answer": "Their total area under the curve is 1."
        },
        {
            "question": "4. If we increase the standard deviation (σ) of a normal distribution, the curve becomes:",
            "options": [
                "Narrower and taller.",
                "Wider and shorter.",
                "Unchanged in shape."
            ],
            "answer": "Wider and shorter."
        },
        {
            "question": "5. True or False: The normal distribution is always centered at zero.",
            "options": [
                "True",
                "False"
            ],
            "answer": "False"
        },
        {
            "question": "6. Approximately what percentage of values lie within one standard deviation (±1σ) of the mean in a normal distribution?",
            "options": [
                "About 68%",
                "About 95%",
                "About 99.7%"
            ],
            "answer": "About 68%"
        }
    ]

    user_answers = {}
    for i, q in enumerate(questions):
        st.subheader(q["question"])
        user_answers[i] = st.radio("Select an answer:", q["options"], key=f"q{i}")

    if st.button("Submit Answers"):
        score = 0
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                st.success(f"Question {i+1}: Correct!")
                score += 1
            else:
                st.error(f"Question {i+1}: Incorrect. The correct answer is: {q['answer']}")
        st.write(f"**Your Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()
            st.write("Excellent! You have a strong grasp of the concepts.")
        elif score > len(questions)/2:
            st.write("Good job! A bit more review could help solidify your understanding.")
        else:
            st.write("Don't worry, you can review the material and try again.")

st.write("---")
st.write("**Inspired by the pedagogical clarity of great educators.**")
