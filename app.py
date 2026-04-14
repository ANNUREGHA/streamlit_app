import streamlit as st
st.title("WELCOME TO ANNU'S COMPATIBILITY APP!!")
st.subheader("CLICK YOUR OPTIONS AMONG THE FOLLOWING QUESTIONS ABOUT ANNU TO CHECK IF YOU LIKE HER 😏")
name=st.text_input("Enter your name mister/miss :")
button1=st.button("CLICK ME TO PROCEED")
if "start" not in st.session_state:
    st.session_state.start=0
if "result" not in st.session_state:
    st.session_state.result=0
if "count" not in st.session_state:
    st.session_state.count=0
if "name" not in st.session_state:
    st.session_state.name=name
if "checkbox2" not in st.session_state:
    st.session_state.checkbox2=False

if button1:
    st.session_state.start=1

        
if st.session_state.start==1:
    c1=st.checkbox("Is she funny?")
    c2=st.checkbox("Do you think she's beautiful?",key="checkbox2")
    c3=st.checkbox("Do you think she has potentials of being a good girlfriend?")
    c4=st.checkbox("Will you allow her to draw on your wrists if she feels creative and too lazy to go find a paper ")
    c5=st.checkbox("Are you are non-vegetarian . PS: same as her who drools over chicken ?")
    c6=st.checkbox("Do you officially recognize her as a terrifying don? 😎")
    c7=st.checkbox("Are you scared of her ?")
    c8=st.checkbox("Are you willing to patiently bear with her mishaps and memory-loss behaviour")
    c9=st.checkbox("Do you like gossips ?")
    c10=st.checkbox("Are you willing to hear her out when she's super , unreasonably , idiotically stressed ?")  
    if c10:
        stress_ans_1=st.radio("Sure ?",["HELLO NO!","YES"])
        if stress_ans_1=="YES":
            stress_ans_2=st.radio("Pakka ?",["DAMN SURE","NOPE!"])
            if stress_ans_2=="DAMN SURE":
                st.write("Let Jesus save you ✝️")
            if stress_ans_2=="NOPE!":
                st.write("Ouch it hurts...but good for you 🥺")
        if stress_ans_1=="HELL NO!":
            st.write("Ouch it hurts...but good for you 🥺")
    st.session_state.count=sum([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])  
    if st.button("SUBMIT"):
        st.session_state.start=0
        st.session_state.result=1
        st.rerun()


if st.session_state.result==1:
    if not st.session_state.checkbox2 :
        st.warning("Youve entered the wrong choice for question number 2 . she's anyways a beauty ... just a different kind from your standards.Kindly choose the correct option 😤")
        if st.button("GO BACK"):
            st.session_state.result=0
            st.rerun()
    else:
        st.subheader("RESULTS :")
        st.write("I know you're nervous . chill out.... She'll like you !!😎❤️")
        st.success(f"you are {st.session_state.count*10} % compatible with annu  🫣")
        st.write(f"Kindly take a screenshot of it and send it to her for proof!!{name}")
        if st.button("GO BACK"):
            st.session_state.result=0
            st.rerun()
    
        