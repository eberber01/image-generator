# -------------------------- MODIFY PARAMETERS HERE -------------------------- #
NUMBER_OF_IMAGES = 10 # <--- Change the number of produced images

# Add as many compnents needed
# "name" key must be the same name as the directory/folder that holds that layer of images
# "amount" key is the amount of images in that directory/folder

imageSchema = [
    {
        'name':"background",      #   <---- Bottom Image 
        'amount': 5               
    },
    {
        'name':"body",
        'amount':1
    },
    {
        'name':"eye",
        'amount': 18
    },
    {
        'name':"mouth",          # <----- Top Image
        'amount': 11
    },
]

# ---------------------------------------------------------------------------- #