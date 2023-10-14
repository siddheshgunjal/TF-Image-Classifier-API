# Custom Image Classification API
This is a Custom Image Classification API built from scratch. The Custom Neural network is built with **TensorFlow v1**.

Don't forget to :star: this repo!

# Table of Contents :notebook:
* [Installation](#installation-arrow_down)
* [Usage](#usage-gear)
	* [Download training images for your task](#download-training-images-for-your-task)
	* [Train Neural Network](#train-neural-network)
	* [Run Prediction from browser](#run-prediction-from-browser)
* [Deploy on AWS with Docker](#deploy-on-aws-with-docker-rocket) 
* [Support](#support-sparkles)
* [Author](#author-sunglasses)


## Installation :arrow_down:
* Use this command to clone this repository: `https://github.com/siddheshgunjal/TF-Image-Classifier-API.git`
* Create environment with your environ management tool, [Virtualenv][virtualenv] or [Conda][conda-env]
* Install packages with pip using `pip install -r requirements.txt`

## Usage :gear:
### Download training images for your task
To download training images for your classes you can utilise the python script from this [gist][img-scrape-gist]. Procedure to use it is as below:
* Download chrome driver for your system from this link: [chromedriver][chrome-driver]
* Open python script and add path to chromedriver at `line 11` or just uncomment the path for already included chromedriver for linux/windows.
* Run scrapper with `python img_scrapper.py` in terminal.
* Enter the search term (For example: Tiger)
* Enter the number of images to download (For example: 50)
* The script will then launch Google Chrome and start scrapping process. Wait till the scrapping process is complete.
* You can find the all the scrapped images in `./Data/Train_data/search_term`
* You can download as many images as you want for as many classes.

### Train Neural Network
* Put all your training data with folder for each class in `./Data/Train_data/class_name`
* Start training with `python train.py`. Default epochs to train are set to 100. you can change it as per your need from `line 48` in `train.py`
* You can also visualize training progress with tensorboard using `tensorboard --logdir Checkpoints/logs`
* After training finishes, you'll get 2 files
	* `model.json`: Neural Network architecture
	* `weights.h5`: Updated weights of neural network after training

### Run Prediction from browser
#### 1. Run application with Flask's in-built server: 
Use `python app.py` in terminal. This will start our application at `localhost:8188`
### OR
#### 2. Run application with Gunicorn server:
Use `gunicorn -b :8188 -c gunicorn.conf.py app:app` in terminal. This will start our application at `localhost:8188`

Visit this URL in browser and you should see the message, **Image Classification API is running**. This verifies that our API is running at server side.
Go to `localhost:8188/classification` for prediction task:
![classification page](./screenshots/1.png?raw=true)
Drag your image in the drop zone or upload it and click **Run Prediction**, which will then run the prediction and show you the result with below screen:
![classification-result page](./screenshots/2.png?raw=true)
![classification-result page](./screenshots/3.png?raw=true)

Your Custom Image classification API is ready!

## Deploy on AWS with Docker :rocket:
Please Refer [AWS docker setup guide][gh-aws-docker] to deploy this application on AWS EC2 instance with docker.

##  Support :sparkles:
If you get stuck, we’re here to help. The following are the best ways to get assistance working through your issue:

* Use our [Github Issue Tracker][gh-issues] for reporting bugs or requesting features.
Contribution are the best way to keep this repo amazing :muscle:
* If you want to contribute please refer [Contributor's Guide][gh-contrib] for how to contribute in a helpful and collaborative way :innocent:

## Author :sunglasses:
### Siddhesh Gunjal
  * [Website][portfolio]
  * [LinkedIn][linkedin]
  * [GitHub][github]

<!-- Markdown link -->
[virtualenv]: https://docs.python.org/3/library/venv.html
[conda-env]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
[img-scrape-gist]: https://gist.github.com/siddheshgunjal/ff7c2b2ee0d98b66245e1efee258a6fa
[chrome-driver]: https://googlechromelabs.github.io/chrome-for-testing/
[gh-issues]: https://github.com/siddheshgunjal/TF-Image-Classifier-API/issues
[gh-aws-docker]: https://github.com/siddheshgunjal/TF-Image-Classifier-API/blob/main/AWS_docker_setup.md
[gh-contrib]: https://github.com/siddheshgunjal/TF-Image-Classifier-API/blob/main/CONTRIBUTING.md
[portfolio]: https://siddheshgunjal.github.io
[github]: https://github.com/siddheshgunjal
[linkedin]: https://linkedin.com/in/siddheshgunjal