import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px

# 1. Menyiapkan data historis sederhana
# Fitur: [Iklan (Juta), Diskon (%)]
X_train = np.array([[5, 10], [10, 20], [15, 5], [20, 25], [25, 15]])

# Target: Keuntungan (Juta)
y_train = np.array([50, 80, 110, 90, 150])

# 2. Melatih model (Mesin Replika)
model = LinearRegression().fit(X_train, y_train)

# 3. Menetapkan Skenario Dasar (Baseline)
# Kondisi saat ini: Iklan 10 Juta, Diskon 10%
baseline_input = np.array([[10, 10]])
baseline_pred = model.predict(baseline_input)[0]
print(f"Prediksi Keuntungan Baseline: Rp {baseline_pred:.2f} Juta")

def run_simulation(new_iklan, new_diskon):
    # Input baru dari user (Intervensi)
    intervention_input = np.array([[new_iklan, new_diskon]])
    # Prediksi hasil intervensi
    prediction = model.predict(intervention_input)[0]
    # Menghitung Delta (Selisih)
    delta_y = prediction - baseline_pred
    return prediction, delta_y

# st.set_page_config(
#     page_title="Simulator Kebijakan Keuntungan Toko",
#     page_icon="🚀",
#     layout="wide"
# )

# st.markdown("""
# <style>

# /* Background utama */
# .stApp{
#     background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
#     background-size: 400% 400%;
#     animation: gradient 15s ease infinite;
# }

# /* Animasi background */
# @keyframes gradient{
#     0%{background-position:0% 50%;}
#     50%{background-position:100% 50%;}
#     100%{background-position:0% 50%;}
# }

# /* Sidebar */
# [data-testid="stSidebar"]{
#     background: rgba(255,255,255,0.1);
#     backdrop-filter: blur(15px);
# }

# /* Judul */
# h1{
#     color:white;
#     text-align:center;
#     animation: fadeIn 1.5s;
# }

# /* Semua teks */
# p, label, div{
#     color:white;
# }

# /* Metric card */
# div[data-testid="metric-container"]{
#     background: rgba(255,255,255,0.15);
#     border:1px solid rgba(255,255,255,0.2);
#     padding:25px;
#     border-radius:20px;
#     backdrop-filter: blur(20px);
#     box-shadow:0 8px 32px rgba(0,0,0,0.3);
#     animation: fadeIn 1.5s;
#     transition:0.3s;
# }

# /* Efek hover */
# div[data-testid="metric-container"]:hover{
#     transform:scale(1.03);
#     box-shadow:0 10px 40px rgba(0,255,255,0.4);
# }

# /* Animasi muncul */
# @keyframes fadeIn{
#     from{
#         opacity:0;
#         transform:translateY(30px);
#     }
#     to{
#         opacity:1;
#         transform:translateY(0);
#     }
# }

# /* Tombol */
# .stButton>button{
#     background:linear-gradient(45deg,#00c6ff,#0072ff);
#     color:white;
#     border:none;
#     border-radius:15px;
#     transition:0.3s;
# }

# .stButton>button:hover{
#     transform:scale(1.05);
# }

# /* Slider */
# .stSlider{
#     animation: fadeIn 2s;
# }

# </style>
# """, unsafe_allow_html=True)

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Simulator Kebijakan Keuntungan Toko",
    page_icon="💳",
    layout="wide"
)

# ================== CSS ==================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e1b4b,#312e81);
}

[data-testid="stSidebar"]{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
}

h1,h2,h3,p,label{
    color:white;
}

/* Card metric */
div[data-testid="metric-container"]{
    background: rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:25px;
    padding:20px;
    box-shadow:0 8px 30px rgba(0,0,0,.3);
}

/* Sidebar text */
section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center'>
🚀 Simulator Kebijakan Keuntungan Toko
</h1>
<h4 style='text-align:center;color:#d1d5db'>
Simulasi What-If untuk menentukan strategi bisnis
</h4>
""", unsafe_allow_html=True)

st.markdown(
    "<center><h4 style='color:#cbd5e1'>Gunakan slider untuk menguji skenario What-If</h4></center>",
    unsafe_allow_html=True
)
st.write("Gunakan slider untuk menguji skenario 'What-If'.")

# --- SIDEBAR: Variabel Kontrol ---
st.sidebar.title("⚙️ Tuas Kebijakan")

iklan_slider = st.sidebar.slider(
    "📢 Anggaran Iklan (Juta)",
    0,
    50,
    10
)

diskon_slider = st.sidebar.slider(
    "🏷️ Besaran Diskon (%)",
    0,
    50,
    10
)

# --- ENGINE: Jalankan Simulasi ---
hasil_pred, delta = run_simulation(
    iklan_slider,
    diskon_slider
)

persen = delta / baseline_pred * 100

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#8b5cf6,#4f46e5);
padding:35px;
border-radius:30px;
box-shadow:0 10px 30px rgba(0,0,0,.4);
">

<h3 style="color:white">
💳 Total Prediksi Keuntungan
</h3>

<h1 style="color:white;font-size:55px">
Rp {hasil_pred:.2f} Juta
</h1>

<p style="color:#e0e7ff">
Simulator Kebijakan Keuntungan Toko
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="metric-container"]{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.18);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(20px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# --- UI: Tampilkan Hasil ---
col1,col2,col3=st.columns(3)

with col1:
    st.metric(
        "💰 Baseline",
        f"Rp {baseline_pred:.2f} Jt"
    )

with col2:
    st.metric(
        "📈 Prediksi Baru",
        f"Rp {hasil_pred:.2f} Jt",
        f"{delta:.2f} Jt"
    )

with col3:
    st.metric(
        "🎯 Persentase",
        f"{persen:.1f}%"
    )
#
#  Visualisasi Perbandingan
data_plot = pd.DataFrame({
    'Skenario':['Baseline','Intervensi'],
    'Keuntungan':[baseline_pred,hasil_pred]
})

fig = px.bar(
    data_plot,
    x='Skenario',
    y='Keuntungan',
    color='Skenario',
    text_auto='.2f',
    template='plotly_dark'
)

fig.update_layout(
    title="📊 Perbandingan Keuntungan",
    title_x=0.5,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

st.plotly_chart(
    fig,
    use_container_width=True
)