import eel
import desktop
import possys

app_name="web"
end_point="desktop.html"
posl1 = possys.Main()

@eel.expose
def order_finish(code, num):
    posl1.main1(code, num)

@eel.expose
def col_finish(depo):
    posl1.main2(depo)

desktop.start(app_name, end_point)