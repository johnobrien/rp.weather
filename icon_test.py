from time import sleep

from papirus import PapirusComposite

textNImg = PapirusComposite(False)

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
    textNImg.AddText(icon, 10, 10, Id="Icon_Name")
    path = prefix + icon
    textNImg.AddImg(path, 20, 20, (100,100) Id="Icon_Image")
    textNImg.WriteAll()
    sleep(1)
