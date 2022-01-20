import csv
from pickle import FALSE
from numpy import std 
import pandas as pd
import plotly.figure_factory as ff
import statistics as st

data = pd.read_csv("data.csv")
height = data["Height(Inches)"].tolist()
weight = data["Weight(Pounds)"].tolist()

h_mean = st.mean(height)
w_mean = st.mean(weight)

h_mode = st.mode(height)
w_mode = st.mode(weight)

h_median = st.median(height)
w_median = st.median(weight)

h_stdev = st.stdev(height)
w_stdev = st.stdev(weight)

print("Mean,Median,Mode and standard deviation of height is {},{},{} and {} respectively".format(h_mean,h_median,h_mode,h_stdev))
print("Mean,Median,Mode and standard deviation of weight is {},{},{} and {} respectively".format(w_mean,w_median,w_mode,w_stdev))

h_f_stdev_start,h_f_stdev_end = h_mean-h_stdev,h_mean+h_stdev
h_s_stdev_start,h_s_stdev_end = h_mean-(2*h_stdev),h_mean+(2*h_stdev)
h_t_stdev_start,h_t_stdev_end = h_mean-(3*h_stdev),h_mean+(3*h_stdev)

w_f_stdev_start,w_f_stdev_end = w_mean-w_stdev,w_mean+w_stdev
w_s_stdev_start,w_s_stdev_end = w_mean-(2*w_stdev),w_mean+(2*w_stdev)
w_t_stdev_start,w_t_stdev_end = w_mean-(3*w_stdev),w_mean+(3*w_stdev)

h_data_1_stdev = [result for result in height if result>h_f_stdev_start and result<h_f_stdev_end]
h_data_2_stdev = [result for result in height if result>h_s_stdev_start and result<h_s_stdev_end]
h_data_3_stdev = [result for result in height if result>h_t_stdev_start and result<h_t_stdev_end]

w_data_1_stdev = [result for result in weight if result>w_f_stdev_start and result<w_f_stdev_end]
w_data_2_stdev = [result for result in weight if result>w_s_stdev_start and result<w_s_stdev_end]
w_data_3_stdev = [result for result in weight if result>w_t_stdev_start and result<w_t_stdev_end]

print("{}% of data for height lies within 1 standard diviation".format(len(h_data_1_stdev)*100/len(height)))
print("{}% of data for height lies within 2 standard diviation".format(len(h_data_2_stdev)*100/len(height)))
print("{}% of data for height lies within 3 standard diviation".format(len(h_data_3_stdev)*100/len(height)))

print("{}% of data for weight lies within 1 standard diviation".format(len(w_data_1_stdev)*100/len(weight)))
print("{}% of data for weight lies within 2 standard diviation".format(len(w_data_2_stdev)*100/len(weight)))
print("{}% of data for weight lies within 3 standard diviation".format(len(w_data_3_stdev)*100/len(weight)))







