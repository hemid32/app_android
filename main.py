﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import kivy
kivy.require('1.9.1')
from kivmob import KivMob, TestIds , RewardedListenerInterface
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
from kivy.core.audio import SoundLoader
from kivy.base import stopTouchApp



class PanelBuilderApp(App):  # display the welcome screen
    def build(self):
        global  dect , status1 , ads
        ads = KivMob('ca-app-pub-1803778669602445~4508591340')
        ads.new_banner('ca-app-pub-1803778669602445/4045093890', top_pos=False)

        dect = {'united-states-of-america':u'امريكا' , 'russia': u'روسيا' , 'china': u'الصين' ,  'india': u'الهند'  ,
        'japan': u'اليابان'  , 'south-korea': u'كورياالجنوبية' , 'france' :u'فرنسا'  , 'united-kingdom': u'بريطانيا' , 'egypt': u'مصر' , 'brazil': u'البرازيل' , 'turkey': u'تركيا',
        'italy': u'ايطاليا', 'germany': u'المانيا' , 'iran': u'ايران', 'pakistan': u'باكستان' , 'indonesia': u'اندونيسيا', 'saudi-arabia': u'السعودية' , 'israel': u'اسرائيل' ,
        'australia': u'اوستراليا' , 'spain': u'اسبانيا' , 'poland': u'بولندا' , 'vietnam': u'فيتنام' , 'canada':  u'كندا', 'north-korea': u'كورياالشمالية' , 'taiwan': u'تايوان' , 'ukraine': u'اوكرانيا' ,
          'algeria': u'الجزائر' , 'south-africa': u'جنوب افريقيا' , 'switzerland':u'سويسرا'  , 'norway': u'النرويج' , 'sweden': u'السويد' , 'greece': u'اليونان' , 'czech-republic':u'التشيك'  ,
        'myanmar': u'مينمار' , 'netherlands': u'هولندا' , 'colombia': u'كولومبيا'  , 'mexico': u'المكسيك' , 'romania': u'رومانيا' , 'peru' : u'بيرو','venezuela': u'فنزويلا' , 'nigeria': u'نيجيريا' ,
        'argentina':  u' الارجنتين' , 'malaysia': u'ماليزيا' ,'united-arab-emirates': u'الامارات' , 'bangladesh': u'بنغلاديش' ,
                'chile': u'تشيلي' , 'denmark': u'الدنمارك' , 'iraq': u'العراق' ,  'singapore': u'سنغافورا' , 'syria': u'سوريا' , 'morocco': u'المغرب' , 'portugal': u'البرتغال' ,
        'ethiopia': u'اثيوبيا' , 'serbia': u'صربيا' ,'croatia': u'كرواتيا' , 'belgium': u'بلجيكا' , 'jordan': u'الاردن' , 'cuba': u'كوبا' , 'yemen': u'اليمن',
         'oman': u'عمان', 'sudan': u'السودان' , 'libya': u'ليبيا' , 'tunisia': u'تونس' , 'kuwait': u'الكويت' , 'qatar': u'قطر' ,
        'bahrain':  u'البحرين' , 'ghana': u'غانا'  , 'south-sudan':  u'جنب السودان' , 'lebanon': u'لبنان', 'thailand': u'تايلاند'}
        #print(len(dect))
        status1 = [

            u'ميزانية الدفاع',
            u'الرؤوس النووية',
            u'كاسحة الغام',
            u'غواصة',
            u'كورفيت',
            u'مدمرة',
            u'فرقاطة',
            u'حاملات الطائرات',
            u'مجموع القطع البحرية',
            u'هيليكوبتر هجومية',
            u'مجموع الهليكوبتر',
            u'طائرات التدريب',
            u'طائرات النقل',
            u'مقاتلات هجومية',
            u'مقاتلات',
            u'مجموع الطائرات',
            u'انظمة الصواريخ',
            u'مدافع',
            u'مدافع ذاتية',
            u'مدرعات',
            u'دبابات',
            u'القوات الاحتياطية',
            u'القوات في الخدمة',
            u'مجموع الجنود',
            u'بلوغ السن العسكري سنويا',
            u'صالح للخدمة',
            u'القوى العاملة',
            u'عدد السكان',
            u'الدولة',
            u'التصنيف العالمي',
            u'الدين الخارجي',
            u'احتياطي النفط(برميل)',
           u'استهلاك النفط(برميل / ي)' ,
            u'انتاج النفط(برميل / ي)' ,
            u'الممرات المائية(كم)' ,
            u'عدد المطارات',
            u'طول الساحل(كم)',
            u'طول السكك الحديدة(كم)',
            u'الطرق المعبدة(كم)',
            u'المساحة(كم/مربع)',

        ]
        global  sm , ss
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcomeScreen'))


        sm.add_widget(shose_contry(name='shose_contry'))
        #sm.add_widget(result_vs(name='result_vs'))
        sm.add_widget(jeux_embdad(str('flag'),'non',name='jeux_embdad'))
        sm.add_widget(jeux_intro(name = 'jeux_intro'))
        sm.add_widget(list_contry(name='list_contry'))
        sm.add_widget(info_contry('non' , name = 'info_contry'))
        #sm.add_widget(result_vs(['algeria','algeria'], name='result_vs'))
        self.sound_non = SoundLoader.load('clk.wav')
        if self.sound_non:
            self.sound_non.play()


        return  sm


    """ def stop(self, *largs):
        self.root_window.close()  # Fix app exit on Android.

        #stopTouchApp()
        return super(PanelBuilderApp, self).stop(*largs)
    def on_stop(self):
        return True"""


