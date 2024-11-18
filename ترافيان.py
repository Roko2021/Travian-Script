from tkinter import *
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import threading

# def ty():
#     threading.Thread(target=def)


def login():
    driver = webdriver.Firefox()
    with open("login.txt", "r") as file:
        for line in file:
            user, passw, url = line.split(",")

        def Trav():
            root = Tk()
            root.title("Travian")
            root.geometry("350x180")

            wood1 = Label(root, text="wood1")
            wood1.grid(row=0, column=0, padx=5, pady=5)
            wood11 = Entry(root, width=4)
            wood11.grid(row=0, column=1)

            wood2 = Label(root, text="wood2")
            wood2.grid(row=1, column=0, padx=5, pady=5)
            wood12 = Entry(root, width=4)
            wood12.grid(row=1, column=1)

            wood3 = Label(root, text="wood3")
            wood3.grid(row=2, column=0, padx=5, pady=5)
            wood13 = Entry(root, width=4)
            wood13.grid(row=2, column=1)

            wood4 = Label(root, text="wood4")
            wood4.grid(row=3, column=0, padx=5, pady=5)
            wood14 = Entry(root, width=4)
            wood14.grid(row=3, column=1)

            steel1 = Label(root, text="steel1")
            steel1.grid(row=0, column=2, padx=5, pady=5)
            steel11 = Entry(root, width=4)
            steel11.grid(row=0, column=3)

            steel2 = Label(root, text="steel2")
            steel2.grid(row=1, column=2, padx=5, pady=5)
            steel12 = Entry(root, width=4)
            steel12.grid(row=1, column=3)

            steel3 = Label(root, text="steel3")
            steel3.grid(row=2, column=2, padx=5, pady=5)
            steel13 = Entry(root, width=4)
            steel13.grid(row=2, column=3)

            steel4 = Label(root, text="steel4")
            steel4.grid(row=3, column=2, padx=5, pady=5)
            steel14 = Entry(root, width=4)
            steel14.grid(row=3, column=3)

            mud1 = Label(root, text="mud1")
            mud1.grid(row=0, column=4, padx=5, pady=5)
            mud11 = Entry(root, width=4)
            mud11.grid(row=0, column=5)

            mud2 = Label(root, text="mud2")
            mud2.grid(row=1, column=4, padx=5, pady=5)
            mud12 = Entry(root, width=4)
            mud12.grid(row=1, column=5)

            mud3 = Label(root, text="mud3")
            mud3.grid(row=2, column=4, padx=5, pady=5)
            mud13 = Entry(root, width=4)
            mud13.grid(row=2, column=5)

            mud4 = Label(root, text="mud4")
            mud4.grid(row=3, column=4, padx=5, pady=5)
            mud14 = Entry(root, width=4)
            mud14.grid(row=3, column=5)

            Wheat1 = Label(root, text="Wheat1")
            Wheat1.grid(row=0, column=7, padx=5, pady=5)
            Wheat11 = Entry(root, width=4)
            Wheat11.grid(row=0, column=8)

            Wheat2 = Label(root, text="Wheat2")
            Wheat2.grid(row=1, column=7, padx=5, pady=5)
            Wheat12 = Entry(root, width=4)
            Wheat12.grid(row=1, column=8)

            Wheat3 = Label(root, text="Wheat3")
            Wheat3.grid(row=2, column=7, padx=5, pady=5)
            Wheat13 = Entry(root, width=4)
            Wheat13.grid(row=2, column=8)

            Wheat4 = Label(root, text="Wheat4")
            Wheat4.grid(row=3, column=7, padx=5, pady=5)
            Wheat14 = Entry(root, width=4)
            Wheat14.grid(row=3, column=8)

            Wheat5 = Label(root, text="Wheat4")
            Wheat5.grid(row=4, column=7, padx=5, pady=5)
            Wheat15 = Entry(root, width=4)
            Wheat15.grid(row=4, column=8)

            Wheat6 = Label(root, text="Wheat4")
            Wheat6.grid(row=5, column=7, padx=5, pady=5)
            Wheat16 = Entry(root, width=4)
            Wheat16.grid(row=5, column=8)

            def refresh():
                driver.get(
                    "https://ts30.x3.international.travian.com/dorf1.php?newdid=28464&"
                )
                time.sleep(2)
                driver.get("https://ts30.x3.international.travian.com/dorf1.php")

            def Ttwer():
                # wood1
                while True:
                    try:
                        refresh()
                        print("1")
                        time.sleep(5)
                        print("2")
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=3&gid=1"
                        )
                        print("3")
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        wood111 = wood11.get()
                        wood112 = float(wood111)
                        print("4")
                        if wood112 >= wood_5:
                            print("5")
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wood1")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=3&gid=1"
                                    )
                                    time.sleep(10)
                            # wood_5 += 1
                            # if a >= 3 :
                            #     break
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=3&gid=1"
                            )

                        time.sleep(5)
                        refresh()

                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=1&gid=1"
                        )
                        time.sleep(2)
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        wood122 = wood12.get()
                        wood123 = float(wood122)
                        if wood123 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wood2")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=1&gid=1"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=1&gid=1"
                            )

                        time.sleep(2)
                        refresh()
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=14&gid=1"
                        )
                        time.sleep(2)
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        wood132 = wood13.get()
                        wood133 = float(wood132)
                        if wood133 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wood3")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=14&gid=1"
                                    )
                                    time.sleep(10)
                            print("hi")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=14&gid=1"
                            )
                        time.sleep(2)
                        refresh()
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=17&gid=1"
                        )
                        time.sleep(2)
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        print("here")
                        wood142 = wood14.get()
                        wood143 = float(wood142)
                        if wood143 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wood4")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=17&gid=1"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=17&gid=1"
                            )

                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=11&gid=3"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        steel111 = steel11.get()
                        steel112 = float(steel111)
                        if steel112 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop steel1")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=11&gid=3"
                                    )
                                    time.sleep(10)
                            # steel_115 += 1
                            # if a >= 3 :
                            #     break
                            print("steel11")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=11&gid=3"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=7&gid=3"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        steel121 = steel12.get()
                        steel122 = float(steel121)
                        if steel122 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop steel2")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=7&gid=3"
                                    )
                                    time.sleep(10)
                            # steel_124 += 1
                            # if a >= 3 :
                            #     break
                            print("steel21")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=7&gid=3"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=10&gid=3"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        steel131 = steel13.get()
                        steel132 = float(steel131)
                        if steel132 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop steel3")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=10&gid=3"
                                    )
                                    time.sleep(10)
                            # steel_134 += 1
                            # print("steel3")
                            # if a >= 3 :
                            #     break
                            print("steel31")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=10&gid=3"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=4&gid=3"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        steel141 = steel14.get()
                        steel142 = float(steel141)
                        if steel142 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop steel4")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=4&gid=3"
                                    )
                                    time.sleep(10)
                            # steel_144 += 1
                            # if a >= 3 :
                            #     break
                            print("steel41")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=4&gid=3"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=6&gid=2"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        mud111 = mud11.get()
                        mud112 = float(mud111)
                        if mud112 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop mud1")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=6&gid=2"
                                    )
                                    time.sleep(10)
                            # mud_114 += 1
                            # if a >= 3 :
                            #     break
                            print("mud11")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=6&gid=2"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=5&gid=1"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        mud121 = mud12.get()
                        mud122 = float(mud121)
                        if mud122 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop mud2")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=5&gid=1"
                                    )
                                    time.sleep(10)
                            # mud_124 += 1
                            print("mud2")
                            # if a >= 3 :
                            # break
                            print("mud21")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=5&gid=2"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=18&gid=2"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        mud131 = mud13.get()
                        mud132 = float(mud131)
                        if mud132 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop mud3")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=18&gid=2"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1

                            # if a >= 3 :
                            #     break
                            print("mud31")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=18&gid=2"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=16&gid=2"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        mud141 = mud14.get()
                        mud142 = float(mud141)
                        if mud142 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop mud4")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=16&gid=2"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("steel41")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=16&gid=2"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=2&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat111 = Wheat11.get()
                        Wheat112 = float(Wheat111)
                        if Wheat112 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat1")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=2&gid=4"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi2")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=2&gid=4"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=15&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat121 = Wheat12.get()
                        Wheat122 = float(Wheat121)
                        if Wheat122 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat2")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=15&gid=4"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi2")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=15&gid=4"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=9&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat131 = Wheat13.get()
                        Wheat132 = float(Wheat131)
                        if Wheat132 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat3")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=9&gid=4"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi2")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=9&gid=4"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=13&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat141 = Wheat14.get()
                        Wheat142 = float(Wheat141)
                        if Wheat142 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat4")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=13&gid=4"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi2")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=13&gid=4"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=8&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat151 = Wheat15.get()
                        Wheat152 = float(Wheat151)
                        if Wheat152 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat5")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=8&gid=4"
                                    )
                                    time.sleep(10)
                            # wood_125 += 1
                            # if a >= 3 :
                            #     break
                            print("hi2")
                            driver.get(
                                "https://ts30.x3.international.travian.com/build.php?id=8&gid=4"
                            )
                        time.sleep(2)
                        refresh()
                        time.sleep(2)
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=12&gid=4"
                        )
                        # mostawa()
                        wood_2 = driver.find_element(By.CLASS_NAME, "level")
                        wood_3 = wood_2.text
                        wood_4 = wood_3.replace("المستوى ", "")
                        wood_5 = float(wood_4)
                        Wheat161 = Wheat16.get()
                        Wheat162 = float(Wheat161)
                        if Wheat162 >= wood_5:
                            # twood3()
                            while True:
                                try:
                                    print("warehouse3")
                                    # warehouse
                                    time.sleep(5)
                                    have = driver.find_element(
                                        By.CLASS_NAME, "warehouse"
                                    )
                                    have1 = have.text.split()
                                    sn, wa, na, sa = have1
                                    rwo = float(wa)
                                    rnu = float(na)
                                    rst = float(sa)

                                    have2 = driver.find_element(
                                        By.CLASS_NAME, "granary"
                                    )
                                    have21 = have2.text.split()
                                    sa, wh, sb = have21
                                    rwh = float(wh)

                                    # how many i need resources
                                    need = driver.find_element(
                                        By.CLASS_NAME, "inlineIconList.resourceWrapper"
                                    )
                                    need1 = need.text.split()
                                    wo, nu, st, wg, _ = need1
                                    nwo = float(wo)
                                    nnu = float(nu)
                                    nst = float(st)
                                    nwg = float(wg)

                                    if (
                                        nwo <= rwo
                                        and nnu <= rnu
                                        and nst <= rst
                                        and nwg <= rwh
                                    ):
                                        print("93")
                                        time.sleep(5)
                                        driver.get(
                                            "https://ts30.x3.international.travian.com/dorf1.php"
                                        )
                                        print("103")
                                        break

                                    else:
                                        print("12")
                                        time.sleep(5)
                                        wood_t2 = driver.find_element(
                                            By.CLASS_NAME, "inlineIcon.duration"
                                        )
                                        wood_t3 = wood_t2.find_element(
                                            By.TAG_NAME, "span"
                                        )
                                        wood_t4 = wood_t3.text
                                        h, m, s = wood_t4.split(":")
                                        th = float(h) * 60 * 60
                                        tth = th * 60 * 60
                                        ttm = float(m) * 60
                                        ts = float(s)
                                        tts = tth + ttm + ts

                                        wood_t7 = driver.find_element(
                                            By.CLASS_NAME, "textButtonV1.green.build"
                                        )
                                        wood_t7.click()
                                        time.sleep(tts + 10)
                                        print("13")
                                        break
                                except:
                                    time.sleep(10)
                                    print("stop wheat6")
                                    driver.get(
                                        "https://ts30.x3.international.travian.com/build.php?id=12&gid=4"
                                    )
                                    time.sleep(10)
                        # wood_125 += 1
                        # if a >= 3 :
                        #     break
                        print("hi2")
                        driver.get(
                            "https://ts30.x3.international.travian.com/build.php?id=12&gid=4"
                        )

                        break

                    except:
                        print("not conect")
                        time.sleep(5)

            # Button

            Button1 = Button(
                root, text="تطوير", command=threading.Thread(target=Ttwer).start
            )
            Button1.grid(row=5, column=4, ipadx=10)

            root.mainloop()

    while True:
        try:
            time.sleep(5)
            driver.get(url)

            username = driver.find_element(By.NAME, "name")
            password = driver.find_element(By.NAME, "password")
            username.clear()
            username.send_keys(user)
            password.clear()
            password.send_keys(passw)
            btnlogin = driver.find_element(By.TAG_NAME, "button")
            btnlogin.click()

            Trav()
            break
        except:
            print("not conect")


def User():
    # make table
    root = Tk()
    root.title("Travian")
    root.geometry("260x140")

    # enter table and id and url
    trav = Label(root, text="Travian", font="calibre 20 bold")
    trav.grid(row=0, column=0, padx=10)

    # ID and url
    username = Label(root, text=("UserName"))
    username.grid(row=1, column=0)
    username1 = Entry(root, width=20)
    username1.grid(row=1, column=2)

    password = Label(root, text=("Password"))
    password.grid(row=2, column=0)
    password1 = Entry(root, width=20)
    password1.grid(row=2, column=2)

    url = Label(root, text=("url"))
    url.grid(row=3, column=0)
    url1 = Entry(root, width=20)
    url1.grid(row=3, column=2)

    def save():
        username12 = username1.get()
        password12 = password1.get()
        url12 = url1.get()
        with open("login.txt", "w") as file:
            file.write(f"{username12},{password12},{url12}")
            file.close
        login()

    # root.destroy()

    # Button
    enter = Button(root, text=("Enter"), command=threading.Thread(target=save))
    enter.grid(row=4, column=2, sticky="we")

    root.mainloop()


if os.path.exists("login.txt"):
    login()

else:
    User()
