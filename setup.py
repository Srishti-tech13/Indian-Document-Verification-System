from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="aadhar-face-match",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered Aadhar face matching and verification system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aadhar-face-match",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/aadhar-face-match/issues",
        "Source Code": "https://github.com/yourusername/aadhar-face-match",
        "Documentation": "https://github.com/yourusername/aadhar-face-match#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Streamlit",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "performance": [
            "mediapipe>=0.10.0",
            "dlib>=19.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "aadhar-face-match=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "face-recognition",
        "identity-verification", 
        "aadhar",
        "ocr",
        "computer-vision",
        "ai",
        "streamlit",
        "deepface",
        "opencv",
        "tesseract",
    ],
)
