## Guide for Dynamic Application Security Testing (DAST) Tool

This guide provides detailed instructions on how to build, run, and use the Dynamic Application Security Testing (DAST) Tool designed to perform security scans on web applications using OWASP ZAP (Zed Attack Proxy).


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Building the Docker Image](#building-the-docker-image)
4. [Running the Docker Container](#running-the-docker-container)
5. [Tool Usage](#tool-usage)
6. [Troubleshooting](#troubleshooting)
7. [Additional Information](#additional-information)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker
- Git (optional, for cloning the repository)

## Project Structure

```
dynamic_application_security_testing/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── GUIDE.md
├── README.md
├── requirements.txt
├── setup.py
|
└── dynamic_application_security_testing/
    ├── __init__.py
    ├── __version__.py
    ├── main.py
    |
    ├── core/
    |   ├── __init__.py
    |   ├── input.py
    |   ├── logger.py
    |   └── models.py
    |
    ├── service/
    |   ├── __init__.py
    |   └── zap.py
    |
    └── support/
        ├── __init__.py
        ├── enums.py
        └── utils.py
```

## Building the Docker Image

1. Open a terminal and navigate to the project directory:

   ```bash
   cd path/to/dynamic-application-security-testing
   ```

2. Build the Docker image using the following command:

   ```bash
   sudo docker build --no-cache . -f Dockerfile -t dynamic-application-security-testing:latest
   ```

   This command builds a Docker image named dynamic-application-security-testing based on the instructions in the Dockerfile.

## Running the Docker Container

To run the Dynamic Application Security Testing Tool inside a Docker container, use the following command structure:

```bash
sudo docker run --rm -it -v $(pwd)/output:/output dynamic-application-security-testing:latest [arguments]
```

Replace `[arguments]` with the actual arguments for the tool.

### Explanation of Docker run options:

- `--rm`: Automatically remove the container when it exits.
- `-it`: Run container in interactive mode.
- `-v $(pwd)/output:/output`: Mount the local `output` directory to `/output` in the container.
- `dynamic-application-security-testing:latest`: The name of the Docker image to run.

## Tool Usage

The Dynamic Application Security Testing Tool accepts several command-line arguments:

- `-t, --target`: (Required) Target Url to scan.
- `-ov, --output-via`: (Required) Specify output method: "file" or "webhook".
- `-w, --webhook`: Webhook URL (required if output_via is "webhook").
- `-o, --output`: File path for output (required if output_via is "file").
- `-l, --log`: Log level (DEBUG or ERROR, default is DEBUG).

### Example Commands:

1. Scan a target and output to a file:
   ```bash
   sudo docker run --rm -it -v $(pwd)/output:/output dynamic-application-security-testing:latest -t https://juice-shop.herokuapp.com -ov file -o /output/results.json
   ```

2. Scan a target  and send results to a webhook:
   ```bash
   sudo docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock dynamic-application-security-testing:latest -t http://www.vulnweb.com/ -ov webhook -w https://your-webhook-url.com
   ```


Note: When using file output, you need to mount volumes to access the results from your host machine.

## Troubleshooting

1. **Permission Issues**: If you encounter permission problems when writing to mounted volumes, you may need to adjust the permissions or use a named volume.

2. **Network Issues**: Ensure your Docker network settings allow the container to access the target network or webhook URL.

3. **Missing Requirements**: If the build fails due to missing requirements, check that your `requirements.txt` file is up to date and includes all necessary dependencies.



## Additional Information

- The tool uses Python 3.9 as specified in the Dockerfile.
- The tool uses the official ZAP stable Docker image as a base.
- The DAST Tool integrates ZAP for web application security assessments. ZAP commands are used internally for different scan modes:

   - Baseline Scan: ```zap-baseline.py -t {target} -J {output}```
   - Full Scan: ```zap-full-scan.py -t {target} -J {output}```
   - API Scan: ```zap-api-scan.py -t {target} -f openapi -J {output}```


## Key Features

**Multiple Scan Types**: Supports baseline, full, and API-specific scans.
**Automated Scanning**: Automatically scans web applications for security vulnerabilities.
**Comprehensive Reporting**: Generates detailed reports of found vulnerabilities.
**Customizable**: Allows for custom configurations and scan policies.
**Integration-Ready**: Can be easily integrated into CI/CD pipelines.


### ZAProxy HELP COMMAND OUTPUT
- [HELP.md](HELP.md) - A detailed prowler `[provide]` --help  command response.

For more information or to report issues, please refer to the project's documentation or repository.