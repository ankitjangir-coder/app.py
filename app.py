import streamlit as st
import urllib.parse

# 1. Page Configuration Settings
st.set_page_config(page_title="Elite Studio Automation", page_icon="🏢", layout="centered")

st.title("🏢 ELITE STUDIO - INSTANT DESIGN & ESTIMATION ENGINE")
st.markdown("*Enter spatial preferences below to generate immediate 3D concepts and pricing sheets within minutes.*")
st.markdown("---")

# 2. Creating User Interface (UI) Dropdowns and Sliders
client_name = st.text_input("👤 Enter Client Name / Business ID:", placeholder="e.g., Ramesh Kumar")

col1, col2 = st.columns(2)
with col1:
    property_type = st.selectbox("🏠 Property Structure Category:", ["Residential", "Commercial"])
with col2:
    design_style = st.selectbox("✨ Aesthetic Identity Direction:", ["Modern Minimalist", "Luxury Classical", "Industrial Loft", "Biophilic Organic"])

col3, col4 = st.columns(2)
with col3:
    carpet_area = st.number_input("📐 Carpet Area Size (in Sqft Metric):", min_value=100, max_value=50000, value=1200, step=50)
with col4:
    quality_tier = st.selectbox("💎 Material Quality Framework:", ["Silver Framework", "Gold Framework", "Diamond Framework"])

st.markdown("---")

# 3. Execution Processing Trigger Button Click Line
if st.button("🚀 GENERATE DESIGN RENDER & ESTIMATION DISPATCH"):
    if not client_name:
        st.warning("⚠️ Action Required: Please enter a valid Client Name to compile reports.")
    else:
        # Core Matrix Cost Logic Engine Matching Spreadsheet Rules
        base_rate = 2500
        if "Silver" in quality_tier:
            base_rate = 1500
        elif "Gold" in quality_tier:
            base_rate = 3000
        elif "Diamond" in quality_tier:
            base_rate = 6000
            
        calculated_cost = carpet_area * base_rate
        safety_buffer_cost = int(calculated_cost * 1.10)
        
        # 4. Displaying High-Precision Output Tables Instantly
        st.success(f"✔ Project Profile Processing Complete for {client_name}!")
        
        st.subheader("📊 Architectural Project Metric Specifications")
        st.markdown(f"**Base Evaluation Value:** INR {calculated_cost:,}/-")
        st.markdown(f"**Safety Margin Total (with 10% Material Protection Buffer):** INR {safety_buffer_cost:,}/-")
        
        # 5. Fetching Free AI Image Render URLs on Screen UI
        raw_prompt = f"hyperrealistic 3d render of a premium interior space designed in a clean {design_style} style for a modern {property_type} architecture 8k resolution photorealistic portfolio shot"
        encoded_query = urllib.parse.quote(raw_prompt)
        ai_image_url = f"https://image.pollinations.ai/prompt/{encoded_query}?width=1280&height=720&nologo=true"
        
        st.markdown("---")
        st.subheader("🎨 Your Customized 3D Conceptual Spatial Moodboard Preview:")
        
        # Direct Backup Link so users can view instantly if render is slow
        st.markdown(f"🔗 *If the image takes time to load, click here to open instantly:* **[View Full 3D Render Concept]({ai_image_url})**")
        
        st.image(ai_image_url, caption=f"Dynamic Vector Rendering Direction Matching Preference Matrix: {design_style}", use_container_width=True)