class WelcomeScreen(Screen): #welcomeScreen subclass
    def __init__(self, **kwargs): #constructor method
        super(WelcomeScreen, self).__init__(**kwargs) #init parent
        ads.show_banner()



        with self.canvas:
            Color(204/255, 204/255, 204/255,mode='rgb')
            Rectangle(size=(Window.width , Window.height))
        ##################
        EventLoop.window.bind(on_keyboard=self.hook_keyboarde)
        self.mm = 0
        self.ruselt_exit = False

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
        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                            allow_stretch=True, keep_ratio=False)
        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.50))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.17))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.28))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.39))

        #welcomeBox1 = Button(text= self.bidi_text1,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.60} ,on_press=self.poptest)
        welcomeBox2 = Button(text= self.bidi_text2 ,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.49} ,on_press=self.poptest2,background_color = (0.,0.,0.,0.),markup = True)
        welcomeBox3 = Button(text= self.bidi_text3,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.38} ,on_press=self.gotojeux,background_color = (0.,0.,0.,0.))
        welcomeBox4 = Button(text= self.bidi_text4,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.27} ,on_press=self.top_,background_color = (0.,0.,0.,0.))
        welcomeBox1 = Button(text= self.bidi_text1,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.60} ,on_press=self.poptest, border =(25, 25, 25, 25),background_color = (0.,0.,0.,0.))
        welcomeBox5 = Button(text= self.bidi_text5,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.27} ,on_press=self.exite ,background_color = (0.,0.,0.,0.)) # self.exite
        #img_ptn1 = Image(source='post_image.png', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'top': 0.60},
        #                   allow_stretch=True, keep_ratio=False)



        welcomePage.add_widget(welcomeBox1)
        welcomePage.add_widget(welcomeBox2)
        welcomePage.add_widget(welcomeBox3)
        #welcomePage.add_widget(welcomeBox4)
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
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        label_cont2 = Label(text=get_display(ar.reshape(u'عند اجراء مقارنة نسحب 4 نقاط من رصيدك')), font_name='hemidi', font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)

        welcomePage.add_widget(label_cont2)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False , title = get_display(ar.reshape(u'انتظر')) , title_font = 'hemidi')

        ads.destroy_banner()
        self.p.open()

        Clock.schedule_once(self.mo9arana)
        self.p.dismiss()

    def poptest2(self,i):

        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False , title = get_display(ar.reshape(u'انتظر')) , title_font = 'hemidi')

        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(self.information)
        self.p.dismiss()





    def mo9arana(self, instance):
        #sm.add_widget(shose_contry(name='shose_contry'))
        sm.switch_to(shose_contry())
        ads.request_banner()
        ads.show_banner()

        self.sound_non = SoundLoader.load('sws.wav')
        if self.sound_non:
            self.sound_non.play()





    def information(self,instant):

        sm.switch_to(list_contry(name='list_contry'))
        self.sound_non = SoundLoader.load('sws.wav')
        if self.sound_non:
            self.sound_non.play()



    def top_(self,instant):

        self.sound_non = SoundLoader.load('sws.wav')
        if self.sound_non:
            self.sound_non.play()
        sm.switch_to(WelcomeScreen())




    def handl(self):

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

        self.cur_h.execute(''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(n) + 5, int(n)))
        self.conn_h.commit()
        sm.switch_to(WelcomeScreen())





    def gotojeux(self,i):
        sm.switch_to(jeux_intro())
        self.sound_non = SoundLoader.load('sws.wav')
        if self.sound_non:
            self.sound_non.play()


    def home(self,inst,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :
            self.sound_non = SoundLoader.load('sws.wav')
            if self.sound_non:
                self.sound_non.play()
            sm.switch_to(WelcomeScreen())

        # x entre [Window.width*0.10 , Window.width*0.18 ]
        # y entre [Window.height*0.89 , Window.height*0.97]

    def exite(self,inst):
        self.ruselt_exit = True


        welcomePage = FloatLayout()
        image2 = "cr.png"
        img = Image(source=str(image2), size_hint=(0.4, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=get_display(ar.reshape(u'خروج')), font_name='hemidi', size_hint=(0.42, 0.1), pos_hint={"x": 0.07, "top": 0.30})
        btn = Button(text=get_display(ar.reshape(u'لا')), font_name='hemidi', size_hint=(0.42, 0.1), pos_hint={"x": 0.51, "top": 0.30})
        text = get_display(ar.reshape(u'هل تريد الخروج ؟'))
        label_cont2 = Label(text=text, font_name='hemidi', font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)

        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)
        welcomePage.add_widget(label_cont2)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'تاكيد الخروج')) , title_font = 'hemidi' )
        btn.bind(on_press=self.continu_)
        btn1.bind(on_press=self.quit)
        self.popup.open()


        #App.get_running_app().stop()
    def continu_(self,i):
        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())
    def quit(self,*args):

        self.popup.dismiss()

        try:
            App.root_window.close()
        except :
            try:
                App.stop()
            except :
                PanelBuilderApp().stop()









        #App.get_running_app().is_desktop = 0


    def hook_keyboarde(self, window, key, *largs):
        if key == 27:
            if self.ruselt_exit == True :
                self.popup.dismiss()

                App.get_running_app().stop()
                return True
            else :
                self.exite(0)
                return True


