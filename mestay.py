import pandas as pd

destionations = pd.read_csv("data/destinations.csv")
test = pd.read_csv("data/test.csv")
train = pd.read_csv("data/train.csv")
print "[>]  SHAPE"
print "[.] Destinations"
print destinations.shape()
print "[.] Test"
print test.shape()
print "[.] Train"
print train.shape()
print "[>]  HEAD"
print "[.] Train"
print train.head(5)
print "[.] Test"
print test.head(5)
