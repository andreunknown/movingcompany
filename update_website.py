
import os
import sys

# Function to get the path to a subfolder
def get_subfolder_path(subfolder_name):
    return '/Users/andrecamara/👀 VisualOffline/Moving Company/website/movingcompany/pictures/' + subfolder_name

# Function to append the img tags for the images in a subfolder to the images.html file
def append_images_to_html(subfolder_path):
    image_names = os.listdir(subfolder_path)
    img_tags = ['<img class="lazy" data-src="' + subfolder_path + '/' + image_name + '" alt="' + image_name + '">' for image_name in image_names]
    with open('/Users/andrecamara/👀 VisualOffline/Moving Company/website/movingcompany/images.html', 'a') as f:
        f.write('
'.join(img_tags))

# Function to update the index.html file to include the images.html file and the lazyload.js file
def update_index_html():
    with open('/Users/andrecamara/👀 VisualOffline/Moving Company/website/movingcompany/index.html', 'r') as f:
        html = f.read()
    if '<!--#include virtual="images.html" -->' not in html:
        html = html.replace('<body>', '<body>
<!--#include virtual="images.html" -->')
    if '<script src="lazyload.js"></script>' not in html:
        html = html.replace('</body>', '<script src="lazyload.js"></script>
</body>')
    with open('/Users/andrecamara/👀 VisualOffline/Moving Company/website/movingcompany/index.html', 'w') as f:
        f.write(html)

# Main script
if __name__ == '__main__':
    subfolder_name = sys.argv[1]
    subfolder_path = get_subfolder_path(subfolder_name)
    append_images_to_html(subfolder_path)
    update_index_html()
