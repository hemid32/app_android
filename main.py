# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import kivy

kivy.require('1.9.1')
from kivmob import KivMob, TestIds, RewardedListenerInterface
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.base import runTouchApp
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ListProperty
from kivy.uix.image import Image
import sqlite3
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from bidi.algorithm import get_display
from kivy.uix.image import AsyncImage
import os, time
import random
import shutil
from kivy.uix.popup import Popup
from kivy import clock
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color , Line ,Ellipse
import os.path
from kivy.base import EventLoop
from kivy.core.audio import SoundLoader
from kivy.base import stopTouchApp


class PanelBuilderApp(App):  # display the welcome screen



    def build(self):
        #Window.bind(on_request_close=self.on_stop)
        global dect, status1, ads
        test = 'ca-app-pub-1803778669602445~4508591340'
        ta3i =  'ca-app-pub-1803778669602445~4508591340'
        ads = KivMob(test)
        vd_tst ='ca-app-pub-1803778669602445/6284628861'
        bauyni_tst = 'ca-app-pub-1803778669602445/7853054920'
        bnr_tst = 'ca-app-pub-1803778669602445/4045093890'
        ads.new_banner(bnr_tst, top_pos=False)
        ads.request_banner()
        ads.new_interstitial(bauyni_tst)
        ads.request_interstitial()

        ads.load_rewarded_ad(vd_tst)
        ads.set_rewarded_ad_listener(RewardsHandler())



        dect = {'united-states-of-america': u'امريكا', 'russia': u'روسيا', 'china': u'الصين', 'india': u'الهند',
                'japan': u'اليابان', 'south-korea': u'كورياالجنوبية', 'france': u'فرنسا', 'united-kingdom': u'بريطانيا',
                'egypt': u'مصر', 'brazil': u'البرازيل', 'turkey': u'تركيا',
                'italy': u'ايطاليا', 'germany': u'المانيا', 'iran': u'ايران', 'pakistan': u'باكستان',
                'indonesia': u'اندونيسيا', 'saudi-arabia': u'السعودية', 'israel': u'اسرائيل',
                'australia': u'اوستراليا', 'spain': u'اسبانيا', 'poland': u'بولندا', 'vietnam': u'فيتنام',
                'canada': u'كندا', 'north-korea': u'كورياالشمالية', 'taiwan': u'تايوان', 'ukraine': u'اوكرانيا',
                'algeria': u'الجزائر', 'south-africa': u'جنوب افريقيا', 'switzerland': u'سويسرا', 'norway': u'النرويج',
                'sweden': u'السويد', 'greece': u'اليونان', 'czech-republic': u'التشيك',
                'myanmar': u'مينمار', 'netherlands': u'هولندا', 'colombia': u'كولومبيا', 'mexico': u'المكسيك',
                'romania': u'رومانيا', 'peru': u'بيرو', 'venezuela': u'فنزويلا', 'nigeria': u'نيجيريا',
                'argentina': u' الارجنتين', 'malaysia': u'ماليزيا', 'united-arab-emirates': u'الامارات',
                'bangladesh': u'بنغلاديش',
                'chile': u'تشيلي', 'denmark': u'الدنمارك', 'iraq': u'العراق', 'singapore': u'سنغافورا',
                'syria': u'سوريا', 'morocco': u'المغرب', 'portugal': u'البرتغال',
                'ethiopia': u'اثيوبيا', 'serbia': u'صربيا', 'croatia': u'كرواتيا', 'belgium': u'بلجيكا',
                'jordan': u'الاردن', 'cuba': u'كوبا', 'yemen': u'اليمن',
                'oman': u'عمان', 'sudan': u'السودان', 'libya': u'ليبيا', 'tunisia': u'تونس', 'kuwait': u'الكويت',
                'qatar': u'قطر',
                'bahrain': u'البحرين', 'ghana': u'غانا', 'south-sudan': u'جنب السودان', 'lebanon': u'لبنان',
                'thailand': u'تايلاند'}
        # print(len(dect))
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
            u'التصنيف العالمي',
            u'الدين الخارجي',
            u'احتياطي النفط(برميل)',
            u'استهلاك النفط(برميل / ي)',
            u'انتاج النفط(برميل / ي)',
            u'الممرات المائية(كم)',
            u'عدد المطارات',
            u'طول الساحل(كم)',
            u'طول السكك الحديدة(كم)',
            u'الطرق المعبدة(كم)',
            u'المساحة(كم/مربع)',
        ]
        global sm, ss
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcomeScreen'))

        #sm.add_widget(shose_contry(name='shose_contry'))
        # sm.add_widget(result_vs(name='result_vs'))
        #sm.add_widget(jeux_embdad(str('flag'), 'non', name='jeux_embdad'))
        #sm.add_widget(jeux_intro(name='jeux_intro'))
        #sm.add_widget(list_contry(name='list_contry'))
        #sm.add_widget(info_contry('non', name='info_contry'))
        # sm.add_widget(result_vs(['algeria','algeria'], name='result_vs'))
        self.sound_non = SoundLoader.load('clk.wav')
        sm.app = self
        if self.sound_non:
            self.sound_non.play()

        return sm

    """ def stop(self, *largs):
        self.root_window.close()  # Fix app exit on Android.

        #stopTouchApp()
        return super(PanelBuilderApp, self).stop(*largs)
    def on_stop(self):
        return True"""

    def on_quit(self):
        exit()
        #sys.exit()

    def on_resume(self):
        vd_tst ='ca-app-pub-1803778669602445/6284628861'
        ads.request_interstitial()
        ads.load_rewarded_ad(vd_tst)

    """ def on_rewarded(self,reward_name, reward_amount):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()

        n = self.data_[0][0]

        m = n + 10  ##################" -5

        self.cur_h.execute(
            ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()"""
