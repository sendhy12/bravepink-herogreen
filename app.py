import streamlit as st
from PIL import Image, ImageOps
import numpy as np

# =============================
# Fungsi efek dua warna
# =============================
def brave_pink_hero_green(img, threshold=128):
    gray = ImageOps.grayscale(img)
    arr = np.array(gray)

    # Warna hex → RGB
    pink = np.array([247, 132, 197])   # #f784c5
    green = np.array([27, 96, 47])     # #1b602f

    # Buat mask berdasarkan threshold
    mask = arr > threshold
    duotone = np.zeros((*arr.shape, 3), dtype=np.uint8)
    duotone[mask] = green
    duotone[~mask] = pink

    return Image.fromarray(duotone)

# =============================
# Streamlit UI
# =============================
st.set_page_config(page_title="Brave Pink – Hero Green Generator", layout="centered")

st.title("🩷💚 Brave Pink – Hero Green Generator")
st.write("Ubah fotomu ke gaya solidaritas **Brave Pink – Hero Green** 🇮🇩")

# Upload foto
uploaded_file = st.file_uploader("Upload foto", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.subheader("Foto Asli")
    st.image(img, use_container_width=True)

    # Slider untuk atur threshold
    threshold = st.slider("Atur intensitas pemisahan warna", 0, 255, 128)

    # Proses efek
    result = brave_pink_hero_green(img, threshold=threshold)

    st.subheader("Foto Brave Pink – Hero Green")
    st.image(result, use_container_width=True)

    # Tombol download
    result.save("brave_pink_hero_green.png")
    with open("brave_pink_hero_green.png", "rb") as f:
        st.download_button("⬇️ Download Hasil", f, file_name="brave_pink_hero_green.png", mime="image/png")
