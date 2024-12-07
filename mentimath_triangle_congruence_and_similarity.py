import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Interactive Tutorial: Triangle Similarity and Congruence",
    layout="centered"
)

# Page Title & Introduction
st.title("Interactive Tutorial: Triangle Similarity and Congruence")
st.write("""
*Subtly explore the nature of triangles and discover the conditions under which they are similar or congruent.*

Triangles are fundamental shapes in geometry. Understanding when they are similar or congruent helps solve a wide range of geometric problems.
This tutorial will guide you through key concepts with interactive illustrations and a short quiz to reinforce your knowledge.

Use the sidebar to select a topic:
- **Triangle Similarity**: Learn how angles and scale factors define similarity.
- **Triangle Congruence**: Explore conditions for exact "match" between triangles.
- **Test Your Knowledge**: Take a quick quiz to check what you've learned.
""")

# Sidebar navigation
topic = st.sidebar.radio(
    "Choose a topic:",
    ["Triangle Similarity", "Triangle Congruence", "Test Your Knowledge"]
)

# Helper Functions
def plot_triangle(ax, vertices, color, label, show_points=True):
    """Plot a triangle given its vertices."""
    x, y = zip(*vertices)
    x = list(x) + [x[0]]  # close the shape
    y = list(y) + [y[0]]
    ax.plot(x, y, color=color, label=label, linewidth=2)
    ax.fill(x, y, color=color, alpha=0.2)
    if show_points:
        ax.scatter(x[:-1], y[:-1], color=color)

def set_dynamic_limits(vertices_list, ax):
    """Automatically set plot limits to fit the triangles nicely."""
    x_vals = []
    y_vals = []
    for vertices in vertices_list:
        for xx, yy in vertices:
            x_vals.append(xx)
            y_vals.append(yy)
    margin = 1
    ax.set_xlim(min(x_vals) - margin, max(x_vals) + margin)
    ax.set_ylim(min(y_vals) - margin, max(y_vals) + margin)
    ax.set_aspect("equal", adjustable='box')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

# Triangle Similarity Section
def draw_similarity():
    st.subheader("Exploring Similarity")
    st.write("""
    Two triangles are **similar** if their corresponding angles are equal and their sides are in proportion.
    This essentially means one is a scaled version of the other. Use the controls below to see how changing the scale 
    factor affects the size of a second triangle while preserving its shape.
    """)

    # Controls in a more integrated layout
    col1, col2 = st.columns(2)
    with col1:
        angle1 = st.slider("Angle 1 of Triangle A (°)", 20, 150, 60, help="Adjust one angle, other angles update automatically.")
        angle2 = st.slider("Angle 2 of Triangle A (°)", 20, 150, 50)
    with col2:
        scale_factor = st.slider("Scale Factor (Triangle B)", 0.5, 3.0, 1.5, help="How much larger or smaller Triangle B is compared to A.")

    angle3 = 180 - angle1 - angle2
    if angle3 <= 0:
        st.error("Angles must sum to 180°. Please adjust your angles.")
        return

    # Calculate vertices for Triangle A
    base_a = 5
    height_a = base_a * np.tan(np.radians(angle2))
    vertices_a = [(0, 0), (base_a, 0), (0, height_a)]

    # Scaled Triangle B
    base_b = base_a * scale_factor
    height_b = height_a * scale_factor
    vertices_b = [(0, 0), (base_b, 0), (0, height_b)]

    fig, ax = plt.subplots(figsize=(5,5))
    plot_triangle(ax, vertices_a, color="blue", label="Triangle A")
    plot_triangle(ax, vertices_b, color="green", label="Triangle B")

    set_dynamic_limits([vertices_a, vertices_b], ax)
    ax.set_title("Triangle Similarity")

    st.pyplot(fig)

    st.write("""
    Notice how changing the scale factor affects only the size, not the shape. The angles remain the same, 
    illustrating that these two triangles remain similar.
    """)

