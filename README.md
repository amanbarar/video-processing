# Video-Processing

The objective of this repo is to create a Python web service using Django framework and PostgreSQL database engine.
This project provides two main functionalities: audio extraction and watermarking.

# Installation Steps

## Requirements

The following are required to be installed in the system.

- Docker
- Postman

## Instructions

Clone this repository on your system using CLI

```sh 
git clone https://github.com/amanbarar/video-processing.git
```

Go into the project directory and then run Docker commands

```sh
cd video-processing
docker-compose up -d --build
```

The backend Django server will run on PORT 8000. 

**NOTE** : The build may fail some time due to limited connectivity so I would suggest to run the docker command again

```sh
docker ps
```

Run this command to ensure that the containers are running. There are two docker containers that are being used:

- `web` which runs our Django backend
- `db` which runs our PostgreSQL database

And our network `video-processing_default` which connects our two containers.

There is one volume `video-processing_postgres_data` which helps in persisting our data within the database.

After making sure that the containers are running, run these scripts to make migrations into the database.

```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

The main django project is `video_processing` and admin dashboard can be accessed from here `http://127.0.0.1:8000/admin`.

It requires username and password which can be created by this simple command:

```sh
docker-compose exec web python manage.py createsuperuser
```

**Postman** is **required** for testing the APIs. You can import the requests via `viyoai_api_testing.postman_collection` which is a json file and can be imported directly into the Postman.

## APIs

### 1) Audio extraction

- Separate app `audio_extraction` has been created for this purpose.

- It consists of one table `Audio extractions` which stores id, video, audio, and extraction timestamp.

- The api is routed to `http://127.0.0.1:8000/audio-extraction/audio-extract/` and requires one key parameter `video`, which will be converted to an mp3 audio file.

- The response will be a json file which consists of an `audio_url`, this url can either directly be clicked in postman and get request can be sent on the url in order to get the mp3 file, or it can be copied and pasted on the browser, add IP and the port on which django is operating (which is 8000).

### 2) Watermarking

- Separate app `watermarking` has been created for this purpose.

- It consists of two tables, `Watermarks` which consists of id, image and upload time, and another table is `Watermarked videoss` which has fields like id, watermark image, position of the watermark, and extraction timestamp.

- The api is routed to `http://127.0.0.1:8000/watermark/watermark-overlay/` and requires 4 key parameters, `video`, `watermark`, `position_x`, and `position_y` which are by default set as 0.
**NOTE** - If you are not setting values to `position_x` and `position_y`, uncheck the key-values of these two.

- The response will be a json file which consists of a message, and `processed_video_url`, this url can either directly be clicked in postman and get request can be sent on the url in order to get the mp3 file, or it can be copied and pasted on the browser, add IP and the port on which django is operating (which is 8000).

## Efficient Architecture Design

### Handling multiple requests concurrently

- To handle multiple video processing requests concurrently, we can handle tasks asynchronously which will help in parallel processing.

- **Celery** is a good fit for this role as it is used for its reliable message broker and multiple worker nodes, it can decoulpe tasks which helps in faster processing.

- Celery can be configured inside the django project.

- After configuring Celery instance, we can set up the message broker. The message broker will communicate between the application and the tasks.

- We can easily define the tasks that needs to be executed asynchronously.

### Optimizing resources

- Since video processing is CPU intensive, it can be dealt by Celery workers which will prevent the main application from being unresponsive to heavy load.

- We can cache processed videos which are very redundant and are frequently accessed.