########### class ads âââââââââââ
class RewardsHandler(RewardedListenerInterface):

    def on_rewarded(self, reward_name, reward_amount):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()

        n = self.data_[0][0]

        m = n + reward_amount ##################" -5
        self.cur_h.execute(
            ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()

        print("User rewarded")

    def on_rewarded_video_ad_completed(self):
        self.on_rewarded("Reward",1)
        print("Ad Completed Time to give Rewards")

    def on_rewarded_video_ad_closed(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()

        n = self.data_[0][0]

        m = n + 0  ##################" -5
        self.cur_h.execute(
            ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()
    def on_rewarded_video_ad_left_application(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()

        n = self.data_[0][0]

        m = n + 0  ##################" -5
        self.cur_h.execute(
            ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()

    def on_rewarded_video_ad_started(self):
        app.on_resume()

    def on_rewarded_video_ad_failed_to_load(self, error_code):
        if(error_code == 0):
            print("Something Went Wrong, Please Try Again")
        elif(error_code == 1):
            print("Please Report To the Developer")
        elif(error_code == 2):
            print("Make Sure You Have Internet Access")
        else:
            print("Please Try Later")

class WelcomeScreen(Screen):  # welcomeScreen subclass
    def __init__(self, **kwargs):  # constructor method
        super(WelcomeScreen, self).__init__(**kwargs)  # init parent
        ads.show_banner()
        with self.canvas:
            Color(204 / 255, 204 / 255, 204 / 255, mode='rgb')
            Rectangle(size=(Window.width, Window.height))
        ##################
        EventLoop.window.bind(on_keyboard=self.hook_keyboarde)
        self.mm = 0
        self.ruselt_exit = False
        with self.canvas:
            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')
            Rectangle(size=(Window.width * 1., Window.height * 0.12), pos=(Window.width * 0., Window.height * 0.88))
        #####################################  bar #########################


        # data
        # print(self.name)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            self.cur_h = db.cursor()
            sql_h = ''' SELECT nombre_point FROM point'''
            self.cur_h.execute(sql_h)
            self.data_ = self.cur_h.fetchall()
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()
        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6
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
        reshaped_text1 = ar.reshape('ابدا')
        self.bidi_text1 = get_display(reshaped_text1)
        reshaped_text2 = ar.reshape(u"قائمة الدول")
        self.bidi_text2 = get_display(reshaped_text2)
        reshaped_text3 = ar.reshape(u"اختبر معلوماتك")
        self.bidi_text3 = get_display(reshaped_text3)
        reshaped_text4 = ar.reshape(u"قيم التطبيق")
        self.bidi_text4 = get_display(reshaped_text4)
        reshaped_text5 = ar.reshape(u"شاهدفيديو واحصل على 20 نقطة")
        self.bidi_text5 = get_display(reshaped_text5)
        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)

        with self.canvas:

            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')

            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.50))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.17))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.28))
            Rectangle(size=(Window.width * 0.9, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.39))

        # welcomeBox1 = Button(text= self.bidi_text1,font_name = 'hemidi', size_hint =(0.90,0.1),pos_hint={"x":0.05,"top":0.60} ,on_press=self.poptest)
        welcomeBox2 = Button(text=self.bidi_text2, font_name='hemidi', size_hint=(0.90, 0.1),
                             pos_hint={"x": 0.05, "top": 0.49}, on_press=self.poptest2,
                             background_color=(0., 0., 0., 0.), markup=True)
        welcomeBox3 = Button(text=self.bidi_text3, font_name='hemidi', size_hint=(0.90, 0.1),
                             pos_hint={"x": 0.05, "top": 0.38}, on_press=self.gotojeux,
                             background_color=(0., 0., 0., 0.) , )
        welcomeBox4 = Button(text=self.bidi_text4, font_name='hemidi', size_hint=(0.90, 0.1),
                             pos_hint={"x": 0.05, "top": 0.27}, on_press=self.top_, background_color=(0., 0., 0., 0.),)

        welcomeBox1 = Button(text=self.bidi_text1, font_name='hemidi', size_hint=(0.90, 0.1),
                             pos_hint={"x": 0.05, "top": 0.60}, on_press=self.poptest, border=(25, 25, 25, 25),
                             background_color=(0., 0., 0., 0.))
        welcomeBox5 = Button(text=self.bidi_text5, font_name='hemidi', size_hint=(0.90, 0.1),
                             pos_hint={"x": 0.05, "top": 0.27},on_release=lambda a:ads.show_rewarded_ad(),
                             background_color=(0., 0., 0., 0.))  # on_press = self.exite
        # img_ptn1 = Image(source='post_image.png', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'top': 0.60},
        #                   allow_stretch=True, keep_ratio=False)
        #welcomeBox5.bind(on_press = lambda l : App.get_running_app().stop())

        welcomePage.add_widget(welcomeBox1)
        welcomePage.add_widget(welcomeBox2)
        welcomePage.add_widget(welcomeBox3)
        # welcomePage.add_widget(welcomeBox4)
        welcomePage.add_widget(welcomeBox5)
        welcomePage.add_widget(post_image)
        # welcomePage.add_widget(img_ptn1)

        welcomePage.add_widget(bar)

        self.add_widget(welcomePage)
    def adss(self,i):
        if self.data_qst[0][0] in range(10,40) :
            #ads.show_interstitial()
            pass

    def btn_(self, i):
        img_ptn2 = Image(source='home.png', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'top': 0.60},
                         allow_stretch=True, keep_ratio=False)
        self.add_widget(img_ptn2)
        # time.sleep(.9)
        self.poptest(0)
    def poptest(self, i):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        label_cont2 = Label(text=get_display(ar.reshape(u'عند اجراء مقارنة نسحب 4 نقاط من رصيدك')), font_name='hemidi',
                            font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)
        label_cont3 = Label(text=get_display(ar.reshape(u'بالاضافة كل تحالف يكلف نقطتين')), font_name='hemidi',
                            font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.85}, markup=True)
        welcomePage.add_widget(label_cont2)
        welcomePage.add_widget(label_cont3)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'انتظر')),
                       title_font='hemidi')
        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(self.mo9arana)
        self.p.dismiss()
    def poptest2(self, i):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'انتظر')),
                       title_font='hemidi')
        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(self.information)
        self.p.dismiss()

    def mo9arana(self, instance):
        # sm.add_widget(shose_contry(name='shose_contry'))
        sm.switch_to(shose_contry())
        ads.request_banner()
        ads.show_banner()


    def information(self, instant):
        sm.switch_to(list_contry(name='list_contry'))
        #self.sound_non = SoundLoader.load('sws.wav')

    def top_(self, instant):
        #self.sound_non = SoundLoader.load('sws.wav')

        sm.switch_to(WelcomeScreen())

    def gotojeux(self, i):
        self.adss(0)
        sm.switch_to(jeux_intro())
        #self.sound_non = SoundLoader.load('sws.wav')


    def home(self, inst, touch):
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):

            sm.switch_to(WelcomeScreen())

        # x entre [Window.width*0.10 , Window.width*0.18 ]
        # y entre [Window.height*0.89 , Window.height*0.97]

    def exite(self, inst):
        self.ruselt_exit = True
        welcomePage = FloatLayout()
        image2 = "cr.png"
        img = Image(source=str(image2), size_hint=(0.4, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=get_display(ar.reshape(u'خروج')), font_name='hemidi', size_hint=(0.42, 0.1),
                      pos_hint={"x": 0.07, "top": 0.30})
        btn = Button(text=get_display(ar.reshape(u'لا')), font_name='hemidi', size_hint=(0.42, 0.1),
                     pos_hint={"x": 0.51, "top": 0.30})
        text = get_display(ar.reshape(u'هل تريد الخروج ؟'))
        label_cont2 = Label(text=text, font_name='hemidi', font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)
        welcomePage.add_widget(label_cont2)
        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'تاكيد الخروج')),
                           title_font='hemidi')
        btn.bind(on_press=self.continu_)
        btn1.bind(on_press=self.quit)
        self.popup.open()
        # App.get_running_app().stop()

    def continu_(self, i):
        self.popup.dismiss()
        sm.switch_to(WelcomeScreen())

    def quit(self, i):
        #print(r)
        #PanelBuilderApp.get_running_app().stop()
        #self.get_root_window().close()

        self.popup.dismiss()
        #App.stop(self)
        #self.manager.stop()
        #sm.screens.stop()
        #app.get_running_app().stop()
        #self.manager.app.stop()
        #app.stop()
        #stopTouchApp()
        app.on_quit()



        """ try:
            App.root_window.close()
        except:
            try:
                App.stop()
            except:
                PanelBuilderApp().stop()"""

        # App.get_running_app().is_desktop = 0
    def video_jx(self,i):
        print('tt')






    def hook_keyboarde(self, window, key, *largs):
        if key == 27:
            if self.ruselt_exit == True:
                self.popup.dismiss()

                #App.get_running_app().stop()
                self.exite(0)
                return True
            else:
                self.exite(0)
                return True


