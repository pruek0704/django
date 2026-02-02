import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_todo_list(self):
        # ชัยเปิดหน้าเว็บ
        self.browser.get(self.live_server_url)
        # ชัยเช็คว่าบน title มีคำว่า "To-Do ไหม"
        self.assertIn("To-Do", self.browser.title)
        # ชัยเช็คว่ามีคำว่า "To-Do" บน tag h1 ไหม
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do",header_text)
        # ชัยพิมพ์ "Buy peacock feathers" ลงใน inputbox
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        # ชัยเลือก priority
        select_box = Select(self.browser.find_element(By.ID, "id_priority")) 
        select_box.select_by_visible_text('High')
        # ชัยกด ENTER
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # ชัยเช็คว่ามี "Buy peacock feathers (High)" บน tag body_text
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("Buy peacock feathers (High)", body_text)
        # ชัยพิมพ์ "Use peacock feathers to make a fly" เพิ่มลงไปใน inputbox
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # ชัยเช็คว่ามี "Buy peacock feathers (High)" และ "Use peacock feathers to make a fly (Medium)" บน tag body_text
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("Buy peacock feathers (High)", body_text)
        self.assertIn("Use peacock feathers to make a fly (Medium)", body_text)
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # ชัยเปิดหน้าเว็บ
        self.browser.get(self.live_server_url)
        # ชัยพิมพ์ "Buy peacock feathers" เพิ่มลงใน inputbox 
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # ชัยเช็คว่ามี "Buy peacock feathers (Medium)" บน tag body_text
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("Buy peacock feathers (Medium)", body_text)
        # เช็ค url ว่าอยู่ในรูปแบบ /list/.+ ไหม
        chai_list_url = self.browser.current_url
        self.assertRegex(chai_list_url, "/lists/.+")
        # ลบ cookies อันเก่าเพื่อให้อีกคนที่เข้ามาใหม่ได้เข้า
        self.browser.delete_all_cookies()
        
        # แอนเปิดหน้าเว็บ
        self.browser.get(self.live_server_url)
        # แอนเช็คว่าไม่มี "Buy peacock feathers (Medium)" บน page_text
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers (Medium)", page_text)
        # แอนพิมพ์ "Buy milk" ลงใน inputbox
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        # แอนเช็คว่ามี "Buy milk (Medium)" บน bode_text
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("Buy milk (Medium)", body_text)
        # เช็ค url ว่าอยู่ในรูปแบบ /list/.+ ไหม
        ann_list_url = self.browser.current_url
        self.assertRegex(ann_list_url, "/lists/.+")
        self.assertNotEqual(ann_list_url, chai_list_url)
        
        time.sleep(1)
        # แอนเช็คอีกครั้งว่าไม่มี ข้อความของ ชัย
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)
        