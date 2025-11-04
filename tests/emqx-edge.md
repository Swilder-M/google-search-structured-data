EMQX Edge - Lightweight MQTT Broker for IoT Edge     /\* Use Inter as the default font \*/ body { font-family: 'Inter', sans-serif; } /\* Custom styles for tab navigation \*/ .tab-btn { @apply px-4 py-3 font-medium text-gray-600 dark:text-gray-400 border-b-2 border-transparent hover:text-blue-600 dark:hover:text-blue-500; } .tab-btn.active { @apply text-blue-600 dark:text-blue-500 border-blue-600 dark:border-blue-500; } .tab-content { display: none; } .tab-content.active { display: block; } /\* Custom styles for accordion \*/ .accordion-icon { transition: transform 0.2s ease-in-out; } .accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease-in-out; }

![EMQX Logo](https://placehold.co/140x40/1e293b/ffffff?text=EMQX)

[Products](#) [Solutions](#) [Docs](#) [Blog](#) [Contact](#)

[Get Started Free](#) Open main menu

[Products](#) [Solutions](#) [Docs](#) [Blog](#) [Contact](#) [Get Started Free](#)

EMQX Edge

Lightweight MQTT Broker for IoT Edge
====================================

Deploy a robust, high-performance MQTT broker at the edge, process data locally, and reliably bridge data to the cloud.

[Download Free](#) [Contact Sales](#)

![EMQX Edge MQTT Broker Architecture Diagram](https://placehold.co/600x500/1e293b/475569?text=EMQX+Edge+Architecture)

< 5ms Latency

100K+ Concurrent Connections

1M+ Messages/Second

< 10MB Memory Footprint

### POWERING INDUSTRIAL DATA FOR LEADING MANUFACTURERS

![Logo of an industry leader using EMQX Edge](https://placehold.co/150x50/e2e8f0/94a3b8?text=Industry+Leader&font=inter)

![Logo of an industry leader using EMQX Edge](https://placehold.co/150x50/e2e8f0/94a3b8?text=Industry+Leader&font=inter)

![Logo of an industry leader using EMQX Edge](https://placehold.co/150x50/e2e8f0/94a3b8?text=Industry+Leader&font=inter)

![Logo of an industry leader using EMQX Edge](https://placehold.co/150x50/e2e8f0/94a3b8?text=Industry+Leader&font=inter)

![Logo of an industry leader using EMQX Edge](https://placehold.co/150x50/e2e8f0/94a3b8?text=Industry+Leader&font=inter)

### Blazing-Fast

Optimized for edge with low latency and high throughput—up to 10x faster than Mosquitto when running on multi-core CPUs.

### Ultra-Lightweight

Minimal footprint with efficient resource utilization, perfect for edge devices. Boot memory footprint is as low as 200KB.

### Cross-Platform

Runs seamlessly on multiple operating systems and hardware architectures, including Linux, Windows, ARM, x86, and RISC-V.

How EMQX Edge Works

IoT Data Hub at the Edge
------------------------

EMQX Edge acts as the central data hub for a local site, factory, or facility. It aggregates data from all local devices (via Neuron or Kepware etc) and bridges it to the cloud.

*   **Connect:** Receives MQTT data from local devices or gateways like EMQX Neuron.
*   **Process (coming soon):** Uses its rule engine to filter, transform, and route data locally.
*   **Bridge:** Publishes data via a secure, reliable MQTT bridge to a central cloud broker.

![EMQX Edge Architecture Diagram](https://placehold.co/600x450/1e293b/475569?text=Simple+Edge+Architecture+Diagram)

Diagram: (Devices/Neuron) -> **EMQX Edge Broker** -> (Cloud) EMQX Cloud

Your Lightweight Edge MQTT Broker
---------------------------------

EMQX Edge is a full-featured MQTT broker that runs on-premise, handling local device communication and bridging critical data to the cloud.

Broker

### Lightweight MQTT Brokering

Provides a full-featured MQTT 5.0 broker at the edge. Manage device-to-device communication, data streams, and local topic trees autonomously.

*   Full MQTT 5.0 & 3.1.1 Support
*   100K+ Connections on a Single Node
*   Runs on x86, ARM, and in Docker

[Learn more →](#)

![Diagram of EMQX Edge as a lightweight MQTT broker](https://placehold.co/500x400/1e293b/475569?text=Edge+Brokering)

![Diagram of the SQL-based rule engine in EMQX Edge](https://placehold.co/500x400/1e293b/475569?text=SQL+Rule+Engine)

Processing (coming soon)

### Real-Time Data Processing

Use the SQL-based rule engine to process data in real-time. Filter noise, aggregate values, and transform data formats locally before bridging to the cloud.

*   Intuitive SQL-like Syntax
*   Trigger Local Actions & Alerts
*   Reduce Cloud Data Costs

[Learn more →](#)

Bridging

### Seamless Cloud Bridging

Securely bridge selected data to any cloud platform. Synchronizes edge data with your central IT systems for a unified view and ensures data is never lost, even with unstable networks.

*   Bi-directional Bridge to EMQX Cloud
*   Connect to AWS IoT, Azure IoT Hub, etc.
*   Automatic Buffering & Re-transmission

[Learn more →](#)

![Diagram of EMQX Edge bridging data to the cloud](https://placehold.co/500x400/1e293b/475569?text=Edge-to-Cloud+Bridging)

![Diagram of OPC UA and Modbus data integrating with MQTT via EMQX Edge](https://placehold.co/500x400/1e293b/475569?text=OPC+UA+%26+MQTT+Integration)

Protocols

### OPC UA & MQTT Integration

Combine the power of industrial protocols with MQTT. EMQX Edge acts as a local hub, receiving standardized MQTT data from OPC UA and Modbus (via Neuron) and bridging it to any MQTT platform.

*   Integrate OPC UA & Modbus
*   Aggregate edge data with MQTT
*   Unified data model for IT/OT

[Learn more →](#)

AI/ML (coming soon)

### Edge AI/ML Integration

Feed processed edge data directly into local AI/ML models. EMQX Edge's rule engine can trigger inference and publish results back via MQTT for real-time decision-making.

*   Low-latency inference at the edge
*   Real-time anomaly detection
*   Optimize predictive maintenance models

[Learn more →](#)

![Diagram illustrating Edge AI and ML integration with EMQX Edge](https://placehold.co/500x400/1e293b/475569?text=Edge+AI/ML+Integration)

Architecture

Unified Namespace: Edge to Cloud
--------------------------------

Seamlessly Integrate EMQX Neuron, Edge, and Cloud to build a unified namespace (UNS) architecture for your industrial data, enabling true IT/OT convergence.

![EMQX Unified Namespace architecture diagram from edge to cloud](https://placehold.co/800x600/1e293b/475569?text=Unified+Namespace+Diagram)

1

#### EMQX Neuron

Connects to OT devices (PLCs, sensors) and publishes data to the local/edge broker.

2

#### EMQX Edge

Acts as the central edge hub, aggregating data from multiple Neuron instances.

3

#### EMQX Cloud

Bridges data from the edge to the cloud, making it available to all enterprise applications (MES, ERP, BI).

Built for the Industrial Edge
-----------------------------

EMQX Edge provides a robust, scalable, and secure broker for your edge to edge, and edge to cloud data pipeline.

### Full MQTT 5.0 Support

Leverage the full power of MQTT 5.0, including shared subscriptions, topic aliases, and user properties etc.

### Persistent Cloud Bridge

Reliably bridge data to any MQTT IoT platforms. Automatic store and forward capabilities for unstable network.

### Powerful Data Processing

Use SQL-like engine to quickly perform real-time data filtering, transformation, and routing (coming soon).

### High-Availability Clustering

Cluster two or more Edge nodes to create a highly available deployment for critical on-premise workloads.

### Enterprise-Grade Security

Secure your edge data with TLS/SSL encryption, plus multiple authentication methods (username and password, JWT).

### Cross-Platform Support

Deploy easily on x86 or ARM architectures, with support for Linux, Windows, macOS, and Docker.

### Easy Observability

A built-in dashboard, view logs, and capabilities of exporting metrics to Prometheus etc.

### REST API Management

Automate and manage your edge deployments at scale using a comprehensive REST API for configuration and monitoring.

Data Processing (coming soon)

Process Data with a SQL-Based Rule Engine
-----------------------------------------

Filter, transform, and route data locally with an intuitive SQL language, without writing complex code.

[Learn more about the Rule Engine →](#)

![EMQX Edge's SQL-based Rule Engine UI](https://placehold.co/800x600/1e293b/475569?text=EMQX+Rule+Engine+UI)

Powering Edge Industrial Scenarios
----------------------------------

See how EMQX Edge is used across leading industries to manage edge data.

Smart Manufacturing Connected Vehicles Smart Utilities

### Factory Floor Data Hub

Deploy EMQX Edge as a local data hub on the factory floor. It aggregates data from multiple EMQX Neuron instances, manages local device communication, and bridges critical OEE data to the central MES/SCADA system.

[Learn more about Smart Manufacturing →](#)

![Smart factory data hub using EMQX Edge](https://placehold.co/600x400/1e293b/475569?text=Factory+Data+Hub)

### In-Vehicle Data Processing (T-BOX)

Run EMQX Edge on in-vehicle T-BOX units. It collects CAN bus data (via Edge extension), processes it in real-time for driver alerts, and uses the persistent bridge to send critical telematics to the cloud platform for fleet management.

[Learn more about Connected Vehicles →](#)

![In-vehicle data processing with EMQX Edge](https://placehold.co/600x400/1e293b/475569?text=In-Vehicle+Data)

### Smart Utility Data Aggregation

Install EMQX Edge on local data concentrators or gateways for smart meters, solar farms, or charging stations. It manages thousands of local device connections and securely bridges aggregated data to the central platform.

[Learn more about Smart Utilities →](#)

![Smart utility data aggregation with EMQX Edge](https://placehold.co/600x400/1e293b/475569?text=Smart+Utilities)

Frequently Asked Questions
--------------------------

Find quick answers to common questions about EMQX Edge.

What is EMQX Edge?

EMQX Edge is a lightweight MQTT broker specifically designed for the industrial IoT edge. It runs on resource-constrained hardware (like industrial PCs and gateways) to manage local device-to-device communication, process data in real-time, and securely bridge data to the cloud.

How is EMQX Edge different from EMQX Neuron?

They work together. EMQX Neuron is a connectivity gateway that collects data from various industrial protocols (like Modbus, OPC-UA) and converts it to MQTT. EMQX Edge is the MQTT broker that receives, processes, and routes that MQTT data. Neuron connects to the devices; Edge manages the data flow.

How is EMQX Edge different from EMQX Enterprise/Cloud?

EMQX Edge is optimized for deployment on edge hardware with limited resources. EMQX Enterprise and Cloud are large-scale, clusterable platforms designed for high-availability, massive-scale deployments in data centers or the cloud. Edge bridges data \*to\* Enterprise or Cloud.

Can EMQX Edge run offline?

Yes. EMQX Edge operates autonomously to manage all local data communication. If the connection to the cloud is lost, it will buffer data (based on configuration) and automatically sync it once the connection is restored, ensuring no data loss.

Is EMQX Edge free?

EMQX Edge is free for use cases with up to 10 concurrent connections. For applications requiring more connections or commercial support, we offer commercial [licenses](https://docs.emqx.com/en/emqx-edge/latest/license-policy.html).

Deploy Your Edge MQTT Broker Today
----------------------------------

Download EMQX Edge for free and start processing your edge data in minutes. Have questions? Our experts are here to help.

[Download Free](#) [Talk to an Expert](#)

![EMQX Logo](https://placehold.co/140x40/1e293b/ffffff?text=EMQX)

The Leader in MQTT & IIoT

[](#)[](#)[](#)

#### Products

*   [EMQX Enterprise](#)
*   [EMQX Cloud](#)
*   [EMQX Edge](#)
*   [EMQX Neuron](#)
*   [NanoMQ](#)

#### Resources

*   [Documentation](#)
*   [Blog](#)
*   [Case Studies](#)
*   [Webinars](#)

#### Company

*   [About Us](#)
*   [Careers](#)
*   [Contact Us](#)
*   [Partners](#)

#### Legal

*   [Privacy Policy](#)
*   [Terms of Service](#)
