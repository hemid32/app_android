#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import  DropDown
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.base import runTouchApp
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty ,ListProperty
from kivy.uix.image import  Image
import sqlite3
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from bidi.algorithm import get_display
from kivy.uix.image import AsyncImage
import  os , time
import random
import shutil
from kivy.uix.popup import Popup
from kivy import clock
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
import os.path
from kivy.base import EventLoop

class PanelBuilderApp(App):  # display the welcome screen
    def build(self):
        global  sm , ss
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcomeScreen'))
        sm.add_widget(list_contry(name='list_contry'  ))
        sm.add_widget(shose_contry(name='shose_contry'))
        #sm.add_widget(result_vs(name='result_vs'))
        sm.add_widget(jeux_embdad(str('flag'),'non',name='jeux_embdad'))
        sm.add_widget(jeux_intro(name = 'jeux_intro'))
        sm.add_widget(info_contry('non' , name = 'info_contry'))
        #sm.add_widget(result_vs(['algeria','algeria'], name='result_vs'))
        return  sm





class WelcomeScreen(Screen): #welcomeScreen subclass
    def __init__(self, **kwargs): #constructor method
        super(WelcomeScreen, self).__init__(**kwargs) #init parent

        with self.canvas:
            Color(204/255, 204/255, 204/255,mode='rgb')
            Rectangle(size=(Window.width , Window.height))
        ##################
        EventLoop.window.bind(on_keyboard=self.hook_keyboarde)
        self.mm = 0


        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))



        #####################################  bar #########################

        #data
        #print(self.name)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\","/")+'/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4



        bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                    allow_stretch=True, keep_ratio=False)
        point  = Label(text= str(self.data_[0][0]), size_hint =(0.08,0.08),pos_hint={"x":0.74,"top":0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})


        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        bar.add_widget(image_star)
        bar.add_widget(self.image_home)
        bar.add_widget(star)
        bar.add_widget(image_point)
        bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################

        welcomePage = FloatLayout()

        reshaped_text1 = ar.reshape('ابدا')
        self.bidi_text1 = get_display(reshaped_text1)
        reshaped_text2 = ar.reshape(u"قائمة الدول")
        self.bidi_text2 = get_display(reshaped_text2)
        reshaped_text3 = ar.reshape(u"اختبر معلوماتك")
        self.bidi_text3 = get_display(reshaped_text3)
        reshaped_text4 = ar.reshape(u"قيم التطبيق")
        self.bidi_text4 = get_display(reshaped_text4)
        reshaped_text5 = ar.reshape(u"خروج")
        self.bidi_text5 = get_display(reshaped_text5)
        post_image = Image(source='post_image.png', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                            allow_stretch=True, keep_ratio=False)
        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.06))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.50))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.17))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.28))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.39))

        #welcomeBox1 = Button(text= self.bidi_text1,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.60} ,on_press=self.poptest)
        welcomeBox2 = Button(text= self.bidi_text2 ,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.49} ,on_press=self.information,background_color = (0.,0.,0.,0.),markup = True)
        welcomeBox3 = Button(text= self.bidi_text3,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.38} ,on_press=self.top_,background_color = (0.,0.,0.,0.))
        welcomeBox4 = Button(text= self.bidi_text4,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.27} ,on_press=self.top_,background_color = (0.,0.,0.,0.))
        welcomeBox1 = Button(text= self.bidi_text1,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.60} ,on_press=self.poptest, border =(25, 25, 25, 25),background_color = (0.,0.,0.,0.))
        welcomeBox5 = Button(text= self.bidi_text5,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.16} ,on_press=self.exite ,background_color = (0.,0.,0.,0.))
        #img_ptn1 = Image(source='post_image.png', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'top': 0.60},
        #                   allow_stretch=True, keep_ratio=False)



        welcomePage.add_widget(welcomeBox1)
        welcomePage.add_widget(welcomeBox2)
        welcomePage.add_widget(welcomeBox3)
        welcomePage.add_widget(welcomeBox4)
        welcomePage.add_widget(welcomeBox5)
        welcomePage.add_widget(post_image)
        #welcomePage.add_widget(img_ptn1)


        welcomePage.add_widget(bar)

        self.add_widget(welcomePage)
    def btn_(self,i):
        img_ptn2 = Image(source='home.png', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'top': 0.60},
                         allow_stretch=True, keep_ratio=False)
        self.add_widget(img_ptn2)
        #time.sleep(.9)

        self.poptest(0)

    def poptest(self,i):

        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.40), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False , title = 'attendre')
        self.p.open()
        Clock.schedule_once(self.mo9arana)
        self.p.dismiss()






    def mo9arana(self, instance):
        #sm.add_widget(shose_contry(name='shose_contry'))
        sm.switch_to(shose_contry())





    def information(self,instant):

        sm.switch_to(list_contry(name='list_contry'))


    def top_(self,instant):
        ##############################

        sm.switch_to(jeux_intro())

    def home(self,inst,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :
            sm.switch_to(WelcomeScreen())
        # x entre [Window.width*0.10 , Window.width*0.18 ]
        # y entre [Window.height*0.89 , Window.height*0.97]

    def exite(self,inst):

        welcomePage = FloatLayout()
        image2 = "non.png"
        img = Image(source=str(image2), size_hint=(1., 1.), pos_hint={'x': 0., 'y': 0.},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text='quite', size_hint=(0.440, 0.1), pos_hint={"x": 0.05, "top": 0.18})
        btn = Button(text='continu', size_hint=(0.440, 0.1), pos_hint={"x": 0.51, "top": 0.18})
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False)
        btn.bind(on_press=self.continu_)
        btn1.bind(on_press=self.quit)
        self.popup.open()


        #App.get_running_app().stop()
    def continu_(self,i):
        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())
    def quit(self,i):
        self.popup.dismiss()
        #App.get_running_app().stop()
        App.get_running_app().stop()

    def hook_keyboarde(self, window, key, *largs):

        # self.name




        if key == 27:
            self.mm += 1
            print(self.mm)
            if  self.mm == 1 :
                self.exite(0)
                return  True
            elif self.mm >= 2 :
                App.get_running_app().stop()




