# Spam Detector ( Gemini + LangChain )

This is a Streamlit application that uses Google's Gemini model via LangChain to classify messages as Spam, Not Spam, or Uncertain.

## Features

*   **Single Message Classification**: Paste any message to get a detailed classification.
*   **Batch CSV Upload**: Upload a CSV file with messages for bulk classification. Take a reference from `sample_messages.csv` file that is available in the repository.
*   **Detailed Analysis**: For each message, it provides:
    *   A clear `label` (Spam, Not Spam, Uncertain).
    *   A `risk_score` from 0 to 100.
    *   `reasons` for the classification.
    *   A list of `red_flags` found in the message.
    *   A `suggested_action`.

## Installation & Setup

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

*   Python 3.8+
*   An active Google Gemini API Key. You can get one from Google AI Studio.

### 2. Install Dependencies

It is recommended to use a virtual environment. Once your environment is set up, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of the project. Add your Gemini API key to this file:

```
GEMINI_API_KEY="your_google_api_key_here"
```

The application reads this key to authenticate with the Gemini API.

## How to Run

To start the Streamlit application, run the following command in your terminal from the project root:

```bash
streamlit run app.py
```

Your browser should open a new tab with the running application.
