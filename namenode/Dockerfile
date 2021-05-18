FROM bde2020/hadoop-namenode

MAINTAINER Nishant Bannikoppa <nishant.bannikoppa@esds.co.in>

HEALTHCHECK CMD curl -f http://172.16.21.13:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
ENV RANGER_HDFS_PLUGIN_HOME /opt/ranger-hdfs-plugin
ENV RANGER_VERSION 2.0.0
COPY ranger-${RANGER_VERSION}-hdfs-plugin.tar.gz /opt/ranger-${RANGER_VERSION}-hdfs-plugin.tar.gz

WORKDIR /opt

RUN mkdir -p /hadoop/dfs/name

RUN tar -xvf ranger-${RANGER_VERSION}-hdfs-plugin.tar.gz \
    && ln -s ranger-${RANGER_VERSION}-hdfs-plugin $RANGER_HDFS_PLUGIN_HOME \
    && rm -f ranger-${RANGER_VERSION}-hdfs-plugin.tar.gz \
    &&curl https://repo1.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar -o $RANGER_HDFS_PLUGIN_HOME/lib/commons-lang-2.6.jar \
    && curl https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.13.3/log4j-api-2.13.3.jar  -o $RANGER_HDFS_PLUGIN_HOME/lib/log4j-api-2.13.3.jar \
    && groupadd hadoop && adduser hdfs && usermod -aG hadoop hdfs 
    
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9870

CMD ["/run.sh"]
