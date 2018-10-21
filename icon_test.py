from time import sleep

from papirus import PapirusImage

image = PapirusImage()

icons = ["clear-day.bmp",
          "clear-night.bmp",
          "rain.bmp",
          "snow.bmp",
          "sleet.bmp",
          "wind.bmp",
          "fog.bmp",
          "cloudy.bmp",
          "partly-cloudy-day.bmp",
          "partly-cloudy-night.bmp"
]

prefix = './assets/icons/'
for icon in icons:
    path = prefix + icon
    image.write(path)
    sleep(5)