class shose_contry(Screen):
    sm = ScreenManager()
    def __init__(self, **kwargs): #constructor method
        super(shose_contry, self).__init__(**kwargs) #init parent
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)





        ############# data base ââââââââââââââââ
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'

        self.file = (db_path)
        self.conn = sqlite3.connect(self.file)
        self.cur = self.conn.cursor()
        sql = ''' SELECT * FROM table_1 '''
        self.cur.execute(sql)
        self.data = self.cur.fetchall()
        ###########################
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))

        #####################################  bar #########################

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))

        bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        bar.add_widget(image_star)
        bar.add_widget(self.image_home)
        bar.add_widget(star)
        bar.add_widget(image_point)
        bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################

        post_image = Image(source='post_image.png', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        post_image2 = Image(source='comparing.jpg', size_hint=(0.9, 0.18), pos_hint={'x': 0.05, 'y': 0.30},
                           allow_stretch=True, keep_ratio=False)

        func = FloatLayout()
        self.dropdown = DropDown()
        self.dropdown2 = DropDown()


        self.welcomeBox1 = Button(text= 'ok', size_hint =(0.6,0.1),pos_hint={"x":0.20,"top":0.25} ,background_color = (0.,0.,0.,0.))
        #self.welcomeBox2 = Button(text='home page', size_hint=(0.3, 0.1), pos_hint={"x": 0.350, "top": 0.90})


        #list_contry
        func.add_widget(self.welcomeBox1)
        func.add_widget(bar)
        reshaped_text1 = (u"اضغط لاختيار دولة")
        text_1 = ar.reshape(reshaped_text1)
        text_1 = get_display(text_1)
        self.text_1 = text_1
        with self.canvas:
            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')
            Rectangle(size=(Window.width * 0.44, Window.height * 0.1), pos=(Window.width * 0.51, Window.height * 0.50))
            Rectangle(size=(Window.width * 0.44, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.50))
            Rectangle(size=(Window.width * 0.6, Window.height * 0.1), pos=(Window.width * 0.20, Window.height * 0.15))



        for index in self.data:
            btn = Button(text='%s' % index[28], size_hint_y=None, height=44)
            btn.bind(on_release=lambda  btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
            # create a big main button
            self.mainbutton = Button(text=text_1,font_name='hemidi', size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.60},background_color = (0.,0.,0.,0.))
            self.mainbutton.bind(on_release=self.dropdown.open)
            self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
            self.dropdown.bind(on_press=self.return_val)

        # self.dropdown.bind(on_select=self.return_val)
            #func.add_widget(dropdown)
        #self.add_widget(dropdown)
        for index in self.data:
            btn2 = Button(text='%s' % index[28], size_hint_y=None, height=44 ,on_release=lambda btn: self.return_val)
            btn2.bind(on_release=lambda btn2: self.dropdown2.select(btn2.text))
            self.dropdown2.add_widget(btn2)
            #################### button drop 2
            self.mainbutton2 = Button(text=text_1,font_name='hemidi', size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.60} , id = 'kiv',background_color = (0.,0.,0.,0.))
            self.mainbutton2.bind(on_release=self.dropdown2.open)

            self.dropdown2.bind(on_select=lambda instance, x: setattr(self.mainbutton2, 'text', x))
            self.dropdown2.bind(on_press=self.return_val)
            # self.a = dropdown2.container
        #setattr(self.mainbutton2, 'text',  )
        self.welcomeBox1.bind(on_press=self.return_val)  # list_contry
        #self.welcomeBox1.bind(on_press=self.list_contry)

        #self.b = dropdown.container

        func.add_widget(self.mainbutton)
        func.add_widget(self.mainbutton2)
        func.add_widget(post_image)
        func.add_widget(post_image2)

        self.add_widget(func)
        val2 = self.mainbutton2.text
        #self.val1 = 'f'


    def return_val(self,instant):
        val2 =  self.mainbutton2.text
        val1 = self.mainbutton.text
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()
        #print(val2,val1)

        if not (val1 == self.text_1 or val2 == self.text_1) :
            if not (self.data_[0][0] < 15):
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                db_path = BASE_DIR.replace("\\", "/") + '/data.db'
                self.file_h = (db_path)
                self.conn_h = sqlite3.connect(self.file_h)
                self.cur_h = self.conn_h.cursor()
                sql_h = ''' SELECT nombre_point FROM point'''
                self.cur_h.execute(sql_h)
                self.data_ = self.cur_h.fetchall()

                n = self.data_[0][0]
                if int(n) < 3:
                    m = 0
                else:

                    m = n - 4  ##################" -5

                self.cur_h.execute(
                    ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
                self.conn_h.commit()
                #print('yes')
                #sm.add_widget(result_vs(list([val1, val2]), name='result_vs'))
                #self.manager.current = 'result_vs'
                #sm.switch_to(result_vs(list([val1,val2])),direction='right', duration=1.)
                #print('iiiiii')
                self.val_ = list([val1, val2])
                self.puptest(0)
            else :
                self.return_jeux(0)
        else :
            pass

    def puptest(self,i):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.40), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False)
        self.p.open()
        Clock.schedule_once(lambda *args: self.eventes(0,self.val_))
        self.p.dismiss()


    def eventes(self,i,k):
        sm.add_widget(result_vs(k,name='result_vs'))
        sm.switch_to(result_vs(k))

    def return_jeux (self,instant):

        reshaped_text3= ar.reshape(u"العب و جمع النقاط")
        self.bidi_text3 = get_display(reshaped_text3)
        reshaped_text4 = ar.reshape(u"الصفحة الرئيسية")
        self.bidi_text4 = get_display(reshaped_text4)
        reshaped_text5 = ar.reshape(u"يجب ان تمتلك 15 نقطعة على الاقل ")
        self.bidi_text5 = get_display(reshaped_text5)

        welcomePage = FloatLayout()
        image2 = "cr.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.40), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=self.bidi_text4,font_name = 'hemidi' ,size_hint=(0.30, 0.1), pos_hint={"x": 0.19, "top": 0.30})
        btn = Button(text=self.bidi_text3,font_name = 'hemidi' , size_hint=(0.30, 0.1), pos_hint={"x": 0.51, "top": 0.30})
        label_cont2 = Label(text=self.bidi_text5,font_name='hemidi', font_size='20sp',size_hint=(0.4, 0.2), pos_hint={'x': 0.3, 'top': 0.95},markup = True)


        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)
        welcomePage.add_widget(label_cont2)

        # content = Button(text='Close me!')
        self.popup = Popup(title = 'sorry',content=welcomePage, auto_dismiss=False)

        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.vers_jeux)
        btn1.bind(on_press=self.vers_home)

        # open the popup
        self.popup.open()

    def vers_jeux(self,ins):
        self.popup.dismiss()
        sm.switch_to(jeux_intro())
    def vers_home(self,ins):
        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())


    def home(self,instant,touch):
        #self.manager.current = 'result_vs' #result_vs
        #self.manager.screens[2].ids.btn.text = self.mainbutton2.text
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :

            sm.switch_to(WelcomeScreen())

    def hook_keyboard(self, window, key, *largs):
        # self.name

        #print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            #EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            sm.switch_to(WelcomeScreen())
            return  True


