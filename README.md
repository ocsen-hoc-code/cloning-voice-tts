# Voice Cloning with XTTS v2

This project uses **Coqui TTS (XTTS v2)** to **clone a voice** from a sample audio file and generate speech based on input text. The model supports multiple languages and can run on both **GPU (CUDA) and CPU**.

---

## **🚀 Installation**

### **1️⃣ Install Dependencies**
Ensure you have Python **3.8+** installed, then run:

```bash
pip install TTS
```

If you want **GPU acceleration**, install PyTorch with CUDA (optional):

```bash
pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

## **📂 Project Structure**

```
📁 project-folder/
│── 📁 speaker/        # Folder containing the sample voice file
│── 📄 my_voice.wav    # Sample speaker audio (inside speaker/)
│── 📄 input.txt       # Text file containing the sentence to be spoken
│── 📄 output.wav      # Generated speech file (output)
│── 📄 main.py  # Main script
│── 📄 README.md       # Documentation
```

---

## **📌 How to Use**

### **1️⃣ Prepare Required Files**
- Place the **speaker’s sample voice** inside the `speaker/` folder (e.g., `speaker/my_voice.wav`).  
- Create an **input text file (`input.txt`)** with the sentence you want to generate speech for.  

### **2️⃣ Run the Script**
To generate speech using the cloned voice, run:

```bash
python main.py
```

If running on **CPU only**, use:

```bash
python main.py --device cpu
```

---

## **🎯 Example Usage**

1. **Prepare the input text (`input.txt`)**:

```
Hello, this is an AI-generated voice cloned from my sample audio.
```

2. **Run the script**:

```bash
python main.py
```

3. **Output**:
- The generated speech will be saved as `output.wav`.

---

## **💡 Notes**
- If you get an error about missing files, ensure `my_voice.wav` and `input.txt` exist.
- For best results, use **at least 10-30 seconds of high-quality speaker audio**.
- GPU acceleration is recommended for faster processing.

---

## **📌 References**
- [Coqui TTS Documentation](https://tts.readthedocs.io/en/latest/)
- [XTTS v2 Model on Hugging Face](https://huggingface.co/coqui)

---

🎉 **Enjoy Cloning Your Voice with AI!**