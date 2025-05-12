import streamlit as st
from chatbot import send_prompt, establish_api

# Establish sessions state variable to save conversation history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

message_history = st.session_state['message_history']

st.header("Caregiver", divider="rainbow")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Tell me how you're feeling", "Tell a Joke", "Excercises and Meditation", "Generate a song"]
)

with tab1:
    st.subheader("Tell me how you're feeling")

    # Story premise
    feeling = st.text_input(
        "How are you feeling right now?: \n\n", key="feeling"
    )
    situation = st.text_input(
        "Can you tell me more about what's going on?: \n\n", key="situation"
    )
    askmood = st.select_slider(
        "How are you feeling right now on a scale of 1 to 10? \n\n", options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], key="askmood"
    )

    
    prompt = f"""The user has come to you to make them feel better. Here is a description of how they're doing. Recommend further actions for them. If you think they should listen to music, meditate, excercise, or hear a joke, direct them to that tab. \n
    
    
    current mood={feeling}\n
    current situtation={situation}\n
    current mood on a scale of 1 to 10={askmood}\n
    """
    generate_t2t = st.button("Generate recommendation", key="generaterecommendation")
    if generate_t2t and prompt:
        # st.write(prompt)
        with st.spinner(
                 f"Generating your recommendation using AI..."
        ):
            first_tab1, first_tab2 = st.tabs(["Recommendation", "Prompt"])
            with first_tab1:
                response = send_prompt(
                    prompt)

                if response:
                    st.write("Your recommendation:")
                    st.write(response)
            with first_tab2:

                st.text(prompt)
with tab2:
    st.subheader("Tell A Joke")
    # Story premise
    typeofjoke = st.text_input(
        "What type of joke would you like to hear?: \n\n", key="typeofjoke")
       
    typeofproblem = st.text_input(
        "What type of problem are you dealing with?: \n\n", key="typeofproblem")
    
    
    prompt = f"""Tell me a joke that best fits these requirements: \n
    type of joke: {typeofjoke} \n
    topic: {typeofproblem} \n 
    """
    generate_t2t = st.button("Tell me a joke", key="tellajoke")
    if generate_t2t and prompt:
        second_tab1, second_tab2 = st.tabs(["Joke", "Prompt"])
        with st.spinner(
                f"Generating your joke using AI ..."
        ):
            with second_tab1:
                response = send_prompt(
                    prompt)
                if response:
                    st.write("Your joke:")
                    st.write(response)
            with second_tab2:
                st.text(prompt)

with tab3:
    st.subheader("Exercise or Meditation")
    # Story premise

    askformood = st.text_input(
        "Enter your mood for recommendation of an excercise or meditation: \n\n", key="askformood"
    )

    areaoftension = st.text_input(
        "Take a second to feel into your body. Does any area feel ache or tense?: \n\n", key="areaoftension")
       
    exerciseormeditation = st.radio(
        "Would you like to do an exercise or meditation?: \n\n",
        ["exercise", "meditation"],
        key="exerciseormeditation",
        horizontal=True,
    )
    
    
    prompt = f"""Tell me an exercise of meditation that best fits these requirements: \n
    current mood: {askformood} \n
    area of tension: {areaoftension} \n
    exercise or meditation: {exerciseormeditation} \n
    """
    generate_t2t = st.button("Generate an exercise or meditation", key="Generateanexerciseormeditation")
    if generate_t2t and prompt:
        third_tab1, third_tab2 = st.tabs(["Excercise or meditation", "Prompt"])
        with st.spinner(
                f"Generating your excercise or meditation using AI ..."
        ):
            with third_tab1:
                response = send_prompt(
                    prompt)
                if response:
                    st.write("Excercise or meditation:")
                    st.write(response)
            with third_tab2:
                st.text(prompt)



with tab4:
    st.subheader("Generate a song")

    # Story premise
    mood = st.text_input(
        "Enter your mood: \n\n", key="mood"
    )

    activity = st.multiselect(
        "What will you be doing while you listen to music? (can select multiple) \n\n",
        [
            "working",
            "relaxing",
            "working out",
            "creative activity",
            "hang out with friends",
            "party",
            "traveling",
            "other",
        ],
        key="activity",

    )

    song_genre = st.multiselect(
        "Select a song genre: \n\n",
        ["pop", "rock", "R&B", "hip-hop", "classical", "jazz", "electronic"],
        key="song_genre",

    )

    lyrics_instrumental = st.radio(
        "Select if your song will be mostly lyrics or instrumentals: \n\n",
        ["lyrics", "instrumental", "no preference"],
        key="lyrics_instrumental",
        horizontal=True,
    )

    era = st.radio(
        "Select your favorite era of music: \n\n",
        ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"],
        key="era",
        horizontal=True,
    )
    prompt = f"""Respond with a popular song ( a song that was once on the billboard top 100) that best fits the description below: \n
    mood: {mood} \n
    song genre: {song_genre} \n
    lyrics or instrumental: {lyrics_instrumental} \n
    Activity performed while listening to music: {activity} \n
    Era of music: {era} \n
    
    List the song on a line of it's own in quotation marks followed by the artists name all in bold. 
    Write a short description on how you chose that song. Do not include the song request in your response.
    """
    generate_t2t = st.button("Select my song", key="generate_t2t")
    if generate_t2t and prompt:
        # st.write(prompt)
        with st.spinner(
                 f"Generating your song using AI..."
        ):
            fourth_tab1, fourth_tab2 = st.tabs(["Song", "Prompt"])
            with fourth_tab1:
                response = send_prompt(
                    prompt)

                if response:
                    st.write("Your song:")
                    st.write(response)
            with fourth_tab2:

                st.text(prompt)
# Insert API key to get started
with st.sidebar:
    if "api_key" not in st.session_state:
        st.title("Insert API Key!")
        api_key = AIzaSyDEizhfTK3wGnmGoWXqpQ89vKwQqGwfD_g
        if api_key:
            st.session_state["api_key"] = api_key
            st.write(establish_api(api_key))
        st.write("**To get started, you'll need a Gemini API key:**")

        instructions = """
        1. **Go to Google AI Studio:** Login and access the platform.
        2. **Click "Get API Key":** Locate the option to obtain an API key.
        3. **Choose Project:** Select a new or existing project for the API key.
        4. **Copy the Key:** Once generated, copy the API key here and have fun!
        """

        st.markdown(instructions)
    else:
        st.write("API Key already entered. Enjoy :D")
