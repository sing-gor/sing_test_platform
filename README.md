## 项目配置

|名称| 介绍  |版本|
|-----|-----|-----|
|Database|     | postgresql |
|python|     |3.8|
|django|     | 3.2.5      |

## 项目初始化

```bash
# 0. 创建虚拟环境

conda create -n <python_env> python=3.8

# 1. 激活虚拟环境
conda activate <python_env>

# 2. 安装必要依赖
pip install -r requirements.txt

# 3. 配置私有配置文件， 如下 所示
nvim ~/<project_path>/customer_service/privta_config.py

# 4. 生成 数据库迁移文件
python manage.py makemigrations

# 5. 数据库迁移
python manage.py migrate

# 6. 创建一个 管理员

python manage.py createsuperuser
```

### 私有文件

```python


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # 本地开发可以切到 mysql
        'NAME': 'xxxxxxxxx',
        'USER': 'xxxxxxx',
        'PASSWORD': 'xxxxxxx',
        'HOST': '192.168.31.10',
        'PORT': '5432',
    }
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxxxxxxxxxxxxx'



```

## 运行项目

```bash
# 0. 激活虚拟环境
conda activate <python_env>

# 1. 启动项目
python manage.py runserver 0.0.0.0:9000

```

## 项目部署相关

### 代码发生变更

```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn_tendcode.service
```

### nginx配置发生变更

```bash
sudo nginx -t
sudo systemctl restart nginx
```