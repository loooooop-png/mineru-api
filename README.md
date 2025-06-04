# MinerU API  
## Usage  
### Init container  
You should run docker container at first:  
    docker-compose up -d  
And then, visit website http://127.0.0.1:8080/docs, you can see:  
![api_website](https://github.com/loooooop-png/mineru-api/blob/main/images/api_website.png)
### Interface 1  
You can input a pdf file and Interface 1 will use MinerU automatically to process the pdf.  
![mineru_interface](https://github.com/loooooop-png/mineru-api/blob/main/images/mineru_interface.png)
### Interface 2  
In this interface, you should input the name of the pdf that you input in Interface 1 and the name shouldn't include .pdf. And you can click **Download file** that I marked by red box。
![download_interface](https://github.com/loooooop-png/mineru-api/blob/main/images/download_interface.png)