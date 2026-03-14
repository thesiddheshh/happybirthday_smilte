import streamlit as st
import html

# -------------------------------
# 🔑 PIN SETUP
# -------------------------------
CORRECT_PIN = "5704"

# Initialize auth state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Hide Streamlit UI after auth
if st.session_state.authenticated:
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# -------------------------------
# 🔒 PIN GATE
# -------------------------------
if not st.session_state.authenticated:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;500&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #fbeaf2 0%, #e5f6ff 100%);
            font-family: 'Poppins', sans-serif;
        }

        .pin-container {
            max-width: 450px;
            margin: 30vh auto;
            text-align: center;
            padding: 2rem;
        }

        .pin-title {
            font-family: 'Dancing Script', cursive;
            font-size: 3.4rem;
            color: #7a5f8c;
            margin-bottom: 1rem;
        }

        .pin-instruction {
            font-size: 1.15rem;
            color: #5a5a72;
            margin-bottom: 1.5rem;
        }

        .stButton>button {
            background: #e0b3d0;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 0.6rem 1.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="pin-container">', unsafe_allow_html=True)
    st.markdown('<div class="pin-title">🔐 For Smilte Only</div>', unsafe_allow_html=True)
    st.markdown('<div class="pin-instruction">Only pookies get past this door… what’s the magic code?</div>', unsafe_allow_html=True)

    pin = st.text_input("PIN", type="password", label_visibility="collapsed")

    if st.button("Unlock 💕", use_container_width=True):
        if pin == CORRECT_PIN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Wrong PIN! Only Smilte knows the code.")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 🎂 MAIN PAGE
# -------------------------------
else:

    SMILTE_MESSAGE = """just a few weeks ago you asked me if i remember how we met and honestly i still don’t know how. i genuinely can’t trace it back to a moment or a day. but i guess that’s not really important. what matters is that somehow, somewhere, we did meet. and meeting someone as genuine, real, and kind as you, especially online, and then just… vibing with them out of nowhere? that’s rare. like actually rare. i never expected that to happen, so yeah i’m still a little lowkey surprised by it.

but i’m really glad it did happen. because idk if this is a given or if you already know it, but you’re genuinely one of my closest friends and i care about you a lot.

and when i think about the past year you’ve had, it honestly feels a bit unfair how much it threw at you. from heartbreak to school stress to things at home, it just kept coming one after the other like life didn’t really give you a break. but the thing that stands out the most isn’t all the stuff that happened to you. it’s how you handled it. you kept fighting through everything even when it probably felt like way too much.

you fought like a warrior this year. and i really hope life becomes a lot kinder to you in the year ahead. but i also hope you take that same warrior version of yourself with you into it.

this next year is going to be a huge one for you. life is going to change a lot. big decisions, moving, new places, new people. but i really do believe things will work out for you.

so happy birthday smilte. i’m really glad you exist and that somehow our paths crossed in whatever random way they did. and i genuinely hope that before you reach full unc status, we actually get to meet in real life.

love, siddh."""

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Homemade+Apple&display=swap');

        .stApp {
            background: linear-gradient(135deg, #fbeaf2 0%, #e5f6ff 100%);
        }

        .main-content {
            max-width: 800px;
            margin: auto;
            padding: 2rem;
        }

        .title {
            font-family: 'Dancing Script', cursive;
            font-size: 4.2rem;
            color: #7a5f8c;
            text-align: center;
            margin-bottom: 2rem;
        }

        .letter {
            background: #fff9f5;
            border-radius: 12px;
            padding: 2.4rem;
            box-shadow: 0 8px 24px rgba(160,130,190,0.25);
            font-family: 'Homemade Apple', cursive;
            font-size: 1.35rem;
            line-height: 1.9;
            color: #7a5f8c;
            text-align: left;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    st.markdown('<div class="title">Happy Birthday, Smilte!</div>', unsafe_allow_html=True)

    safe_message = html.escape(SMILTE_MESSAGE)

    st.markdown(f"""
    <div class="letter">
    {safe_message.replace("\n", "<br><br>")}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
