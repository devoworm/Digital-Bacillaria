## Methodology for TensorFlow Implementation
Ujjwal Singh, Asmit Singh, Bradly Alicea   

### INTRODUCTION
In order to train your model on the deep networks, you will need to do the following:

1. create your Dataset  
  
2. train your model  
  
3. test your models  
  
Creating your data will depend on your domain of interest. You need to have a sizable sample (20-200 images) and perhaps use methods such as data augmentation [1] to improve the performance of your model.

We will also go through a brief explaination of how to train your model using TensorFlow and Deeplab. You can use many other models as well, these steps are going to the same for almost all the models. Let us discuss the above steps in detail

### 1. MAKE YOUR DATASET
It is one of the most essential parts to make the dataset, the two things which should be kept in mind is that your dataset must be accurate and should cover a large variety of things related to your model.

In the case of _Bacillaria_ model training, we have first done the microscopy of the worm, then we have split that microscopy into various frames to form our dataset. We have included both dark and light backgrounds to make our dataset more enriched and so that it covers a variety of cases.

Once your dataset is ready, you have to somehow convert it into a language that your machine can understand. It doesn’t know initially what we want from these images.

For this case, there are several options available -

1. unsupervised segmentation of images using Watershed or Canny Edge detection can be found useful in many cases which are general and not too detailed images. In our case, it doesn’t provide us results that we want.  
  
2. you can also lebel your dataset manually. Manual annotation will allow you to extract information specific to your images. It also helps to create more accurate labels and features for your dataset.  
  
There are many image annotation tools available over github developed by different developers, you can use any of them according to your choice.

### 2. TRAIN YOUR MODEL
Once you are sorted with your dataset, you need to train your model using this dataset, this is one of the most important part while you are training your dataset on neural networks or any sort of the Deep networks.

Once you have labeled the images with help of a tool, you have noticed that your records are stored in XML format (in most cases, some tools store it directly in the csv format). We need to convert these records from XML formar to csv format, as this will help us in further steps that we encounter later in this part of the chapter.

    def main():
	      for directory in ['train','test']:
		        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
		        xml_df = xml_to_csv(image_path)
		        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
		        print ('Successfully converted xml to csv.')

This code defines two folders: train and test, and also converts the image output from XML to csv. 

Now you have csv file for training and testing dataset. Our next would be to generate our TensorFlow records from these csv files. To proceed, you will need to install a few libraries

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

After you have installed all these libraries we can commence with our code.



First of all define your csv input path, from where this script can pick up the _csv_ files which we have created in the above part, and also define your output path, where you want to save these TensorFlow records which will be created during this script execution.
After this, you need to define a function which returns a value of "1" whenever _row_label_ matches to your label name. In this context, label is the column name assigned during annotation.

Next, define a _create_tf_ function that will eventually convert these csv files into TensorFlow records. In this function, you have to extract all the information which is present in the _csv_ file. You can do this by following the below function.

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

Change this function according to the features you want to define. After this just wrap up your python file by defining main function according to your need, your TensorFlow records are ready. You can find the code of this script in our GitHub repository. After all, this done, we are left with our data, files of XML records, CSV records, and TFrecords. We now need a TFrecord file to do the learning process.



Here,wehavetwooptions.Wecanuseapre-trainedmodel,andthenusetransferlearningto learnanewobject,orwecouldlearnnewobjectsentirelyfromscratch.Thebenefitoftransfer learningisthattrainingcanbemuchquicker,andtherequireddatathatyoumightneedismuch less.Forthisreason,we'regoingtobedoingtransferlearninghere.

Therearefewpre-trainedmodelsavailablewiththeTensorflowlibrary,Weareusingmobilenet forourpurpose.(DeepLabV3+,willbeinnextsheetforahigherlevelofnetworksunderstanding audience,forbeginnersweareusingmobilenets).

Links:-

https://raw.githubusercontent.com/tensorflow/models/master/object_detection/samples/configs/ssd_mobilenet_v1_pets.config


http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz


Download these files using the _wget_ command on Linux or install manually on Windows. Put _config_ in the training directory, and extract _ssd_mobilenet_v1_ in the _models/object_detection_ directory.


Intheconfigurationfile*,youneedtosearchforallofthePATH_TO_BE_CONFIGUREDpoints andchangethem.Youmayalsowanttomodifythebatchsize.Currently,itissetto36inour configurationfile.Othermodelsmayhavedifferentbatchsizes.Ifyougetamemoryerror,you cantrytodecreasethebatchsizetogetthemodeltofitinyourVRAM.Finally,youalsoneedto changethecheckpointname/path,num_classesto1,num_examplesto12,and label_map_path:"training/object-detect.pbtxt"


Yourstepsstartat1andthelosswillbemuchhigher.DependingonyourGPUandhowmuch trainingdatayouhave,thisprocesswilltakevaryingamountsoftime.Onsomethinglikea
1080ti,itshouldtakeonlyaboutadayorso.Ifyouhavealotoftrainingdata,itmighttakemuch longer.Youwanttoshootforalossofabout~1onaverage(orlower).Iwouldn'tstoptraining untilyouareforsureunder2.













*Configuration files can be found here
TESTING OUR MODEL -



Now,inthemodels/object_detectiondirectory,thereisascriptforus:
export_inference_graph.py



Torunthis,youjustneedtopassinyourcheckpointandyourpipelineconfig,thenwhereveryou wanttheinferencegraphtobeplaced.Forexample:

python3 export_inference_graph.py \
--input_type image_tensor \
--pipeline_config_path training/ssd_mobilenet_v1_pets.config \
--trained_checkpoint_prefix training/model.ckpt-10856 \
--output_directory bacillaria_inference_graph

Yourcheckpointfilesshouldbeinthetrainingdirectory.Next,makesurethe pipeline_config_pathissettowhateverconfigfileyouchose,andthenfinallychoosethe namefortheoutputdirectory,wewentwithbacillaria_inference_graph.

Runtheabovecommandfrommodels/object_detection

Ifyougetanerroraboutno module named 'nets',thenyouneedtore-run:

# From tensorflow/models/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
# switch back to object_detection after this and re-run the above command



Otherwise,youshouldhaveanewdirectory,inourcaseisbacillaria_inference_graph, insideit,Ihavenewcheckpointdata,asaved_modeldirectory,and,mostimportantly,the forzen_inference_graph.pbfile.

Bootingupjupyternotebookandopeningthebacillaria_detection.ipynb*,let'smakea fewchanges.First,headtotheVariablessection,andlet'schangethemodelname,andthe pathstothecheckpointandthelabels:



# model to download.
MODEL_NAME = 'bacillaria_inference_graph'


# Path to frozen detection graph(actual model). PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that are used to add a correct label for each box.
PATH_TO_LABELS = os.path.join('training', 'object-detection.pbtxt')
* can be found in GitHub repo
NUM_CLASSES = 1

Finally,intheDetectionsection,changetheTEST_IMAGE_PATHSvarto:

TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR,
'image{}.jpg'.format(i)) for i in range(min, max) ]


Min-lowest image number/indes
Max-highest image number/index


Below are a few of our results -


This is how you can train your own model, if you get errors or do not get satisfactory results, this might be due to poor annotation or the pre-trained model used in this doesn’t suit your model. Try to look at the annotation again and if still no improvement, try to use other pre-trained models at TensorFlow.

## REFERENCES:
[1] Shorten, C. and Khoshgoftaar, T.M. (2019). [A survey on Image Data Augmentation for Deep Learning](https://link.springer.com/article/10.1186/s40537-019-0197-0). _Journal of Big Data_, 6, 60.  