# Triangle Congruence Section
def draw_congruence():
    st.subheader("Exploring Congruence")
    st.write("""
    Two triangles are **congruent** if they are identical in shape and size. 
    This means you can place one triangle on top of the other and they would align perfectly. 
    Experiment with the sliders below to try to make both triangles match exactly.
    """)

    col1, col2 = st.columns(2)
    with col1:
        side_a1 = st.slider("Triangle A: Side A", 1.0, 10.0, 5.0)
        side_b1 = st.slider("Triangle A: Side B", 1.0, 10.0, 7.0)
        angle_a = st.slider("Triangle A: Included Angle (°)", 10, 170, 60)
    with col2:
        side_a2 = st.slider("Triangle B: Side A", 1.0, 10.0, 5.0)
        side_b2 = st.slider("Triangle B: Side B", 1.0, 10.0, 7.0)
        angle_b = st.slider("Triangle B: Included Angle (°)", 10, 170, 60)

    # Calculate vertices for Triangle A
    x2_a = side_a1 * np.cos(np.radians(angle_a))
    y2_a = side_a1 * np.sin(np.radians(angle_a))
    vertices_a = [(0, 0), (side_b1, 0), (x2_a, y2_a)]

    # Calculate vertices for Triangle B
    x2_b = side_a2 * np.cos(np.radians(angle_b))
    y2_b = side_a2 * np.sin(np.radians(angle_b))
    vertices_b = [(0, 0), (side_b2, 0), (x2_b, y2_b)]

    fig, ax = plt.subplots(figsize=(5,5))
    plot_triangle(ax, vertices_a, color="blue", label="Triangle A")
    plot_triangle(ax, vertices_b, color="red", label="Triangle B")
    set_dynamic_limits([vertices_a, vertices_b], ax)
    ax.set_title("Triangle Congruence")

    st.pyplot(fig)

    st.write("""
    Try to set the sides and included angle of Triangle B equal to those of Triangle A. 
    When all corresponding sides and angles are the same, the triangles become congruent.
    """)

# Test Your Knowledge Section
def test_your_knowledge():
    st.subheader("Test Your Knowledge")
    st.write("""
    Ready for a quick check? Select the best answer for each question, then click "Submit All Answers" at the end.
    """)

    questions = [
        {
            "q": "1. Which is a valid criterion for triangle similarity?",
            "options": ["SSA", "AAA", "ASA (for similarity)"],
            "answer": "AAA"
        },
        {
            "q": "2. If two triangles are similar, what must be true?",
            "options": [
                "All corresponding angles match, and sides are in proportion.",
                "They have the same area.",
                "They must be congruent."
            ],
            "answer": "All corresponding angles match, and sides are in proportion."
        },
        {
            "q": "3. The sum of the interior angles of any triangle is:",
            "options": ["90°", "180°", "360°"],
            "answer": "180°"
        },
        {
            "q": "4. Which of the following ensures two triangles are congruent?",
            "options": ["SSS", "AAA", "Just equal angles"],
            "answer": "SSS"
        },
        {
            "q": "5. True or False: All equilateral triangles are similar.",
            "options": ["True", "False"],
            "answer": "True"
        },
        {
            "q": "6. Are right triangles with one angle of 30° similar to each other?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },
        {
            "q": "7. Is AAA a valid criterion for congruence?",
            "options": ["Yes", "No"],
            "answer": "No"
        }
    ]

    user_answers = []
    for i, q in enumerate(questions):
        ans = st.radio(q["q"], q["options"], key=f"q{i}", index=0)
        user_answers.append(ans)

    if st.button("Submit All Answers"):
        score = 0
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                st.success(f"Q{i+1}: Correct!")
                score += 1
            else:
                st.error(f"Q{i+1}: Incorrect. Correct answer: {q['answer']}")
        st.write(f"**Your Score: {score}/{len(questions)}**")
        if score == len(questions):
            st.balloons()

# Execute the selected topic
if topic == "Triangle Similarity":
    draw_similarity()
elif topic == "Triangle Congruence":
    draw_congruence()
else:
    test_your_knowledge()

st.write("---")
st.write("*Continue exploring geometry or revisit the material to strengthen your understanding.*")
