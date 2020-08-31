FROM python:3.7

MAINTAINER Maciej Garbacz <maciejgarbacz7@gmail.com>

# set work directory
WORKDIR /src

# copy requirements.txt
COPY ./requirements.txt /src/app/requirements.txt

# install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# set work directory
WORKDIR /src

# set app port
EXPOSE 5000

# Run app.py when the container launches
CMD [ "python3", "/src/main.py"]