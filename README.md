<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">Links_API</h1>
</p>
<p align="center">
    <em>For educational & research purposes only</em>
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/-Selenium-43B02A?style=flat&logo=selenium&logoColor=white" alt="Selenium">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/-Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" alt="Kubernetes">
    <img src="https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white" alt="JSON">
    <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
    
</p>
<hr>

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> - [ Getting Started](#getting-started)
>   - [ Installation](#installation)
>   - [ Running links_API](#running-links_API)
> - [ License](#license)

---

##  Overview

This web application is a FastAPI-based API service designed to retrieve and process sports match data.

- **Football Match Data:** The `/football` endpoint fetches real-time football match data from the SofaScores API. It requires a valid `SOFA_API_KEY` and filters results based on specified tournaments.
- **Data Extraction:** The `/links` endpoint accesses an internal Python application responsible for web scraping and data extraction from a designated URL.
- **Infrastructure:** Includes pre-configured command files for building Docker images and Kubernetes pods to streamline continuous integration and delivery (CI/CD) processes.
- This application showcases proficiency in Python, FastAPI, web scraping, API integration, and containerization technologies.
---

##  Features

This Python application is designed to extract and process sports match data. Key functionalities include:

- **Web Scraping:** Utilizes Selenium and BeautifulSoup to extract relevant information from target websites.
- **Data Parsing:** Processes extracted HTML content to identify and extract specific data points such as match titles, links, timestamps, sports, countries, and fixtures.
- **Data Structuring:** Organizes extracted data into structured formats like lists and dictionaries for further processing or consumption.
- **API Integration:** Leverages the FastAPI framework to create a RESTful API for exposing extracted data.
- **Flexibility:** Offers options to return data in JSON format or as Python dictionaries, accommodating various use cases.
- By combining these features, the application provides a robust solution for efficiently retrieving and managing sports match data.
---

##  Repository Structure

```sh
└── links_API/
    ├── Api
    │   ├── __init__.py
    │   ├── apps
    │   │   ├── __init__.py
    │   │   └── all_scrap.py
    │   └── main.py
    ├── oldCMDs
    │   ├── DockerContainerBuild.cmd    
    ├── DockerImageBuild.cmd
    ├── Dockerfile
    ├── K8sCreate.cmd
    ├── K8sRun.cmd
    ├── LICENSE
    ├── deployment.yaml
    └── requirement.txt
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **<code>► Docker-desktop with kubernetes enabled</code>**: `version: 4.32.0`

###  Installation

1. Clone the links_API repository:

```sh
> git clone https://github.com/defendergr/links_API.git
```

2. Change to the project directory:

```sh
> cd links_API
```

3. (optional) Navigate and sign up to rapidapi for token:

```sh
https://rapidapi.com/rapidsportapi/api/sportapi7/playground/
```
4. (optional) Run `WinSetToken.cmd` will prompt you to paste your SofaScores API token without quotation marks:
```sh
> WinSetToken.cmd
```

5. Build Docker image:

```sh
> DockerImageBuild.cmd
```

6. Create pod's:

```sh
> K8sCreate.cmd
```

###  Running links_API

Run the application:

```sh
> K8sRun.cmd
```

---

Connect to :

```sh
> http://localhost:8030/docs
```

---

##  License

This project is protected under the [AGPL-3.0 license](LICENSE) License.

---
