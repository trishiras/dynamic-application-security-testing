##********************** MAIN BUILD **********************##
FROM ghcr.io/zaproxy/zaproxy:stable


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /usr/src/app


# Copy the current directory contents into the container
COPY . .


# Install dependencies and the package
RUN pip install --no-cache-dir --user --root-user-action=ignore -r requirements.txt && \
    python setup.py install --user && \
    rm -rf /root/.cache/pip


# Add /home/zap/.local/bin to PATH
# As it is where dynamic_application_security_testing executable is in this image
ENV PATH=$PATH:/home/zap/.local/bin



# Run dynamic-application-security-testing when the container launches
ENTRYPOINT ["dynamic_application_security_testing"]