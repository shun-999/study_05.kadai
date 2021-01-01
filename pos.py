import eel
import desktop
import possys

app_name="web"
end_point="desktop.html"
posl1 = possys.Main()

@eel.expose
def master_finish(file_name):
    posl1.master_input(file_name)

@eel.expose
def order_finish(code, num):
    posl1.order_input(code, num)

@eel.expose
def calculation_finish(deposit, count):
    posl1.calculation_result(deposit, count)

desktop.start(app_name, end_point)