class shose_contry(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):  # constructor method
        super(shose_contry, self).__init__(**kwargs)  # init parent

        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.ruselt_1 = False
        print('hemidi benameuuuuuuur  ')
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6

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
        backround = Image(source='bcr_f.png', size_hint=(1., 0.88), pos_hint={'x': 0., 'top': 0.88},
                           allow_stretch=True, keep_ratio=False)


        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        post_image2 = Image(source='comparing.jpg', size_hint=(0.9, 0.18), pos_hint={'x': 0.05, 'y': 0.30},
                            allow_stretch=True, keep_ratio=False)

        func = FloatLayout()
        #self.dropdown = DropDown()
        #self.dropdown2 = DropDown()

        self.welcomeBox1 = Button(text=get_display(ar.reshape(u'قارن')), font_name='hemidi', size_hint=(0.6, 0.1),
                                  pos_hint={"x": 0.20, "top": 0.25},  )
        # self.welcomeBox2 = Button(text='home page', size_hint=(0.3, 0.1), pos_hint={"x": 0.350, "top": 0.90})

        # list_contry
        func.add_widget(backround)
        func.add_widget(bar)

        reshaped_text1 = (u"اضغط لاختيار دولة")
        text_1 = ar.reshape(reshaped_text1)
        text_1 = get_display(text_1)
        self.text_1 = text_1
        with self.canvas:
            Color(45 / 255, 79 / 255, 112 / 255, mode='rgb')
            Rectangle(size=(Window.width * 0.44, Window.height * 0.1), pos=(Window.width * 0.51, Window.height * 0.76))
            Rectangle(size=(Window.width * 0.44, Window.height * 0.1), pos=(Window.width * 0.05, Window.height * 0.76))
            Rectangle(size=(Window.width * 0.6, Window.height * 0.1), pos=(Window.width * 0.20, Window.height * 0.15))
        dropdown = DropDown()
        dropdown2 = DropDown()

        for index in self.data:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text='%s' % (get_display(ar.reshape(dect.get(index[28])))), font_name='hemidi',
                         size_hint_y=None, height=55)
            btn2 = Button(text='%s' % (get_display(ar.reshape(dect.get(index[28])))), font_name='hemidi',
                          size_hint_y=None, height=55)


            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))


            # then add the button inside the dropdown
            dropdown.add_widget(btn)
            dropdown2.add_widget(btn2)
            #dropdown3.add_widget(btn3)
            #dropdown4.add_widget(btn4)

        # create a big main button
        self.mainbutton = Button(text=text_1, font_name='hemidi', size_hint=(0.44, 0.1),
                                 pos_hint={"x": 0.05, "top": 0.86}, )
        self.mainbutton2 = Button(text=text_1, font_name='hemidi', size_hint=(0.44, 0.1),
                                  pos_hint={"x": 0.51, "top": 0.86}, )
        self.thlf = Button(text=get_display(ar.reshape(u'اضافة تحالف')), font_name='hemidi', size_hint=(0.40, 0.1),
                           pos_hint={"x": 0.30, "top": 0.40},on_press=self.tahalef )
        text35 = get_display(ar.reshape(u'اضغط لاختيار تحالف'))
        self.thlf1_1 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                           pos_hint={"x": 0.05, "top": 0.75}, opacity = 0 , disabled = True)
        self.thlf1_2 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.51, "top": 0.75},opacity=0, disabled=True )
        self.thlf2_1 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.05, "top": 0.64}, opacity=0, disabled=True)
        self.thlf2_2 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.51, "top": 0.64},opacity=0, disabled=True )
        self.thlf3_1 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.05, "top": 0.53}, opacity=0, disabled=True)
        self.thlf3_2 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.51, "top": 0.53}, opacity=0, disabled=True)
        self.thlf4_1 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.05, "top": 0.42}, opacity=0, disabled=True)
        self.thlf4_2 = Button(text=text35, font_name='hemidi', size_hint=(0.44, 0.1),
                              pos_hint={"x": 0.51, "top": 0.42}, opacity=0, disabled=True)
        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.tahalef_target = 0
        #self.tahalef(0,0)
        #self.thlf.bind(on_press=self.tahalef )
        #Clock.schedule_interval(self.tmr, 1)
        #Clock.schedule_once(my_callback)
        #print('rrr')
        self.welcomeBox1.bind(on_press=self.poptest)
        self.thlf1_1.bind(on_release=dropdown.open)
        self.thlf1_2.bind(on_release=dropdown2.open)
        self.thlf2_1.bind(on_release=dropdown.open)
        self.thlf2_2.bind(on_release=dropdown2.open)
        self.thlf3_1.bind(on_release=dropdown.open)
        self.thlf3_2.bind(on_release=dropdown2.open)
        self.thlf4_1.bind(on_release=dropdown.open)
        self.thlf4_2.bind(on_release=dropdown2.open)
        self.mainbutton.bind(on_release=dropdown.open)
        self.mainbutton2.bind(on_release=dropdown2.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.

        dropdown.bind(on_select=lambda instance, x:self.return_satter_button_drop(0,x) ) #self.mainbutton self.return_satter_button_drop(0,x)
        dropdown2.bind(on_select=lambda instance, x2:self.return_satter_button_drop2(0,x2)) #self.return_satter_button_drop2(0,x)
        dropdown.bind(on_press=self.return_val)
        dropdown2.bind(on_press=self.return_val)

        # runTouchApp(mainbutton)



        #func.add_widget(post_image)
        #func.add_widget(post_image2)

        func.add_widget(self.thlf4_1)
        func.add_widget(self.thlf4_2)
        func.add_widget(self.thlf3_1)
        func.add_widget(self.thlf3_2)
        func.add_widget(self.thlf2_1)
        func.add_widget(self.thlf2_2)
        func.add_widget(self.thlf1_1)
        func.add_widget(self.thlf1_2)
        func.add_widget(self.mainbutton2)
        func.add_widget(self.mainbutton)
        func.add_widget(self.thlf)
        func.add_widget(self.welcomeBox1)




        self.add_widget(func)
        #val2 = self.mainbutton2.text
        # self.val1 = 'f'

    def return_satter_button_drop(self,i,x):

        if self.tahalef_target == 1 :
            setattr(self.thlf1_1, 'text', x)
        elif self.tahalef_target == 2 :
            setattr(self.thlf2_1, 'text', x)
        elif self.tahalef_target == 3:
            setattr(self.thlf3_1, 'text', x)
        elif self.tahalef_target == 4:
            setattr(self.thlf4_1, 'text', x)
        else :
            setattr(self.mainbutton, 'text', x)
    def return_satter_button_drop2(self,i,x):

        if self.tahalef_target == 1:
            setattr(self.thlf1_2, 'text', x)
        elif self.tahalef_target == 2:
            setattr(self.thlf2_2, 'text', x)
        elif self.tahalef_target == 3:
            setattr(self.thlf3_2, 'text', x)
        elif self.tahalef_target == 4:
            setattr(self.thlf4_2, 'text', x)
        else:
            setattr(self.mainbutton2, 'text', x)


    def tahalef(self,i ):

        self.tahalef_target = self.tahalef_target + 1
        #print(self.tahalef_target)
        if self.tahalef_target == 1 :
            self.thlf1_1.opacity = 1
            self.thlf1_1.disabled = False
            self.thlf1_2.opacity = 1
            self.thlf1_2.disabled = False
            self.mainbutton.disabled = True
            self.mainbutton2.disabled = True
        elif self.tahalef_target == 2 :
            self.thlf2_1.opacity = 1
            self.thlf2_1.disabled = False
            self.thlf2_2.opacity = 1
            self.thlf2_2.disabled = False
            self.thlf1_1.disabled = True
            self.thlf1_2.disabled = True
        elif self.tahalef_target == 3:
            self.thlf3_1.opacity = 1
            self.thlf3_1.disabled = False
            self.thlf3_2.opacity = 1
            self.thlf3_2.disabled = False
            self.thlf2_1.disabled = True
            self.thlf2_2.disabled = True
        elif self.tahalef_target == 4:
            self.thlf.opacity = 0
            self.thlf.disabled = True
            self.thlf4_1.opacity = 1
            self.thlf4_1.disabled = False
            self.thlf4_2.opacity = 1
            self.thlf4_2.disabled = False
            self.thlf3_1.disabled = True
            self.thlf3_2.disabled = True
        #print('hhhh')
        #self.tahalef_target = self.tahalef_target + 1



    def get_key(self, i, val):
        # print(val)
        f = 0
        for i in dect.values():

            if val == get_display(ar.reshape(i)):
                for key, value in dect.items():
                    # print(val , value)
                    if i == value:
                        f = 1
                        return key
            else:
                # return 'nnnnnnn'
                pass
        if f == 0:
            return False
    def poptest(self, i):
        welcomePage = FloatLayout()
        image2 = "vs.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        label_cont2 = Label(text=get_display(ar.reshape(u'الرجاء الانتظار جاري تحضير المقارنة ...')), font_name='hemidi',
                            font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)

        welcomePage.add_widget(label_cont2)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'انتظر')),
                       title_font='hemidi')
        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(self.return_val)
        self.p.dismiss()

    def return_val(self, instant):


        val22 = self.get_key(0,self.mainbutton2.text)  # dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val11 = self.get_key(0, self.mainbutton.text)
        #
        val4 = self.get_key(0,self.thlf1_2.text)  # dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val3 = self.get_key(0, self.thlf1_1.text)
        #
        val6 = self.get_key(0,self.thlf2_2.text)  # dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val5 = self.get_key(0, self.thlf2_1.text)
        #
        val8 = self.get_key(0,self.thlf3_2.text)  # dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val7 = self.get_key(0, self.thlf3_1.text)
        #
        val10 = self.get_key(0,self.thlf4_2.text)  # dect[self.get_key(0,get_display(ar.reshape(self.mainbutton2.text)))]
        val9 = self.get_key(0, self.thlf4_1.text)
        #print(val3,val4,val5,val6,val7,val8,val9,val10)
        val1 = [val11,val3 , val5 , val7, val9]
        val2 = [val22 , val4 , val6 , val8 , val10]
        val1 = [s for s in val1 if s != False]
        val2 = [s for s in val2 if s != False]
        #print(cont_1 )

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        self.file_h = (db_path)
        self.conn_h = sqlite3.connect(self.file_h)
        self.cur_h = self.conn_h.cursor()
        sql_h = ''' SELECT nombre_point FROM point'''
        self.cur_h.execute(sql_h)
        self.data_ = self.cur_h.fetchall()
        # print(val2,val1)
        # print(self.text_1)

        if not (val11 == False or val22 == False ):
            ads.destroy_banner()
            #if not ( (self.data_[0][0] < 20) or (self.nv == 6)  ) : #20
            if ( (self.data_[0][0] >= 20) or (self.nv == 6)  ) : #20
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                db_path = BASE_DIR.replace("\\", "/") + '/data.db'
                self.file_h = (db_path)
                self.conn_h = sqlite3.connect(self.file_h)
                self.cur_h = self.conn_h.cursor()
                sql_h = ''' SELECT nombre_point FROM point'''
                self.cur_h.execute(sql_h)
                self.data_ = self.cur_h.fetchall()
                # qst
                self.file_qst = (db_path)
                self.conn_qst = sqlite3.connect(self.file_qst)
                self.cur_qst = self.conn_qst.cursor()
                sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
                self.cur_qst.execute(sql_qst)
                self.data_qst = self.cur_qst.fetchall()

                n = self.data_[0][0]

                h = (len(val1) + len(val2))-2
                if h != 0 :
                    if int(n) < (4+h*2):
                        m = 0
                    else :
                        m = n - (4+h*2) ##################" -5
                else :
                    if int(n) < 4 :
                        m = 0
                    else :
                        m = n - 4

                self.cur_h.execute(
                    ''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
                self.conn_h.commit()

                # print('yes')
                # sm.add_widget(result_vs(list([val1, val2]), name='result_vs'))
                # self.manager.current = 'result_vs'
                # sm.switch_to(result_vs(list([val1,val2])),direction='right', duration=1.)
                # print('iiiiii')
                self.val_ = list([val1, val2])
                #self.puptest(0)
                self.eventes(0, self.val_)
            else:
                self.ruselt_1 = True
                self.return_jeux(0)
        else:
            pass

    def puptest(self, i):
        welcomePage = FloatLayout()
        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'انتظر')),
                       title_font='hemidi')
        self.p.open()
        Clock.schedule_once(lambda *args: self.eventes(0, self.val_))
        self.p.dismiss()

    def eventes(self, i, k):
        #sm.add_widget(result_vs(k, name='result_vs'))
        sm.switch_to(result_vs(k))
        #pass
        #print(k)

    def return_jeux(self, instant):

        reshaped_text3 = ar.reshape(u"العب و جمع النقاط")
        self.bidi_text3 = get_display(reshaped_text3)
        reshaped_text4 = ar.reshape(u"شاهد فيديو مقابل 20 نقطة")
        self.bidi_text4 = get_display(reshaped_text4)
        reshaped_text5 = ar.reshape(u"يجب ان تمتلك 20 نقطعة على الاقل ")
        self.bidi_text5 = get_display(reshaped_text5)
        reshaped_text6 = ar.reshape(u"او تصل للمستوى السادس")
        self.bidi_text6 = get_display(reshaped_text6)

        welcomePage = FloatLayout()
        image2 = "cr.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.27), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=self.bidi_text4, font_name='hemidi', size_hint=(0.47, 0.1),
                      pos_hint={"x": 0.02, "top": 0.30})
        btn = Button(text=self.bidi_text3, font_name='hemidi', size_hint=(0.47, 0.1), pos_hint={"x": 0.51, "top": 0.30})
        label_cont2 = Label(text=self.bidi_text5, font_name='hemidi', font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.95}, markup=True)
        label_cont3 = Label(text=self.bidi_text6, font_name='hemidi', font_size='20sp', size_hint=(0.4, 0.2),
                            pos_hint={'x': 0.3, 'top': 0.85}, markup=True)

        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)
        welcomePage.add_widget(label_cont2)
        welcomePage.add_widget(label_cont3)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False,
                           title=get_display(ar.reshape(u'للاسف لا يمكن اجراء المقارنة')), title_font='hemidi')

        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.vers_jeux)
        btn1.bind(on_press=self.vers_home)

        # open the popup
        self.popup.open()


    def vers_jeux(self, ins):
        self.popup.dismiss()
        sm.switch_to(jeux_intro())


    def vers_home(self, ins):
        self.popup.dismiss()
        #sm.switch_to(WelcomeScreen())
        ads.show_rewarded_ad()


    def home(self, instant, touch):
        # self.manager.current = 'result_vs' #result_vs
        # self.manager.screens[2].ids.btn.text = self.mainbutton2.text
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())


    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            if self.ruselt_1 == True:
                self.popup.dismiss()
                ads.destroy_banner()
                sm.switch_to(WelcomeScreen())


                return True
            else:
                ads.destroy_banner()
                sm.switch_to(WelcomeScreen())


                return True


