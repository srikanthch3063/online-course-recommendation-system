import streamlit as st
import pandas as pd
import numpy as np

# Set up page
st.set_page_config(page_title="Course Recommendation System", layout="wide")
st.title("🎓 Online Course Recommendation System")

st.write("Welcome to the Online Course Recommendation System! Select your preferences below to get tailored course suggestions.")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_excel('online_course_recommendation.xlsx')
        return df
    except Exception as e:
        # Generate dummy data
        data = {
            'course_name': ['Python for Beginners', 'Advanced Machine Learning', 'Data Science with R', 'Introduction to SQL', 'Web Development Bootcamp'],
            'difficulty_level': ['Beginner', 'Advanced', 'Intermediate', 'Beginner', 'Beginner'],
            'rating': [4.8, 4.9, 4.5, 4.6, 4.7],
            'enrollment_count': [15000, 5000, 8000, 12000, 20000],
            'course_category': ['Programming', 'AI', 'Data Science', 'Databases', 'Web Dev']
        }
        df = pd.DataFrame(data)
        st.info("Using sample dataset.")
        return df

df = load_data()

if not df.empty:
    st.sidebar.header("User Preferences")
    
    # Filter by Difficulty
    difficulties = df['difficulty_level'].unique().tolist() if 'difficulty_level' in df.columns else ['Beginner', 'Intermediate', 'Advanced']
    selected_difficulty = st.sidebar.selectbox("Select Difficulty Level", difficulties)
    
    # Filter by Minimum Rating
    min_rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 4.0, 0.1)
    
    if st.sidebar.button("Get Recommendations"):
        st.subheader(f"Top Recommended Courses (Difficulty: {selected_difficulty})")
        
        # Simple rule-based recommendation for the UI
        if 'difficulty_level' in df.columns and 'rating' in df.columns:
            recommendations = df[(df['difficulty_level'] == selected_difficulty) & (df['rating'] >= min_rating)]
            recommendations = recommendations.sort_values(by=['rating', 'enrollment_count'], ascending=[False, False])
            
            if not recommendations.empty:
                st.dataframe(recommendations[['course_name', 'difficulty_level', 'rating', 'enrollment_count', 'course_category']].head(10))
            else:
                st.write("No courses found matching your criteria.")
        else:
            # Fallback if columns don't match exactly
            st.dataframe(df.head(10))
            
    st.write("---")
    st.subheader("Explore the Dataset")
    if st.checkbox("Show raw data"):
        st.dataframe(df.head(50))
