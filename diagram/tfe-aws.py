#!/usr/bin/env python3
from diagrams import Diagram
from diagrams import Cluster
from diagrams.aws.compute import EC2Instance
from diagrams.aws.compute import EC2ElasticIpAddress
from diagrams.aws.network import VPC
from diagrams.aws.database import RDSPostgresqlInstance
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

with Diagram("TFE AWS", show=False, direction="TB"):
    with Cluster("VPC"):
        EC2ElasticIpAddress("TFE IP") >> EC2Instance("Amazon Linux") >> [ 
            RDSPostgresqlInstance("aakulov-tfe"),
            SimpleStorageServiceS3Bucket("aakulov")
        ]
