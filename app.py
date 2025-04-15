import streamlit as st

# Function to analyze the intent of the keyword
def analyze_intent(keyword):
    # Keywords to check for transactional, informational, or navigational intent
    transactional_keywords = ["buy", "purchase", "order", "shop", "deal", "sale", "discount"]
    informational_keywords = ["how to", "tutorial", "guide", "learn", "benefits", "review", "best"]
    navigational_keywords = ["login", "website", "official site", "support", "contact", "home"]

    # Check for transactional intent
    if any(word in keyword.lower() for word in transactional_keywords):
        return "transactional"
    
    # Check for informational intent
    elif any(word in keyword.lower() for word in informational_keywords):
        return "informational"
    
    # Check for navigational intent
    elif any(word in keyword.lower() for word in navigational_keywords):
        return "navigational"
    
    # Default to informational if no match is found
    return "informational"

# Function to generate Meta Title based on intent
def generate_meta_title(keyword, intent):
    if intent == "transactional":
        return f"Buy {keyword} - Best Deals Available Now"
    elif intent == "informational":
        return f"Learn How to {keyword} - Step-by-Step Guide"
    elif intent == "navigational":
        return f"Visit the Official {keyword} Website"
    else:
        return f"Explore {keyword} - Find Out More"

# Function to generate Meta Description based on intent
def generate_meta_description(keyword, intent):
    if intent == "transactional":
        return f"Shop for {keyword} online. Find the best deals and offers, and enjoy easy purchasing options."
    elif intent == "informational":
        return f"Get detailed insights into {keyword}. Read our comprehensive guide to learn everything you need to know."
    elif intent == "navigational":
        return f"Access the official {keyword} website. Find everything you need, from support to login information."
    else:
        return f"Discover everything about {keyword}. Explore our in-depth resources and expert advice."

# Streamlit app
def app():
    st.title("Meta Title & Meta Description Generator Based on Keyword Intent")

    # User input for the keyword
    keyword = st.text_input("Enter a Keyword:", "")

    if keyword:
        # Analyze the intent of the keyword
        intent = analyze_intent(keyword)
        
        # Generate the Meta Title and Meta Description based on the intent
        meta_title = generate_meta_title(keyword, intent)
        meta_description = generate_meta_description(keyword, intent)
        
        # Display the results
        st.subheader("Generated Meta Title:")
        st.write(meta_title)
        
        st.subheader("Generated Meta Description:")
        st.write(meta_description)

if __name__ == "__main__":
    app()