class shose_contry(Screen):
    sm = ScreenManager()
    def __init__(self, **kwargs): #constructor method
        super(shose_contry, self).__init__(**kwargs) #init parent

        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.ruselt_1 = False

        ###################### ads  ###########################
        #####



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

        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        post_image2 = Image(source='comparing.jpg', size_hint=(0.9, 0.18), pos_hint={'x': 0.05, 'y': 0.30},
                           allow_stretch=True, keep_ratio=False)

        func = FloatLayout()
        self.dropdown = DropDown()
        self.dropdown2 = DropDown()



        self.welcomeBox1 = Button(text=  get_display(ar.reshape(u'قارن')),font_name = 'hemidi', size_hint =(0.6,0.1),pos_hint={"x":0.20,"top":0.25} ,background_color = (0.,0.,0.,0.))
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
            btn = Button(text=get_display(ar.reshape(dect.get(index[28]))),font_name = 'hemidi' , size_hint_y=None, height=55)
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
            btn2 = Button(text=get_display(ar.reshape(dect.get(index[28]))), font_name = 'hemidi',size_hint_y=None, height=55 ,on_release=lambda btn: self.return_val)
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

    def get_key(self,i,val):
        #print(val)
        f = 0
        for i in dect.values():


            if val == get_display(ar.reshape(i)):
                for key, value in dect.items():
                    # print(val , value)
                    if i == value:
                        f = 1
                        return key
            else :
                #return 'nnnnnnn'
                pass
        if f == 0 :
            return False


    def return_val(self,instant ):

        val2 =  self.get_key(0,self.mainbutton2.text) #dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val1 =  self.get_key(0,self.mainbutton.text)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()
        #print(val2,val1)
        #print(self.text_1)

        if not (val1 == False or val2 == False) :
            ads.destroy_banner()
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
                self.ruselt_1 = True
                self.return_jeux(0)
        else :
            pass

    def puptest(self,i):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'انتظر')) , title_font = 'hemidi')
        self.p.open()
        Clock.schedule_once(lambda *args: self.eventes(0,self.val_))
        self.p.dismiss()


    def eventes(self,i,k):
        sm.add_widget(result_vs(k,name='result_vs'))
        sm.switch_to(result_vs(k))
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()

    def return_jeux (self,instant):

        reshaped_text3= ar.reshape(u"العب و جمع النقاط")
        self.bidi_text3 = get_display(reshaped_text3)
        reshaped_text4 = ar.reshape(u"الصفحة الرئيسية")
        self.bidi_text4 = get_display(reshaped_text4)
        reshaped_text5 = ar.reshape(u"يجب ان تمتلك 15 نقطعة على الاقل ")
        self.bidi_text5 = get_display(reshaped_text5)

        welcomePage = FloatLayout()
        image2 = "cr.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=self.bidi_text4,font_name = 'hemidi' ,size_hint=(0.47, 0.1), pos_hint={"x": 0.02, "top": 0.30})
        btn = Button(text=self.bidi_text3,font_name = 'hemidi' , size_hint=(0.47, 0.1), pos_hint={"x": 0.51, "top": 0.30})
        label_cont2 = Label(text=self.bidi_text5,font_name='hemidi', font_size='20sp',size_hint=(0.4, 0.2), pos_hint={'x': 0.3, 'top': 0.95},markup = True)



        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)
        welcomePage.add_widget(label_cont2)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'للاسف لا يمكن اجراء المقارنة')) , title_font = 'hemidi')


        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.vers_jeux)
        btn1.bind(on_press=self.vers_home)

        # open the popup
        self.popup.open()
        self.sound_non = SoundLoader.load('non.wav')
        if self.sound_non:
            self.sound_non.play()

    def vers_jeux(self,ins):
        self.popup.dismiss()
        sm.switch_to(jeux_intro())
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()
    def vers_home(self,ins):
        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()


    def home(self,instant,touch):
        #self.manager.current = 'result_vs' #result_vs
        #self.manager.screens[2].ids.btn.text = self.mainbutton2.text
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()

    def hook_keyboard(self, window, key, *largs):
        # self.name

        #print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            #EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            if self.ruselt_1  == True :
                self.popup.dismiss()
                ads.destroy_banner()
                sm.switch_to(WelcomeScreen())
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()

                return True
            else :
                ads.destroy_banner()
                sm.switch_to(WelcomeScreen())
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()

                return  True


