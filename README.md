# Federated Learning Local System

Central node and a client node implementation to build a Federated Learning network in local.
The central node orchestrates the training of one or several models that is performed by the client nodes.
Each client node has its own dataset to train a local model, and sends the result of the training to the 
central node, that calculates the average of all the weights of the node clients models. That average 
will be used by the clients on the next rounds of trainings. The local data of each client node is never 
shared with any other node.

For the execution, we will be using a standard local installation from the command line.

### Datasets
For now, there are two models for training: MNIST and Chest X-Ray. For using the MNIST one you don't need to install anything else because
the client node downloads the dataset when it runs the training, but for the Chest X-Ray model you'll need a dataset to get it working.

The dataset was downloaded from https://data.mendeley.com/public-files/datasets/rscbjbr9sj/files/f12eaf6d-6023-432f-acc9-80c9d7393433/file_downloaded, 
As you can see, it is already attached in th directory datasets of this repo.
The final structure should be (other content in this folder will be ignored):

    chest_xray
         |----- train
         |        |----- NORMAL
         |        |----- PNEUMONIA
         |
         |----- test
                  |----- NORMAL
                  |----- PNEUMONIA

By default, the client node looks for it at GLOBAL_DATASETS/chest_xray. The variable GLOBAL_DATASETS is defined 
in the configuration file `client/config.py`. Everything is already well defined. In particular, for Chest X-Ray training, it'll expect a directory `chest_xray` in your dataset's directory with at least two folders `train` and `test` with x-ray images. 

    
### Command line local execution
You must install everything and running from the command line.
Python version must be 3.8, I haven't tested it with 3.9 or <3.8 versions.

The best way is to have an isolated environment using conda or similar environment managers.
If you use miniconda or conda, just do:

    conda create --name fedlearning python=3.8
    conda activate fedlearning

Once you're ready to install packages, do this:

     pip install torch torchvision
     pip install tensorflow
     pip install fastai
     pip install python-dotenv
     pip install aiohttp[speedups]
     pip install flask
    
#### Running the project   
##### Central node
That's very simple, just go to `federated-learning-network/server` and execute:

    flask run
    
It'll start a central node in `http://localhost:5000`. To see that's running well, open a browser and go to that URL.
You'll see the dashboard of the network.

##### Client nodes
Open a new console, or just do it in another computer which has access to the server.
Go to `federated-learning-network/client` and execute:

    export CLIENT_URL='http://localhost:5001'
    flask run --port 5001
    
Do that for every client, changing the listening port. You'll see some log traces telling the client 
has started and has registered in the network:

    Registering in server: http://127.0.0.1:5000
    Doing request http://127.0.0.1:5000/client
    Response received from registration: <Response [201]>
    Client registered successfully

If you refresh the central’s node dashboard you can see all the clients registered in the network.

### Training sessions
Once we have the central node and clients running properly and registered, just open the server dashboard and click on 
the _Launch training_ button.
This action will launch a training session between all the clients registered. You can see the progress of the training in each 
client's console. For example, for MNIST training you will see something like this in the client node console:

    Federated Learning config:
    --Learning Rate: 1.0
    --Epochs: 20
    --Batch size: 256
    
    Training started...
    Accuracy of model trained at epoch 1 : 0.9118
    Accuracy of model trained at epoch 2 : 0.9118
    Accuracy of model trained at epoch 3 : 0.9118
    Accuracy of model trained at epoch 4 : 0.9118
    Accuracy of model trained at epoch 5 : 0.8824
    Accuracy of model trained at epoch 6 : 0.8824
    Accuracy of model trained at epoch 7 : 0.9118
    Accuracy of model trained at epoch 8 : 0.9118
    Accuracy of model trained at epoch 9 : 0.9118
    Accuracy of model trained at epoch 10 : 0.9118
    Accuracy of model trained at epoch 11 : 0.9118
    Accuracy of model trained at epoch 12 : 0.9118
    Accuracy of model trained at epoch 13 : 0.9118
    Accuracy of model trained at epoch 14 : 0.9118
    Accuracy of model trained at epoch 15 : 0.9118
    Accuracy of model trained at epoch 16 : 0.9412
    Accuracy of model trained at epoch 17 : 0.9412
    Accuracy of model trained at epoch 18 : 0.9412
    Accuracy of model trained at epoch 19 : 0.9412
    Accuracy of model trained at epoch 20 : 0.9412
    Training finished...

You can do more training sessions afterwards and see how the model improves. 

## Customization
You can change some training parameters (epochs, batch size and learning rate) at:

      federated-learning-network/server/server.py start_training method

In the future it'll be possible to do it from the central node's dashboard.

## Known issues
There's no persistence implemented yet, so everytime you start servers & clients the model will be initialized with 
random values and must be trained from the beginning.

This is a very early version, so it has room for lots of improvements, so new features will be added.

