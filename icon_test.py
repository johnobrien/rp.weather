from time import sleep

from papirus import PapirusComposite


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
    textNImg = PapirusComposite(False)
    textNImg.AddText(icon, 10, 110, Id="Icon_Name")
    textNImg.AddImg(path, 10, 0, (100,100), Id="Icon_Image")
    textNImg.WriteAll()
    sleep(1)
