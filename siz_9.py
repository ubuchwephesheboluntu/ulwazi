"""
Isikhungo Sezobuchwepheshe Boluntu — Website
=============================================
A Streamlit website for a business/organisation focused on helping
communities develop digitally (digital literacy, tech access, training,
and community upliftment through technology).
 
Run locally with:
    pip install streamlit
    streamlit run app.py
"""
 
from pathlib import Path

import streamlit as st


APP_DIRECTORY = Path(__file__).resolve().parent
HERO_IMAGE = APP_DIRECTORY / "hero-image.png"

# -----------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Isikhungo Sezobuchwepheshe Boluntu™",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# -----------------------------------------------------------------------
# GLOBAL STYLING
# -----------------------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background: #120E08;
            color: #F7E6B2;
        }
        [data-testid="stSidebar"] {
            background: #1D140A;
            border-right: 1px solid #6E4210;
        }
        [data-testid="stSidebar"] * {
            color: #F7E6B2;
        }
        h1, h2, h3, h4, p, label, .stMarkdown, .stText {
            color: #F7E6B2;
        }
        .main-title {
            font-size: 2.6rem;
            font-weight: 800;
            color: #F6C64E;
            text-shadow: 0 0 12px rgba(246, 162, 20, 0.35);
            margin-bottom: 0;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #D9A441;
            margin-top: 0;
        }
        .section-header {
            font-size: 1.8rem;
            font-weight: 700;
            color: #F6C64E;
            border-bottom: 3px solid #D98B17;
            padding-bottom: 6px;
            margin-top: 2rem;
        }
        .card {
            background: linear-gradient(135deg, #2A1A0B, #1B1209);
            color: #F7E6B2;
            padding: 1.2rem;
            border-radius: 12px;
            border: 1px solid #6E4210;
            border-left: 6px solid #E6A62E;
            margin-bottom: 1rem;
        }
        .stat-box {
            text-align: center;
            padding: 1rem;
            background: linear-gradient(135deg, #7A420B, #3A2109);
            color: #FFF0BD;
            border-radius: 12px;
            border: 1px solid #D98B17;
            box-shadow: 0 0 16px rgba(217, 139, 23, 0.2);
        }
        [data-testid="stMetric"] {
            background: #24170B;
            border: 1px solid #6E4210;
            border-radius: 12px;
            padding: 1rem;
        }
        [data-testid="stMetricLabel"] *, [data-testid="stMetricValue"] * {
            color: #F6C64E;
        }
        .stButton > button, [data-testid="stFormSubmitButton"] > button {
            background: #D98B17;
            color: #1A1006;
            border: 1px solid #F6C64E;
            font-weight: 700;
        }
        .stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {
            background: #F6C64E;
            color: #1A1006;
            border-color: #FFF0BD;
        }
        [data-baseweb="input"] > div, [data-baseweb="textarea"] > div {
            background-color: #24170B;
            border-color: #6E4210;
        }
        input, textarea {
            color: #FFF0BD !important;
        }
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
 
# -----------------------------------------------------------------------
# NAVIGATION (SIDEBAR)
# -----------------------------------------------------------------------
st.sidebar.title("📍 Okuqukethwe")
page = st.sidebar.radio(
    "Yiya",
    ["eKhaya", "Okumayelana nathi", "Imisebenzi esiyenzayo", "Esiphokophele kukho", "Xhumana nathi"],
)
 
st.sidebar.markdown("---")
st.sidebar.markdown("**Isikhungo Sezobuchwepheshe Boluntu™**")
st.sidebar.markdown("_Sakhela Imiphakathi Yethu Izinhlelo Zobuchwepheshe!")
 
# -----------------------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------------------
if page == "eKhaya":
    st.markdown('<p class="main-title">Isikhungo Sezobuchwepheshe Boluntu™</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sakhela Imiphakathi Yethu Izinhlelo Zobuchwepheshe Besimanje</p>', unsafe_allow_html=True)
 
    st.image(
        HERO_IMAGE,
        use_container_width=True,
        caption="Isikhungo Sezobuchwepheshe Boluntu™",
    )
 
    st.markdown("### Siyakwamukela")
    st.write(
        """
        **Isikhungo Sezobuchwepheshe Boluntu™** (Isikhungo Somphakathi Sokwakha Izinhlelo Zobuchwepheshe) lesi sikhungo sakhelwe ukuba sisize imiphakathi
        ukuba yakhe izinhlelo zobuchwepheshe besimanje. Kulesi sikhungo sikholelwa wukuthi ukuba nezinhlelo zobuchwepheshe besimanje, kanye nokuzisebenzisa lezi zinhlelo,
         yilungelo lawo wonke umuntu!
        Izinhlelo zobuchwepheshe mazingakhelwa kuphela labo abadla izambane likapondo; kepha nalabo abadla imbuya ngothi kumele babenazo izinhlelo zobuchwepheshe besimanje.
        Izinhlelo zobuchwepheshe besimanje kumele zilotshwe ngolimi lwesintu, ulimi olukhulunywa yiningi labantu emiphakathini.
 
        Sakha izinhlelo zobuchwepheshe; siqeqesha abantu ngokwakha kanye nangokusebenzisa izinhlelo zobuchwepheshe;
        sifundisa ngobuchwepheshe besimanje; sihlanganisa ubuchwepheshe besimanje kanye nezilimi zesintu;
        sihlela izimbizo lapho sibhunga khona ngobuchwepheshe; sifundisa abantu abasha ngokwakha izinhlelo zobuchwepheshe; siguqula izinhlelo ezikhona zobuchwepheshe
        ukuba zisebenziseke esintwini; sixhumanisa imiphakathi yethu kanye namanye amazwe.
        
        """
    )
 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-box"><h2>500+</h2>Abantu Okuhloswe ukuba Baqeqeshwe</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box"><h2>20+</h2>Imiphakathi Okuhloswe ukuba Kufinyelelwe kuyo</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box"><h2>50+</h2>Izimbizo Okuhloswe ukuba Zibanjwe</div>', unsafe_allow_html=True)
 
# -----------------------------------------------------------------------
# ABOUT US PAGE
# -----------------------------------------------------------------------
elif page == "Okumayelana nathi":
    st.markdown('<p class="section-header">Okumayelana nathi</p>', unsafe_allow_html=True)
 
    st.write(
        """
        Isikhungo Sezobuchwepheshe Boluntu sakhelwe esisekelweni kanye nasenkolelweni
        yokuba wonke umuntu kumele akwazi ukusebenzisa kanye nokufinyelela
        ebuchwephesheni besimanje.Ukusebenzisa ubuchwepheshe besimanje kumele kube yilungelo lawo wonke umuntu.
        Iningi lobuchwepheshe obukhona njengamanje lusesimweni sokuba yisilungu. Ubuchwepheshe besimanje kumele buhambelane futhi nesintu.
        """
    )
 
    st.markdown("#### Inhlosongqangi yethu")
    st.markdown(
        """
        <div class="card">
        Ukwakha izinhlelo zobuchwepheshe besimanje ezihambisana nenhlalonhle yabantu emiphakathini.
        </div>
        """,
        unsafe_allow_html=True,
    )
 
    st.markdown("#### Esiphokophele kukho")
    st.markdown(
        """
        <div class="card">
        Ukwenza impilo yabantu emiphakathini ibe ngcono ngokusebenzisa izinhlelo zobuchwepheshe besimanje. Ukufundisa abantu ngezinhlelo zobuchwepheshe.
        </div>
        """,
        unsafe_allow_html=True,
    )
 
    st.markdown("#### Esikholelwa kukho")
    values = {
        "Ubuntu": "Ukuthuthukisa Imiphakathi ngokusebenzisana.",
        "Ilungelo": "Ukusebenzisa Ubuchwepheshe Besimanje Kumele Kube Yilungelo Lawo Wonke Umuntu.",
        "Ulimi": "Izinhlelo Zobuchwepheshe Besimanje kumele zilotshwe ngezilimi Zesintu.",
        "Inqubekela-phambili": "Ukwakha izinhlelo zobuchwepheshe besimanje ukudambisa izinkinga ezingakhungatha imiphakathi yethu.",
    }
    for value, description in values.items():
        st.markdown(f"**{value}** — {description}")
 
# -----------------------------------------------------------------------
# SERVICES PAGE
# -----------------------------------------------------------------------
elif page == "Imisebenzi esiyenzayo":
    st.markdown('<p class="section-header">Imisebenzi esiyenzayo</p>', unsafe_allow_html=True)
    st.write("Ziningi Izinhlelo Esinazo Esihlose Ngazo Ukuthuthukisa Imiphakathi.")
 
    services = [
        ("💻 Ukufundisa Ngobuchwepheshe Besimanje", "Lapha kufundiswa abantu emiphakathini ngobuchwepheshe besimanje."),
        ("📱 Izimbizo Zobuchwepheshe", "Lapha kuhlelwa imihlangano lapho khona uluntu lubhunga ngobuchwepheshe besimanje."),
        ("🧑‍💼 Ukuthuthukisa Amabhungu Namatshitshi", "Lapha kufundiswa abantu abasha ngobuchwepheshe besimanje."),
        ("🏪 Ukwakha Izinhlelo Zobuchwepheshe", "Lapha kulesi sikhungo kwakhiwa izinhlelo zobuchwepheshe."),
        ("🌐 Izinhlelo Zokufunda Nokufundisa", "Lapha kwakhiwa izinhlelo ezisiza ekufundeni kanye nasekufundiseni."),
        ("🎓 Uqeqesho", "Ukuqeqesha abantu abazokwazi ukuba bakhe izinhlelo zobuchwepheshe ezihambelana nesintu."),
    ]
 
    for i in range(0, len(services), 2):
        cols = st.columns(2)
        for col, (title, desc) in zip(cols, services[i:i + 2]):
            with col:
                st.markdown(f'<div class="card"><h4>{title}</h4>{desc}</div>', unsafe_allow_html=True)
 
# -----------------------------------------------------------------------
# IMPACT PAGE
# -----------------------------------------------------------------------
elif page == "Esiphokophele kukho":
    st.markdown('<p class="section-header">Esiphokophele kukho</p>', unsafe_allow_html=True)
 
    st.write(
        """
        Sihlose ukusebenzisana nemiphakathi ukufaka izinhlelo
        zobuchwepheshe besimanje emiphakathini. Lezi kumele kube 
        yizinhlelo ezihambisana nesintu, ezilotshwe ngolimi lwesintu, 
        futhi ezisiza abantu emiphakathini ukuba bathuthukise izimpilo zabo.
        """
    )
 
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Iningi labantu okuhloswe ukuba liqeqeshwe", "500+")
    col2.metric("Isibalo semiphakathi okuhloswe ukuba kufinyelelwe kuyo", "20+")
    col3.metric("Izimbizo okuhloswe ukuba zibanjwe", "50+")
    col4.metric("Izinhlaka ezahlukene okuhlelwe ukuba kusetshenzwe nazo", "10+")
 
    st.markdown("#### Izindaba ezivela emiphakathini")
    st.markdown(
        """
        <div class="card">
        "Bengingazi lutho ngobuchwepheshe besimanje. Manje, ngesikhungo sezobuchwepheshe boluntu,
        ngifunde lukhulu!" — <i>Ilungu lomphakathi elifike kwenye yezimbizo</i>
        </div>
        <div class="card">
        "Ngangithi ubuchwepheshe yinto nje yabelungu kuphela.
        Ngangingazi mina ukuba nasesintwini ubuchwepheshe buyangena?" — <i>Impunga yendawo</i>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
# -----------------------------------------------------------------------
# CONTACT PAGE
# -----------------------------------------------------------------------
elif page == "Xhumana nathi":
    st.markdown('<p class="section-header">Xhumana nathi</p>', unsafe_allow_html=True)
    st.write("Xhumana nathi usazise ngezinhlelo zobuchwepheshe ofuna ukuzibona zakhiwa. Sishayele ucingo, noma usithumele umbikombani.")

    st.markdown("#### Imininingwane Yethu")
    st.markdown(
        """
        <div class="card">
        📍 <b>Address:</b> 2205 Silverrich Grove, Newlands West, eThekwini<br><br>
        📞 <b>Inombolo yocingo yokuqala:</b> <a href="tel:0729066360" style="color:#F6C64E;">072 906 6360</a><br><br>
        📞 <b>Inombolo yocingo yesibili:</b> <a href="tel:0754454728" style="color:#F6C64E;">075 445 4728</a><br><br>
        ✉️ <b>Umbikombani wokuqala:</b> <a href="ubuchwephesheboluntu@gmail.com" style="color:#F6C64E;">ubuchwephesheboluntu@gmail.com</a><br><br>
        ✉️ <b>Umbikombani wesibili:</b> <a href="isikhungosezobuchwepheshe@gmail.com" style="color:#F6C64E;">isikhungosezobuchwepheshe@gmail.com</a><br><br>
        🕒 <b>Isikhathi Sokusebenza:</b> UMsombuluko–ULwesihlanu, 08:00–16:00  -  UMgqibelo–YiSonto, 08:00–13:00
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------
# FOOTER (shown on every page)
# -----------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2026 Isikhungo Sezobuchwepheshe Boluntu™. "
    "All rights reserved. | Empowering Communities Through Technology.</p>",
    unsafe_allow_html=True,
)
 
