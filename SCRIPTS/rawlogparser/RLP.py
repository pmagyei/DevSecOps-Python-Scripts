raw_logs = [
    "192.168.1.50 - GET /index.html 200",
    "10.0.0.12 - POST /login.php 404",
    "172.16.0.4 - GET /assets/logo.png 200",
    "192.168.1.50 - GET /admin_panel 404",
    "203.0.113.8 - GET /about_us 200"
]


for log in raw_logs:
    if "404" in log: # if error 404 is in one the loga, include that log in the subsequent line of code
        print(log.split(" ")[0])
        # .split(" ") is used to chop the list contents into substring using spaces
        # [0] is then used to select index 0 of the substring the log list



