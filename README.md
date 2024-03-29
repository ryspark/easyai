
# EasyAI

EasyAI (`easyai`) is a small wrapper API for Keras, written for use by CSII AI at Millburn High School. It simplifies Keras so that a person with little programming experience and machine learning knowledge can use it. Users should use this API as a springboard from which they can start coding using advanced and capable tools. EasyAI is centered around neural network algorithms  due to their recent prevalence and popularity.

EasyAI was created as a teaching library in order to minimize code frustration. In this case, code is just the means of implementing concepts already learned-- it should be the easy part. While this attitude towards code may (should) change in the future, this style of learning will allow for users to learn with minimal programming difficulties.

Author: Ryan Park (22parkr@millburn.org)

## Core principles

* **Ease of use.** EasyAI was created for a very specific target audience: those who are just beginning their 
machine learning (and coding) journeys. It is meant to emulate pseudocode as much as possible. Because of its overly simple design, many features are not customizable. However, since the purpose of this API is to provide a simple introduction to programming AI, a lack of functionality is acceptable.

* **Ease of transition.** Ultimately, EasyAI is just an introduction to AI programming. Hopefully, EasyAI users 
will move on to more advanced and capable machine learning libraries. Since EasyAI is built off of Keras, users will
probably find it easiest to transition to Keras from EasyAI.

## Using EasyAI

As previously stated, EasyAI focuses on usability and should be simple to use _if you have some understanding of machine learning concepts_. Since this library is meant to be a teaching library, using it does require a bit of background knowledge.

The most basic EasyAI model is the `NN` object.

```python

from easyai import NN
from easyai.layers import Input, FC

net = NN(Input(input_shape=100), FC(num_neurons=200), FC(num_neurons=5))

```

You can add and remove layers using the `add_layer` and `rm_layer` functions.

```python

net.add_layer(FC(num_neurons=200), position=1)

net.rm_layer(position=1)

```

Training is as easy as `neural_network.train()`.

```python

x_train = "your training examples here"
y_train = "your training labels here"

neural_network.train(x_train, y_train, epochs=10)

```

Neural networks are cool, but the real fun is in their applications. Run `easyai.applications` to see neural networks in action!

```python

from easyai.applications import SlowNST
from easyai.support.load import load_imgs

content_img = load_imgs("your content image here")
style_img = load_imgs("your style image here")

style_transfer_net = SlowNST()
style_transfer_net.train(content_img, style_img)

# runs neural style transfer, which combines the style of an image (e.g., Van Gogh's Starry Night)
# with the content of another one (e.g., a dog) to create a new, unique image (Starry Dog!)

```

Need help getting started? Run `easyai.support.examples`.

```python

from easyai.support.examples import MNIST

MNIST.mlp()

# creates and runs a neural network on the digit classifying dataset, MNIST

```

## Downloading EasyAI

EasyAI is a Python package and can therefore be installed with Python's installation tool, `pip`. In order to install EasyAI, you must have Python >= 3.6.0.

Mac users: you may need to run the Python certificate script before using EasyAI. In order to do so, locate the `Python 3.x` folder in your `Applications` folder in Finder and run `Install Certificate.command` and `Update Shell Profile.command`.

### Installation

If you have a CUDA-capable GPU and CUDA software (if you don't know what that means, you don't have it), install EasyAI using this command: `pip3 install git+https://github.com/orangese/easyai.git#egg=easyai[gpu]`.

Otherwise, use: `pip3 install git+https://github.com/orangese/easyai.git#egg=easyai[cpu]`.

### Upgrade

If you have a CUDA-capable GPU and CUDA software, upgrade EasyAI by using the below command:  
`pip3 install --upgrade git+https://github.com/orangese/easyai.git#egg=easyai[gpu]`.

Otherwise, use: `pip3 install --upgrade git+https://github.com/orangese/easyai.git#egg=easyai[cpu]`.
