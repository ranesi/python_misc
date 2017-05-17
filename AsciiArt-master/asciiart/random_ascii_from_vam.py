import asciify
import vam

# Get random image
print('Fetching a random image from the V&A collection...')
filename = vam.download_random_vam_image()
print('done, saved as ' + filename)

asciify.ascii_art(filename)
