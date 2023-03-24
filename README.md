# Large-scale study on domain transferability of artificial intelligence models for diagnosis of chest radiographs


Overview
------

* This is the official repository of the study **Building Bridges, Not Walls – A Comprehensive Analysis of Domain Transferability Using Deep-Learning-Based Interpretation of Chest Radiographs**.



Introduction
------
In the context of AI-based interpretation of chest radiographs, we perform a large-scale analysis of domain transferability on more than 800,000 chest x-rays and assess the contributions of network architecture, dataset characteristics, and imaging findings.


### Prerequisites

The software is developed in **Python 3.10**. For the deep learning, the **PyTorch 1.13** framework is used.



Main Python modules required for the software can be installed from ./requirements in three stages:

1. Create a Python3 environment by installing the conda `environment.yml` file:

```
$ conda env create -f environment.yml
$ source activate domainchestx
```


2. Install the remaining dependencies from `requirements.txt`.


**Note:** These might take a few minutes.


Code structure
---

Our source code for domain transfer as well as training and evaluation of the deep neural networks, image analysis and preprocessing, and data augmentation are available here.

1. Everything can be run from *./main_2D_chestx_domain.py*. 
* The data preprocessing parameters, directories, hyper-parameters, and model parameters can be modified from *./configs/config.yaml*.
* Also, you should first choose an `experiment` name (if you are starting a new experiment) for training, in which all the evaluation and loss value statistics, tensorboard events, and model & checkpoints will be stored. Furthermore, a `config.yaml` file will be created for each experiment storing all the information needed.
* For testing, just load the experiment which its model you need.

2. The rest of the files:
* *./data/* directory contains all the data preprocessing, augmentation, and loading files.
* *./Train_Valid_chestx_domain.py* contains the training and validation processes.
* *./Prediction_chestx_domain.py* all the prediction and testing processes.


Citation
---

### In case you use this repository, please cite the original work:

S. Tayebi Arasteh, F. Khader, M. Lotfinia, G. Mueller-Franzes, G. Kaissis, A. Ziller, J.N. Kather, P. Isfort, C. Kuhl, D. Truhn, S. Nebelung. "*Building Bridges, Not Walls – A Comprehensive Analysis of Domain Transferability Using Deep-Learning-Based Interpretation of Chest Radiographs*". 2023.


### BibTex

    @article {chestxdomain,
      author = {Tayebi Arasteh, Soroosh and Khader, Firas and Lotfinia, Mahshad and Mueller-Franzes, Gustav and Kaissis, Georgios and Ziller, Alexander and Kather, Jakob Nikolas and Isfort, Peter and Kuhl, Christiane and Truhn, Daniel and Nebelung, Sven},
      title = {Building Bridges, Not Walls – A Comprehensive Analysis of Domain Transferability Using Deep-Learning-Based Interpretation of Chest Radiographs},
      year = {2023}
    }