class list_contry(Screen):
    def __init__(self, **kwargs ): #constructor method
        super( list_contry,self).__init__(**kwargs) #init parent
        ads.destroy_banner()
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

        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        func.add_widget(post_image)

        self.layout = GridLayout(cols=1, spacing=10, size_hint=(1., None), pos_hint ={"centre_x":0.30} , height= 1920)
        # Make sure the height is such that there is something to scroll.
        #self.layout.bind(minimum_height=self.layout.setter('height'))
        #self.layout = ObjectProperty(None)
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
        """        ml=1
        for i in self.data:
            self.btn = Button(text=i[28], font_name='hemidi', size_hint_y=None, size_hint_x=1.,
                              pos_hint={'x': 0., 'top': None}, height=80 , id=str(ml),on_release =  lambda  *args : self.vers_info_contry(0,self.btn.text) )  #on_press =lambda  *args : self.vers_info_contry(0,self.btn.text))
            self.layout.add_widget(self.btn)
           

           """


        #print(len(self.data))
        """h = []
        for i in self.data :
            h.append(i[28])
        print(h)
        print('************')
        for  l  in dect.keys() :
            if l not in h :
                print(l)"""



        self.btn1 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[0][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[0][28])) )
        self.btn2 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[1][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[1][28])) )
        self.btn3 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[2][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[2][28])) )
        self.btn4 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[3][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[3][28])) )
        self.btn5 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[4][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[4][28])) )
        self.btn6 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[5][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[5][28])) )
        self.btn7 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[6][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[6][28])) )
        self.btn8 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[7][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[7][28])) )
        self.btn9 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[8][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[8][28])) )
        self.btn10 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[9][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[9][28])) )
        self.btn11=   Button(text=get_display(ar.reshape(dect.get(str(self.data[10][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[10][28])) )
        self.btn12 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[11][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[11][28])) )
        self.btn13 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[12][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[12][28])) )
        self.btn14 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[13][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[13][28])) )
        self.btn15 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[14][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[14][28])) )
        self.btn16=   Button(text=get_display(ar.reshape(dect.get(str(self.data[15][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[15][28])) )
        self.btn17 =  Button(text=get_display(ar.reshape(dect.get(str(self.data[16][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[16][28])) )
        self.btn18 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[17][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[17][28])) )
        self.btn19 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[18][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[18][28])) )
        self.btn20 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[19][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[19][28])) )
        self.btn21 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[20][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[20][28])) )
        self.btn22 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[21][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[21][28])) )
        self.btn23=   Button(text=get_display(ar.reshape(dect.get(str(self.data[22][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[22][28])) )
        self.btn24=   Button(text=get_display(ar.reshape(dect.get(str(self.data[23][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[23][28])) )
        self.btn25=   Button(text=get_display(ar.reshape(dect.get(str(self.data[24][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[24][28])) )
        self.btn26=   Button(text=get_display(ar.reshape(dect.get(str(self.data[25][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[25][28])) )
        self.btn27=   Button(text=get_display(ar.reshape(dect.get(str(self.data[26][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[26][28])) )
        self.btn28=   Button(text=get_display(ar.reshape(dect.get(str(self.data[27][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[27][28])) )
        self.btn29=   Button(text=get_display(ar.reshape(dect.get(str(self.data[28][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[28][28])) )
        self.btn30=   Button(text=get_display(ar.reshape(dect.get(str(self.data[29][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[29][28])) )
        self.btn31=   Button(text=get_display(ar.reshape(dect.get(str(self.data[30][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[30][28])) )
        self.btn32=   Button(text=get_display(ar.reshape(dect.get(str(self.data[31][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[31][28])) )
        self.btn33=   Button(text=get_display(ar.reshape(dect.get(str(self.data[32][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[32][28])) )
        self.btn34=   Button(text=get_display(ar.reshape(dect.get(str(self.data[33][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[33][28])) )
        self.btn35=   Button(text=get_display(ar.reshape(dect.get(str(self.data[34][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[34][28])) )
        self.btn36=   Button(text=get_display(ar.reshape(dect.get(str(self.data[35][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[35][28])) )
        self.btn37=   Button(text=get_display(ar.reshape(dect.get(str(self.data[36][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[36][28])) )
        self.btn38=   Button(text=get_display(ar.reshape(dect.get(str(self.data[37][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[37][28])) )
        self.btn39=   Button(text=get_display(ar.reshape(dect.get(str(self.data[38][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[38][28])) )
        self.btn40 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[39][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[39][28])) )
        self.btn41 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[40][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[40][28])) )
        self.btn42 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[41][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[41][28])) )
        self.btn43 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[42][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[42][28])) )
        self.btn44 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[43][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[42][28])) )
        self.btn45 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[44][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[44][28])) )
        self.btn46 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[45][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[45][28])) )
        self.btn47 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[46][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[46][28])) )
        self.btn48 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[47][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[47][28])) )
        self.btn49 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[48][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[48][28])) )
        self.btn50 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[49][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[49][28])) )
        self.btn51 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[50][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[50][28])) )
        self.btn52 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[51][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[51][28])) )
        self.btn53 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[52][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[52][28])) )
        self.btn54 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[53][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[53][28])) )
        self.btn55 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[54][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[54][28])) )
        self.btn56 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[55][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[55][28])) )
        self.btn57 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[56][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[56][28])) )
        self.btn58 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[57][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[57][28])) )
        self.btn59 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[58][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[58][28])) )
        self.btn60 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[59][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[59][28])) )
        self.btn61 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[60][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[60][28])) )
        self.btn62 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[61][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[61][28])) )
        self.btn63 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[62][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[62][28])) )
        self.btn64 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[63][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[63][28])) )
        self.btn65 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[64][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[64][28])) )
        self.btn66 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[65][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[65][28])) )
        self.btn67 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[66][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[66][28])) )
        self.btn68 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[67][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[67][28])) )
        self.btn69 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[68][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[68][28])) )
        self.btn70 =   Button(text=get_display(ar.reshape(dect.get(str(self.data[69][28])))), font_name = 'hemidi',size_hint_y=None,size_hint_x=1.,pos_hint={'x':0.05 ,'top':None} ,height=80 , on_press =lambda  *args : self.vers_info_contry(0,str(self.data[69][28])) )

        lst  = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5 , self.btn6 , self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12 , self.btn13  ,
                self.btn14, self.btn15, self.btn16, self.btn17, self.btn18, self.btn19, self.btn20, self.btn21, self.btn22,
                self.btn23, self.btn24, self.btn25, self.btn26 ,
                self.btn27, self.btn28, self.btn29, self.btn30, self.btn31, self.btn32, self.btn33, self.btn34, self.btn35,
                self.btn36, self.btn37, self.btn38, self.btn39 , self.btn40,
                self.btn41, self.btn42, self.btn43, self.btn44, self.btn45, self.btn46, self.btn47, self.btn48,self.btn49 ,
                self.btn50 , self.btn51 , self.btn52 , self.btn53, self.btn54,self.btn55, self.btn56, self.btn57, self.btn58, self.btn59, self.btn60, self.btn61, self.btn62,
                self.btn63,self.btn64, self.btn65, self.btn66, self.btn67, self.btn68 , self.btn69 , self.btn70



                ]
        """self.btn55, self.btn56, self.btn57, self.btn58, self.btn59, self.btn60, self.btn61, self.btn62,
        self.btn63,
        self.btn64, self.btn65, self.btn66, self.btn67, self.btn68, self.btn49,self.btn50, self.btn51, self.btn52, self.btn53, self.btn54,"""
        i = 0
        for  ig  in  lst :
            """self.btn1 = Button(text=str(ig[28]), size_hint_y=None, size_hint_x=1.,
                               pos_hint={'x': 0.05, 'top': None}, height=60,on_press=lambda *args: self.vers_info_contry(0, ig[28])
                              )"""

            self.layout.add_widget(ig)
        #print(self.btn1.pos)








        self.root = ScrollView(size_hint=(0.90, None) ,size=(Window.width,Window.height), pos_hint={"x":0.05,"top":0.60} )
        self.root.add_widget(self.layout)
        func.add_widget(self.root)
        func.add_widget(bar)

        self.add_widget(func)




    def home(self,instant,touch):
        #self.manager.current = 'welcomeScreen'
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()




    def vers_info_contry(self,i,inst):
        welcomePage = FloatLayout()


        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'انتظر')) , title_font = 'hemidi')
        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(lambda *args: self.vers_info_contry_2(0,inst))
        self.p.dismiss()


    def vers_info_contry_2(self,i,inst):

        sm.switch_to(info_contry(inst , name = 'info_contry'))
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()

    def hook_keyboard(self, window, key, *largs):
        # self.name

        #print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            #EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
            return  True


