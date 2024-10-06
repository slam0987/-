from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/like-video', methods=['POST'])
def like_video():
    data = request.get_json()
    video_url = data.get('url')
    
    if not video_url:
        return jsonify({'message': 'No URL provided'}), 400
    
    try:
        # Initialize Selenium WebDriver (make sure you have chromedriver installed)
        driver = webdriver.Chrome()

        # Open the TikTok video
        driver.get(video_url)
        time.sleep(5)  # Let the page load

        # Example of locating the like button (you need to adjust this selector as needed)
        like_button = driver.find_element(By.XPATH, '//*[@data-e2e="like-icon"]')
        like_button.click()

        time.sleep(2)  # Wait to ensure the click is registered

        driver.quit()

        return jsonify({'message': 'Video liked successfully!'}), 200

    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
