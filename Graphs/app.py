import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Streamlit page setup
st.set_page_config(page_title="Multi-Domain Recommendation System", layout="wide")
st.title("🤖 Multi-Domain Recommendation System (Random Sample View)")

# Create 3 tabs
tab1, tab2, tab3 = st.tabs(["🎓 Course", "🎬 Movie", "🛒 E-Commerce"])

# ================================
# 🎓 Course Tab – Random Pie Chart
# ================================
with tab1:
    st.header("🎓 Course Recommendations (Random Sample)")

    # Show random course recommendations
    st.subheader("📘 Sample Course List")
    sample_courses = pd.DataFrame({
        'Course Name': [f"Course {i}" for i in range(1, 6)],
        'University': np.random.choice(['MIT', 'Stanford', 'Harvard'], 5),
        'Difficulty': np.random.choice(['Beginner', 'Intermediate', 'Advanced'], 5),
        'Rating': np.round(np.random.uniform(3.0, 5.0, 5), 1)
    })

    for _, row in sample_courses.iterrows():
        with st.expander(row['Course Name']):
            st.markdown(f"**University**: {row['University']}")
            st.markdown(f"**Difficulty**: {row['Difficulty']}")
            st.markdown(f"**Rating**: ⭐ {row['Rating']}")
            st.markdown("**Description**: This is a placeholder course description.")
            st.markdown("[🔗 Go to Course](https://example.com)")

    # Pie chart
    st.subheader("📊 Difficulty Level Distribution (Random)")
    diff_data = pd.DataFrame({
        'Difficulty': ['Beginner', 'Intermediate', 'Advanced'],
        'Count': np.random.randint(10, 50, 3)
    })
    fig1, ax1 = plt.subplots()
    ax1.pie(diff_data['Count'], labels=diff_data['Difficulty'], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    ax1.axis('equal')
    st.pyplot(fig1)

# =============================
# 🎬 Movie Tab – Random Bar Chart
# =============================
with tab2:
    st.header("🎬 Movie Recommendations (Random Sample)")

    # Show random movies
    st.subheader("🎞️ Sample Movie List")
    sample_movies = pd.DataFrame({
        'Title': [f"Movie {i}" for i in range(1, 6)],
        'Genre': np.random.choice(['Action', 'Drama', 'Comedy', 'Sci-Fi'], 5),
        'Year': np.random.randint(2000, 2024, 5),
        'Rating': np.round(np.random.uniform(2.5, 5.0, 5), 1)
    })

    for _, row in sample_movies.iterrows():
        st.markdown(f"### 🎬 {row['Title']} ({row['Year']})")
        st.markdown(f"**Genre**: {row['Genre']} | ⭐ {row['Rating']}")
        st.markdown("**Plot**: This is a random movie plot summary.")

    # Bar chart
    st.subheader("🎥 Genre Distribution (Random)")
    genres = ['Action', 'Drama', 'Comedy', 'Sci-Fi', 'Thriller']
    genre_counts = np.random.randint(10, 40, len(genres))
    genre_df = pd.DataFrame({'Genre': genres, 'Count': genre_counts})
    fig2, ax2 = plt.subplots()
    sns.barplot(data=genre_df, x='Genre', y='Count', palette='coolwarm', ax=ax2)
    st.pyplot(fig2)

# ==================================
# 🛒 E-Commerce Tab – Random Histogram
# ==================================
with tab3:
    st.header("🛒 E-Commerce Recommendations (Random Sample)")

    # Show random products
    st.subheader("🛍️ Sample Product List")
    sample_products = pd.DataFrame({
        'Product Name': [f"Product {i}" for i in range(1, 6)],
        'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Toys'], 5),
        'Price': np.random.randint(300, 3000, 5),
        'Rating': np.round(np.random.uniform(3.0, 5.0, 5), 1)
    })

    for _, row in sample_products.iterrows():
        st.markdown(f"### 🛒 {row['Product Name']}")
        st.markdown(f"**Category**: {row['Category']} | ⭐ {row['Rating']} | ₹{row['Price']}")
        st.markdown("**Description**: This is a random product description.")

    # Price histogram
    st.subheader("📈 Price Distribution (Random)")
    prices = np.random.normal(loc=1500, scale=500, size=100)
    fig3, ax3 = plt.subplots()
    sns.histplot(prices, bins=20, kde=True, ax=ax3, color="skyblue")
    st.pyplot(fig3)
