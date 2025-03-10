import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="📖  Text Analysis Tool")

# Add custom CSS styling with new colors
st.markdown("""
    <style>
    body, .stApp {
        background-color: #f3e5f5; /* Soft Lavender */
    }
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #b71540; /* Deep Purple */
        color: white;
        text-align: center;
        margin-bottom:40px
        padding: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title section with new colors and emojis
st.markdown("<h1 style='text-align: center; background-color: #ffcccb; color: #2e86de;'>📊 Text Analysis Tool 📖</h1>", unsafe_allow_html=True)

# Function to count vowels in the paragraph
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# User Input for the paragraph
st.markdown("📝 Enter a paragraph for analysis:")
paragraph = st.text_area("", placeholder="✏️ Type your paragraph here...", height=150, key="input_paragraph")

# Search and Replace Input Fields
search_word = st.text_input("🔍 Enter a word to search for:")
replace_word = st.text_input("🔄 Enter a word to replace it with:")

# Analyze Text Button
if st.button("Analyze Text 🔄"):
    # Ensure the input is not empty
    if paragraph:
        # Text Analysis
        
        # 1. Word and Character Count
        words = paragraph.split()
        total_words = len(words)
        total_characters = len(paragraph)
        
        # 2. Vowel Count
        vowel_count = count_vowels(paragraph)
        
        # Perform search and replace if both fields are provided
        if search_word and replace_word:
            modified_paragraph = paragraph.replace(search_word, replace_word)
        else:
            modified_paragraph = paragraph
        
        # 4. Uppercase and Lowercase Conversion
        uppercase_paragraph = paragraph.upper()
        lowercase_paragraph = paragraph.lower()
        
        # 3. Type Casting
        word_count_str = str(total_words)
        vowel_count_str = str(vowel_count)
        
        # 4. Operators
        # Check if "Python" is in the paragraph
        contains_python = "Python" in paragraph
        
        # Calculate average word length
        if total_words != 0:
            avg_word_length = total_characters / total_words
        else:
            avg_word_length = 0
        
        # Show the analysis results with styled headers and emojis
        st.markdown(f"<h3 style='color: #26a69a;'>🔡 Analysis Results</h3>", unsafe_allow_html=True)
        
        st.markdown(f"<h2 style='color: #e74c3c;'>📝 Word and Character Count:</h2>", unsafe_allow_html=True)
        st.write(f"Total Words: {total_words}")
        st.write(f"Total Characters (including spaces): {total_characters}")
        
        st.markdown(f"<h2 style='color: #e91e63;'>🔠 Vowel Count:</h2>", unsafe_allow_html=True)
        st.write(f"Number of Vowels: {vowel_count}")
        
        st.markdown(f"<h2 style='color: #f39c12;'>🔄 Search and Replace:</h2>", unsafe_allow_html=True)
        if search_word and replace_word:
            st.write(f"Original Paragraph: {paragraph}")
            st.write(f"Modified Paragraph: {modified_paragraph}")
        else:
            st.write("No search and replace performed.")
        
        st.markdown(f"<h2 style='color: #2e86de;'>🔠 Uppercase and Lowercase Conversion:</h2>", unsafe_allow_html=True)
        st.write("Paragraph in Uppercase:")
        st.write(uppercase_paragraph)
        
        st.write("Paragraph in Lowercase:")
        st.write(lowercase_paragraph)
        
        st.markdown(f"<h2 style='color: #8e44ad;'>⚡ Additional Checks:</h2>", unsafe_allow_html=True)
        if contains_python:
            st.markdown(f"<h3 style='color: red;'>🐍 The paragraph contains the word '🐍 python'</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: gray;'>❌ The paragraph does not contain the word '🐍 python'</h3>", unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='color: magenta;'>📊 Average word length: {avg_word_length:.2f}</h3>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a paragraph before clicking 'Analyze Text'.")
else:
    st.warning("Please enter a paragraph for analysis.")

# Footer
st.markdown("""
    <footer>
       <p>Built with ❣️ by Kiran 😊 | © 2025 </p>
    </footer>
    """, unsafe_allow_html=True)
