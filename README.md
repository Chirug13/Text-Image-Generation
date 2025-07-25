# Text-Image-Generation
# 🖼️ Text-to-Image Generation with Stable Diffusion XL (LoRA) and Flask

This project is a local Flask-based web application for generating images from text prompts using **Stable Diffusion XL 1.0** with LoRA (Low-Rank Adaptation) fine-tuning. It supports GPU-accelerated inference and displays previously generated images in a gallery format.

---

## 🚀 Features

- 🔥 **GPU-based** image generation with SDXL + LoRA
- 🖼️ Auto-gallery view of generated images by date
- 📝 HTML form for prompt input
- 🧹 Clear gallery feature
- 📦 Fully local, no external API required

---

## 📁 Folder Structure

Text-Image-Generation/
├── app.py # Flask application backend
├── requirements.txt # Required Python packages
├── generated/ # Stores generated images (auto-organized by date)
├── models/ # Pretrained SDXL and LoRA model files
│ ├── Stable-diffusion/
│ │ └── stable-diffusion-xl-base-1.0/
│ └── Lora/
│ └── SDXL_BetterFaces-LoRA_v1.safetensors
├── templates/
│ └── index.html # Main UI template for prompt input & gallery

yaml
Copy
Edit

---

## 🧠 Models Used

1. **Stable Diffusion XL Base 1.0**  
2. **BetterFaces-LoRA v1** (for enhanced facial rendering)

---

## 📥 How to Download Models

### 🔹 1. `stable-diffusion-xl-base-1.0`

- Go to the [Hugging Face model page](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- Click “⋯” ➜ **Download model**
- Or install via code (requires Hugging Face CLI):
```bash
huggingface-cli login
git lfs install
git clone https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
Place the downloaded folder under:

pgsql
Copy
Edit
models/Stable-diffusion/stable-diffusion-xl-base-1.0/
🔹 2. SDXL_BetterFaces-LoRA_v1.safetensors
Visit Civitai - SDXL BetterFaces LoRA

Click Download for the .safetensors version

Place the file under:

swift
Copy
Edit
models/Lora/SDXL_BetterFaces-LoRA_v1.safetensors
⚙️ Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/Text-Image-Generation.git
cd Text-Image-Generation
2. Create & Activate Virtual Environment (Optional)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Linux/Mac
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
bash
Copy
Edit
python app.py
Then open http://localhost:5000 in your browser.

📌 Notes
Requires CUDA-enabled GPU for optimal performance.

Ensure model paths are set correctly in app.py:

python
Copy
Edit
model_path = "D:/Redhats/AI_Image_Generation/models/Stable-diffusion/stable-diffusion-xl-base-1.0"
lora_path  = "D:/Redhats/AI_Image_Generation/models/Lora/SDXL_BetterFaces-LoRA_v1.safetensors"
Generated images are stored under /generated/YYYY-MM-DD/.

🖼️ Screenshot

🛡️ License
MIT License (or your preferred license)

👤 Author
Chiru
Santosh
