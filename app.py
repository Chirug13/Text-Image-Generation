from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from diffusers import DiffusionPipeline
import torch
import uuid
import os
import shutil
import traceback
from datetime import datetime

app = Flask(__name__)
base_output_dir = "generated"
os.makedirs(base_output_dir, exist_ok=True)

model_path = "D:/Redhats/AI_Image_Generation/models/Stable-diffusion/stable-diffusion-xl-base-1.0"
lora_path = "D:/Redhats/AI_Image_Generation/models/Lora/SDXL_BetterFaces-LoRA_v1.safetensors"

try:
    print("🔁 Loading SDXL model...")
    pipe = DiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    ).to("cuda")
    pipe.load_lora_weights(lora_path)
    pipe.fuse_lora()
    print("✅ Model loaded.")
except Exception:
    print("❌ Failed to load model:")
    print(traceback.format_exc())
    pipe = None

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    prompt = None
    error = None
    if request.method == 'POST':
        if request.form.get("clear_gallery") == "true":
            for subdir in os.listdir(base_output_dir):
                shutil.rmtree(os.path.join(base_output_dir, subdir), ignore_errors=True)
            return redirect(url_for('index'))

        prompt = request.form.get('prompt')
        if not prompt:
            error = 'Prompt is required.'
        elif not pipe:
            error = 'Model not loaded. Check server logs.'
        else:
            try:
                today_dir = os.path.join(base_output_dir, datetime.now().strftime("%Y-%m-%d"))
                os.makedirs(today_dir, exist_ok=True)
                image = pipe(prompt=prompt, num_inference_steps=50).images[0]
                filename = f"{uuid.uuid4().hex}.png"
                path = os.path.join(today_dir, filename)
                image.save(path)
                filename = f"{datetime.now().strftime('%Y-%m-%d')}/{filename}"
            except Exception as e:
                error = str(e)

    images = []
    for subfolder in sorted(os.listdir(base_output_dir), reverse=True):
        folder_path = os.path.join(base_output_dir, subfolder)
        if os.path.isdir(folder_path):
            for file in sorted(os.listdir(folder_path), reverse=True):
                if file.endswith(".png"):
                    images.append(f"{subfolder}/{file}")
    return render_template('index.html', filename=filename, prompt=prompt, error=error, images=images)

@app.route('/generated/<path:filename>')
def serve_image(filename):
    return send_from_directory(base_output_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
