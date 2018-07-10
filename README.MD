## 安装 flask

## 关于 virtualenv
- 1.1 安装

            pip install virtualenv

- 1.2 新建虚拟环境
        
            virtualenv evn

- 1.3 进入虚拟环境

            evn\Scripts\activate

- 1.4 查看模块 pip list
- 1.5 安装模块 pip install flask
- 1.6 关于requirements

            (venv) $ pip freeze >requirements.txt    # 生成
            (venv) $ pip install -r requirements.txt    # 安装

- 1.7 退出 deactivate

## 关于git推送

        echo "# flask_learn" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git remote add origin https://github.com/1988yekai/flask_learn.git
        git push -u origin master

参考url： https://blog.csdn.net/u011054333/article/details/70151857/
