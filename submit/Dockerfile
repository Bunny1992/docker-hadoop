FROM bde2020/hadoop-base

MAINTAINER Nishant Bannikoppa <nishant.bannikoppa@esds.co.in>

COPY WordCount.jar /opt/hadoop/applications/WordCount.jar

ENV JAR_FILEPATH="/opt/hadoop/applications/WordCount.jar"
ENV CLASS_TO_RUN="WordCount"
ENV PARAMS="/user/hdfs/in/Wordcount /user/hdfs/out/Wordcount"

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
