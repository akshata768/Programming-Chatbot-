import streamlit as st

# SIDEBAR

with st.sidebar:

    st.title("🎓 Programming Tutor")

    if st.button("📘 Pipeline", use_container_width=True):
        st.session_state.selected_page = "Pipeline"

    if st.button("👥 Info", use_container_width=True):
        st.session_state.selected_page = "Info"

    st.divider()

    if st.session_state.selected_page == "Pipeline":

        st.subheader("📘 About Our Project")

        st.write(
            "Programming Tutor Chatbot is an AI-based "
            "learning application for C, Java, and Python."
        )

        st.subheader("🎯 Project Purpose")

        st.write(
            "To help students learn programming easily."
        )

        st.subheader("⚙️ How It Works")

        st.write("1. Select a programming language.")
        st.write("2. Upload your code.")
        st.write("3. Ask a question.")
        st.write("4. Click Ask AI.")
        st.write("5. Get an answer.")

    elif st.session_state.selected_page == "Info":

        st.subheader("👥 Team Members")

        st.write("1. Akshata")
        st.write("2. Team Member 2")
        st.write("3. Team Member 3")

st.title("💻 Programming Chatbot")
st.write("Learn C, Python, and Java in one place!")

language = st.selectbox(
    "Choose a programming language",
    ["C", "Python", "Java"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your programming question...")

def get_answer(language, question):
    q = question.lower()

    if language == "C":
        if "loop" in q:
            return "C has 3 loops: for, while, and do-while."
        elif "array" in q:
            return "An array stores multiple values of the same data type."
        elif "pointer" in q:
            return "A pointer stores the memory address of a variable."
        elif "function" in q:
            return "A function is a block of code used to perform a specific task."
        elif "hello" in q:
            return 'C code: printf("Hello World");'
        else:
            return "C is a procedural programming language. Ask me about loops, arrays, pointers, functions, or programs."

    elif language == "Python":
        if "loop" in q:
            return "Python has for loops and while loops."
        elif "list" in q:
            return "A list stores multiple values. Example: numbers = [10, 20, 30]"
        elif "function" in q:
            return "Python functions are created using the def keyword."
        elif "hello" in q:
            return 'Python code: print("Hello World")'
        else:
            return "Python is a simple and beginner-friendly language. Ask me about loops, lists, functions, or programs."

    elif language == "Java":
        if "loop" in q:
            return "Java has for loops, while loops, and do-while loops."
        elif "class" in q:
            return "A class is a blueprint used to create objects."
        elif "object" in q:
            return "An object is an instance of a class."
        elif "function" in q or "method" in q:
            return "A method is a block of code that performs a task in Java."
        elif "hello" in q:
            return 'Java code: System.out.println("Hello World");'
        else:
            return "Java is an object-oriented programming language. Ask me about classes, objects, loops, methods, or programs."

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = get_answer(language, question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()
