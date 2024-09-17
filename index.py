import streamlit as st
import spacy_streamlit as spt
import spacy


nlp = spacy.load('en_core_web_sm')

def main():
   
    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            color: #00aaff; /* Light blue color for the title */
        }
        .stApp {
            background-color: #e0f7fa; /* Light blue background for the entire app */
            color: #000000; /* Black text color for the app */
        }
        .sidebar .sidebar-content {
            background-color: #003366; /* Dark blue background for sidebar */
            color: #ffffff; /* White text color for sidebar */
        }
        .sidebar .sidebar-content .stSelectbox, .sidebar .sidebar-content .stButton {
            background-color: #003366; /* Dark blue background for select box and buttons in sidebar */
            color: #ffffff; /* White text color for select box and buttons in sidebar */
        }
        .stTextInput, .stTextArea, .stButton {
            background-color: #ffffff; /* White background for form elements */
            color: #000000; /* Black text color for form elements */
        }
        .stTextInput textarea, .stTextArea textarea {
            background-color: #ffffff; /* White background for text areas */
            color: #000000; /* Black text color for text areas */
        }
        .stMarkdown, .stText {
            color: #000000; /* Black text color for other text elements */
        }
        </style>
        """, unsafe_allow_html=True)
    
   
    st.title('Named Entity Recognition App')
    st.markdown('<p class="big-font">Analyze and visualize text with NER and Tokenization!</p>', unsafe_allow_html=True)


    st.sidebar.title('Navigation')
    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox('Select Menu', menu)
    
    if choice == 'Home':
        st.subheader('Word Tokenization')
        
       
        raw_text = st.text_area('Enter Text for Tokenization:', 'Type your text here...')
        
        if st.button('Tokenize'):
        
            docs = nlp(raw_text)
            st.write("Here are the tokens in your text:")
            spt.visualize_tokens(docs)
    
    elif choice == 'NER':
        st.subheader('Named Entity Recognition')
        
       
        raw_text = st.text_area('Enter Text for NER:', 'Type your text here...')
        
        if st.button('Analyze'):
           
            docs = nlp(raw_text)
            st.write("Here are the named entities in your text:")
            spt.visualize_ner(docs)


if __name__ == '__main__':
    main()
