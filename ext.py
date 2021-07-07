from lib.smartdict import convert

# Add new directories for other file extentions (read README.md)
# Format: [ [list of extentions], path ]
# Path starts with C:/Users/yourlogin

extentions = convert([
    # Documents
    [["doc", "docx", "pdf", "ppt", "pptx", "txt"], "/Documents"],

    # Images
    [["png", "jpg", "jpeg", "jfif", "gif", "tiff", "webp", "svg", "tif"], "/Pictures"],

    # Videos
    [["mov", "mp4"], "/Videos"],

    # Audio
    [["mp3", "wav"], "/Music"]
])