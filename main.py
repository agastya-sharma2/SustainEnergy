import streamlit as st
import pandas as pd
import altair as alt
from streamlit_carousel import carousel

st.set_page_config(layout="wide", page_title="#SustainEnergy", page_icon="🌍")

with st.container():
    st.markdown( #Title Box
        """

        <div style="background:#0e4460;padding:2rem;border-radius:10px;width:83.5%;margin:auto;">
            <h1 style="color:white;text-align:center;">#SustainEnergy</h1>
        </div>
        <br/> 

        """,
        
        unsafe_allow_html=True
    )

    carousel_items = [
        dict(
            title="",
            text="",
            img="https://eridirect.com/wp-content/uploads/2021/02/bigstock-Solar-panel-against-blue-sky-16564781.jpg",
            interval=2000
        ),
        dict(
            title="",
            text="",
            img="https://erepublic.brightspotcdn.com/dims4/default/4821f36/2147483647/strip/true/crop/840x438+0+0/resize/840x438!/quality/90/?url=http%3A%2F%2Ferepublic-brightspot.s3.us-west-2.amazonaws.com%2F35%2Fc1%2F8c4c58184ac689456a0c1397b494%2Fniezrecki-wind-shutterstock.jpg",
            interval=2000
        ),
        dict(
            title="",
            text="",
            img="https://imgproxy.divecdn.com/uhnLGd81D6S6IR64c6tUlTZ8D3zXyufEAvDewllqImQ/g:nowe:12:177/c:996:563/rs:fill:1200:675:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS85OTUyMjU1MjU2XzFlZDNmNzYyMTlfYi5qcGc=.webp",
            interval=2000
        )
    ]

    carousel(items=carousel_items, width=100, indicators=False)
    #Intro
    st.write("Energy is a huge deal in todays world which is why it should be sustainable. The more common ways of obtaining energy, such as fossil fuels, hurt our environment and are not resuable. Solar power on the other hand is sustainable and doesn't damage our ecosystem. Other processes include wind power and hydro power which also are sustainable. Hydro power is so superior, its been used for a very long time and is the most popular.")

    #st.write("This application visualizes energy usage over time using a bar graph. The data represents energy consumption trends.")

    data = {
        "Year": list(range(2006, 2024)),  # Years from 2000 to 2017
        "Energy Usage (TWh)": [
            143482, 147434, 148960, 146669, 153125, 156261, 158186, 160629, 
            162111, 163146, 164719, 168363, 172629, 174458, 168779, 176840, 179819, 183230
        ]
    }

    df = pd.DataFrame(data)

    #General Graph
    st.title("Energy Usage Over Time (2006 to 2023)")
    st.line_chart(
        df.set_index("Year"),
        use_container_width=True,
        height=400,
        width=1000,
        x_label="Year",
        y_label="Energy Usage (TWh)",
        
    )

    #Solar energy graph
    with st.expander("Solar Energy Usage Over Time"):

    # Add the chart inside the expander
        data = {
            "Year": list(range(2006, 2024)),  # Years from 2000 to 2017
            "Energy Usage (TWh)": [
                16, 22, 36, 59, 94, 181, 278, 378,
                534, 689, 879, 1185, 1521, 1860,
                2245, 2752, 3446, 4264
            ]
        }

        df = pd.DataFrame(data)

        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("Year:O", title="Year"),
                y=alt.Y("Energy Usage (TWh):Q", title="Energy Usage (TWh)"),
                tooltip=["Year", "Energy Usage (TWh)"]
            )
            .properties(
                title="Energy Usage Over Time (2006 to 2023)",
                width=700,
                height=400
            )
        )

        # Display the chart in Streamlit
        st.altair_chart(chart)

    #Wind energy graph    
    with st.expander("Wind Energy Usage Over Time"):

        data = {
            "Year": list(range(2006, 2024)),  # Years from 2000 to 2017
            "Energy Usage (TWh)": [
                380, 485, 622, 773, 961, 1216, 1455,
                1732, 1912, 2239, 2576, 3039, 3361, 3747,
                4188, 4866, 5496, 6040
            ]
        }

        df = pd.DataFrame(data)

        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("Year:O", title="Year"),
                y=alt.Y("Energy Usage (TWh):Q", title="Energy Usage (TWh)"),
                tooltip=["Year", "Energy Usage (TWh)"]
            )
            .properties(
                title="Energy Usage Over Time (2006 to 2023)",
                width=700,
                height=400
            )
        )

        # Display the chart in Streamlit
        st.altair_chart(chart)

    #Hydro energy graph
    with st.expander("Hydro Energy Usage Over Time"):

        data = {
            "Year": list(range(2006, 2024)),  # Years from 2000 to 2017
            "Energy Usage (TWh)": [
                8599, 8688, 9137, 9066, 9521, 9635, 9985, 10324,
                10535, 10455, 10750, 10827, 11081, 11185, 11449,
                11222, 11272, 11014
            ]
        }

        df = pd.DataFrame(data)

        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("Year:O", title="Year"),
                y=alt.Y("Energy Usage (TWh):Q", title="Energy Usage (TWh)"),
                tooltip=["Year", "Energy Usage (TWh)"]
            )
            .properties(
                title="Energy Usage Over Time (2006 to 2023)",
                width=700,
                height=400
            )
        )

        # Display the chart in Streamlit
        st.altair_chart(chart)
    
    #Ways to sustain energy
    st.title("How can you sustain energy?")
    st.write("There are many ways to sustain energy at home such as unplugging unused appliances, turning off the lights, and using alternative sources. An example would be to wear a sweater or jacket if you're cold instead of turning on the heater. Using electric cars over gas cars also makes a huge difference.")
    
    
    st.title("Fun Facts!")
    st.html(
    """
    <div style="display: flex; flex-direction: column; align-items: center; padding:10px; margin:10px;">
        <p><span style="border: white 5px solid; border-radius: 12px; padding: 10px; margin: 10px">One wind turbine can power up to 1,500 homes for a year</span></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; padding:10px; margin:10px;">
        <p><span style="border: white 5px solid; border-radius: 12px; padding: 10px; margin: 10px">One Hour of Solar Energy Can Power the Entire Planet For One Year</span></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; padding:10px; margin:10px;">
        <p><span style="border: white 5px solid; border-radius: 12px; padding: 10px; margin: 10px">Solar power is predicted to be the world's top power source by 2050</span></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; padding:10px;">
        <p><span style="border: white 5px solid; border-radius: 12px; padding: 10px;">Hydropower is considered to the world's oldest form of renewable energy</span></p>
    </div>

    """
    )
    # st.html(
    # """
    # <p><span style="border: white 5px solid; border-radius: 12px; padding: 10px;">Testing</span></p>
    # """
    # )


    #Quiz
    if "questions" not in st.session_state:
        st.session_state.questions = [
        {"question": "What are some ways to sustain energy at home?", "options": ["Unplug any unneccesary appliances in your home", "Make sure you turn off the lights", "Use alternative options(instead of a heater, wear a sweater)", "All of the above"],
         "answer": "All of the above"},
        {"question": "What distinguishes renewable energy from traditional fossil fuels in terms of environmental impact?", "options": ["Higher energy output", "Lower operational costs", "Reduced greenhouse gas emissions", "Increased reliance on water resources"],
         "answer": "Reduced greenhouse gas emissions"},
        {"question": "We can improve our energy sustainability by using ______", "options": ["Wind Energy", "Fossil Fuels", "Natural Gasses"], "answer": "Wind Energy"},
        {"question": "What is the most common type of renewable energy?", "options": ["Solar Energy", "Wind Energy", "Hydro Energy", "Geothermal Energy"], "answer": "Hydro Energy"},
        {"question": "Which of the following is NOT a benefit of renewable energy?", "options": ["Reduces greenhouse gas emissions", "Decreases air pollution", "Creates jobs", "Increases reliance on fossil fuels"], 
         "answer": "Increases reliance on fossil fuels"},
        {"question": "What is the main source of energy for wind turbines?", "options": ["Solar energy", "Wind energy", "Geothermal energy", "Hydropower"], 
         "answer": "Wind energy"},
        {"question": "Which country is the largest producer of solar energy?", "options": ["Germany", "China", "United States", "India"], 
         "answer": "China"},
        
    ]

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "feedback" not in st.session_state:
        st.session_state.feedback = None

    @st.fragment
    def question_fragment():
        """
            Fragment to display a question and capture the user's response.
        """
        question_data = st.session_state.questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}/{len(st.session_state.questions)}")
        st.write(question_data['question'])

        selected_option = st.radio('Choose an answer: ', question_data['options'])
        if st.button('Check'):
            if selected_option == question_data['answer']:
                st.session_state.feedback = ('success', 'Correct! 🎉')
                st.session_state.score += 1
            else:
                st.session_state.feedback = ("error", f"Wrong! The correct answer was: {question_data['answer']}")

            if st.session_state.current_question + 1 < len(st.session_state.questions):
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.current_question = None
                st.rerun()

    @st.fragment
    def feedback_fragment():
        """
        Fragment to display feedback messages.
        """
        if st.session_state.feedback:
            msg_type, msg_content = st.session_state.feedback
            if msg_type == "success":
                st.success(msg_content)
            elif msg_type == "error":
                st.error(msg_content)
            st.session_state.feedback = None

    @st.fragment
    def score_fragment():
        """
            Fragment to display the user's current score.
        """
        st.metric('Current Score', st.session_state.score)

    @st.fragment
    def restart_quiz_fragment():
        """
            Fragment to restart the quiz.
        """
        if st.button('Restart Quiz'):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.feedback = None
            st.rerun()

    st.title('Quiz yourself!')

    feedback_fragment()

    if st.session_state.current_question is not None:
        score_fragment()
        question_fragment()
    else:
        st.subheader('Quiz Finished! 🎉')
        st.write(f"Your final score is {st.session_state.score}/{len(st.session_state.questions)}.")
        restart_quiz_fragment()