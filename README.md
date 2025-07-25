<img width="1024" height="1024" alt="5caec095df2745d08e28b128e4e15b6f" src="https://github.com/user-attachments/assets/676e747b-51bf-412b-a6d2-33e1649e4382" />Text-Image-Generation

**Text-to-Image Generation using Stable Diffusion XL (SDXL) + LoRA in Flask**

This project is a local Flask-based application that converts text prompts into AI-generated images using the **Stable Diffusion XL Base 1.0** model and **BetterFaces LoRA** for enhanced face quality. It runs entirely offline on your GPU machine and saves images into a gallery structure by date.

---

## Preview

![App Screenshot](assets/preview.png)

---<img width="1024" height="1024" alt="4c355a23aad647e1a6c65695e4438f6b" src="https://github.com/user-attachments/assets/75b773cc-3af0-4c58-a4ca-9972b3e5316f" />
<img width="1024" height="1024" alt="5caec095df2745d08e28b128e4e15b6f" src="https://github.com/user-attachments/assets/c6db1398-47b8-4ad0-bcf1-cc6c27fb01bd" />
<img width="1024" height="1024" alt="20cf4bf52cbe48c4812e2ac368bb38b3" src="https://github.com/user-attachments/assets/c9ce8d03-b57e-4a2e-a920-a4a39ac541ef" />
<img width="1024" height="1024" alt="c75760ac972e4d02b344bf4e14756e57" src="https://github.com/user-attachments/assets/0f9ad75e-2aae-4bd0-9b15-4d16bfe35c27" />
img width="1024" height="1024" alt="bae2ab29d5dc41978f7811a98851e9ba" src="https://github.com/user-attachments/assets/7161ca24-37fd-4424-8c85-f78fddb9b392" />
<img width="1024" height="1024" alt="7f56d0603059426fa3c9df0e55cbc919" src="https://github.com/user-attachments/assets/f27a4c78-1660-4f4c-8995-cddf9472cc98" />
<img width="1024" height="1024" alt="ac6a77c5b9544b588e1881f21fd2b423" src="https://github.com/user-attachments/assets/10b4be5d-444a-4668-8c58-d4fc1da492b9" />







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
