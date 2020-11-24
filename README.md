# HighResNet

This repo contains the reproduced and adapted work of the paper HighRes-net: [*Recursive Fusion for Multi-Frame Super-Resolution of Satellite Imagery*].(https://arxiv.org/abs/2002.06460)

* **Network**: Contains all the source and configuration files needed to run HighRes-Net. These files have been modified from the original version to be adapted to work with the Virtual Moon Dataset.
* **Utils**: Contains the utility scripts that were created to automate several processes:
  - *lro_url_download.py*: Reads a list of urls from a CSV file and download the files of those links into a specified directory.
  - **database**: Contains all the scripts related to the Virtual Moon database creation:
    - *8to16.py*: Converts images from 8 bits to 16 bits.
    - *database.py*: Converts into greyscale the images inside every dataset in the directory and includes the clearance maps needed for the 
    - *lro_image_slicer*: Crops a selected LRO image into small slices after modifying the intensity 3 times to create a validation dataset of a total of 20 LR images for the network.
    - *monochannel.py*: Converts images from color (3 channels) to greyscale (1 channel).
    - *slicer.py*: Creates datasets containing one HR and 20 LR images per input

**Additional information**
* [Weights of the trained network (ESA + VM100, VM1000, ESA)](https://dropit.uni.lu/p/e20qcQPdlZWEi1b29bV1i6SbJjM+DlwlOUC4HtRnB0UdmwyPPDYnDIQX4hVGjPP1Nb)
* [Complete datasets used for training and validation (VM, LRO, ESA)](https://dropit.uni.lu/p/e2OIvj074+73paoXzQKXu0dq/XHDIhxQ/7hKdYMJNMnQOhpxQm5NsVo1DshtD4+3Cz)
* [Original repo](https://github.com/ElementAI/HighRes-net)
