
# PostTechBot

Welcome to **PostTechBot**! This is a Python script designed to automate interactions on the [Post.tech](https://post.tech/) platform using Selenium and the ChatGPT API for generating tweets and replies. If you find this script useful, please consider giving it a star.

## Features

- **Automated Tweeting**: PostTechBot can create and send tweets on your behalf using the ChatGPT API.

- **Automated Replies**: It can also automatically reply to messages on the Post.tech platform using the ChatGPT API.

## Getting Started

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/PostTechBot.git
   ```

2. Install the required Python packages:

   ```shell
   pip install selenium
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment (skip this step if you didn't create a virtual environment):

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Set up your environment variables by creating a `.env` file in the project directory with the following content:

   ```env
   username=user1
   password=pass
   gpt=apikey
   ```

   Replace `user1`, `pass`, and `apikey` with your actual Post.tech username, password, and ChatGPT API key.

6. Install the required Firefox WebDriver:

   - Download the latest GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases).
   - Add the GeckoDriver executable to your system's PATH.

7. Configure your ChatGPT API credentials:

   - Obtain your API key from the OpenAI platform.

   - Set your API key as an environment variable:

     ```shell
     export OPENAI_API_KEY=your_api_key
     ```

8. Run the script:

   ```shell
   python posttechbot.py
   ```

   This will start the automation process.

## Configuration

- You can customize the tweet and reply messages by modifying the `tweet_message` and `reply_message` variables in the script.

## Dependencies

- Selenium: [https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy automating your interactions on Post.tech with PostTechBot, powered by the ChatGPT API! If you encounter any issues or have suggestions for improvements, please open an issue on this repository. Thank you for using PostTechBot! 🚀
