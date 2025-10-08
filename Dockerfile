FROM python:3.10.4-slim-buster

ENV DEBIAN_FRONTEND=noninteractive

# Fix Buster repo location and install dependencies including ffmpeg
RUN sed -i 's|http://deb.debian.org|http://archive.debian.org|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        wget \
        bash \
        neofetch \
        software-properties-common \
        build-essential \
        ca-certificates \
        ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip wheel && \
    pip3 install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . .

# Expose port for Flask (webhook)
EXPOSE 5000

# Run bot + Flask webhook
CMD ["sh", "-c", "python3 -m devgagan & flask run -h 0.0.0.0 -p 5000"]
