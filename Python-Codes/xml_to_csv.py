# -*- coding: utf-8 -*-

""" importing Libraries for our converstion
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

""" Defining function to convert all XML Files into CSV files
"""

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


""" 
   I have make a parent folder and under this I have created two folders whose description is written below-
  
   images - this folder contains test and train images which their respective xml files | Test contain 10 percent data of train folder in my case.
   data - where train_labels.csv and test_labels.csv file will be generated.
   
   This file is not in digital notebook format because its has nothing to show, and it is difficult to upload such a huge data on colab or Jupyter Notebooks.

"""
  
  
def main():
    for directory in ['train','test']:
        image_path = os.path.join(os.getcwd(), 'data/{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')


main()
