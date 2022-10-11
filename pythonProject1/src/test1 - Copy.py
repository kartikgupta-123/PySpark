from BaseClass import *
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import configparser

class FirstPyspark(BaseClass):
    pass

baseobj = FirstPyspark()


def main():
    print(baseobj.getConfig('Mysql', 'url'))
    #import spark.implicits._
    txnsdf= spark.read.option("header","true").csv("D:\\BD_Data\\Raw_Data\\txns_head")
    #    txnsdf.show()
    print(txnsdf.count())

    jsondf1 = spark.read.option("header", "true").csv("D:\\BD_Data\\Raw_Data\\file4.json")
    jsondf= spark.read.json("D:\\BD_Data\\Raw_Data\\file4.json")
    #    jsondf.show()
    print(jsondf.count())

    jtdf= txnsdf.join(jsondf, txnsdf.txnno == jsondf.txnno, "inner")
    jtdf.show()
    print(jtdf.count())

    countrydf = spark.read.option("header", "true").csv("D:\\BD_Data\\Raw_Data\\all_country.csv")

if __name__=="__main__" :
    #    conf = SparkConf().setAppName("spark").setMaster("local[*]")
    #    sc = SparkContext(conf)
    #    sc.setLogLevel("Error")
    spark = SparkSession.builder.master("local[*]").appName("spark").getOrCreate()
    #    spark = SparkSession.builder().getOrCreate()

    main()
