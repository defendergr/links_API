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
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/-Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" alt="Kubernetes">
    <img src="https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white" alt="JSON">

</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running links_API](#-running-links_API)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

This code snippet is a FastAPI application that provides an API for retrieving information about sports matches.

It imports necessary modules such as jsonable_encoder from fastapi.encoders, app from Api, games from Api.apps, os for file operations, requests for making HTTP requests, JSONResponse from fastapi.responses, and datetime for date and time operations.

It loads environment variables from the Api\env.py file if it exists, otherwise it creates the file with default values and loads the environment variables.

It defines two routes: / and /links, which return a simple text message and the links data respectively.

The /football route retrieves football match data for today's matches from the Sofa Scores API. It checks if the SOFA_API_KEY is set, sets the URL and query parameters for the API request, sets the headers, makes the API request, filters the matches by specific tournaments, and returns the match data in a JSON response.

Overall, this code snippet sets up a FastAPI application with routes for retrieving information about sports matches using the Sofa Scores API.

---

##  Features

HTTP error 401 for prompt `features`

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
    ├── DockerImageBuild.cmd
    ├── Dockerfile
    ├── K8sCreate.cmd
    ├── K8sRun.cmd
    ├── LICENSE
    ├── deployment.yaml
    ├── gitOnlyGet.cmd
    ├── gitSave.cmd
    ├── oldCMDs
    │   ├── DockerContainerBuild.cmd
    │   └── win-run.cmd
    ├── requirement.txt
    └── run.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                 | Summary                                          |
| ---                                                                                                  | ---                                              |
| [DockerImageBuild.cmd](https://github.com/defendergr/links_API.git/blob/master/DockerImageBuild.cmd) | HTTP error 401 for prompt `DockerImageBuild.cmd` |
| [gitSave.cmd](https://github.com/defendergr/links_API.git/blob/master/gitSave.cmd)                   | HTTP error 401 for prompt `gitSave.cmd`          |
| [deployment.yaml](https://github.com/defendergr/links_API.git/blob/master/deployment.yaml)           | HTTP error 401 for prompt `deployment.yaml`      |
| [requirement.txt](https://github.com/defendergr/links_API.git/blob/master/requirement.txt)           | HTTP error 401 for prompt `requirement.txt`      |
| [Dockerfile](https://github.com/defendergr/links_API.git/blob/master/Dockerfile)                     | HTTP error 401 for prompt `Dockerfile`           |
| [K8sRun.cmd](https://github.com/defendergr/links_API.git/blob/master/K8sRun.cmd)                     | HTTP error 401 for prompt `K8sRun.cmd`           |
| [K8sCreate.cmd](https://github.com/defendergr/links_API.git/blob/master/K8sCreate.cmd)               | HTTP error 401 for prompt `K8sCreate.cmd`        |
| [run.py](https://github.com/defendergr/links_API.git/blob/master/run.py)                             | HTTP error 401 for prompt `run.py`               |
| [gitOnlyGet.cmd](https://github.com/defendergr/links_API.git/blob/master/gitOnlyGet.cmd)             | HTTP error 401 for prompt `gitOnlyGet.cmd`       |

</details>

<details closed><summary>Api</summary>

| File                                                                           | Summary                                 |
| ---                                                                            | ---                                     |
| [main.py](https://github.com/defendergr/links_API.git/blob/master/Api/main.py) | HTTP error 401 for prompt `Api/main.py` |

</details>

<details closed><summary>Api.apps</summary>

| File                                                                                          | Summary                                           |
| ---                                                                                           | ---                                               |
| [all_scrap.py](https://github.com/defendergr/links_API.git/blob/master/Api/apps/all_scrap.py) | HTTP error 401 for prompt `Api/apps/all_scrap.py` |

</details>

<details closed><summary>oldCMD's</summary>

| File                                                                                                                  | Summary                                                       |
| ---                                                                                                                   | ---                                                           |
| [win-run.cmd](https://github.com/defendergr/links_API.git/blob/master/oldCMD's/win-run.cmd)                           | HTTP error 401 for prompt `oldCMD's/win-run.cmd`              |
| [DockerContainerBuild.cmd](https://github.com/defendergr/links_API.git/blob/master/oldCMD's/DockerContainerBuild.cmd) | HTTP error 401 for prompt `oldCMD's/DockerContainerBuild.cmd` |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **<code>► INSERT-TEXT-HERE</code>**: `version x.y.z`

###  Installation

1. Clone the links_API repository:

```sh
git clone https://github.com/defendergr/links_API.git
```

2. Change to the project directory:

```sh
cd links_API
```

3. Install the dependencies:

```sh
> INSERT-INSTALL-COMMANDS
```

###  Running links_API

Use the following command to run links_API:

```sh
> INSERT-RUN-COMMANDS
```

###  Tests

To execute tests, run:

```sh
> INSERT-TEST-COMMANDS
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/defendergr/links_API.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/defendergr/links_API.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/defendergr/links_API.git/issues)**: Submit bugs found or log feature requests for Links_api.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/defendergr/links_API.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
