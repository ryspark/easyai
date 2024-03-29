"""

"easyai.support.examples.py"

Program that implements easyai.support.datasets.datasets and easyai.core in examples like MNIST.

"""

from easyai.layers import *
from easyai.support.datasets import *
from easyai.support.models import *


# CLASSES
class MNIST(Static):
    """
    Contains examples using MNIST and Fashion-MNIST datasets.
    """

    @staticmethod
    def mlp(version: str = "digits") -> NN:
        """
        MNIST multi-layer perceptron network.

        :param version: "digits" for MNIST dataset or "fashion" for Fashion-MNIST dataset.
        :return: trained NN model.
        """
        (x_train, y_train), (x_test, y_test) = Builtins.load_mnist(version=version, mode="mlp")
        print("Loaded MNIST data\n")

        plt.imshow(x_train[0].reshape(28, 28), cmap="gray")
        plt.title("Label: {}".format(np.argmax(y_train[0])))
        plt.axis("off")
        plt.show()

        mlp = NN(Input(784), FC(100), FC(50), FC(10, actv="softmax"), loss="categorical_crossentropy")
        mlp.summary()

        mlp.train(x_train, y_train, lr=3.0, epochs=1)
        mlp.evaluate(x_test, y_test)

        return mlp

    @staticmethod
    def cnn(version: str = "digits") -> NN:
        """
        MNIST convolutional network.

        :param version: "digits" for MNIST dataset or "fashion" for Fashion-MNIST dataset.
        :return: trained NN model.
        """
        (x_train, y_train), (x_test, y_test) = Builtins.load_mnist(version=version, mode="conv")
        print("Loaded MNIST data")

        labels = ["t_shirt_top", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "bag",
                  "ankle_boots"]
        if version == "digits":
            labels = list(range(10))
        plt.imshow(x_train[0].reshape(*x_train[0].shape[:-1]), cmap="gray")
        plt.title("Label: {}".format(labels[int(np.argmax(y_train[0]))]))
        plt.axis("off")
        plt.show()

        conv_nn = NN(Input(28, 28), Conv((5, 5), 20), Pooling(2, 2), FC(100), FC(10, actv="softmax"),
                     loss="categorical_crossentropy")
        conv_nn.summary()

        conv_nn.train(x_train, y_train, lr=0.1, epochs=60)
        conv_nn.evaluate(x_test, y_test)

        return conv_nn


class LendingClub(Static):
    """
    Contains examples using LendingClub credit rating dataset.
    """

    @staticmethod
    def mlp() -> NN:
        """
        LendingClub MLP.

        :return: trained NN model.
        """
        (x_train, y_train), (x_test, y_test) = Extras.load_lending_club()
        print("Loaded LendingClub data")

        mlp = NN(Input(9), FC(200, actv="relu"), FC(200, actv="relu"), FC(7, actv="softmax"),
                 loss="categorical_crossentropy")
        mlp.summary()

        mlp.train(x_train, y_train, lr=0.01, epochs=50)
        mlp.evaluate(x_test, y_test)

        return mlp


class Art(Static):
    """
    Art generated with AI.
    """

    @staticmethod
    def slow_nst(content_name: str = None, style_name: str = None, save_path: str = None) -> np.ndarray:
        """
        (Slow) neural style transfer with art and photographs.

        :param content_name: name of content image from dataset. Default is a random image from built-in datasets.
        :param style_name: name of style image from dataset. Default is a random image from built-in datasets.
        :param save_path: path to which to save final result. Default is None.
        :return: final image.
        """
        images = Extras.load_nst_imgs()
        print("Loaded NST images")

        content_name, content_img = Helpers.get_img(content_name, "content", images)
        style_name, style_img = Helpers.get_img(style_name, "style", images)

        print("Using content image \"{0}\" and style image \"{1}\"".format(content_name, style_name))

        model = SlowNST("vgg19")

        final_img = model.train(content_img, style_img, epochs=25, init_noise=0.6)

        SlowNST.display_img(final_img, "Final result", model.generated.shape[1:])

        if save_path is not None:
            full_save_path = save_path + "/{0}_{1}.jpg".format(content_name, style_name)
            keras.preprocessing.image.save_img(full_save_path, final_img)
            print("Saved image at \"{0}\"".format(full_save_path))

        return final_img

    @staticmethod
    def fast_nst(content_name: str = None, style_net: str = None, save_path: str = None) -> np.ndarray:
        """
        (Fast) neural style transfer with arts and photographs, using pretrained models.

        :param content_name: name of content image. Default is None.
        :param style_net: name of style network. Default is None.
        :param save_path: path to which to save the final result. Default is None.
        :return: final image.
        """
        images = Extras.load_nst_imgs()
        print("Loaded NST images")

        content_name, content_img = Helpers.get_img(content_name, "content", images)

        if style_net is None:
            model = FastNSTModels.random_net()
        else:
            model = FastNSTModels.load_net(style_net)

        print("Using content image \"{0}\" and style net trained on  \"{1}\"".format(content_name, style_net))

        final_img = model.run_nst(content_img)

        SlowNST.display_img(final_img, "Final result")

        if save_path is not None:
            full_save_path = save_path + "/{0}_{1}.jpg".format(content_img, style_net)
            keras.preprocessing.image.save_img(full_save_path, final_img)
            print("Saved image at \"{0}\"".format(full_save_path))

        return final_img


if __name__ == "__main__":
    # filename = "test.png"
    # Unsupported.draw("test.png")
    # activation = Unsupported.getActivation(filename)
    # Unsupported.display_image(activation)
    MNIST.mlp("digits")

    raise ValueError()
    nst = SlowNST()
    nst.train(Image.open("/home/ryan/test.jpg"), Image.open("/home/ryan/style.jpg"), 25)

    from easyai.support.load import load_imgs
    from easyai.support.datasets import NST

    nst = SlowNST()
    SlowNST.HYPERPARAMS["coef_s"] = 1e5
    for link in list(NST.style.keys()):
        final_img = nst.train(load_imgs("/Users/ryan/Downloads/test.jpg"),
                              # load_imgs(NST.style[link]), epochs = 25, verbose = True)
                              load_imgs("/Users/ryan/Downloads/drive-download-20190820T070132Z-001/"
                                        "wheatfields_with_crows_van_gogh.jpg"), epochs=25, verbose=True)

        keras.preprocessing.image.save_img("/Users/ryan/Pictures/nst_generated/genji_{0}.jpg".format(link), final_img)
