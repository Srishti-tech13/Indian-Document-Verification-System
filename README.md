# Indian-Document-Verification-System
A Python-based system that combines face recognition with optical character recognition (OCR) to extract and verify identity information from ID documents like Aadhaar cards. Supports image-based input, face matching, and text extraction using OpenCV, face recognition, and Tesseract OCR.

# 🔐 Aadhar Face Match & Verification

A secure AI-powered identity verification system that matches faces from Aadhar cards with live selfies using advanced computer vision and OCR technology.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![OpenCV](https://img.shields.io/badge/opencv-v4.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **🎯 AI-Powered Face Matching**: Uses DeepFace library for accurate facial recognition
- **📸 Live Selfie Capture**: Real-time webcam integration for selfie capture
- **🔍 OCR Text Extraction**: Automatic date of birth extraction from Aadhar cards
- **⚡ Real-time Verification**: Instant results with confidence scores
- **🎨 Modern UI**: Glassmorphism design with smooth animations
- **🔒 Privacy First**: Local processing - images deleted after verification
- **📊 Quality Assessment**: Image sharpness and quality analysis
- **🎂 Age Verification**: Automatic age calculation and eligibility check

## 🖥️ Screenshots
![WhatsApp Image 2025-06-25 at 4 33 33 PM](https://github.com/user-attachments/assets/d06e041e-2f33-4095-9fab-084f77a75840)
![WhatsApp Image 2025-06-25 at 4 39 39 PM](https://github.com/user-attachments/assets/c432e5e1-c0a5-440a-b5c4-70b5c6666c22)
![WhatsApp Image 2025-06-25 at 4 45 06 PM](https://github.com/user-attachments/assets/8c21ab13-06cb-4890-856d-64e60b33e95d)
![WhatsApp Image 2025-06-25 at 4 37 29 PM](https://github.com/user-attachments/assets/dc2fce51-1f5a-4eeb-a762-ae036e963155)
![WhatsApp Image 2025-06-25 at 4 36 32 PM](https://github.com/user-attachments/assets/7defded9-abae-4fce-9c9a-f656a163d369)
![WhatsApp Image 2025-06-25 at 4 34 38 PM](https://github.com/user-attachments/assets/e8efd176-3c81-479d-89b3-81a6f1f36728)




### Main Interface
*Modern glassmorphism UI with smooth animations*

### Verification Results
*Real-time face matching with confidence scores*

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam access
- Tesseract OCR installed

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aadhar-face-match.git
   cd aadhar-face-match
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR**
   
   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to: `C:\Program Files\Tesseract-OCR\`
   
   **macOS:**
   ```bash
   brew install tesseract
   ```
   
   **Linux:**
   ```bash
   sudo apt-get install tesseract-ocr
   ```

4. **Update Tesseract path** (if needed)
   
   Edit line 10 in `app.py` to match your Tesseract installation path:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"YOUR_TESSERACT_PATH"
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501`

## 📋 Usage

1. **Upload Aadhar Image**: Select a clear image of your Aadhar card
2. **Capture Selfie**: Use the webcam to take a live selfie
3. **Get Results**: View verification results with confidence scores
4. **Age Verification**: Automatic DOB extraction and age validation

## 🛠️ Technical Details

### Core Technologies

- **DeepFace**: State-of-the-art facial recognition
- **OpenCV**: Computer vision and image processing
- **Tesseract OCR**: Text extraction from images
- **Streamlit**: Modern web application framework

### Architecture

```
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # Documentation
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── assets/              # Screenshots and media
```

### Security Features

- **Local Processing**: All computations happen locally
- **Automatic Cleanup**: Images deleted after verification
- **No Data Storage**: No personal data is stored or transmitted
- **Privacy First**: Designed with privacy by design principles

## 🎨 UI Features

- **Glassmorphism Design**: Modern frosted glass effect
- **Smooth Animations**: CSS animations and transitions
- **Responsive Layout**: Works on all screen sizes
- **Dark Theme**: Eye-friendly dark interface
- **Real-time Feedback**: Live status updates and progress indicators

## 📊 Verification Metrics

| Metric | Description | Range |
|--------|-------------|-------|
| **Face Match Score** | Similarity confidence | 0-100% |
| **Image Quality** | Sharpness assessment | Clear/Blurry |
| **Age Verification** | DOB extraction status | Eligible/Not Eligible |

## 🔧 Configuration

### Adjusting Verification Sensitivity

Modify the verification threshold in `app.py`:

```python
# More strict verification (higher accuracy, less tolerance)
threshold = 0.4  # Default: 0.6

# More lenient verification (lower accuracy, more tolerance)  
threshold = 0.8
```

### Image Quality Settings

Adjust blur detection sensitivity:

```python
def is_blurry(img_array, threshold=100):  # Lower = more sensitive
    # Your blur detection logic
```

## 🚨 Troubleshooting

### Common Issues

**Camera not working:**
- Check webcam permissions
- Ensure no other apps are using the camera
- Try restarting the application

**Tesseract not found:**
- Verify Tesseract installation path
- Update the path in `app.py` line 10
- Restart the application

**Poor verification results:**
- Ensure good lighting conditions
- Use high-quality images
- Keep face clearly visible and unobstructed

**OCR not extracting text:**
- Use clear, high-resolution Aadhar images
- Ensure text is not blurry or distorted
- Try different image formats (PNG, JPG)

## 📄 File Structure

```
aadhar-face-match/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore patterns
│
├── assets/               # Project assets
│   ├── screenshots/      # UI screenshots
│   └── demo/            # Demo files
│
├── docs/                 # Additional documentation
│   ├── INSTALLATION.md   # Detailed installation guide
│   ├── API.md           # API documentation
│   └── CONTRIBUTING.md   # Contribution guidelines
│
└── tests/               # Test files
    ├── test_face_match.py
    ├── test_ocr.py
    └── sample_images/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📈 Performance

- **Face Matching**: ~2-3 seconds per verification
- **OCR Processing**: ~1-2 seconds per image
- **Memory Usage**: ~200-500MB during processing
- **Supported Image Formats**: JPG, JPEG, PNG
- **Max Image Size**: 10MB recommended

## 🔐 Privacy & Security

- **No Cloud Processing**: Everything runs locally
- **Temporary Storage**: Images deleted immediately after processing
- **No Data Collection**: Zero personal data storage
- **Open Source**: Full transparency in code

## 📱 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full |
| Firefox | ✅ Full |
| Safari | ✅ Full |
| Edge | ✅ Full |

## 🆔 Supported ID Documents

Currently optimized for:
- Indian Aadhar Cards
- Clear, well-lit photographs
- Standard Aadhar card layouts

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/aadhar-face-match/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/aadhar-face-match/discussions)
- **Email**: your.email@example.com

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DeepFace](https://github.com/serengil/deepface) - Face recognition library
- [Streamlit](https://streamlit.io/) - Web app framework
- [OpenCV](https://opencv.org/) - Computer vision library
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR engine

## 🔮 Future Enhancements

- [ ] Multi-language OCR support
- [ ] Batch processing capabilities
- [ ] API endpoint creation
- [ ] Mobile app version
- [ ] Enhanced security features
- [ ] Support for multiple ID types
- [ ] Cloud deployment options
- [ ] Advanced analytics dashboard

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/aadhar-face-match)
![GitHub forks](https://img.shields.io/github/forks/yourusername/aadhar-face-match)
![GitHub issues](https://img.shields.io/github/issues/yourusername/aadhar-face-match)
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/aadhar-face-match)

---

<div align="center">
  
**Made with ❤️ for secure identity verification**

[⭐ Star this repo](https://github.com/yourusername/aadhar-face-match) • [🐛 Report Bug](https://github.com/yourusername/aadhar-face-match/issues) • [💡 Request Feature](https://github.com/yourusername/aadhar-face-match/issues)

</div>
