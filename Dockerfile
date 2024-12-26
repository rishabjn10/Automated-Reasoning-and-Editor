# Use official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory
COPY . .

# Create output directory
RUN mkdir -p /app/output

# Run crewai flow kickoff
CMD ["crewai", "flow", "kickoff"]
