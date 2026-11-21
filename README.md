# 🎬 Python YouTube Video Downloader

A simple and lightweight Python application, that allows users to download YouTube videos in their best quality available directly using a video URL. Built with Python, FFmpeg and the powerful `yt-dlp` library.

## 📌 About the Project

The **Python YouTube Video Downloader** is a Python-based project designed to make downloading YouTube videos simple and straightforward.

The program prompts users to enter a YouTube video URL and automatically downloads the video using the best available video and audio formats.

🎯 This project demonstrates Python input handling, external library integration, and video downloading automation.

## ✨ Features

- 🔗 **URL Input:** Allows users to enter their desired YouTube video URL.
- 🎥 **High-Quality Downloads:** Selects the best available video and audio formats.
- 🔊 **Audio and Video:** Downloads video with its corresponding audio.
- ⚡ **Simple Execution:** Easy-to-use command-line interface.
- 🐍 **Python Powered:** Built using Python and the `yt-dlp` library.
- 📥 **Automated Downloading:** Starts the download process automatically after receiving a URL.

## 🛠️ Technologies Used

- 🐍 **Python 3** – Main programming language.
- 📦 **yt-dlp** – Python library for downloading video and audio.
- 💻 **Command Line Interface (CLI)** – User interaction.

## 📂 Project Structure

```text
Python-Youtube-Video-Downloader/
│
├── Download.py
├── README.md
└── LICENSE
```

## ⚙️ Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

You will need:

Python & Git installed on your computer. You might also need FFmpeg an (open-source command-line tool used to process, convert, and manipulate audio and video files). You can download it using PowerShell or a Command Prompt, using this command.

```bash
winget install Gyan.FFmpeg
```

A code editor such as Visual Studio Code.

## Installation

### 1️⃣ Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/BJomo001/Python-Youtube-Video-Downloader.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Python-Youtube-Video-Downloader
```

### 3️⃣ Install Dependencies

Install the required Python library:

```bash
pip install yt-dlp
```

Alternatively:

```bash
python -m pip install yt-dlp
```

### 4️⃣ Run the Application

Execute the following command:

```bash
python Download.py
```

## 💻 How It Works

1. 🚀 The program starts and prompts the user to enter a YouTube video URL.
2. 🔗 The user provides the URL of the desired video.
3. 🔍 The `yt-dlp` library processes the supplied URL.
4. 🎥 The program selects the best available video and audio formats.
5. 📥 The download begins automatically.
6. ✅ Once completed, the downloaded file is saved in the current working directory, subject to the downloader's output settings.

## 📝 Example Usage

**Run the program:**

```bash
python Download.py
```

**Example interaction:**

```text
Please enter your desired YouTube video URL: https://www.youtube.com/watch?v=VIDEO_ID

[YouTube] Extracting video information...
[download] Downloading video...
[download] 100% of video downloaded

Download completed!
```

*Note: This is illustrative output. Actual messages depend on the video and `yt-dlp` version.*

## 📚 Learning Objectives

Through this project, you will explore:

- 🐍 Python programming fundamentals.
- ⌨️ User input and handling.
- 📦 Installing and importing external Python libraries.
- 🔗 Working with URLs.
- 🎬 Video downloading automation.
- ⚙️ Using third-party Python packages.
- 🧩 Integrating external libraries into Python applications.

## ⚠️ Important Notes

- 📌 Ensure that Python 3 is installed on your computer.
- 🌐 An active internet connection is required.
- 📦 Make sure `yt-dlp` is installed before running the application.
- 🎞️ Some formats may require FFmpeg for merging separate video and audio streams.
- 💾 Downloaded files are saved according to the downloader's output settings.

## 🛡️ Legal and Ethical Use

This project is intended for educational purposes and authorized personal use.

Users are responsible for ensuring that their downloads comply with applicable copyright laws, YouTube's Terms of Service, and the permissions of the content owners.

Only download content that you own, have permission to download, or are otherwise legally permitted to access.

## 🚀 Future Improvements

Potential enhancements include:

- 📊 Adding a download progress indicator.
- 🎚️ Allowing users to select video quality and resolution.
- 🎵 Supporting audio-only downloads.
- 📁 Allowing users to choose a download location.
- 📋 Displaying video title, duration, and file size before downloading.
- 🖥️ Developing a graphical user interface (GUI).
- 📥 Supporting playlist downloads.

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!

To contribute:

Fork this repository.

Create a new branch for your changes.

Commit your improvements.

Push your branch to GitHub.

Open a pull request describing your changes.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

## 👨‍💻 Author

**BJomo001**

🐙 GitHub: [@BJomo001](https://github.com/BJomo001)

---

⭐ If you find this project useful, consider giving the repository a star!

🎬 *Code. Download. Explore.*

