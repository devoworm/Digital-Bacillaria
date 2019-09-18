## Methodology for TensorFlow Implementation
Ujjwal Singh, Asmit Singh, Bradly Alicea   

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


-	Some unsupervised segmentation of images like Watershed, canny’s edge detection, etc can be found useful in many cases which are general and not too detailed images. In our case, it doesn’t provide us results that we want.


-	Then, the old school techinique comes handy that you label your dataset by hands, this will allow you to extract specifically which information you want from your images and also helps in creating more accurate labels for your dataset as a human is annotating them.


There are many image annotation tools available over github developed by different developers, you can use any of them according to your choice.

### 2. TRAIN YOUR MODEL
Once you are sorted with your dataset, you need to train your model using this dataset, this is one of the most important part while you are training your dataset on neural networks or any sort of the Deep networks.

Once you have labeled the images with help of a tool, you have noticed that your records are stored in XML format (in most cases, some tools store it directly in the csv format). We need to convert these records from XML formar to csv format, as this will help us in further steps that we encounter later in this part of the chapter.

| aaa
aaaa

aaa|
|---|




We have created two folders train and test, converted images from XML to csv.


By now, we have converted our XML records to the csv records respectively, now you have csv file for training and testing dataset.

Our next would be to generate our TensorFlow records from these csv files, in order to proceed with this, first, you will be required to install few libraries like,







After you have installed all these libraries we can commence with our code,



First of all define your csv input path, from where this script can pick up the csv files which we have created in the above part, and also define your output path, where you want to save these TensorFlow records which will be created during this script execution.
After this, you need to define a function which returns 1 whenever row_label matches to your label* name.


Then, define a create_tf function that will eventually convert these csv files into TensorFlow records. In this function, you have to extract all the information which is present in the csv file.


You can do this by following the below function.





Change this function according to your needs.


After this just wrap up your python file by defining main function according to your need, your
TensorFlow records are ready**.










*Label is the what you have defined in the name column when you are annotating your dataset.
** You can find the code of this script in our GitHub repository.
After all, this done, we are left with our data, files of XML records, CSV records, and TFrecords. We now need a TFrecord file to do the learning process.



Here,wehavetwooptions.Wecanuseapre-trainedmodel,andthenusetransferlearningto learnanewobject,orwecouldlearnnewobjectsentirelyfromscratch.Thebenefitoftransfer learningisthattrainingcanbemuchquicker,andtherequireddatathatyoumightneedismuch less.Forthisreason,we'regoingtobedoingtransferlearninghere.

Therearefewpre-trainedmodelsavailablewiththeTensorflowlibrary,Weareusingmobilenet forourpurpose.(DeepLabV3+,willbeinnextsheetforahigherlevelofnetworksunderstanding audience,forbeginnersweareusingmobilenets).

Links:-


https://raw.githubusercontent.com/tensorflow/models/master/object_det ection/samples/configs/ssd_mobilenet_v1_pets.config


http://download.tensorflow.org/models/object_detection/ssd_mobilenet_
v1_coco_11_06_2017.tar.gz


Download these files using wget command on Linux or install manually on windows.


Puttheconfiginthetrainingdirectory,andextractthessd_mobilenet_v1inthe models/object_detectiondirectory


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





## REFERENCES:
Shorten, C. and Khoshgoftaar, T.M. (2019). [A survey on Image Data Augmentation for Deep Learning](https://link.springer.com/article/10.1186/s40537-019-0197-0). Journal of Big Data, 6, 60.  









This is how you can train your own model, if you get errors or do not get satisfactory results, this might be due to poor annotation or the pre-trained model used in this doesn’t suit your model. Try to look at the annotation again and if still no improvement, try to use other
pre-trained models at TensorFlow.
