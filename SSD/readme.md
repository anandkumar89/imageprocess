# Single Shot Multibox Detector

SSD is based on a modified VGG-16 pre-trained on the Imagenet Data. The following modifications have been made to the base network ( VGG16 ).
1. ``pool5`` was changed from 2x2 (stride 2) to 3x3 (stride 1)
2. ``fc5`` and ``fc7`` layers were converted to convolutional layers and **subsampled**
3. *atrous convolution* was used in ``fc6``
4. ``fc8`` and all of the dropout layers were removed
![alt VGG-16 architecture](img/vgg16.png "VGG 16 architecture")
Below is SSD architecture
![alt Single Shot Multibox architecture](img/ssd_network.png "SSD architecture")
