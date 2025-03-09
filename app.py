#  impor streamlit module
import streamlit as st

# here i gage page title
st.set_page_config(page_title="📖  Text Analysis Tool")
st.markdown("""
    <style>
    body,.stApp {
        background-color: #ffeaa7;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 style = 'text-align: center; backgroung-color:#ffcccb;'>📖 Text Analysis Tool </h1>" ,unsafe_allow_html=True)


# here i get input from user

user_paragraph= st.text_area("✏️  Enter a paragraph for analysis.")


# input validation

if user_paragraph:
    # count word and character
    # first split paragraph into word
    words = user_paragraph.split()
    # count world length
    words_count_length = len(words)
    #  count character length
    char_length_count = len(user_paragraph)
    
    
    st.markdown(f"<h3 style = 'color : green;'> 📝 Total number of words: {words_count_length}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style = 'color : blue;'> 🔡 Total number of characters (include space): {char_length_count}</h3>", unsafe_allow_html=True)
    
    #  count vowel
    vowels ="aeiouAEIOU"
    
    vowel_count = sum(1 for char in user_paragraph if char in vowels)
    st.markdown(f"<h3 style = 'color : purple;'> 🔡 Total number vowels : {vowel_count}</h3>", unsafe_allow_html=True)
    
    # now here i search and replace it with new word
    
    search_word = st.text_input("🔍 Enter a word to search\n")
    replace_word = st.text_input("🔄 Enter a word to replace it with\n")
    
    if search_word and replace_word:
        modified_paragraph = user_paragraph.replace(search_word, replace_word)
        st.markdown(f"<h3 style = 'color : orange;'> 🔡 Modified Paragraph</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style = 'backgroung-color:#ffe4b5; padding : 10px;'>{modified_paragraph} </p>", unsafe_allow_html=True)
        
    #   conversion of paragraph in UPPERCASE and lowercase
    
        st.markdown(f"<h3 style = 'color : darkblue;'> 🔡 Paragraph In Uppercase</h3>", unsafe_allow_html=True) 
        st.markdown(f"<p style = 'backgroung-color:#ffe4b5; padding : 10px;'>{modified_paragraph.upper()} </p>", unsafe_allow_html=True)
       
        st.markdown(f"<h3 style = 'color : darkgreen;'> 🔡 Paragraph In Lowercase</h3>", unsafe_allow_html=True) 
        st.markdown(f"<p style = 'backgroung-color:#fafad2; padding : 10px;'>{modified_paragraph.lower()} </p>", unsafe_allow_html=True)
       
        word_count_str = str(words_count_length)
        vowel_count_str = str(vowel_count)
        
        st.markdown(f"<h3 style = 'color : brown;'> Word count as a string: {word_count_str} ✅</h3>", unsafe_allow_html=True) 
        st.markdown(f"<h3 style = 'color : brown;'> vowel count as a string: {word_count_str} ✅</h3>", unsafe_allow_html=True) 
        
        #  now chek if python have in paragraph
        
        contain_python = 'python' in user_paragraph
        if contain_python:
           st.markdown(f"<h3 style = 'color : red;'>🐍 The paragraph contains the word '🐍 python'</h3>", unsafe_allow_html=True) 
        else:
            st.markdown(f"<h3 style = 'color : gray;'>❌  The paragraph contains the word '🐍 python'</h3>", unsafe_allow_html=True) 
      
        #  now average
        if words_count_length !=0:
            avg_word_length = char_length_count / words_count_length
            st.markdown(f"<h3 style = 'color : magenta;'>📊 Average word length.: {avg_word_length}</h3>", unsafe_allow_html=True) 
            
    else:
        st.warning(f"<h3 style = 'color : red;'>⚠️ Please enter a paragraph to analyze</h3>", unsafe_allow_html=True) 
      
        
      
st.markdown("""
            
            <footer>
               <p>built with ❣️by Kiran😊 | © 2025 </p>
            </footer/>
            
                  """, unsafe_allow_html=True)      
      