################################### hkendemti  fine


class result_vs(Screen):
    #code = StringProperty('')
    code = ListProperty()
    def __init__(self,acc, **kwargs ): #constructor method
        super(result_vs, self).__init__(**kwargs) #init parent
        ads.destroy_banner()
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
        image1 =  'flag/'+ acc[0] + '.png'

        image2 = 'flag/'+ acc[1] + '.png'
        img = Image(source=str(image1), size_hint=(0.2866, 0.15), pos_hint={'x': 0.05, 'y': 0.62},
                    allow_stretch=True, keep_ratio=False)
        img2 = Image(source=str(image2), size_hint=(0.2866, 0.15), pos_hint={'x': 0.6566, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)
        img3 = Image(source='vs.png', size_hint=(0.2866, 0.15), pos_hint={'x': 0.35, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)

        self.func.add_widget(img2)
        self.func.add_widget(img)
        self.func.add_widget(img3)
        self.func.add_widget(self.bar)


        for i in range(len(data[1])):



            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                         pos_hint={'x': 0.3, 'top': None}, height=60 )
            #print(v_contry1[i])

            self.btn1 = Button(text='hello2', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                          pos_hint={'x': 0.3, 'top': None}, height=60 )
            self.btn2 = Button(text='gg', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None},
                              height=60)






            #self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)
            self.layout.add_widget(self.btn2)

            reshaped_text = ar.reshape((status1[i]))
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
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
    def jeux(self,instant):
        #self.manager.current = 'welcomeScreen'
        #print(self.code)
        pass
    def return_(self,window):

        sm.switch_to(shose_contry())
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()


    def poptest(self,window , key , *args):
        if key == 27 :
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
            return  True


