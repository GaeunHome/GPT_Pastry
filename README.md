# 糕點訂購網站

[![Python](https://img.shields.io/badge/Python-3-3776AB)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-092E20)](https://www.djangoproject.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991)](https://openai.com/)

## 專案目的

本專案的主要目的是利用 **gpt-3.5-turbo** (未使用 **gpt-3.5-turbo-16k**) 自行生成一個完整的電商購物網站系統。這個系統將展示如何利用 GPT-3.5 模型自動生成可運行的網站框架與功能，並以糕點訂購為主題，讓顧客可以在線選擇與訂購糕點。

## 專案目標

利用 **gpt-3.5-turbo** 根據提供的 Prompt，自動生成可運行的電商購物網站，包含基礎的購物車、商品展示、登入/註冊功能等。最終目的是展示如何利用現代人工智能技術進行快速的網站開發。

## 預期功能

1. **商品展示**：顯示所有可選擇的糕點商品。
2. **購物車功能**：用戶可以將商品加入購物車並進行結帳。
3. **會員系統**：用戶可以註冊帳戶、登入和管理個人資料。
4. **訂單管理**：用戶可以查看過去的訂單並追蹤其狀態。

## 備註

- 該專案中的資料夾內的資料僅供展示使用，並不代表實際的生產資料庫。
- 本專案是展示如何運用 AI 工具來自動化開發過程，並以糕點電商為主題。

## 專案結構

```
GPT_Pastry/
├── Project/
│   ├── manage.py               # Django 管理指令
│   ├── Project/                # Django 專案設定
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── pastry/                 # 糕點 App
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   ├── static/                 # 靜態資源
│   │   └── css/
│   ├── templates/              # 模板
│   └── media/                  # 商品圖片
│       └── images/
├── .gitignore
└── README.md
```

## 快速開始

```bash
cd Project
pip install django
python manage.py migrate
python manage.py runserver
```
