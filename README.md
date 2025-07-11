"# Blur"

\# Technical Specification (Spec): Logo Blur Web Service



\## 🧩 Project Overview



The goal is to build a web service that allows users to upload an image, automatically detects logos within it, and returns the same image with all logos blurred.



---



\## 🎯 Objectives



\- Build an API endpoint that accepts an image upload.

\- Use a deep learning model to detect logos.

\- Apply Gaussian blur to detected logo regions.

\- Return the processed image to the client.

\- (Optional later) Provide batch upload and API keys.



---



\## 📐 Functional Requirements



\### Endpoint



\- \*\*URL:\*\* `/blur`

\- \*\*Method:\*\* `POST`

\- \*\*Request:\*\*

&nbsp; - `multipart/form-data`

&nbsp; - Field: `file` — image (JPG/PNG)

\- \*\*Response:\*\*

&nbsp; - `200 OK`

&nbsp; - Content-Type: `image/png`

&nbsp; - Image with logos blurred



---



\## ⚙️ Technology Stack



\### Backend



\- \*\*FastAPI\*\* — web server \& routing

\- \*\*Pillow / OpenCV\*\* — image processing and blurring

\- \*\*Ultralytics YOLOv8\*\* — logo detection model

\- \*\*Python 3.10+\*\*



\### Optional tools



\- \*\*Docker\*\* — containerization (optional)

\- \*\*Gradio / Streamlit\*\* — for interactive testing (optional)

\- \*\*Torch / CUDA\*\* — GPU acceleration (optional)



---



\## 🔄 Workflow



\### Step 1: Set Up Project



\- Create FastAPI project structure

\- Install dependencies

\- Write minimal working API



\### Step 2: Load Logo Detection Model



\- Use pretrained YOLOv8 model

\- Optionally fine-tune on a logo dataset (e.g. Open Logos Dataset)



\### Step 3: Detect Logos on Uploaded Image



\- Convert uploaded image to NumPy array

\- Run model inference

\- Extract bounding boxes for detected logos



\### Step 4: Apply Gaussian Blur



\- For each bounding box:

&nbsp; - Extract region of interest

&nbsp; - Apply OpenCV Gaussian blur

&nbsp; - Replace original region



\### Step 5: Return Image



\- Convert image back to PNG

\- Stream response to client



---



\## 🗂 Directory Structure





