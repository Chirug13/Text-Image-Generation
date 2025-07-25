Text-Image-Generation

**Text-to-Image Generation using Stable Diffusion XL (SDXL) + LoRA in Flask**

This project is a local Flask-based application that converts text prompts into AI-generated images using the **Stable Diffusion XL Base 1.0** model and **BetterFaces LoRA** for enhanced face quality. It runs entirely offline on your GPU machine and saves images into a gallery structure by date.

---

## Preview

![App Screenshot](assets/preview.png)

---

## Project Structure

Text-Image-Generation/
├── app.py # Main Flask backend
├── requirements.txt # Python dependencies
├── generated/ # Output folder (auto-created by app)
├── models/ # Contains SDXL and LoRA weights
│ ├── Stable-diffusion/
│ │ └── stable-diffusion-xl-base-1.0/
│ └── Lora/
│ └── SDXL_BetterFaces-LoRA_v1.safetensors
├── templates/
│ └── index.html # Web frontend template
├── assets/
│ └── preview.png # Optional sample image for README

yaml
Copy
Edit

---

## Models Used

### Stable Diffusion XL Base 1.0
Download: [Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- Use `git lfs`:
```bash
git lfs install
git clone https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
LoRA: SDXL_BetterFaces-LoRA_v1
Download: CivitAI Model Page

File to use: SDXL_BetterFaces-LoRA_v1.safetensors

⚙️ Setup Instructions
1. Clone this repo
bash
Copy
Edit
git clone https://github.com/Chirug13/Text-Image-Generation.git
cd Text-Image-Generation
2. Set up Python environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

Run the App
bash
Copy
Edit
python app.py
Open your browser and go to:
http://localhost:5000

Notes
Requires NVIDIA GPU with CUDA for inference (torch.float16).

All generated images are saved in:

bash
Copy
Edit
/generated/YYYY-MM-DD/
To clear the image gallery, use the "Clear Gallery" button in the UI.

Optional: Ignore heavy folders
If you're using Git, add this to .gitignore:

pgsql
Copy
Edit
generated/
models/
*.safetensors

License
Open Source

👤 Author
Chiru
Santosh
