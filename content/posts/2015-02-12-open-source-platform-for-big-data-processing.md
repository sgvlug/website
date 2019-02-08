Title: Streaming-OODT: An Open-Source Platform for Big-Data Processing
Date: 2015-02-12 19:00
published: 2015-01-28 16:12
event_date: 2015-02-12 19:00
event_location: Burger Continental, 535 S Lake Ave, Pasadena, CA, 91101
event_updated: 1422489664000

Streaming-OODT was originally conceived to overcome the limitations of
traditional big-data processing and management systems. It is based on an open
source data processing framework called OODT (Object Oriented Data Technology)
and was funded by NASA Jet Propulsion Laboratory's Big Data Research &
Technology Development initiative "Archiving, Processing and Dissemination for
the Big Data Era". The vision behind the project is to combine state-of-the-
art technologies into an easy-to-use big-data processing system prepackaged to
allow users to quickly process big-data without the need to patch together
individual technologies.

Streaming-OODT provides both traditional batch processing as well as in-memory
MapReduce processing for use on general computing clusters. Cluster management
and multi-tenancy is provided via Apache Mesos, which manages batch processing
as well as the Streaming-OODT's underlying technologies. This ensures that
multi-tenancy is applied to both the system and the user's processing.

Apache Spark provides in-memory MapReduce processing enabling processing at
speeds hundreds of times faster than Hadoop MapReduce. This system is
augmented by Apache Kafka used to manage streaming data. This enables the user
to process streaming data alongside traditional data in Apache Spark and thus
tackle data-sets too large to persist en-masse to disk, while not losing the
ability to process data sets that already exist on disk.

Tachyon, an in-memory distributed file system, provides lightning-fast
distributed access to data files and streams on all nodes of the cluster.
Persistence is provided by Hadoop Distributed File System (HDFS) thus allowing
the user both fast data access and persistence to disk.

The purpose of this talk is to demonstrate Streaming-OODT, which will enable
the audience to use Streaming-OODT and supporting technologies to quickly
tackle their own big-data problems. The talk will introduce Streaming-OODT,
show how to quickly install and configure the system, explain the value added
by the underlying technologies, and walk through a working example of big-data
processing. Finally, benchmarks will be presented so that the audience can see
the benefit of these technologies and their combination.

**Speaker**: Michael Starch

[ ![Meetup Event Page]({filename}/images/meetup_logo_45.png) ](https://www.meetup.com/SGVTech/events/219406181/)
