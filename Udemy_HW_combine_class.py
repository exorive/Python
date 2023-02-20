# The task

# 1. Create the Image class
# 2. Each instance of the Image class must have
# three attributes: resolution, title, extension
# 3. The class must have a resize method that
# method you can use to change the resolution of the image. You just have to change
# resolution attribute
# 4. Create multiple instances of the Image class and call the resize method

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution


# Example usage
image1 = Image("1920x1080", "beach", "jpg")
image2 = Image("1280x720", "mountain", "png")

print(f"Before resize: {image1.title} - {image1.resolution}")
image1.resize("3840x2160")
print(f"After resize: {image1.title} - {image1.resolution}")

print(f"Before resize: {image2.title} - {image2.resolution}")
image2.resize("2560x1440")
print(f"After resize: {image2.title} - {image2.resolution}")