class jeux_embdad(Screen): #welcomeScreen subclass
    coord = StringProperty('')
    def __init__(self, hemidi, rune, **kwargs): #constructor method
        super(jeux_embdad, self).__init__(**kwargs) #init parent
        ads.request_banner()
        ads.show_banner()
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
            self.ruselta = False


            ############################



            nome_image = os.listdir(r"%s"%(self.file_j))


            self.img_embdad = random.choice(nome_image)

            welcomePage = FloatLayout()
            image2 = "%s/%s"%(str(self.file_j),str(self.img_embdad))
            nome_image.remove(self.img_embdad)
            #cont =random.choices(nome_image , k=3) #malaysia
            cont = []
            im1 = random.choice(nome_image)
            nome_image.remove(im1)
            cont.append(im1)
            im2 = random.choice(nome_image)
            nome_image.remove(im2)
            cont.append(im2)
            im3 = random.choice(nome_image)
            nome_image.remove(im3)
            cont.append(im3)
            cont.append(self.img_embdad)
            #image2 = "embadad/spain.png"
            img = Image(source=str(image2), size_hint=(0.80, 0.30), pos_hint={'x': 0.1, 'y': 0.40},
                        allow_stretch=True, keep_ratio=False)

            with self.canvas:

                Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

                Rectangle(size=(Window.width * 0.44, Window.height * 0.1),
                          pos=(Window.width * 0.05, Window.height * 0.28))
                Rectangle(size=(Window.width * 0.44, Window.height * 0.1),
                          pos=(Window.width * 0.51, Window.height * 0.28))
                Rectangle(size=(Window.width * 0.44, Window.height * 0.1),
                          pos=(Window.width * 0.05, Window.height * 0.15))
                Rectangle(size=(Window.width * 0.44, Window.height * 0.1),
                          pos=(Window.width * 0.51, Window.height * 0.15))



            l1 = random.choice(cont)
            welcomeBox1 = Button(text=get_display(ar.reshape(dect.get(str(l1[:-4])))),font_name = 'hemidi' , size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.38},background_color = (0.,0.,0.,0.))
            welcomeBox1.bind(on_press=lambda *args: self.result_in(0,l1))

            cont.remove(l1)
            l2 = random.choice(cont)
            welcomeBox2 = Button(text=get_display(ar.reshape(dect.get(str(l2[:-4])))), font_name = 'hemidi',size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.38},background_color = (0.,0.,0.,0.))
            welcomeBox2.bind(on_press=lambda *args: self.result_in(0,l2))

            cont.remove(l2)
            l3 = random.choice(cont)
            welcomeBox3 = Button(text=get_display(ar.reshape(dect.get(str(l3[:-4])))), font_name='hemidi',size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.25},background_color = (0.,0.,0.,0.))
            welcomeBox3.bind(on_press=lambda *args: self.result_in(0,l3))


            cont.remove(l3)
            l4 = cont[0]
            welcomeBox4 = Button(text=get_display(ar.reshape(dect.get(str(l4[:-4])))), font_name = 'hemidi',size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.25},background_color = (0.,0.,0.,0.))
            welcomeBox4.bind(on_press=lambda *args: self.result_in(0,l4))
            text = ar.reshape(text2)
            self.text_label = get_display(text)
            #"[b][color=#070B19]%s[/color][/b]"% ('time')

            btn1 = Label(text="[b][color=#070B19]%s[/color][/b]"% (self.text_label), font_name = 'hemidi',size_hint=(0.80,0.1),
                              pos_hint={'x': 0.1, 'top': 0.80}, markup = True)


            welcomePage.add_widget(welcomeBox1)
            welcomePage.add_widget(welcomeBox2)
            welcomePage.add_widget(welcomeBox3)
            welcomePage.add_widget(welcomeBox4)
            welcomePage.add_widget(bar)


            #self.event()
            self.timer_ = Label(text="[b][color=#070B19]%s[/color][/b]"% ('time'), size_hint=(0.24, 0.05), pos_hint={"x": 0.38, "top": 0.850}, markup = True)
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
        #print(l) afficher timer

        XI = 0

        if '-1 day' not in str(l):
            #self.root.ids.time.text = 'Time Over!'
            setattr(self.timer_, 'text', "[b][color=#070B19]%s[/color][/b]"% str(l))
            self.sound_time = SoundLoader.load('time.wav')
            if self.sound_time:
                self.sound_time.play()
            L = int(self.XI)
            L += 1
            self.XI = str(L)
        else :
            setattr(jeux_embdad, self.rune, 'non')
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
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()

    def result_in(self,n , l):
        ads.destroy_banner()
        self.sound_time = SoundLoader.load('time.wav')
        if self.sound_time:
            self.sound_time.stop()
        self.ruselta = True
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
        sound = SoundLoader.load('yes.wav')
        if sound:
            sound.play()
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
        btn = Button(text=get_display(ar.reshape(u'مواصلة اللعب')), font_name = 'hemidi', size_hint=(0.70, 0.1), pos_hint={"x": 0.150, "top": 0.18})
        btn.bind(on_press=self.vers_)
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        #content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'احسنت لقد كسبت 3 نقاط')) , title_font = 'hemidi')

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
        self.sound_error = SoundLoader.load('error.wav')
        if self.sound_error:
            self.sound_error.play()
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
        btn1 = Button(text=get_display(ar.reshape(u'خروج')), font_name = 'hemidi',size_hint=(0.440, 0.1), pos_hint={"x": 0.05, "top": 0.18})
        btn = Button(text=get_display(ar.reshape(u'محاولة اخرى')), font_name = 'hemidi',size_hint=(0.440, 0.1), pos_hint={"x": 0.51, "top": 0.18})
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'خسرت 3 نقاط')) , title_font = 'hemidi')

        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.continu_)
        btn1.bind(on_press=self.quit)


        # open the popup
        self.popup.open()

    def quit(self, instant):
        # if result false and shose quite
        self.sound_error.stop()
        setattr(jeux_embdad, self.rune, 'non')

        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())
        self.sound_sws = SoundLoader.load('sws.wav')
        if self.sound_sws:
            self.sound_sws.play()

    def continu_(self,instant):
        # if result false and shose continu
        self.sound_error.stop()
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
            if  self.ruselta == True :
                self.event.cancel()
                ads.destroy_banner()
                setattr(jeux_embdad, self.rune, 'non')
                setattr(jeux_embdad, self.XI, '0')
                self.XI = '0'
                self.popup.dismiss()
                sm.switch_to(jeux_intro())
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()



                return  True
            else :

                self.event.cancel()
                ads.destroy_banner()
                setattr(jeux_embdad, self.rune, 'non')
                setattr(jeux_embdad, self.XI, '0')
                self.XI = '0'

                sm.switch_to(jeux_intro())
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()


                return True


