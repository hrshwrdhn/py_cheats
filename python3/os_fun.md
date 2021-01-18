## Create folder if path not exist
```
if not os.path.exists(savepath):
    os.makedirs(savepath)
```

## list folder or file in path
``` for imgname in os.listdir(imagepath) ```
