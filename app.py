import streamlit as st

# Function to generate Meta Title
def generate_meta_title(keyword):
    cta = " - Buy Now"
    title = f"{keyword} {cta}"
    
    # Ensure the title does not exceed 70 characters
    if len(title) > 70:
        title = title[:67] + "..."  # Truncate if needed
    
    return title

# Function to generate Meta Description
def generate_meta_description(keyword):
    description = f"Discover the best products and services related to {keyword}. Explore our offerings and get started today!"
    
    # Ensure the description does not exceed 160 characters
    if len(description) > 160:
        description = description[:157] + "..."  # Truncate if needed
    
    return description

# Streamlit app
def app():
    st.title("Meta Title & Meta Description Generator")

    # User input for the keyword
    keyword = st.text_input("Enter a Keyword:", "")

    if keyword:
        # Generate the Meta Title and Meta Description
        meta_title = generate_meta_title(keyword)
        meta_description = generate_meta_description(keyword)
        
        # Display the results
        st.subheader("Generated Meta Title:")
        st.write(meta_title)
        
        st.subheader("Generated Meta Description:")
        st.write(meta_description)

if __name__ == "__main__":
    app()