class jeux_intro(Screen):
    code = ListProperty()
    def __init__(self, **kwargs): #constructor method
        super(jeux_intro, self).__init__(**kwargs) #init parent
        ads.destroy_banner()
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
        elif int(self.data_[0][0]) < 45:
            self.nv = 3
        elif int(self.data_[0][0]) >= 45 :
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
        if int(self.data_[0][0]) >= 60 :
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

        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
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
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.38 and touch.pos[1] <= Window.height * 0.58):

            if int(self.data_[0][0]) < 30  and int(self.data_[0][0]) >= 15:

                sm.switch_to(jeux_embdad("embadad", 'yes'))
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()

        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_[0][0]) < 45  and int(self.data_[0][0]) >= 30 :
                sm.switch_to(jeux_embdad("map",'yes'))
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()
        


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_[0][0]) >= 45  :
                sm.switch_to(jeux_embdad("map", 'yes'))
                self.sound_sws = SoundLoader.load('sws.wav')
                if self.sound_sws:
                    self.sound_sws.play()






    def home(self,instant,touch):
        if (touch.pos[0] >= Window.width*0.10 and touch.pos[0] <= Window.width*0.18 ) and (touch.pos[1] >= Window.height*0.89 and touch.pos[1] <= Window.height*0.97)  :

            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            sm.switch_to(WelcomeScreen())
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
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

        self.func = FloatLayout()

        self.layout = GridLayout(cols=2, spacing=10, size_hint_y=None, pos_hint={"centre_x": 0.02})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        #https://googledrive.com/host/<folderID>/<filename>
        #https://drive.google.com/uc?id=FILE_ID
        image1 =  'https://drive.google.com/uc?id=1Wo_j02PZP53uXoIVsw_5jXlkF0QWsnOh'   #flag.png'
        image1 = AsyncImage(source=image1)
        #print(acc) # nome contry  acc
        image_flag1 = 'flag/' + acc  + '.png'
        image_embdad1 = 'embadad/' + acc + '.png'
        image_map1 = 'map/'+acc + '.png'
        image2 = 'flag.png'
        text_flag = u'العلم'
        text_flag = ar.reshape(text_flag)
        tx = get_display(text_flag)
        text_embdad = u'الشعار'
        text_embdad = ar.reshape(text_embdad)
        tx2 = get_display(text_embdad)
        text_map = u'الخريطة'
        text_map = ar.reshape(text_map)
        tx3 = get_display(text_map)
        label_flag =  Label(text="[b][color=#070B19]%s[/color][/b]"% (tx),font_name = 'hemidi', size_hint=(0.3, 0.05), pos_hint={"x": 0.70/2, "top": 0.87},markup = True)
        img_flag = Image(source=image_flag1, size_hint=(0.90, 0.15), pos_hint={'x': 0.10/2, 'y': 0.67},
                    allow_stretch=True, keep_ratio=False)
        label_embdad = Label(text="[b][color=#070B19]%s[/color][/b]"% (tx2),font_name = 'hemidi', size_hint=(0.3, 0.05), pos_hint={"x": 0.1, "top": 0.66} , markup = True)
        img_embdad = Image(source=image_embdad1, size_hint=(0.88/2, 0.15), pos_hint={'x': 0.10/2, 'y': 0.46},
                    allow_stretch=True, keep_ratio=False)
        label_map = Label(text="[b][color=#070B19]%s[/color][/b]"% (tx3), font_name = 'hemidi',size_hint=(0.3, 0.05), pos_hint={"x": 0.6, "top": 0.66},markup = True)
        img_map = Image(source=image_map1, size_hint=(0.88/2, 0.15), pos_hint={'x': (0.88/2)+0.06, 'y': 0.46},
                    allow_stretch=True, keep_ratio=False)

        self.func.add_widget(img_flag)
        self.func.add_widget(label_flag)
        self.func.add_widget(label_embdad)
        self.func.add_widget(img_embdad)
        self.func.add_widget(label_map)
        self.func.add_widget(img_map)

        self.func.add_widget(self.bar)

        #print(len(data[1]))
        #print(len(status1))
        for i in range(len(data[1])):
            reshaped_text = ar.reshape((status1[i]))
            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                         pos_hint={'x': 0.3, 'top': None}, height=60 )
            #print(v_contry1[i])

            self.btn1 = Button(text=get_display(reshaped_text), font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                          pos_hint={'x': 0.3, 'top': None}, height=60 )








            #self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)

            reshaped_text = (status1[i])
            self.bidi_text = get_display(reshaped_text)


            setattr(self.btn, 'text', str(v_contry1[i]))
            #setattr(self.btn1, 'text', self.bidi_text)

        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                          pos_hint={"x": 0.05, "top": 0.45})  # , size=(Window.width, Window.height)
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
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()










    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            #Window.close()
            sm.switch_to(WelcomeScreen())
            #sm.current_screen
            self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()
            return True



if __name__ == '__main__':
    try :
        import arabic_reshaper as ar
    except:
        BASE_DIR = '/data/user/0/android.kivy.org.myapp/files/app/_python_bundle/site-packages/arabic_reshaper/__version__.py'
        f = open(BASE_DIR, 'w')
        f.write("__version__ = '2.0.15'")
        f.close()
        import arabic_reshaper as ar




    PanelBuilderApp().run()
