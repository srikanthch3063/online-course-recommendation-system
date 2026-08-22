import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AI Online Course Recommendation System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .course-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
        transition: transform 0.2s;
    }
    .course-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
    }
    .badge-beginner { background-color: #DEF7EC; color: #03543F; }
    .badge-intermediate { background-color: #E1EFFE; color: #1E429F; }
    .badge-advanced { background-color: #FDE8E8; color: #9B1C1C; }
    .badge-cat { background-color: #F3F4F6; color: #374151; }
</style>
""", unsafe_allow_html=True)

# Generate comprehensive course dataset
@st.cache_data
def get_course_data():
    courses = [
        {"course_id": 101, "course_name": "Complete Python Bootcamp: From Zero to Hero", "category": "Programming", "difficulty_level": "Beginner", "rating": 4.9, "enrollment_count": 84500, "duration_hrs": 24, "instructor": "Jose Portilla"},
        {"course_id": 102, "course_name": "Machine Learning A-Z: AI, Python & R", "category": "Data Science & AI", "difficulty_level": "Intermediate", "rating": 4.8, "enrollment_count": 69200, "duration_hrs": 42, "instructor": "Kirill Eremenko"},
        {"course_id": 103, "course_name": "Deep Learning Specialization with PyTorch & TensorFlow", "category": "Data Science & AI", "difficulty_level": "Advanced", "rating": 4.9, "enrollment_count": 42000, "duration_hrs": 55, "instructor": "Andrew Ng"},
        {"course_id": 104, "course_name": "Full Stack Web Development with React & Node.js", "category": "Web Development", "difficulty_level": "Intermediate", "rating": 4.7, "enrollment_count": 53100, "duration_hrs": 38, "instructor": "Colt Steele"},
        {"course_id": 105, "course_name": "AWS Certified Solutions Architect Associate 2026", "category": "Cloud & DevOps", "difficulty_level": "Intermediate", "rating": 4.9, "enrollment_count": 61400, "duration_hrs": 28, "instructor": "Stephane Maarek"},
        {"course_id": 106, "course_name": "Docker & Kubernetes: The Practical Guide", "category": "Cloud & DevOps", "difficulty_level": "Advanced", "rating": 4.8, "enrollment_count": 39800, "duration_hrs": 23, "instructor": "Maximilian Schwarzmüller"},
        {"course_id": 107, "course_name": "SQL & Relational Databases for Beginners", "category": "Databases", "difficulty_level": "Beginner", "rating": 4.6, "enrollment_count": 48200, "duration_hrs": 12, "instructor": "Ben Brumm"},
        {"course_id": 108, "course_name": "Cybersecurity Fundamentals: Defense & Ethical Hacking", "category": "Cybersecurity", "difficulty_level": "Beginner", "rating": 4.7, "enrollment_count": 31500, "duration_hrs": 18, "instructor": "Nathan House"},
        {"course_id": 109, "course_name": "Advanced Data Structures & Algorithms in Java", "category": "Programming", "difficulty_level": "Advanced", "rating": 4.9, "enrollment_count": 27400, "duration_hrs": 32, "instructor": "Abdul Bari"},
        {"course_id": 110, "course_name": "UI/UX Design Masterclass: Figma to Product", "category": "Design", "difficulty_level": "Beginner", "rating": 4.8, "enrollment_count": 35600, "duration_hrs": 16, "instructor": "Daniel Walter Scott"},
        {"course_id": 111, "course_name": "Natural Language Processing with Transformers & LLMs", "category": "Data Science & AI", "difficulty_level": "Advanced", "rating": 4.9, "enrollment_count": 29800, "duration_hrs": 30, "instructor": "Hugging Face Team"},
        {"course_id": 112, "course_name": "Data Visualization & Business Intelligence with Tableau", "category": "Data Science & AI", "difficulty_level": "Beginner", "rating": 4.6, "enrollment_count": 24900, "duration_hrs": 14, "instructor": "Pavel N."},
        {"course_id": 113, "course_name": "Modern JavaScript from the Beginning", "category": "Web Development", "difficulty_level": "Beginner", "rating": 4.8, "enrollment_count": 51200, "duration_hrs": 21, "instructor": "Brad Traversy"},
        {"course_id": 114, "course_name": "Kubernetes Administration (CKA) Certification Guide", "category": "Cloud & DevOps", "difficulty_level": "Advanced", "rating": 4.9, "enrollment_count": 18900, "duration_hrs": 26, "instructor": "Mumshad Mannambeth"},
        {"course_id": 115, "course_name": "Flutter & Dart: Complete Cross-Platform Mobile App Dev", "category": "Mobile Development", "difficulty_level": "Intermediate", "rating": 4.7, "enrollment_count": 34200, "duration_hrs": 35, "instructor": "Angela Yu"}
    ]
    return pd.DataFrame(courses)

df = get_course_data()

# Header Section
st.markdown("<h1 class='main-title'>🎓 AI-Powered Online Course Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Discover tailored courses driven by intelligent collaborative & content-based filtering algorithms.</p>", unsafe_allow_html=True)

# Overview Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("📚 Total Courses Catalog", f"{len(df)}+")
col2.metric("👥 Active Learners", f"{df['enrollment_count'].sum():,}")
col3.metric("⭐ Average Rating", f"{df['rating'].mean():.2f} / 5.0")
col4.metric("🏆 Top Domain", df['category'].value_counts().index[0])

st.markdown("---")

# Sidebar Controls
st.sidebar.header("🎯 Recommendation Engine Settings")

rec_mode = st.sidebar.radio(
    "Select Recommendation Strategy",
    ["Intelligent Filtering (Rule & Content)", "User Profile Matching", "Explore All Courses"]
)

if rec_mode == "Intelligent Filtering (Rule & Content)":
    st.sidebar.subheader("Filter Criteria")
    categories = ["All Categories"] + sorted(df['category'].unique().tolist())
    selected_cat = st.sidebar.selectbox("Course Category", categories)
    
    difficulties = ["All Levels"] + df['difficulty_level'].unique().tolist()
    selected_diff = st.sidebar.selectbox("Difficulty Level", difficulties)
    
    min_rating = st.sidebar.slider("Minimum Rating Threshold", 4.0, 5.0, 4.6, 0.1)
    
    sort_by = st.sidebar.selectbox("Sort Results By", ["Highest Rating", "Most Popular (Enrollments)", "Duration (Short to Long)"])
    
    # Filter logic
    filtered_df = df.copy()
    if selected_cat != "All Categories":
        filtered_df = filtered_df[filtered_df['category'] == selected_cat]
    if selected_diff != "All Levels":
        filtered_df = filtered_df[filtered_df['difficulty_level'] == selected_diff]
    filtered_df = filtered_df[filtered_df['rating'] >= min_rating]
    
    if sort_by == "Highest Rating":
        filtered_df = filtered_df.sort_values(by="rating", ascending=False)
    elif sort_by == "Most Popular (Enrollments)":
        filtered_df = filtered_df.sort_values(by="enrollment_count", ascending=False)
    else:
        filtered_df = filtered_df.sort_values(by="duration_hrs", ascending=True)
        
    st.subheader(f"✨ Recommended Courses ({len(filtered_df)} matches)")
    
    if filtered_df.empty:
        st.warning("No courses match the exact filters. Try relaxing the rating threshold.")
    else:
        for _, row in filtered_df.iterrows():
            badge_class = f"badge-{row['difficulty_level'].lower()}"
            st.markdown(f"""
            <div class='course-card'>
                <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
                    <div>
                        <h3 style='margin: 0 0 8px 0; color: #111827;'>{row['course_name']}</h3>
                        <p style='margin: 0 0 10px 0; color: #6B7280; font-size: 0.9rem;'>Instructor: <strong>{row['instructor']}</strong></p>
                        <span class='badge {badge_class}'>{row['difficulty_level']}</span>
                        <span class='badge badge-cat'>{row['category']}</span>
                        <span class='badge badge-cat'>⏱️ {row['duration_hrs']} hours</span>
                    </div>
                    <div style='text-align: right;'>
                        <div style='font-size: 1.3rem; font-weight: 700; color: #D97706;'>★ {row['rating']}</div>
                        <div style='font-size: 0.85rem; color: #6B7280;'>{row['enrollment_count']:,} students</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif rec_mode == "User Profile Matching":
    st.subheader("👤 Student Profile Recommender")
    st.write("Input student background and target goals to predict top matching learning paths:")
    
    pcol1, pcol2 = st.columns(2)
    with pcol1:
        target_role = st.selectbox("Target Career Path", ["AI / Machine Learning Engineer", "Full-Stack Web Developer", "Cloud Solutions Architect", "Data Analyst"])
        current_exp = st.select_slider("Current Experience Level", options=["Beginner (No coding)", "Intermediate (Some projects)", "Advanced (Professional)"])
    with pcol2:
        hours_per_week = st.slider("Weekly Learning Time Commitment (Hours)", 5, 40, 15)
        preferred_learning = st.radio("Learning Preference", ["Hands-on Projects", "Certification Prep", "Comprehensive Masterclass"])
        
    if st.button("🚀 Generate Personalized Learning Roadmap"):
        st.success(f"Generated AI Roadmap for target role: **{target_role}**")
        
        category_map = {
            "AI / Machine Learning Engineer": "Data Science & AI",
            "Full-Stack Web Developer": "Web Development",
            "Cloud Solutions Architect": "Cloud & DevOps",
            "Data Analyst": "Data Science & AI"
        }
        
        target_cat = category_map.get(target_role, "Data Science & AI")
        matches = df[df['category'] == target_cat].sort_values(by="rating", ascending=False)
        
        st.write("### Recommended Step-by-Step Curriculum:")
        step = 1
        for _, row in matches.iterrows():
            st.markdown(f"**Step {step}: {row['course_name']}** — *{row['difficulty_level']}* ({row['duration_hrs']} hrs, ⭐ {row['rating']})")
            st.progress(min(1.0, step * 0.33))
            step += 1

else:
    st.subheader("📊 Interactive Catalog & Dataset Explorer")
    st.dataframe(df, use_container_width=True)
    
    st.write("### Category Distribution")
    cat_counts = df['category'].value_counts()
    st.bar_chart(cat_counts)
