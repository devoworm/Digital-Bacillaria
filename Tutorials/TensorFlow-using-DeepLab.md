## TensorFlow Implementation using Pre-trained Models (MobileNet/DeepNet v3)
Ujjwal Singh<sup>1,2</sup>, Asmit Singh<sup>1,2</sup>, Bradly Alicea<sup>2,3</sup> 

Version 1.0, [CC-BY-SA-4.0 License](https://github.com/devoworm/Licensing-DRM/blob/master/CC-BY-SA-4.0%20License.md)

<sup>1</sup> IIT Delhi, <sup>2</sup> OpenWorm Foundation, <sup>2</sup> Orthogonal Research and Education Laboratory

### INTRODUCTION
In order to implement a deep network analysis, you will need to do the following:

1. Create your dataset  
  
2. Train your model  
  
3. Test your models  
  
Creating your dataset will depend on your domain of interest. You need to have a sizable sample (20-200 images) and perhaps use methods such as data augmentation [1] to improve the performance of your model.

We will also go through a brief explaination of how to train your model using TensorFlow and Deeplab. You can use many other models as well, these steps are going to the same for almost all the models. Let us discuss the above steps in detail:

### 1. MAKE YOUR DATASET
Creating a suitable dataset is the most essential aspect of TensorFlow implementation. You should keep in mind that your dataset must be accurate and should cover a large amount of variation relted to your phenomenon of interest.

In the case of _Bacillaria_ model training, we have split the microscopy data (movies) into a collection of image files. We have included both dark and light backgrounds to make our dataset more enriched and so that it covers a variety of cases.

Once your dataset is ready, you have to somehow convert it into a language that your machine can understand. It doesn’t know initially what we want from these images.

For this case, there are several options available:

1. Unsupervised segmentation of images using Watershed or Canny Edge detection can be found useful in many cases which are general and not too detailed images. In our case, it does not provide us desirable results.  
  
2. You can also label your dataset manually. Manual annotation will allow you to extract information specific to your images. It also helps to create more accurate labels and features for your dataset.  
  
There are many image annotation tools available on Github offered by different developers, you can use any of them according to your choice.

### 2. TRAIN YOUR MODEL
Once you have settled on your input dataset, you need to train your model using this dataset. In this case, a trained model is equivalent to a Neural or Deep Learning Network weighted to match the features of your data.

Once you have labeled the images with help of a tool, you have noticed that your records are stored in _XML_ format (in most cases, some tools store it directly in the _csv_ format). We need to convert these records from _XML_ format to _csv_ format, as this will help us in further steps that we encounter later in this tutorial.

```python

    def main():
	    for directory in ['train','test']:
		    image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
		    xml_df = xml_to_csv(image_path)
		    xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
		print ('Successfully converted xml to csv.')

```				

This code defines two folders: train and test, and also converts the image output from _XML_ to _csv_. 

Now you have a csv file for both the training and testing data. Our next step is to generate our TensorFlow records from these _csv_ files. To proceed, you will need to install a few libraries

```python

    from_future_import division
    from_future_import print function
    from_future_import absolute_import

    import os
    import io
    import pandas as pd
    import tensorflow as tf

    from PIL import Image
    from object_detection.utils import dataset_util
    from collections import namedtuple, OrderedDict

```	

Now we can create a template. The first step is to define your _csv_ input path where this script can pick up the _csv_ files. These are the files which we created in the previous step. You also need to define your output path, or where you want to save the TensorFlow records which will be created during script execution. Then, you need to define a function which returns a value of "1" whenever _row_label_ matches to your label name. In this context, label is the column name assigned during annotation.

Next, define a _create_tf_ function that will eventually convert these csv files into TensorFlow records. For this function, you have to extract all the information which is present in the _csv_ file. You can do this by following the below function.

```python

    def create_tf_example(group, path):
	    with tf.gfile.GFile(os.path.jin(path, '{}'.format(group.filename)), 'rb') as fid:
		    encoded_jpg = fid.red()
	    encoded_jpg_io = io.BytesIO(encoded_jpg)
	    image = Image.open(encoded_jpg_io)
	    width, height = image.size
	
	   finename = group.filename.encode('utf8')
	   image_format = b'jpg'
	   xmins = []
	   xmaxs = []
	   ymins = []
	   ymaxs = []
	   classes_text = []
	   classes = []
	
	    for index, row in group.object.iterrows():
		    xmins.append(row['xmin'] / width)
		    xmaxs.append(row['xmax'] / width)
		    ymins.append(row['ymin'] / height)
		    ymaxs.append(row['ymax'] / height)
		    classes_text.append(row['class'].encode('utf8'))
		    classes_append(class_text_to_int(row['class']))
		
	    tf_example = tf.train.Example(features=tf.train.Features(feature={
		    'image/height' : dataset_util.int64_feature(height),
		    'image/width' : dataset_util.int64_feature(width),
		    'image/filename' : dataset_util.bytes_feature(filename),
		    'image/source_id' : dataset_util.bytes_feature(source_id),
		    'image/encoded' : dataset_util.bytes_feature(encoded_jpg),
		    'image/format' : dataset_util.bytes_feature(image_format),
		    'image/object/bbox/xmin' : dataset_util.float_list_feature(xmins),
		    'image/object/bbox/xmax' : dataset_util.float_list_feature(xmaxs),
		    'image/object/bbox/ymin' : dataset_util.float_list_feature(ymins),
		    'image/object/bbox/ymax' : dataset_util.float_list_feature(ymaxs),
		    'image/object/class/text' : dataset_util.bytes_list_feature(classes_text),
		    'image/object/class/label' : dataset_util.int64_list_feature(classes),
	   }))
	   return tf_example

```
Change this function according to the features you want to define. After this just wrap up your python file by defining main function according to your need, your TensorFlow records are ready. You can find the code of this script in our GitHub repository. After all, this done, we are left with our data, files of _XML_ records, _CSV_ records, and _TF_ records. We now need a _TF_ record file to do the learning process.

Here, we have two options. We can use a pre-trained model, and then use transfer learning to learn a new object, or we could learn new objects entirely from scratch. The benefit of transfer learning is that training can be much quicker, and the required data that you might need is much less. For this reason, we are going to be doing transfer learning here.

### CHOOSING A PRE-TRAINED MODEL
There are a number of pre-trained models available within the [TensorFlow library](https://github.com/tensorflow/models). We recommend either [DeepLabv3](https://towardsdatascience.com/deeplabv3-c5c749322ffa) or [MobileNet](https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html). MobileNet is particularly suitable for beginners and users with limited computational power. Below are the files required to run MobileNet.

Download MobileNet (pre-trained TensorFlow model for object detection)   [tar file link](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz)
  
Download configuration file for MobileNet   [link](https://raw.githubusercontent.com/tensorflow/models/master/object_detection/samples/configs/ssd_mobilenet_v1_pets.config)

Download manually on Windows or fetch these files using the _wget_ command on Linux. Put _config_ in the training directory, and extract _ssd_mobilenet_v1_ in the _models/object_detection_ directory. In the configuration file, you need to search for all of the PATH_TO_BE_CONFIGURED points and change them. You may also want to modify the batch size. In our configuration file, it is set to 36. Other models may have different batch sizes. If you get a memory error, you can try to decrease the batch size to get the model to fit in your VRAM. Finally, you must change the _checkpointname/path_, _num_classesto1_, _num_examplesto12_, and _label_map_path_ to _training/object-detect.pbtxt_.

Your steps start at 1 and the loss will be much higher. Depending on your GPU and volume of training data, this process will take varying amounts of time. On a nVidia GeForce 1080ti or similar processor, it should only take about a day or so. If you have a lot of training data, it might take much longer. You want to aim for a loss of well under 2, and ideally about ~1 on average or less. 

### TESTING OUR PRE-TRAINED MODEL
In the _models/object_detection_ directory, there is a Python script called _export_inference_graph.py_. To run this, you just need to pass in your checkpoint and pipeline config, then whatever directory you want the inference graph to be saved. For example:

```bsh

    python3 export_inference_graph.py \
        input_type image_tensor \
        pipeline_config_path training/ssd_mobilenet_v1_pets.config \
        trained_checkpoint_prefix training/model.ckpt-10856 \
        output_directory bacillaria_inference_graph

```

Your checkpoint files should be in the training directory. Next, make sure the _pipeline_config_path_ is set to whatever config file you chose, and then finally choose the name for the output directory, we went with _bacillaria_inference_graph_. Run the above command from _models/object_detection_. If you get an error that the module named _nets_ is required, then you need to re-run _models/object_detection_.

```bsh

    # From tensorflow/models/
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    # switch back to object_detection after this and re-run the above command
```

Otherwise, you should have a new directory, in our case is _bacillaria_inference_graph_, inside this new directory, we find new checkpoint data, a _saved_model_ directory, and the _forzen_inference_graph.pbfile_. This last item is the most important contents of the directory. Booting up Jupyter notebook and opening the _bacillaria_detection.ipynb_ (whch can be found in the Github repo), let us make a few changes. First, head to the Variables section, change the model name as well as the paths to the checkpoint and the labels.

```python

    # model to download.
    MODEL_NAME = 'bacillaria_inference_graph'
    # Path to frozen detection graph(actual model). 
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'  
    # List of the strings that are used to add a correct label for each box.
    PATH_TO_LABELS = os.path.join('training', 'object-detection.pbtxt')
    NUM_CLASSES = 1
```

Finally, in the Detection section, change _TEST_IMAGE_PATHS_ to:

```python

    TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR,
    'image{}.jpg'.format(i)) for i in range(min, max) ]
    Min-lowest image number/indes
    Max-highest image number/index

```

If you get errors or do not get satisfactory results, this might be due to two factors: poor annotation of the source data, or an ill-suited pre-trained model relative to your input data. Look over the annotation for inconsistencies. If this does not result in an improvement, try [other pre-trained models at in the TensorFlow library](https://www.tensorflow.org/resources/models-datasets).

## REFERENCES:
[1] Shorten, C. and Khoshgoftaar, T.M. (2019). [A survey on Image Data Augmentation for Deep Learning](https://link.springer.com/article/10.1186/s40537-019-0197-0). _Journal of Big Data_, 6, 60.  
