# Custom Image Classification API
This is a Custom Image Classification API built from scratch. The Custom Neural network is built with **TensorFlow v1**.

Don't forget to :star: this repo :smiley:

# Table of Contents :notebook:
* [Installation](#installation-arrow_down)
* [Usage](#usage-gear)
	* [Download training images for your task](#download-training-images-for-your-task)
	* [Train Neural Network](#train-neural-network)
	* [Run Prediction from browser](#run-prediction-from-browser)
* [Support](#support-sparkles)
* [Author](#author-sunglasses)


## Installation :arrow_down:
* Use this command to clone this repository: `https://github.com/siddheshgunjal/TF-Image-Classifier-API.git`
* Create environment with your environ management tool, [Virtualenv][virtualenv] or [Conda][conda-env]
* Install packages with pip using `pip install -r requirements.txt`

## Usage :gear:
### Download training images for your task
* Download chrome driver for your system from this link: [chromedriver][chrome-driver]
* Open `img_scrapper.py` and add path to chromedriver at `line 11` or just uncomment the path for already included chromedriver for linux/windows.
* Run scrapper with `python img_scrapper.py` in terminal.
* Enter the search term (For example: Tiger)
* Enter the number of images to download (For example: 50)
* The script will then launch Google Chrome and start scrapping process. Wait till the scrapping process is complete.
* You can find the all the scrapped images in `./Data/Train_data/search_term`
* You can download as many images as you want for as many classes.

### Train Neural Network
* Start training with `python train.py`. Default epochs to train are set to 100. you can change it as per your need from `line 48` in `train.py`
* You can also visualize training progress with tensorboard using `tensorboard --logdir Checkpoints/logs`
* After training finishes, you'll get 2 files
	* `model.json`: Neural Network architecture
	* `weights.h5`: Updated weights of neural network after training

### Run Prediction from browser
* Run Flask application with `python app.py`. This will start our application at `localhost:8108`
* Visit this URL in browser and you should see the message, **Image Classification API is running**. This verifies that our API is running at server side.
* Go to `localhost:8108/classification` for prediction task:
![classification page](./screenshots/1.png?raw=true)
* Drag your image in the drop zone or upload it and click **Run Prediction**, which will then run the prediction and show you the result with below screen:
![classification-result page](./screenshots/2.png?raw=true)
![classification-result page](./screenshots/3.png?raw=true)

Your Custom Image classification API is ready!

##  Support :sparkles:
If you get stuck, we’re here to help. The following are the best ways to get assistance working through your issue:

* Use our [Github Issue Tracker][gh-issues] for reporting bugs or requesting features.
Contribution are the best way to keep this repo amazing :muscle:
* If you want to contribute please refer [Contributor's Guide][gh-contrib] for how to contribute in a helpful and collaborative way :innocent:

## Author :sunglasses:
* Siddhesh Gunjal
  * [Website][portfolio]
  * [GitHub][github]
  * [LinkedIn][linkedin]


<!-- Markdown link -->
[virtualenv]: https://docs.python.org/3/library/venv.html
[conda-env]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
[chrome-driver]: https://googlechromelabs.github.io/chrome-for-testing/
[gh-issues]: https://github.com/siddheshgunjal/TF-Image-Classifier-API/issues
[gh-contrib]: https://github.com/siddheshgunjal/TF-Image-Classifier-API/blob/main/CONTRIBUTING.md
[portfolio]: https://siddheshgunjal.github.io
[github]: https://github.com/siddheshgunjal
[linkedin]: https://linkedin.com/in/siddheshgunjal