class list_contry(Screen):
    def __init__(self, **kwargs):  # constructor method
        super(list_contry, self).__init__(**kwargs)  # init parent
        ads.destroy_banner()
        self.hh(0)
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hh(self, i):
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6

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

        self.layout = GridLayout(cols=1, spacing=10, size_hint=(1., None), pos_hint={"centre_x": 0.30}, height=1920)
        # Make sure the height is such that there is something to scroll.
        # self.layout.bind(minimum_height=self.layout.setter('height'))
        # self.layout = ObjectProperty(None)
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
        d = 0
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
        # print(self.data[134][28])
        """        ml=1
        for i in self.data:
            self.btn = Button(text=i[28], font_name='hemidi', size_hint_y=None, size_hint_x=1.,
                              pos_hint={'x': 0., 'top': None}, height=80 , id=str(ml),on_release =  lambda  *args : self.vers_info_contry(0,self.btn.text) )  #on_press =lambda  *args : self.vers_info_contry(0,self.btn.text))
            self.layout.add_widget(self.btn)


           """

        # print(len(self.data))
        """h = []
        for i in self.data :
            h.append(i[28])
        print(h)
        print('************')
        for  l  in dect.keys() :
            if l not in h :
                print(l)"""
        #self.data[69][28]

        self.btn1 = Button(text=get_display(ar.reshape(dect.get(str(self.data[0][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[0][28])))
        self.btn2 = Button(text=get_display(ar.reshape(dect.get(str(self.data[1][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[1][28])))
        self.btn3 = Button(text=get_display(ar.reshape(dect.get(str(self.data[2][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[2][28])))
        self.btn4 = Button(text=get_display(ar.reshape(dect.get(str(self.data[3][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[3][28])))
        self.btn5 = Button(text=get_display(ar.reshape(dect.get(str(self.data[4][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[4][28])))
        self.btn6 = Button(text=get_display(ar.reshape(dect.get(str(self.data[5][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[5][28])))
        self.btn7 = Button(text=get_display(ar.reshape(dect.get(str(self.data[6][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[6][28])))
        self.btn8 = Button(text=get_display(ar.reshape(dect.get(str(self.data[7][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[7][28])))
        self.btn9 = Button(text=get_display(ar.reshape(dect.get(str(self.data[8][28])))), font_name='hemidi',
                           size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                           on_press=lambda *args: self.vers_info_contry(0, str(self.data[8][28])))
        self.btn10 = Button(text=get_display(ar.reshape(dect.get(str(self.data[9][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[9][28])))
        self.btn11 = Button(text=get_display(ar.reshape(dect.get(str(self.data[10][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[10][28])))
        self.btn12 = Button(text=get_display(ar.reshape(dect.get(str(self.data[11][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[11][28])))
        self.btn13 = Button(text=get_display(ar.reshape(dect.get(str(self.data[12][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[12][28])))
        self.btn14 = Button(text=get_display(ar.reshape(dect.get(str(self.data[13][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[13][28])))
        self.btn15 = Button(text=get_display(ar.reshape(dect.get(str(self.data[14][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[14][28])))
        self.btn16 = Button(text=get_display(ar.reshape(dect.get(str(self.data[15][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[15][28])))
        self.btn17 = Button(text=get_display(ar.reshape(dect.get(str(self.data[16][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[16][28])))
        self.btn18 = Button(text=get_display(ar.reshape(dect.get(str(self.data[17][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[17][28])))
        self.btn19 = Button(text=get_display(ar.reshape(dect.get(str(self.data[18][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[18][28])))
        self.btn20 = Button(text=get_display(ar.reshape(dect.get(str(self.data[19][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[19][28])))
        self.btn21 = Button(text=get_display(ar.reshape(dect.get(str(self.data[20][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[20][28])))
        self.btn22 = Button(text=get_display(ar.reshape(dect.get(str(self.data[21][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[21][28])))
        self.btn23 = Button(text=get_display(ar.reshape(dect.get(str(self.data[22][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[22][28])))
        self.btn24 = Button(text=get_display(ar.reshape(dect.get(str(self.data[23][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[23][28])))
        self.btn25 = Button(text=get_display(ar.reshape(dect.get(str(self.data[24][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[24][28])))
        self.btn26 = Button(text=get_display(ar.reshape(dect.get(str(self.data[25][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[25][28])))
        self.btn27 = Button(text=get_display(ar.reshape(dect.get(str(self.data[26][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[26][28])))
        self.btn28 = Button(text=get_display(ar.reshape(dect.get(str(self.data[27][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[27][28])))
        self.btn29 = Button(text=get_display(ar.reshape(dect.get(str(self.data[28][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[28][28])))
        self.btn30 = Button(text=get_display(ar.reshape(dect.get(str(self.data[29][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[29][28])))
        self.btn31 = Button(text=get_display(ar.reshape(dect.get(str(self.data[30][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[30][28])))
        self.btn32 = Button(text=get_display(ar.reshape(dect.get(str(self.data[31][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[31][28])))
        self.btn33 = Button(text=get_display(ar.reshape(dect.get(str(self.data[32][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[32][28])))
        self.btn34 = Button(text=get_display(ar.reshape(dect.get(str(self.data[33][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[33][28])))
        self.btn35 = Button(text=get_display(ar.reshape(dect.get(str(self.data[34][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[34][28])))
        self.btn36 = Button(text=get_display(ar.reshape(dect.get(str(self.data[35][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[35][28])))
        self.btn37 = Button(text=get_display(ar.reshape(dect.get(str(self.data[36][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[36][28])))
        self.btn38 = Button(text=get_display(ar.reshape(dect.get(str(self.data[37][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[37][28])))
        self.btn39 = Button(text=get_display(ar.reshape(dect.get(str(self.data[38][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[38][28])))
        self.btn40 = Button(text=get_display(ar.reshape(dect.get(str(self.data[39][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[39][28])))
        self.btn41 = Button(text=get_display(ar.reshape(dect.get(str(self.data[40][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[40][28])))
        self.btn42 = Button(text=get_display(ar.reshape(dect.get(str(self.data[41][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[41][28])))
        self.btn43 = Button(text=get_display(ar.reshape(dect.get(str(self.data[42][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[42][28])))
        self.btn44 = Button(text=get_display(ar.reshape(dect.get(str(self.data[43][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[42][28])))
        self.btn45 = Button(text=get_display(ar.reshape(dect.get(str(self.data[44][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[44][28])))
        self.btn46 = Button(text=get_display(ar.reshape(dect.get(str(self.data[45][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[45][28])))
        self.btn47 = Button(text=get_display(ar.reshape(dect.get(str(self.data[46][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[46][28])))
        self.btn48 = Button(text=get_display(ar.reshape(dect.get(str(self.data[47][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[47][28])))
        self.btn49 = Button(text=get_display(ar.reshape(dect.get(str(self.data[48][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[48][28])))
        self.btn50 = Button(text=get_display(ar.reshape(dect.get(str(self.data[49][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[49][28])))
        self.btn51 = Button(text=get_display(ar.reshape(dect.get(str(self.data[50][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[50][28])))
        self.btn52 = Button(text=get_display(ar.reshape(dect.get(str(self.data[51][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[51][28])))
        self.btn53 = Button(text=get_display(ar.reshape(dect.get(str(self.data[52][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[52][28])))
        self.btn54 = Button(text=get_display(ar.reshape(dect.get(str(self.data[53][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[53][28])))
        self.btn55 = Button(text=get_display(ar.reshape(dect.get(str(self.data[54][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[54][28])))
        self.btn56 = Button(text=get_display(ar.reshape(dect.get(str(self.data[55][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[55][28])))
        self.btn57 = Button(text=get_display(ar.reshape(dect.get(str(self.data[56][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[56][28])))
        self.btn58 = Button(text=get_display(ar.reshape(dect.get(str(self.data[57][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[57][28])))
        self.btn59 = Button(text=get_display(ar.reshape(dect.get(str(self.data[58][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[58][28])))
        self.btn60 = Button(text=get_display(ar.reshape(dect.get(str(self.data[59][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[59][28])))
        self.btn61 = Button(text=get_display(ar.reshape(dect.get(str(self.data[60][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[60][28])))
        self.btn62 = Button(text=get_display(ar.reshape(dect.get(str(self.data[61][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[61][28])))
        self.btn63 = Button(text=get_display(ar.reshape(dect.get(str(self.data[62][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[62][28])))
        self.btn64 = Button(text=get_display(ar.reshape(dect.get(str(self.data[63][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[63][28])))
        self.btn65 = Button(text=get_display(ar.reshape(dect.get(str(self.data[64][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[64][28])))
        self.btn66 = Button(text=get_display(ar.reshape(dect.get(str(self.data[65][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[65][28])))
        self.btn67 = Button(text=get_display(ar.reshape(dect.get(str(self.data[66][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[66][28])))
        self.btn68 = Button(text=get_display(ar.reshape(dect.get(str(self.data[67][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[67][28])))
        self.btn69 = Button(text=get_display(ar.reshape(dect.get(str(self.data[68][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[68][28])))
        self.btn70 = Button(text=get_display(ar.reshape(dect.get(str(self.data[69][28])))), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            on_press=lambda *args: self.vers_info_contry(0, str(self.data[69][28])))
        self.btn71= Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )

        self.btn73 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )
        self.btn74 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )
        self.btn72 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )
        self.btn75 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )
        self.btn76 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi',
                            size_hint_y=None, size_hint_x=1., pos_hint={'x': 0.05, 'top': None}, height=80,
                            )
        lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,
               self.btn10, self.btn11, self.btn12, self.btn13,
               self.btn14, self.btn15, self.btn16, self.btn17, self.btn18, self.btn19, self.btn20, self.btn21,
               self.btn22,
               self.btn23, self.btn24, self.btn25, self.btn26,
               self.btn27, self.btn28, self.btn29, self.btn30, self.btn31, self.btn32, self.btn33, self.btn34,
               self.btn35,
               self.btn36, self.btn37, self.btn38, self.btn39, self.btn40,
               self.btn41, self.btn42, self.btn43, self.btn44, self.btn45, self.btn46, self.btn47, self.btn48,
               self.btn49,
               self.btn50, self.btn51, self.btn52, self.btn53, self.btn54, self.btn55, self.btn56, self.btn57,
               self.btn58, self.btn59, self.btn60, self.btn61, self.btn62,
               self.btn63, self.btn64, self.btn65, self.btn66, self.btn67, self.btn68 , self.btn69 , self.btn70 , self.btn71,
               self.btn72 , self.btn73 , self.btn74 , self.btn75 , self.btn76

               ]
        """self.btn55, self.btn56, self.btn57, self.btn58, self.btn59, self.btn60, self.btn61, self.btn62,
        self.btn63,
        self.btn64, self.btn65, self.btn66, self.btn67, self.btn68, self.btn49,self.btn50, self.btn51, self.btn52, self.btn53, self.btn54,"""
        i = 0
        for ig in lst:
            """self.btn1 = Button(text=str(ig[28]), size_hint_y=None, size_hint_x=1.,
                               pos_hint={'x': 0.05, 'top': None}, height=60,on_press=lambda *args: self.vers_info_contry(0, ig[28])
                              )"""

            self.layout.add_widget(ig)
        # print(self.btn1.pos)

        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                               pos_hint={"x": 0.05, "top": 0.60})
        self.root.add_widget(self.layout)
        func.add_widget(self.root)
        func.add_widget(bar)

        self.add_widget(func)

    def home(self, instant, touch):
        # self.manager.current = 'welcomeScreen'
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())


    def vers_info_contry(self, i, inst):
        welcomePage = FloatLayout()

        image2 = "attn.png"
        img = Image(source=str(image2), size_hint=(0.40, 0.270), pos_hint={'x': 0.30, 'y': 0.36},
                    allow_stretch=True, keep_ratio=False)
        welcomePage.add_widget(img)
        self.p = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'انتظر')),
                       title_font='hemidi')
        ads.destroy_banner()
        self.p.open()
        Clock.schedule_once(lambda *args: self.vers_info_contry_2(0, inst))
        self.p.dismiss()

    def vers_info_contry_2(self, i, inst):

        sm.switch_to(info_contry(inst, name='info_contry'))

    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())

            return True


################################### hkendemti  fine


class result_vs(Screen):
    # code = StringProperty('')
    code = ListProperty()

    def __init__(self, acc, **kwargs):  # constructor method
        super(result_vs, self).__init__(**kwargs)  # init parent
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6

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
        # print(acc)
        # print(acc)

        self.cr(0, acc)
        # print(self.code)

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

    def cr(self, i, acc):
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
        v_contry1 = [0]*len(status)
        v_contry2 = [0]*len(status)

        for i in data:
            for pay in acc[0] :
                if pay == i[28]:
                    m = list(i)
                    m.remove(i[28])
                    m = list(map(int, m))

                    h1 = [m,v_contry1]
                    v_contry1 = [sum(x) for x in zip(*h1)]
            for pay2 in acc[1]:
                if pay2 == i[28]:
                    m1 = list(i)
                    m1.remove(i[28])
                    m1 = list(map(int, m1))
                    h2 = [m1,v_contry2]
                    v_contry2 = [sum(x) for x in zip(*h2)]


        # print(len(self.status))
        # print(len(self.v_contry1))
        # print(len(self.v_contry2))

        self.func = FloatLayout()

        self.layout = GridLayout(cols=3, spacing=10, size_hint_y=None, pos_hint={"centre_x": 0.02})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        # https://googledrive.com/host/<folderID>/<filename>
        # https://drive.google.com/uc?id=FILE_ID
        image1 = 'flag/' + acc[0][0] + '.png'

        image2 = 'flag/' + acc[1][0] + '.png'
        img = Image(source=str(image1), size_hint=(0.2866, 0.15), pos_hint={'x': 0.05, 'y': 0.62},
                    allow_stretch=True, keep_ratio=False)
        img2 = Image(source=str(image2), size_hint=(0.2866, 0.15), pos_hint={'x': 0.6566, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)
        img3 = Image(source='vs.png', size_hint=(0.2866, 0.15), pos_hint={'x': 0.35, 'y': 0.62},
                     allow_stretch=True, keep_ratio=False)

        btn3_l = Label(text="[b][color=#070B19]%s[/color][/b]" % (get_display(ar.reshape(dect[acc[0][0]]))), font_name='hemidi',
                       size_hint=(0.280, 0.1),
                       pos_hint={'x': 0.05, 'top': 0.90}, markup=True)

        if len(acc[0]) == 1:
            hlha = 0

        else:
            #print(acc[1:])
            #mo = list(acc[1:])
            #for i in acc[0][1:]:
            #hlha = dect[i] +' '+ u'و' +' ' +hlha
            hlha = len(acc[0])
            v_contry1[28] = 0
        if len(acc[1]) == 1:
            hlha5 = 0
            self.tasnif2 = True
        else:
            #print(acc[1:])
            #mo = list(acc[1:])
            #for i in acc[1][1:]:
            #hlha5 = dect[i] +' '+ u'و' +' ' +hlha5
            hlha5 = len(acc[1])
            v_contry2[28] = 0

        tx4 = get_display(ar.reshape( u'التحالفات'+' '+':'+str(hlha)) )
        tx5 = get_display(ar.reshape( u'التحالفات'+' '+':'+str(hlha5)) )

        btn1_l = Label(text="[b][color=#070B19]%s[/color][/b]" % (tx4) , font_name='hemidi',
                     size_hint=(0.280, 0.1),
                     pos_hint={'x': 0.05, 'top': 0.85}, markup=True)
        btn2_l = Label(text="[b][color=#070B19]%s[/color][/b]" % (get_display(ar.reshape(dect[acc[1][0]]))),
                       font_name='hemidi',
                       size_hint=(0.280, 0.1),
                       pos_hint={'x': 0.65, 'top': 0.90}, markup=True)
        btn5_l = Label(text="[b][color=#070B19]%s[/color][/b]" % (tx5), font_name='hemidi',
                       size_hint=(0.280, 0.1),
                       pos_hint={'x': 0.65, 'top': 0.85}, markup=True)

        self.func.add_widget(img2)
        self.func.add_widget(btn1_l)
        self.func.add_widget(btn2_l)
        self.func.add_widget(btn3_l)
        self.func.add_widget(btn5_l)
        self.func.add_widget(img)
        self.func.add_widget(img3)
        self.func.add_widget(self.bar)

        n = 0.1
        for i in range(len(data[1])-1):

            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None}, height=60)
            # print(v_contry1[i])


            self.btn1 = Button(text='hello2', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None}, height=60)
            self.btn2 = Button(text='gg', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None},
                               height=60)



            # self.btn.text = str(v_contry1[i])
            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)
            self.layout.add_widget(self.btn2)

            reshaped_text = ar.reshape((status1[i]))
            self.bidi_text = get_display(reshaped_text)

            setattr(self.btn, 'text', str("{:,}".format(int(v_contry1[i]))))
            setattr(self.btn1, 'text', self.bidi_text)
            setattr(self.btn2, 'text', str("{:,}".format(int(v_contry2[i]))))
        for i in range(7):
            self.btn10 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None}, height=60)
            # print(v_contry1[i])

            self.btn11 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None}, height=60)
            self.btn12 = Button(text=get_display(ar.reshape(u'غير متوفر')), font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None},
                               height=60)
            self.layout.add_widget(self.btn10)
            self.layout.add_widget(self.btn11)
            self.layout.add_widget(self.btn12)
        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                               pos_hint={"x": 0.05, "top": 0.59})  # , size=(Window.width, Window.height)
        self.root.add_widget(self.layout)
        self.func.add_widget(self.root)
        self.add_widget(self.func)
        # self.add_widget(img)

    def update(self, instant):
        self.btn.text = 'hemidi'

    def press(self, instant):
        # print(self.contry_vs)

        pass

    def home(self, instant, touch):
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())


    def jeux(self, instant):
        # self.manager.current = 'welcomeScreen'
        # print(self.code)
        pass

    def return_(self, window):

        sm.switch_to(shose_contry())


    def poptest(self, window, key, *args):
        if key == 27:
            ads.destroy_banner()
            sm.switch_to(WelcomeScreen())

            return True







class jeux_embdad(Screen):  # welcomeScreen subclass
    coord = StringProperty('')

    def __init__(self, hemidi, rune, **kwargs):  # constructor method
        super(jeux_embdad, self).__init__(**kwargs)  # init parent
        self.sound_time = SoundLoader.load('time.wav')

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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()
        #ads
        if int(self.data_qst[0][0]==15):
            ads.show_interstitial()
        if int(self.data_qst[0][0]==30):
            ads.show_interstitial()
        if int(self.data_qst[0][0]==45):
            ads.show_interstitial()
        if int(self.data_qst[0][0]==60):
            ads.show_interstitial()
        if int(self.data_qst[0][0]==75):
            ads.show_interstitial()
        if int(self.data_qst[0][0] == 90):
            ads.show_interstitial()
        if int(self.data_qst[0][0] == 105):
            ads.show_interstitial()
        if int(self.data_qst[0][0] == 120):
            ads.show_interstitial()
        if int(self.data_qst[0][0] == 135):
            ads.show_interstitial()
        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
            text2 = u'هذا العلم لاي دولة ؟ '
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
            text2 = u'هذا الشعار  لاي دولة ؟ '
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
            text2 = u'هذه الخريطة لاي دولة ؟ '
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
            text2 = u'كم عدد سكان '
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
            text2 = u'تصنيف جيش '
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6
            text2 = u'بالكيلومتر مربع كم مساحة'

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

        if self.rune == 'yes':
            # print(self.data_[1][0])
            # print(self.data_[0][0])
            self.ruselta = False

            ############################
            if self.file_j == 'embadad'  or  self.file_j == 'map' or self.file_j == 'flag' :
                self.target_text = 'text'
                nome_image = os.listdir(r"%s" % (self.file_j))

                self.img_embdad = random.choice(nome_image)

                welcomePage = FloatLayout()
                image2 = "%s/%s" % (str(self.file_j), str(self.img_embdad))
                nome_image.remove(self.img_embdad)
                # cont =random.choices(nome_image , k=3) #malaysia
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
                # image2 = "embadad/spain.png"
                img = Image(source=str(image2), size_hint=(0.80, 0.30), pos_hint={'x': 0.1, 'y': 0.40},
                            allow_stretch=True, keep_ratio=False)
            else :
                kk =list(dect.keys())
                kk.remove('israel')#'israel'
                nome_pay = random.choice(kk)
                self.target_text = 'nombre'
                if self.file_j == 'pop':
                    # 3adad sokan
                    image2 = "flag/%s" % (str(nome_pay) + '.png')
                    some = 27
                if self.file_j == 'GBD':
                    # tasnif  doli
                    image2 = "embadad/%s" % (str(nome_pay) + '.png')
                    some = 29
                if self.file_j == 'MD':
                    # misaha
                    image2 = "map/%s" % (str(nome_pay) + '.png')
                    some = 39
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                db_path = BASE_DIR.replace("\\", "/") + '/data.db'

                self.file = (db_path)
                self.conn = sqlite3.connect(self.file)
                self.cur = self.conn.cursor()
                sql = ''' SELECT * FROM table_1 '''
                self.cur.execute(sql)
                self.data = self.cur.fetchall()
                nome_image = self.data

                for i in nome_image :
                    if i[28]  ==  nome_pay :
                        self.rslt = i[some]
                        nome_image.remove(i)
                self.img_embdad = self.rslt
                #print(self.img_embdad)
                welcomePage = FloatLayout()
                #image2 = "%s/%s" % (str(self.file_j), str(self.file_j)+'.jpg')
                #nome_image.remove(self.img_embdad)
                # cont =random.choices(nome_image , k=3) #malaysia
                cont = []
                im11 = random.choice(nome_image)
                im1 = im11[some]
                nome_image.remove(im11)
                cont.append(im1)
                im22 = random.choice(nome_image)
                im2 = im22[some]
                nome_image.remove(im22)
                cont.append(im2)
                im33 = random.choice(nome_image)
                im3 = im33[some]
                nome_image.remove(im33)
                cont.append(im3)
                cont.append(self.img_embdad)
                # image2 = "embadad/spain.png"
                img = Image(source=str(image2), size_hint=(0.80, 0.30), pos_hint={'x': 0.1, 'y': 0.40},
                            allow_stretch=True, keep_ratio=False)
                #print(cont)




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
            if self.target_text == 'text' :
                txt0 = get_display(ar.reshape(dect.get(str(l1[:-4]))))
            else  :
                txt0 = "{:,}".format(int(l1))
            welcomeBox1 = Button(text=txt0, font_name='hemidi',
                                 size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.38},
                                 background_color=(0., 0., 0., 0.))
            welcomeBox1.bind(on_press=lambda *args: self.result_in(0, l1))
            welcomeBox1.bind(on_press=lambda u: self.sound_time.stop())

            cont.remove(l1)
            l2 = random.choice(cont)
            if self.target_text == 'text' :
                txt1 = get_display(ar.reshape(dect.get(str(l2[:-4]))))
            else  :
                txt1 = "{:,}".format(int(l2))
            welcomeBox2 = Button(text=txt1, font_name='hemidi',
                                 size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.38},
                                 background_color=(0., 0., 0., 0.))
            welcomeBox2.bind(on_press=lambda *args: self.result_in(0, l2))
            welcomeBox2.bind(on_press=lambda u: self.sound_time.stop())

            cont.remove(l2)
            l3 = random.choice(cont)
            if self.target_text == 'text' :
                txt2 = get_display(ar.reshape(dect.get(str(l3[:-4]))))
            else  :

                txt2 = "{:,}".format(int(l3))
            welcomeBox3 = Button(text=txt2, font_name='hemidi',
                                 size_hint=(0.44, 0.1), pos_hint={"x": 0.05, "top": 0.25},
                                 background_color=(0., 0., 0., 0.))
            welcomeBox3.bind(on_press=lambda *args: self.result_in(0, l3))
            welcomeBox3.bind(on_press=lambda u: self.sound_time.stop())

            cont.remove(l3)
            l4 = cont[0]
            if self.target_text == 'text' :
                txt3 = get_display(ar.reshape(dect.get(str(l4[:-4]))))
            else  :
                txt3 = "{:,}".format(int(l4))
            welcomeBox4 = Button(text=txt3, font_name='hemidi',
                                 size_hint=(0.44, 0.1), pos_hint={"x": 0.51, "top": 0.25},
                                 background_color=(0., 0., 0., 0.))
            welcomeBox4.bind(on_press=lambda *args: self.result_in(0, l4))
            welcomeBox4.bind(on_press=lambda u: self.sound_time.stop())
            #print(dect[nome_pay])
            #print(self.target_text)
            if self.target_text ==  'nombre' :
                add_txt = ' ' + dect[nome_pay]
                #print(add_txt)

            else  :
                add_txt = ''
            text = ar.reshape(text2+add_txt)
            self.text_label = get_display(text)
            # "[b][color=#070B19]%s[/color][/b]"% ('time')

            btn1 = Label(text="[b][color=#070B19]%s[/color][/b]" % (self.text_label), font_name='hemidi',
                         size_hint=(0.80, 0.1),
                         pos_hint={'x': 0.1, 'top': 0.80}, markup=True)

            welcomePage.add_widget(welcomeBox1)
            welcomePage.add_widget(welcomeBox2)
            welcomePage.add_widget(welcomeBox3)
            welcomePage.add_widget(welcomeBox4)
            welcomePage.add_widget(bar)

            # self.event()
            self.timer_ = Label(text="[b][color=#070B19]%s[/color][/b]" % ('time'), size_hint=(0.24, 0.05),
                                pos_hint={"x": 0.38, "top": 0.850}, markup=True)
            welcomePage.add_widget(self.timer_)

            welcomePage.add_widget(img)
            welcomePage.add_widget(btn1)

            self.add_widget(welcomePage)
            self.XI = '0'
            self.event = Clock.schedule_interval(self.tmr, 1)

        else:
            pass


    def tmr(self, *args):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds += 60
            self.minutes -= 1
        if self.minutes == 0 and self.seconds == 0:
            self.minutes = 0
            self.seconds = 0

        self.time_ = datetime.timedelta(minutes=self.minutes, seconds=self.seconds)
        l = str(self.time_)
        # print(l) afficher timer

        XI = 0

        if '-1 day' not in str(l):
            # self.root.ids.time.text = 'Time Over!'
            setattr(self.timer_, 'text', "[b][color=#070B19]%s[/color][/b]" % str(l))
            if self.sound_time:
                self.sound_time.play()
            L = int(self.XI)
            L += 1
            self.XI = str(L)
        else:
            setattr(jeux_embdad, self.rune, 'non')
            setattr(self.timer_, 'text', "over time")
            XI = 0

        if int(self.XI) == 15:
            setattr(jeux_embdad, self.rune, 'non')
            self.result_in(0, 'non')

            self.XI = '0'

    def home(self, instant, touch):
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):

            self.event.cancel()
            setattr(jeux_embdad, self.rune, 'non')
            setattr(jeux_embdad, self.XI, '0')
            sm.switch_to(WelcomeScreen())
            '''self.sound_sws = SoundLoader.load('sws.wav')
            if self.sound_sws:
                self.sound_sws.play()'''

    def result_in(self, n, l):
        ads.destroy_banner()
        """self.sound_time = SoundLoader.load('time.wav')
        if self.sound_time:
            self.sound_time.stop()"""
        self.ruselta = True
        self.event.cancel()
        setattr(jeux_embdad, self.rune, 'non')
        setattr(jeux_embdad, self.XI, '0')

        if self.img_embdad == str(l):
            self.result_tru(0)
            # print('yess')
        else:
            self.result_false(0)
            # print("noooo")

    def result_tru(self, instant):
        self.sound23 = SoundLoader.load('yes.wav')
        if self.sound23:
            self.sound23.play()
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()


        n = self.data_[0][0]
        nqst =  self.data_qst[0][0]

        self.cur_h.execute(''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(n) + 3, int(n)))
        self.conn_h.commit()
        ## qst
        self.cur_qst.execute(''' UPDATE point_qst  SET nombre_pointqst = %s  WHERE nombre_pointqst = %s;''' % (int(nqst) + 3, int(nqst)))
        self.conn_qst.commit()



        welcomePage = FloatLayout()
        image2 = "yes.png"
        img = Image(source=str(image2), size_hint=(1., 1.), pos_hint={'x': 0., 'y': 0.},
                    allow_stretch=True, keep_ratio=False)
        btn = Button(text=get_display(ar.reshape(u'مواصلة اللعب')), font_name = 'hemidi', size_hint=(0.70, 0.1), pos_hint={"x": 0.150, "top": 0.18})
        btn.bind(on_press=self.vers_)
        btn.bind(on_press=lambda  x : self.sound23.stop())
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        #content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title = get_display(ar.reshape(u'احسنت لقد كسبت 3 نقاط')) , title_font = 'hemidi')

        self.popup.open()







    def vers_(self, instant):
        #self.p1.dismiss()
        self.popup.dismiss()


        self.problem_continu_ok += 1

        if self.problem_continu_ok == 1:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = BASE_DIR.replace("\\", "/") + '/data.db'
            with sqlite3.connect(db_path) as db:
                self.file_h = (db_path)
                self.conn_h = sqlite3.connect(self.file_h)
                self.cur_h = self.conn_h.cursor()
                sql_h = ''' SELECT nombre_point FROM point'''
                self.cur_h.execute(sql_h)
                self.data_ = self.cur_h.fetchall()
                # qst
                self.file_qst = (db_path)
                self.conn_qst = sqlite3.connect(self.file_qst)
                self.cur_qst = self.conn_qst.cursor()
                sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
                self.cur_qst.execute(sql_qst)
                self.data_qst = self.cur_qst.fetchall()

            if int(self.data_qst[0][0]) < 15:
                sm.switch_to(jeux_embdad("flag", 'yes'))
            elif int(self.data_qst[0][0]) < 30:
                sm.switch_to(jeux_embdad("embadad", 'yes'))
            elif int(self.data_qst[0][0]) < 45:
                sm.switch_to(jeux_embdad("map", 'yes'))
            elif int(self.data_qst[0][0]) < 60:
                sm.switch_to(jeux_embdad("pop", 'yes'))
            elif int(self.data_qst[0][0]) < 75:
                sm.switch_to(jeux_embdad("GBD", 'yes'))
            elif int(self.data_qst[0][0]) >=  75:
                sm.switch_to(jeux_embdad("MD", 'yes'))

    def result_false(self, instant):
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        n = self.data_[0][0]
        nqst = self.data_qst[0][0]
        if int(n) < 3:
            m = n
        else:
            m = n
        if int(nqst) < 3:
            mqst = 0
        else:
            mqst = nqst - 3

        self.cur_h.execute(''' UPDATE point  SET nombre_point = %s  WHERE nombre_point = %s;''' % (int(m), int(n)))
        self.conn_h.commit()
        #qst
        self.cur_qst.execute(''' UPDATE point_qst  SET nombre_pointqst = %s  WHERE nombre_pointqst = %s;''' % (int(mqst), int(nqst)))
        self.conn_qst.commit()

        #runTouchApp(self.popup23.open())
        welcomePage = FloatLayout()
        image2 = "non.png"
        img = Image(source=str(image2), size_hint=(1., 1.), pos_hint={'x': 0., 'y': 0.},
                    allow_stretch=True, keep_ratio=False)
        btn1 = Button(text=get_display(ar.reshape(u'خروج')), font_name='hemidi', size_hint=(0.440, 0.1),
                      pos_hint={"x": 0.05, "top": 0.18})
        btn = Button(text=get_display(ar.reshape(u'محاولة اخرى')), font_name='hemidi', size_hint=(0.440, 0.1),
                     pos_hint={"x": 0.51, "top": 0.18})
        welcomePage.add_widget(img)
        welcomePage.add_widget(btn)
        welcomePage.add_widget(btn1)

        # content = Button(text='Close me!')
        self.popup = Popup(content=welcomePage, auto_dismiss=False, title=get_display(ar.reshape(u'خسرت 3 نقاط')),
                           title_font='hemidi')

        # bind the on_press event of the button to the dismiss function
        btn.bind(on_press=self.continu_)
        btn.bind(on_press=lambda  x : self.sound_error.stop())
        btn1.bind(on_press=self.quit)
        btn1.bind(on_press= lambda x: self.sound_error.stop())

        # open the popup
        self.popup.open()


    def quit(self, instant):
        # if result false and shose quite
        self.popup.dismiss()
        #self.sound_error.stop()
        setattr(jeux_embdad, self.rune, 'non')


        sm.switch_to(WelcomeScreen())

        #self.popup23.dismiss()
        #self.remove_widget(CustomPopup())

    def continu_(self, instant):
        # if result false and shose continu
        self.popup.dismiss()

        #self.sound_error.stop()
        setattr(jeux_embdad, self.rune, 'non')

        self.problem_continu_ok += 1
        if self.problem_continu_ok == 1:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = BASE_DIR.replace("\\", "/") + '/data.db'
            with sqlite3.connect(db_path) as db:


                # qst
                self.file_qst = (db_path)
                self.conn_qst = sqlite3.connect(self.file_qst)
                self.cur_qst = self.conn_qst.cursor()
                sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
                self.cur_qst.execute(sql_qst)
                self.data_qst = self.cur_qst.fetchall()


            if int(self.data_qst[0][0]) < 15:
                sm.switch_to(jeux_embdad("flag", 'yes'))
            elif int(self.data_qst[0][0]) < 30:
                sm.switch_to(jeux_embdad("embadad", 'yes'))
            elif int(self.data_qst[0][0]) < 45:
                sm.switch_to(jeux_embdad("map", 'yes'))
            elif int(self.data_qst[0][0]) < 60:
                sm.switch_to(jeux_embdad("pop", 'yes'))
            elif int(self.data_qst[0][0]) < 75:
                sm.switch_to(jeux_embdad("GBD", 'yes'))
            elif int(self.data_qst[0][0]) >= 75:
                sm.switch_to(jeux_embdad("MD", 'yes'))
        #self.remove_widget(CustomPopup())


    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            if self.ruselta == True:
                self.event.cancel()
                ads.destroy_banner()
                setattr(jeux_embdad, self.rune, 'non')
                setattr(jeux_embdad, self.XI, '0')
                self.XI = '0'
                sm.switch_to(jeux_intro())
                try:
                    self.popup.dismiss()
                except :
                    pass
                try:
                    self.popup.dismiss()
                except:
                    pass


                return True
            else:

                self.event.cancel()
                ads.destroy_banner()
                setattr(jeux_embdad, self.rune, 'non')
                setattr(jeux_embdad, self.XI, '0')
                self.XI = '0'

                sm.switch_to(jeux_intro())


                return True


class jeux_intro(Screen):
    code = ListProperty()

    def __init__(self, **kwargs):  # constructor method
        super(jeux_intro, self).__init__(**kwargs)  # init parent
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6

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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 75:
            self.nv = 6

        image1 = 'flag_frm.png'
        image2 = 'embadad_frm.png'
        image3 = 'map_frm.png'
        image4 = 'pop_frm.png'
        image5 = 'SR_frm.png'
        image6 = 'GBD_frm.png'
        image1_p = 'd_0_0_0_0_0.png'
        image2_p = 'd_0_0_0_0_0.png'
        image3_p = 'd_0_0_0_0_0.png'
        image4_p = 'd_0_0_0_0_0.png'
        image5_p = 'd_0_0_0_0_0.png'
        image6_p = 'd_0_0_0_0_0.png'

        if self.nv > 1:
            image1 = 'flag_ovr.png'
        if self.nv > 2:
            image2 = 'embadad_ovr.png'
        if self.nv > 3:
            image3 = 'map_ovr.png'
        if self.nv > 4:
            image4 = 'pop_ovr.png'
        if self.nv > 5:
            image5 = 'SR_ovr.png'
        if int(self.data_qst[0][0]) >= 90:
            image6 = 'GBD_ovr.png'

        if self.nv == 1:
            image1_p = self.calc(0, self.data_qst[0][0])

        if self.nv == 2:
            image1_p = 'd_1_1_1_1_1.png'
            image2_p = self.calc(0, self.data_qst[0][0] - 15)
        if self.nv == 3:
            image1_p = 'd_1_1_1_1_1.png'
            image2_p = 'd_1_1_1_1_1.png'
            image3_p = self.calc(0, self.data_qst[0][0] - 30)
        if self.nv == 4:
            image1_p = 'd_1_1_1_1_1.png'
            image2_p = 'd_1_1_1_1_1.png'
            image3_p = 'd_1_1_1_1_1.png'
            image4_p = self.calc(0, self.data_qst[0][0] - 45)
        if self.nv  == 5 :
            image1_p = 'd_1_1_1_1_1.png'
            image2_p = 'd_1_1_1_1_1.png'
            image3_p = 'd_1_1_1_1_1.png'
            image4_p = 'd_1_1_1_1_1.png'
            image5_p = self.calc(0, self.data_qst[0][0] - 60)
        if self.nv == 6:
            image1_p = 'd_1_1_1_1_1.png'
            image2_p = 'd_1_1_1_1_1.png'
            image3_p = 'd_1_1_1_1_1.png'
            image4_p = 'd_1_1_1_1_1.png'
            image5_p = 'd_1_1_1_1_1.png'
            if self.data_[0][0] < 90:
                image6_p = self.calc(0, self.data_qst[0][0] - 75)
            else:

                image6_p = self.calc(0, 15)

        post_image = Image(source='post_image.jpg', size_hint=(0.9, 0.26), pos_hint={'x': 0.05, 'y': 0.61},
                           allow_stretch=True, keep_ratio=False)
        img1 = Image(source=str(image1), size_hint=(0.3, 0.200), pos_hint={'x': 0.15, 'y': 0.65},
                     allow_stretch=True, keep_ratio=False)
        img2 = Image(source=str(image2), size_hint=(0.3, 0.200), pos_hint={'x': 0.55, 'y': 0.65},
                     allow_stretch=True, keep_ratio=False)
        img3 = Image(source=str(image3), size_hint=(0.3, 0.200), pos_hint={'x': 0.15, 'y': 0.37},
                     allow_stretch=True, keep_ratio=False)
        img4 = Image(source=str(image4), size_hint=(0.3, 0.200), pos_hint={'x': 0.55, 'y': 0.37},
                     allow_stretch=True, keep_ratio=False)
        img5 = Image(source=str(image5), size_hint=(0.3, 0.200), pos_hint={'x': 0.15, 'y': 0.10},
                     allow_stretch=True, keep_ratio=False)
        img6 = Image(source=str(image6), size_hint=(0.3, 0.200), pos_hint={'x': 0.55, 'y': 0.10},
                     allow_stretch=True, keep_ratio=False)

        img1_p = Image(source=str(image1_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.15, 'y': 0.59},
                       allow_stretch=True, keep_ratio=False)
        img2_p = Image(source=str(image2_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.55, 'y': 0.59},
                       allow_stretch=True, keep_ratio=False)
        img3_p = Image(source=str(image3_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.15, 'y': 0.31},
                       allow_stretch=True, keep_ratio=False)
        img4_p = Image(source=str(image4_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.55, 'y': 0.31},
                       allow_stretch=True, keep_ratio=False)
        img5_p = Image(source=str(image5_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.15, 'y': 0.04},
                       allow_stretch=True, keep_ratio=False)
        img6_p = Image(source=str(image6_p), size_hint=(0.3, 0.050), pos_hint={'x': 0.55, 'y': 0.04},
                       allow_stretch=True, keep_ratio=False)

        welcomePage.add_widget(img1)
        welcomePage.add_widget(img2)
        welcomePage.add_widget(img3)
        welcomePage.add_widget(img4)
        welcomePage.add_widget(img5)
        welcomePage.add_widget(img6)
        welcomePage.add_widget(img1_p)
        welcomePage.add_widget(img2_p)
        welcomePage.add_widget(img3_p)
        welcomePage.add_widget(img4_p)
        welcomePage.add_widget(img5_p)
        welcomePage.add_widget(img6_p)
        welcomePage.add_widget(bar)
        #welcomePage.add_widget(post_image)

        if self.nv == 1:
            img1.bind(on_touch_down=self.top_)

        if self.nv == 2:
            img2.bind(on_touch_down=self.top_)
        if self.nv == 3:
            img3.bind(on_touch_down=self.top_)
        if self.nv == 4:
            img4.bind(on_touch_down=self.top_)
        if self.nv == 5:
            img5.bind(on_touch_down=self.top_)
        if self.nv == 6:
            img6.bind(on_touch_down=self.top_)
        self.add_widget(welcomePage)

    def calc(self, inst, val):
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
        rs = 'd_' + stre + '.png'
        return rs

    def top_(self, instant, touch):
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()
        # print(self.data_[1][0])
        # print(self.data_[0][0])
        ##############################

        # sm.add_widget(jeux_embdad('flag','yes'))

        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.65 and touch.pos[1] <= Window.height * 0.85):
            if int(self.data_qst[0][0]) < 15:
                sm.switch_to(jeux_embdad("flag", 'yes'))


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.65 and touch.pos[1] <= Window.height * 0.85):

            if int(self.data_qst[0][0]) < 30 and int(self.data_qst[0][0]) >= 15:

                sm.switch_to(jeux_embdad("embadad", 'yes'))


        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.37 and touch.pos[1] <= Window.height * 0.57):
            if int(self.data_qst[0][0]) < 45 and int(self.data_qst[0][0]) >= 30:
                sm.switch_to(jeux_embdad("map", 'yes'))


        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.37 and touch.pos[1] <= Window.height * 0.57):
            if int(self.data_qst[0][0]) < 60 and int(self.data_qst[0][0]) >= 45:
                sm.switch_to(jeux_embdad("pop", 'yes'))

        if (touch.pos[0] >= Window.width * 0.15 and touch.pos[0] <= Window.width * 0.45) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_qst[0][0]) < 75 and int(self.data_qst[0][0]) >= 60:
                sm.switch_to(jeux_embdad("GBD", 'yes'))  # التصنيف

        if (touch.pos[0] >= Window.width * 0.55 and touch.pos[0] <= Window.width * 0.85) and (
                touch.pos[1] >= Window.height * 0.10 and touch.pos[1] <= Window.height * 0.30):
            if int(self.data_qst[0][0]) >= 75:
                sm.switch_to(jeux_embdad("MD", 'yes')) # المساحة


    def home(self, instant, touch):
        if (touch.pos[0] >= Window.width * 0.10 and touch.pos[0] <= Window.width * 0.18) and (
                touch.pos[1] >= Window.height * 0.89 and touch.pos[1] <= Window.height * 0.97):
            ads.destroy_interstitial()
            sm.switch_to(WelcomeScreen())


    def hook_keyboard(self, window, key, *largs):
        # self.name

        # print(key)

        if key == 27:
            # print(sm.next())
            # print(sm.previous())
            # EventLoop.window.bind(on_keyboard=self.hook_keyboard)
            ads.destroy_interstitial()
            sm.switch_to(WelcomeScreen())

            return True


class info_contry(Screen):
    # code = StringProperty('')
    code = ListProperty()

    def __init__(self, acc, **kwargs):  # constructor method
        super(info_contry, self).__init__(**kwargs)  # init parent
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
            # qst
            self.file_qst = (db_path)
            self.conn_qst = sqlite3.connect(self.file_qst)
            self.cur_qst = self.conn_qst.cursor()
            sql_qst = ''' SELECT nombre_pointqst FROM point_qst'''
            self.cur_qst.execute(sql_qst)
            self.data_qst = self.cur_qst.fetchall()

        if int(self.data_qst[0][0]) < 15:
            self.nv = 1
        elif int(self.data_qst[0][0]) < 30:
            self.nv = 2
        elif int(self.data_qst[0][0]) < 45:
            self.nv = 3
        elif int(self.data_qst[0][0]) < 60:
            self.nv = 4
        elif int(self.data_qst[0][0]) < 75:
            self.nv = 5
        elif int(self.data_qst[0][0]) >= 90:
            self.nv = 6
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
            self.cr(0, acc)

        # list = [val1 , val2]
        # print(acc)

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

    def cr(self, i, acc):
        #acc  = 'cuba'

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = BASE_DIR.replace("\\", "/") + '/data.db'
        with sqlite3.connect(db_path) as db:
            file = (db_path)
            conn = sqlite3.connect(file)
            cur = conn.cursor()
            sql = ''' SELECT * FROM table_1 '''
            cur.execute(sql)
            data = cur.fetchall()


        v_contry1 = []

        for i in data:
            if acc == i[28]:
                for e in i:
                    v_contry1.append(e)
        v_contry1.remove(acc)
        self.func = FloatLayout()

        self.layout = GridLayout(cols=2, spacing=10, size_hint_y=None, pos_hint={"centre_x": 0.02})
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        # https://googledrive.com/host/<folderID>/<filename>
        # https://drive.google.com/uc?id=FILE_ID
        image1 = 'https://drive.google.com/uc?id=1Wo_j02PZP53uXoIVsw_5jXlkF0QWsnOh'  # flag.png'
        image1 = AsyncImage(source=image1)
        # print(acc) # nome contry  acc
        image_flag1 = 'flag/' + acc + '.png'
        image_embdad1 = 'embadad/' + acc + '.png'
        image_map1 = 'map/' + acc + '.png'
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
        label_flag = Label(text="[b][color=#070B19]%s[/color][/b]" % (tx), font_name='hemidi', size_hint=(0.3, 0.05),
                           pos_hint={"x": 0.70 / 2, "top": 0.87}, markup=True)
        img_flag = Image(source=image_flag1, size_hint=(0.90, 0.15), pos_hint={'x': 0.10 / 2, 'y': 0.67},
                         allow_stretch=True, keep_ratio=False)
        label_embdad = Label(text="[b][color=#070B19]%s[/color][/b]" % (tx2), font_name='hemidi', size_hint=(0.3, 0.05),
                             pos_hint={"x": 0.1, "top": 0.66}, markup=True)
        img_embdad = Image(source=image_embdad1, size_hint=(0.88 / 2, 0.15), pos_hint={'x': 0.10 / 2, 'y': 0.46},
                           allow_stretch=True, keep_ratio=False)
        label_map = Label(text="[b][color=#070B19]%s[/color][/b]" % (tx3), font_name='hemidi', size_hint=(0.3, 0.05),
                          pos_hint={"x": 0.6, "top": 0.66}, markup=True)
        img_map = Image(source=image_map1, size_hint=(0.88 / 2, 0.15), pos_hint={'x': (0.88 / 2) + 0.06, 'y': 0.46},
                        allow_stretch=True, keep_ratio=False)

        self.func.add_widget(img_flag)
        self.func.add_widget(label_flag)
        self.func.add_widget(label_embdad)
        self.func.add_widget(img_embdad)
        self.func.add_widget(label_map)
        self.func.add_widget(img_map)

        self.func.add_widget(self.bar)

        # print(len(data[1]))
        # print(len(status1))
        #"{:,}".format(int(v_contry1[i])))
        for i in range(len(data[1])-1):
            reshaped_text = ar.reshape((status1[i]))
            self.btn = Button(text='hello', font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None}, height=60)
            # print(v_contry1[i])

            self.btn1 = Button(text=get_display(reshaped_text), font_name='hemidi', size_hint_y=None,
                               size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None}, height=60)

            # self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn)
            self.layout.add_widget(self.btn1)

            reshaped_text = (status1[i])
            self.bidi_text = get_display(reshaped_text)

            setattr(self.btn, 'text', str("{:,}".format(int(v_contry1[i]))))
            # setattr(self.btn1, 'text', self.bidi_text)
        for i in range(5):
            reshaped_text = get_display(ar.reshape(u'غير متوفر'))
            self.btn10 = Button(text=reshaped_text, font_name='hemidi', size_hint_y=None, size_hint_x=0.3185185185,
                              pos_hint={'x': 0.3, 'top': None}, height=60)
            # print(v_contry1[i])

            self.btn12 = Button(text=reshaped_text, font_name='hemidi', size_hint_y=None,
                               size_hint_x=0.3185185185,
                               pos_hint={'x': 0.3, 'top': None}, height=60)

            # self.btn.text = str(v_contry1[i])

            self.layout.add_widget(self.btn10)
            self.layout.add_widget(self.btn12)

        self.root = ScrollView(size_hint=(0.90, None), size=(Window.width, Window.height),
                               pos_hint={"x": 0.05, "top": 0.45})  # , size=(Window.width, Window.height)
        self.root.add_widget(self.layout)
        self.func.add_widget(self.root)
        self.add_widget(self.func)
        # self.add_widget(img)

    def update(self, instant):
        self.btn.text = 'hemidi'

    def press(self, instant):
        # print(self.contry_vs)

        pass

    def home(self, instant, touch):

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
            # Window.close()
            sm.switch_to(WelcomeScreen())
            # sm.current_screen

            return True


if __name__ == '__main__':
    try:
        import arabic_reshaper as ar
    except:
        BASE_DIR = '/data/user/0/rogassa.kivyy.myapp/files/app/_python_bundle/site-packages/arabic_reshaper/__version__.py'
        f = open(BASE_DIR, 'w')
        f.write("__version__ = '2.0.15'")
        f.close()
        import arabic_reshaper as ar
    app = PanelBuilderApp()
    #PanelBuilderApp().run()
    app.run()
