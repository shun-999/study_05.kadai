import eel
import desktop
import possys

app_name="web"
end_point="desktop.html"

@eel.expose
def order_finish(code, num):
    possys.main1(code, num)

@eel.expose
def col_finish(depo):
    possys.main2(depo)

desktop.start(app_name, end_point)