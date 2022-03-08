FROM elasticsearch:7.17.0

WORKDIR /usr/share/elasticsearch
COPY resource/elasticsearch-analysis-ik-7.17.0.zip .
RUN unzip elasticsearch-analysis-ik-7.17.0.zip -d /usr/share/elasticsearch/plugins/ik
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins/ik
