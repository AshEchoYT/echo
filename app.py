from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

im = Image.open("image/favicon.ico")

st.set_page_config( page_title="AshEcho", page_icon=im,layout="wide" )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Style
def local_styl(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_styl("style/style.css")

#----- Assets-----
lottie_coding = load_lottieurl("https://lottie.host/00fd5679-73a2-4b92-89a9-3a870fbfe9d1/5xuq0oy9xg.json")
img_mc1 = Image.open("image/ep 1.jpg")
img_mc2 = Image.open("image/ep 2.jpg")

#-----HEADER SECTION----
with st.container():
    st.subheader("Hi, we are ash,anush and surya :wave:")
    st.title("We are students of DRNKVV")
    st.write("We are passionate about learning pythons and finding new ways to integrate in our day-to-day life")
    st.write("[Learn More>](https://ashecho.blogspot.com/)")
 # --------What we do-------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Meet Our Talented Team Who Made this Project")
        st.write("##")
        st.write(
            """
            In our diverse team, 
            - Ash takes the lead as a dynamic YouTuber with a talent for creating gaming and informative content. With impressive video editing skills and a deep love for gaming, he ensures your content is not only engaging but also informative.
            - Anush brings his unique blend of humor and athleticism to the table, making him a versatile asset for any project. His knack for sports and commitment to his studies make him an all-rounder, and he's also known to create quirky emojis for added fun.
            - Surya, a true jack-of-all-trades, is a former taekwondo champion with a strong academic record. He adds a touch of uniqueness to our team as a dedicated "weeb" and brings his diverse skills to every project he's involved in.

            These three talented individuals are the driving force behind our portfolio blog, and they are ready to bring their expertise to your new project.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@AshEcho)")
    with right_column:
        st_lottie(lottie_coding, height=500,key="coding")

#-----PROJECTS-----
with st.container():
    st.write("---")
    st.header("Ash's Projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_mc1)

    with text_column:
        st.subheader("Most Chaotic தமிழ் MINECRAFT SMP ECHO CRAFT! in Tamil || Ep 1|| AshEcho")
        st.write(
            """
            Watch this video for a Wild Ride!!
            In this video, you will be watching my adventures in Minecraft SMP with my 2 friends. 
            As it is a pilot episode, we would have had some fun.
           """
        )
        st.markdown("[Watch Video...](https://youtu.be/OQFK0Yna_4Q)")

with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_mc2)

    with text_column:
        st.subheader("EXPLORING MINESHAFT! தமிழ் ECHO CRAFT SMP! in Tamil  Ep 2 AshEcho")
        st.write(
            """
            Watch this video for a Fun Filled Ride!!
            In this video, you will be watching my adventures in Minecraft SMP with my 2 friends. 
            And in this video we will be exploring a mineshaft 
           """
        )
        st.markdown("[Watch Video...](https://youtu.be/1xqfKkntpiE)")

#----Contact----
with st.container():
    st.write("---")
    st.header("Get in Touch With Us!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/ashecho006@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your Message here" required></textarea>
         <button type="submit">Send</button>
    </form>

    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
