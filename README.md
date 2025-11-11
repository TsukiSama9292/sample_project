# 基礎專案 (Sample Django Project)

這是一個簡單的 Django 範例專案骨架，包含基本的資料庫遷移與本機開發啟動指令。

## 簡介

此專案主要用於快速起始 Django 應用開發。專案目錄結構已包含一個 Django 專案（位於 `projectdev/`）。

## 前置需求

- Python 3.8+（請依專案 `pyproject.toml` 或您的環境需求選擇適當版本）
- 建議使用 uv 來管理虛擬環境

## 快速開始（建議）

1. 進入專案根目錄：

```bash
git clone 
cd sample_project

```

2. 建立虛擬環境並安裝相依套件

```bash
uv sync
```

## 常用 Django 指令

專案的 Django 管理指令位於 `projectdev/manage.py`（根目錄下的 `projectdev/` 已包含 `manage.py` 與設定）。

若您在工作流程中使用名為 `uv` 的終端別名或工具（workspace 中的 terminal 顯示有 `uv`），可以用類似下列方式執行管理指令：

```bash
cd projectdev
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py runserver
```

說明：
- `makemigrations`：建立模型變更的遷移檔
- `migrate`：套用遷移到資料庫（預設 SQLite：`projectdev/db.sqlite3`）
- `runserver`：啟動開發伺服器（預設 http://127.0.0.1:8000/）

## 建立應用

```bash
uv run manage.py startapp 應用名稱
```

例如:

```
uv run manage.py startapp ai
```

在 `projectdev/projectdev/settings.py` 中加入：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ai',  # 👈 新增 app 名稱
]
```

建立 `projectdev/ai/urls.py`：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

在 `projectdev/projectdev/urls.py` 加入 ai 應用的 urls：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai.urls')),  # 👈 加上這行(這是新專案沒有舊路由所以要用根路由)
    # path('blog/', include('blog.urls')), # 👈 有根路由後，其他應用可以加上這行
]
```

## 建立網頁

1. 伺服器設定檔案(`projectdev/projectdev/settings.py`) 的 `APP_DIRS=True`會讓專案具備更高的隔離性
2. 因為每個應用都有隔離性，所以網頁要寫在 `{專案名}/{應用名}/templates/{應用名}/index.html`
3. 網頁需要被渲染，所以要修改應用的路由(`projectdev/ai/views.py`)：
    
    ```python
    from django.shortcuts import render

    def index(request):
        context = {'title': '這是網頁標題', 'message': '這是網頁內容'}
        return render(request, 'ai/index.html', context)
    ```

## 資料庫

- 此專案包含本機 SQLite 檔案 `projectdev/db.sqlite3`。
- 若要使用其他資料庫（Postgres、MySQL 等），請修改 `projectdev/projectdev/settings.py` 中的 DATABASES 設定並安裝相應驅動。

## 環境變數

- 若您在 `settings.py` 中使用環境變數（例如 SECRET_KEY、DEBUG、DATABASE_URL），請在本機建立 `.env` 或透過系統環境變數提供。

## 測試

如果專案包含測試，可使用以下指令執行（在 `projectdev` 目錄）：

```bash
python manage.py test
```

## 常見問題

- 如果遷移失敗，先檢查模型是否有語法錯誤，或是否有尚未安裝的相依套件。
- 若埠號 8000 已被佔用，可透過 `python manage.py runserver 0.0.0.0:8001` 指定其他埠號。

## 授權

本專案使用 Apache 2.0 開源協議