class list_contry(Screen):
    def __init__(self, **kwargs ): #constructor method
        super( list_contry,self).__init__(**kwargs) #init parent
        self.hh(0)
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)





    def hh(self,i):
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))
        #####################################  bar #########################

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))

        bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        bar.add_widget(image_star)
        bar.add_widget(self.image_home)
        bar.add_widget(star)
        bar.add_widget(image_point)
        bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################



        func = FloatLayout()

        post_image = Image(source='post_image.png', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        func.add_widget(post_image)

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None , pos_hint ={"centre_x":0.30})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))


        ########################"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file = (db_path)
            self.conn = sqlite3.connect(self.file)
            self.cur = self.conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            self.cur.execute(sql)
            self.data = self.cur.fetchall()
        d=0
        self.ttt = 'non'
        d = 1
        """
        for i in self.data :
            d = d+1
            self.btn = Button(text=str(i[28]),id='%s'%(d) , size_hint_y=None,pos_hint={'x':0.3 ,'top':None} ,height=40 )
            # lambda instance, x: setattr(self.mainbutton2, 'text', x)
            self.btn.bind(on_press=lambda *args: self.vers_info_contry(0,d) )
            self.layout.add_widget(self.btn)
            
         """
        # add button manuale  20/03/2020
        #print(self.data[134][28])
        for  i  in range(1) :
            #
            btn1 =   Button(text=str(self.data[0][28]), size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press =lambda  *args : self.vers_info_contry(0,btn1.text)  ,background_normal = 'BTN.jpg')
            self.layout.add_widget(btn1)

            btn2 =   Button(text=str(self.data[1][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args :  self.vers_info_contry(0,btn2.text) )
            self.layout.add_widget(btn2)
            btn3 =   Button(text=str(self.data[2][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press =lambda  *args :   self.vers_info_contry(0,btn3.text) )
            self.layout.add_widget(btn3)
            btn4 =   Button(text=str(self.data[3][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn4.text) )
            self.layout.add_widget(btn4)
            btn5 =   Button(text=str(self.data[4][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args :  self.vers_info_contry(0,btn5.text) )
            self.layout.add_widget(btn5)
            btn6 =   Button(text=str(self.data[5][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press =lambda  *args :  self.vers_info_contry(0,btn6.text) )
            self.layout.add_widget(btn6)
            btn7 =   Button(text=str(self.data[6][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn7.text) )
            self.layout.add_widget(btn7)
            btn8 =   Button(text=str(self.data[7][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn8.text) )
            self.layout.add_widget(btn8)
            btn9 =   Button(text=str(self.data[8][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn9.text) )
            self.layout.add_widget(btn9)
            btn10 =   Button(text=str(self.data[9][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press =lambda  *args :  self.vers_info_contry(0,btn10.text) )
            self.layout.add_widget(btn10)
            btn11 =   Button(text=str(self.data[10][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn11.text) )
            self.layout.add_widget(btn11)
            btn12 =   Button(text=str(self.data[11][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn12.text) )
            self.layout.add_widget(btn12)
            btn13 =   Button(text=str(self.data[12][28]) , size_hint_y=None,pos_hint={'x':0.05 ,'top':None} ,height=40 , on_press = lambda  *args : self.vers_info_contry(0,btn13.text) )
            self.layout.add_widget(btn13)





        root = ScrollView(size_hint=(0.90, None) ,size=(Window.width, Window.height), pos_hint={"x":0.05,"top":0.60} ) #, size=(Window.width, Window.height)
        root.add_widget(self.layout)
        func.add_widget(root)
        func.add_widget(bar)

        self.add_widget(func)




    def home(self,instant,touch):
        #self.manager.current = 'welcomeScreen'
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :
            sm.switch_to(WelcomeScreen())




    def vers_info_contry(self,i,inst):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.40), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False)
        self.p.open()
        Clock.schedule_once(lambda *args: self.vers_info_contry_2(0,inst))
        self.p.dismiss()

    def vers_info_contry_2(self,i,inst):
        sm.switch_to(info_contry(inst))

    def hook_keyboard(self, window, key, *largs):
        # self.name

        #print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            #EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            sm.switch_to(WelcomeScreen())
            return  True




################################### hkendemti  fine

class result_vs(Screen):
    #code = StringProperty('')
    code = ListProperty()
    def __init__(self,acc, **kwargs ): #constructor method
        super(result_vs, self).__init__(**kwargs) #init parent
        EventLoop.window.bind(on_keyboard=self.poptest)
        self.lk = 0
        self.lk += 1
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))

        #####################################  bar #########################

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))

        self.bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        self.bar.add_widget(image_star)
        self.bar.add_widget(self.image_home)
        self.bar.add_widget(star)
        self.bar.add_widget(image_point)
        self.bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################

        # list = [val1 , val2]
        #print(acc)
        #print(acc)

        self.cr(0,acc)
        #print(self.code)


        ############# data base ââââââââââââââââ
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file = (db_path)
            self.conn = sqlite3.connect(self.file)
            self.cur = self.conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            self.cur.execute(sql)
            self.data = self.cur.fetchall()
        ###########################
        ##### valeur_contry1 et 2

    def cr(self,i,acc):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            file = (db_path)
            conn = sqlite3.connect(file)
            cur = conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            cur.execute(sql)
            data = cur.fetchall()



        status = ['عدد السكان'] * 100
        v_contry1 = []
        v_contry2 = []

        for i in data:
            if acc[0] == i[28]:
                for e in i:
                    v_contry1.append(e)
            if acc[1] == i[28]:
                for e in i:
                    v_contry2.append(e)

        #print(len(self.status))
        #print(len(self.v_contry1))
        #print(len(self.v_contry2))

        self.func = FloatLayout()

        self.layout = GridLayout(cols=3, spacing=10, size_hint_y=None, pos_hint={"centre_x": 0.02})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        #https://googledrive.com/host/<folderID>/<filename>
        #https://drive.google.com/uc?id=FILE_ID
        image1 =  'https://drive.google.com/uc?id=1Wo_j02PZP53uXoIVsw_5jXlkF0QWsnOh'   #flag.png'
        image1 = AsyncImage(source=image1)
        image2 = 'flag.png'
        img = Image(source=image2, size_hint=(0.2866, 0.23), pos_hint={'x': 0.05, 'y': 0.62},
                    allow_stretch=True, keep_ratio=False)
        img2 = Image(source=image2, size_hint=(0.2866, 0.23), pos_hint={'x': 0.6566, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)
        img3 = Image(source='vs.png', size_hint=(0.2866, 0.23), pos_hint={'x': 0.35, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)

        self.func.add_widget(img2)
        self.func.add_widget(img)
        self.func.add_widget(img3)
        self.func.add_widget(self.bar)


        for i in range(len(data[1])):



            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                         pos_hint={'x': 0.3, 'top': None}, height=40 )
            #print(v_contry1[i])

            self.btn1 = Button(text='hello2', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                          pos_hint={'x': 0.3, 'top': None}, height=40 )
            self.btn2 = Button(text='gg', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None},
                              height=40)






            #self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)
            self.layout.add_widget(self.btn2)

            reshaped_text = (status[i])
            self.bidi_text = get_display(reshaped_text)


            setattr(self.btn, 'text', str(v_contry1[i]))
            setattr(self.btn1, 'text', self.bidi_text)
            setattr(self.btn2, 'text', str(v_contry2[i]))
        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                          pos_hint={"x": 0.05, "top": 0.59})  # , size=(Window.width, Window.height)
        self.root.add_widget(self.layout)
        self.func.add_widget(self.root)
        self.add_widget(self.func)
        # self.add_widget(img)
    def update(self,instant):
        self.btn.text = 'hemidi'


    def press(self,instant):
            #print(self.contry_vs)

            pass
    def home(self,instant,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :

            sm.switch_to(WelcomeScreen())
    def jeux(self,instant):
        #self.manager.current = 'welcomeScreen'
        #print(self.code)
        pass
    def return_(self,window):

        sm.switch_to(shose_contry())


    def poptest(self,window , key , *args):
        if key == 27 :
            sm.switch_to(WelcomeScreen())
            return  True


class jeux_embdad(Screen): #welcomeScreen subclass
    coord = StringProperty('')
    def __init__(self, hemidi, rune, **kwargs): #constructor method
        super(jeux_embdad, self).__init__(**kwargs) #init parent
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))



        #####################################  bar #########################
        self.problem_continu_ok = 0

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
            text2 = u'هذا العلم لاي دولة ؟ '
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
            text2 = u'هذا الشعار  لاي دولة ؟ '
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
            text2 = u'هذه الخريطة لاي دولة ؟ '
        else:
            self.nv = 4
            text2=u'اجب حسب الصورة'



        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))

        bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        bar.add_widget(image_star)
        bar.add_widget(self.image_home)
        bar.add_widget(star)
        bar.add_widget(image_point)
        bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################


        ############################
        self.rune = rune
        self.minutes = 0
        self.seconds = 15
        self.file_j = hemidi  ## nome fime soit embadad or flag ect ..
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file_h = (db_path)
            self.conn_h = sqlite3.connect(self.file_h)
            self.cur_h = self.conn_h.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if self.rune == 'yes' :

            #print(self.data_[1][0])
            #print(self.data_[0][0])


            ############################



            nome_image = os.listdir(r"%s"%(self.file_j))

            self.img_embdad = random.choice(nome_image)

            welcomePage = FloatLayout()
            image2 = "%s/%s"%(str(self.file_j),str(self.img_embdad))
            nome_image.remove(self.img_embdad)
            cont =random.choices(nome_image , k=3)
            cont.append(self.img_embdad)
            #image2 = "embadad/spain.png"
            img = Image(source=str(image2), size_hint=(0.90, 0.30), pos_hint={'x': 0.05, 'y': 0.40},
                        allow_stretch=True, keep_ratio=False)






            l1 = random.choice(cont)
            welcomeBox1 = Button(text=str(l1), size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.35})
            welcomeBox1.bind(on_press=lambda *args: self.result_in(0,l1))

            cont.remove(l1)
            l2 = random.choice(cont)
            welcomeBox2 = Button(text=str(l2), size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.35})
            welcomeBox2.bind(on_press=lambda *args: self.result_in(0,l2))

            cont.remove(l2)
            l3 = random.choice(cont)
            welcomeBox3 = Button(text=str(l3), size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.22})
            welcomeBox3.bind(on_press=lambda *args: self.result_in(0,l3))


            cont.remove(l3)
            l4 = cont[0]
            welcomeBox4 = Button(text=str(l4), size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.22})
            welcomeBox4.bind(on_press=lambda *args: self.result_in(0,l4))
            text = ar.reshape(text2)
            self.text_label = get_display(text)

            btn1 = Label(text=self.text_label, font_name = 'hemidi',size_hint=(0.80,0.1),
                              pos_hint={'x': 0.1, 'top': 0.80})


            welcomePage.add_widget(welcomeBox1)
            welcomePage.add_widget(welcomeBox2)
            welcomePage.add_widget(welcomeBox3)
            welcomePage.add_widget(welcomeBox4)
            welcomePage.add_widget(bar)


            #self.event()
            self.timer_ = Label(text='niveau %s' % ('non'), size_hint=(0.24, 0.05), pos_hint={"x": 0.38, "top": 0.850})
            welcomePage.add_widget(self.timer_)





            welcomePage.add_widget(img)
            welcomePage.add_widget(btn1)

            self.add_widget(welcomePage)
            self.XI = '0'
            self.event =  Clock.schedule_interval(self.tmr, 1)

        else :
            pass


    def tmr(self, *args):
        self.seconds -=1
        if self.seconds == -1:
            self.seconds += 60
            self.minutes -= 1
        if self.minutes == 0 and self.seconds == 0:
            self.minutes = 0
            self.seconds = 0

        self.time_ = datetime.timedelta(minutes=self.minutes, seconds=self.seconds)
        l = str(self.time_)
        print(l)

        XI = 0

        if '-1 day' not in str(l):
            #self.root.ids.time.text = 'Time Over!'
            setattr(self.timer_, 'text', str(l))
            L = int(self.XI)
            L += 1
            self.XI = str(L)
        else :
            setattr(self.timer_, 'text', "over time")
            XI = 0

        if int(self.XI) == 15 :
            setattr(jeux_embdad, self.rune, 'non')
            self.result_in(0,'non')

            self.XI = '0'






    def home(self,instant,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :

            self.event.cancel()
            setattr(jeux_embdad, self.rune, 'non')
            setattr(jeux_embdad, self.XI, '0')
            sm.switch_to(WelcomeScreen())

    def result_in(self,n , l):
        self.event.cancel()
        setattr(jeux_embdad , self.rune , 'non')
        setattr(jeux_embdad, self.XI, '0')

        if self.img_embdad == str(l) :
            self.result_tru(0)
            #print('yess')
        else :
            self.result_false(0)
            #print("noooo")
    def result_tru(self,instant):
        setattr(jeux_embdad, self.rune, 'non')
        setattr(jeux_embdad, self.XI, '0')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file_h = (db_path)
            self.conn_h = sqlite3.connect(self.file_h)
            self.cur_h = self.conn_h.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()
        n = self.data_[0][0]



        self.cur_h.execute(''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;'''%(int(n)+3,int(n)))
        self.conn_h.commit()

        welcomePage = FloatLayout()
        image2 = "yes.png"
        img = Image(source=str(image2), size_hint=(1., 1.), pos_hint={'x': 0., 'y': 0.},
                    allow_stretch=True, keep_ratio=False)
        btn = Button(text='ok', size_hint=(0.70, 0.1), pos_hint={"x": 0.150, "top": 0.18})
        btn.bind(on_press=self.vers_)
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        #content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False)

        self.popup.open()

    def vers_(self,instant):
        self.popup.dismiss()
        self.problem_continu_ok += 1

        if self.problem_continu_ok == 1 :
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = BASE_DIR.replace("\\", "/") + '/data.db'
            with sqlite3.connect(db_path) as db:
                self.file_h = (db_path)
                self.conn_h = sqlite3.connect(self.file_h)
                self.cur_h = self.conn_h.cursor()
                sql_h = ''' SELECT nombre_point FROM point'''
                self.cur_h.execute(sql_h)
                self.data_ = self.cur_h.fetchall()



            if int(self.data_[0][0]) < 15:
                sm.switch_to(jeux_embdad("flag",'yes'))
            elif int(self.data_[0][0]) < 30:
                sm.switch_to(jeux_embdad("embadad",'yes'))
            elif int(self.data_[0][0]) < 45:
                sm.switch_to(jeux_embdad("map",'yes'))
            else :
                sm.switch_to(jeux_embdad("map",'yes'))




    def result_false(self,instant):

        setattr(jeux_embdad, self.rune, 'non')
        setattr(jeux_embdad, self.XI, '0')
        self.event.cancel()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'data.db')
        with sqlite3.connect(db_path) as db:
            self.file_h = (db_path)
            self.conn_h = sqlite3.connect(self.file_h)
            self.cur_h = self.conn_h.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        n = self.data_[0][0]
        if int(n)<3 :
            m=0
        else:

            m= n-3


        self.cur_h.execute(''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()

        welcomePage = FloatLayout()
        image2 = "non.png"
        img = Image(source=str(image2), size_hint=(1., 1.), pos_hint={'x': 0., 'y': 0.},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text='quite', size_hint=(0.440, 0.1), pos_hint={"x": 0.05, "top": 0.18})
        btn = Button(text='continu', size_hint=(0.440, 0.1), pos_hint={"x": 0.51, "top": 0.18})
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False)

        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.continu_)
        btn1.bind(on_press=self.quit)


        # open the popup
        self.popup.open()

    def quit(self, instant):
        # if result false and shose quite
        setattr(jeux_embdad, self.rune, 'non')

        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())

    def continu_(self,instant):
        # if result false and shose continu
        setattr(jeux_embdad, self.rune, 'non')
        self.popup.dismiss()
        self.problem_continu_ok +=1
        if self.problem_continu_ok == 1 :
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = BASE_DIR.replace("\\", "/") + '/data.db'
            with sqlite3.connect(db_path) as db:
                self.file_h = (db_path)
                self.conn_h = sqlite3.connect(self.file_h)
                self.cur_h = self.conn_h.cursor()
                sql_h = ''' SELECT nombre_point FROM point'''
                self.cur_h.execute(sql_h)
                self.data_ = self.cur_h.fetchall()

            if int(self.data_[0][0]) < 15:
                sm.switch_to(jeux_embdad("flag",'yes'))
            elif int(self.data_[0][0]) < 30:
                sm.switch_to(jeux_embdad("embadad",'yes'))
            elif int(self.data_[0][0]) < 50:
                sm.switch_to(jeux_embdad("map",'yes'))
            else :
                sm.switch_to(jeux_embdad("map",'yes'))

    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            setattr(jeux_embdad, self.rune, 'non')
            setattr(jeux_embdad, self.XI, '0')
            self.XI = '0'

            sm.switch_to(jeux_intro())
            return True






class jeux_intro(Screen):
    code = ListProperty()
    def __init__(self, **kwargs): #constructor method
        super(jeux_intro, self).__init__(**kwargs) #init parent
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))

        #####################################  bar #########################

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))

        bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        bar.add_widget(image_star)
        bar.add_widget(self.image_home)
        bar.add_widget(star)
        bar.add_widget(image_point)
        bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################

        welcomePage = FloatLayout()

        # image2 = "embadad/spain.png"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file_h = (db_path)
            self.conn_h = sqlite3.connect(self.file_h)
            self.cur_h = self.conn_h.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 50:
            self.nv = 3
        else:
            self.nv = 4

        image1 = 'frm.jpg'
        image2 = 'frm.jpg'
        image3 = 'frm.jpg'
        image4 = 'frm.jpg'
        image1_p = 'd_0_0_0_0_0.jpg'
        image2_p = 'd_0_0_0_0_0.jpg'
        image3_p = 'd_0_0_0_0_0.jpg'
        image4_p = 'd_0_0_0_0_0.jpg'

        if self.nv > 1 :
            image1 = 'ovr.jpg'
        if self.nv > 2 :
            image2 = 'ovr.jpg'
        if self.nv > 3 :
            image3 = 'ovr.jpg'
        if self.nv >= 4 :
            image4 = 'ovr.jpg'

        if self.nv == 1 :
            image1_p = self.calc(0,self.data_[0][0])

        if self.nv == 2 :
            image1_p = 'd_1_1_1_1_1.jpg'
            image2_p = self.calc(0,self.data_[0][0]-15)
        if self.nv == 3 :
            image1_p = 'd_1_1_1_1_1.jpg'
            image2_p = 'd_1_1_1_1_1.jpg'
            image3_p = self.calc(0, self.data_[0][0] - 30)
        if self.nv == 4 :
            image1_p = 'd_1_1_1_1_1.jpg'
            image2_p = 'd_1_1_1_1_1.jpg'
            image3_p = 'd_1_1_1_1_1.jpg'
            if self.data_[0][0] < 60 :
                image4_p = self.calc(0, self.data_[0][0] - 45)
            else :

                image4_p = self.calc(0, 15)

        post_image = Image(source='post_image.png', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        img1 = Image(source=str(image1), size_hint=(0.3, 0.200), pos_hint={'x': 0.15, 'y': 0.38},
                    allow_stretch=True, keep_ratio=False)
        img2 = Image(source=str(image2), size_hint=(0.3, 0.200), pos_hint={'x': 0.55, 'y': 0.38},
                     allow_stretch=True, keep_ratio=False)
        img3 = Image(source=str(image3), size_hint=(0.3, 0.200), pos_hint={'x': 0.15, 'y': 0.10},
                     allow_stretch=True, keep_ratio=False)
        img4 = Image(source=str(image4), size_hint=(0.3, 0.200), pos_hint={'x': 0.55, 'y': 0.10},
                     allow_stretch=True, keep_ratio=False)

        img1_p = Image(source=str(image1_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.15, 'y': 0.32},
                     allow_stretch=True, keep_ratio=False)
        img2_p = Image(source=str(image2_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.55, 'y': 0.32},
                     allow_stretch=True, keep_ratio=False)
        img3_p = Image(source=str(image3_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.15, 'y': 0.04},
                     allow_stretch=True, keep_ratio=False)
        img4_p = Image(source=str(image4_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.55, 'y': 0.04},
                     allow_stretch=True, keep_ratio=False)


        welcomePage.add_widget(img1)
        welcomePage.add_widget(img2)
        welcomePage.add_widget(img3)
        welcomePage.add_widget(img4)
        welcomePage.add_widget(img1_p)
        welcomePage.add_widget(img2_p)
        welcomePage.add_widget(img3_p)
        welcomePage.add_widget(img4_p)
        welcomePage.add_widget(bar)
        welcomePage.add_widget(post_image)

        if self.nv == 1:

            img1.bind(on_touch_down=self.top_)

        if self.nv ==  2:
            img2.bind(on_touch_down=self.top_)
        if self.nv == 3:
            img3.bind(on_touch_down=self.top_)
        if self.nv == 4 :
            img4.bind(on_touch_down=self.top_)


        self.add_widget(welcomePage)

    def calc(self,inst,val):
        stre = '0_0_0_0_0'
        l = int(val / 3)
        if l == 1:
            stre = '1_0_0_0_0'
        elif l == 2:
            stre = '1_1_0_0_0'
        elif l == 3:
            stre = '1_1_1_0_0'
        elif l == 4:
            stre = '1_1_1_1_0'
        elif l == 5:
            stre = '1_1_1_1_1'
        rs = 'd_'+ stre + '.jpg'
        return  rs
    def top_(self,instant,touch):
        ##############################

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file_h = (db_path)
            self.conn_h = sqlite3.connect(self.file_h)
            self.cur_h = self.conn_h.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()
        # print(self.data_[1][0])
        # print(self.data_[0][0])
        ##############################

        #sm.add_widget(jeux_embdad('flag','yes'))




        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.38 and touch.pos[1] <= Window.height * 0.58):
            if int(self.data_[0][0]) < 15 :
                sm.switch_to(jeux_embdad("flag",'yes')) 


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.38 and touch.pos[1] <= Window.height * 0.58):

            if int(self.data_[0][0]) < 30  and int(self.data_[0][0]) >= 15:

                sm.switch_to(jeux_embdad("embadad", 'yes'))

        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_[0][0]) < 45  and int(self.data_[0][0]) >= 30 :
                sm.switch_to(jeux_embdad("map",'yes'))
        


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_[0][0]) > 45  :
                sm.switch_to(jeux_embdad("map", 'yes'))






    def home(self,instant,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :

            sm.switch_to(WelcomeScreen())
    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            sm.switch_to(WelcomeScreen())
            return True

class info_contry(Screen):
    #code = StringProperty('')
    code = ListProperty()
    def __init__(self,acc, **kwargs ): #constructor method
        super(info_contry, self).__init__(**kwargs) #init parent
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))

        #####################################  bar #########################

        # data
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()

        if int(self.data_[0][0]) < 15:
            self.nv = 1
        elif int(self.data_[0][0]) < 30:
            self.nv = 2
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        else:
            self.nv = 4

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))
        self.bar = FloatLayout()
        image_point = Image(source='point.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.82, 'y': 0.90},
                            allow_stretch=True, keep_ratio=False)
        point = Label(text=str(self.data_[0][0]), size_hint=(0.08, 0.08), pos_hint={"x": 0.74, "top": 0.97})

        image_star = Image(source='star.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.51, 'y': 0.90},
                           allow_stretch=True, keep_ratio=False)
        star = Label(text=str(self.nv), size_hint=(0.08, 0.08), pos_hint={"x": 0.41, "top": 0.97})

        self.image_home = Image(source='home.png', size_hint=(0.08, 0.08), pos_hint={'x': 0.10, 'y': 0.90},
                                allow_stretch=True, keep_ratio=False)
        self.image_home.bind(on_touch_down=self.home)
        self.bar.add_widget(image_star)
        self.bar.add_widget(self.image_home)
        self.bar.add_widget(star)
        self.bar.add_widget(image_point)
        self.bar.add_widget(point)

        # add bar from widgat princibal and add method home
        #####################################################################
        if acc != 'non':
            self.cr(0,acc)

        # list = [val1 , val2]
        #print(acc)




        ############# data base ââââââââââââââââ
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.file = (db_path)
            self.conn = sqlite3.connect(self.file)
            self.cur = self.conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            self.cur.execute(sql)
            self.data = self.cur.fetchall()
        ###########################
        ##### valeur_contry1 et 2

    def cr(self,i,acc):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            file = (db_path)
            conn = sqlite3.connect(file)
            cur = conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            cur.execute(sql)
            data = cur.fetchall()



        status = ['عدد السكان'] * 100
        v_contry1 = []


        for i in data:
            if acc == i[28]:
                for e in i:
                    v_contry1.append(e)

        #print(len(self.status))
        #print(len(self.v_contry1))
        #print(len(self.v_contry2))

        self.func = FloatLayout()

        self.layout = GridLayout(cols=2, spacing=10, size_hint_y=None, pos_hint={"centre_x": 0.02})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        #https://googledrive.com/host/<folderID>/<filename>
        #https://drive.google.com/uc?id=FILE_ID
        image1 =  'https://drive.google.com/uc?id=1Wo_j02PZP53uXoIVsw_5jXlkF0QWsnOh'   #flag.png'
        image1 = AsyncImage(source=image1)
        image2 = 'flag.png'
        img = Image(source=image2, size_hint=(0.90, 0.23), pos_hint={'x': 0.05, 'y': 0.62},
                    allow_stretch=True, keep_ratio=False)



        self.func.add_widget(img)

        self.func.add_widget(self.bar)


        for i in range(len(data[1])):



            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                         pos_hint={'x': 0.3, 'top': None}, height=40 )
            #print(v_contry1[i])

            self.btn1 = Button(text='hello2', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                          pos_hint={'x': 0.3, 'top': None}, height=40 )








            #self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)

            reshaped_text = (status[i])
            self.bidi_text = get_display(reshaped_text)


            setattr(self.btn, 'text', str(v_contry1[i]))
            setattr(self.btn1, 'text', self.bidi_text)

        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                          pos_hint={"x": 0.05, "top": 0.59})  # , size=(Window.width, Window.height)
        self.root.add_widget(self.layout)
        self.func.add_widget(self.root)
        self.add_widget(self.func)
        # self.add_widget(img)
    def update(self,instant):
        self.btn.text = 'hemidi'


    def press(self,instant):
            #print(self.contry_vs)

            pass
    def home(self,instant,touch):


        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):
            sm.switch_to(WelcomeScreen())










    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            sm.switch_to(list_contry())
            return True


if __name__ == '__main__':
    try :
        import arabic_reshaper as ar
    except:
        f = open('/data/user/0/org.test.myapp/files/app/_python_bundle/site-packages/arabic_reshaper/__version__.py', 'w')
        f.write("__version__ = '2.0.15'")
        f.close()
        import arabic_reshaper as ar





    PanelBuilderApp().run()
