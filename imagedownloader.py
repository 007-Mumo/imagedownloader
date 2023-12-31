import httprequests
import time

img_urls=[
'https://unsplash.com/photos/a-large-body-of-water-surrounded-by-mountains-ASLZdaigJH8'
'https://unsplash.com/photos/a-night-sky-with-a-shooting-star-and-a-joshua-tree-4zjF9-s-gac'
'https://unsplash.com/photos/XzEqlPQsLdI'
]
t1= time.perf_counter()


for img_url in img_urls:
    img_bytes =httprequests.get(img_url).content
    img_name =img_url.split('/')[3]
    img_name =f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f' {img_name} was downloaded.....')


t2=time.perf_counter()

print(f'finished in {t2-t1} seconds')