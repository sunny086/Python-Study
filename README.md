# Python-Study
Python日常工作 demo测试



## 安装

```markdown
# 查看版本号
python --version
# pip镜像 清华大学 阿里云 豆瓣
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config list
```



## 虚拟环境

```markdown
# 安装
我的mac的命令是pip3
pip show virtualenv
pip install virtualenv
也可以直接执行python3.13 -m venv <venv_name> 直接创建虚拟环境 可以指定python版本
# 新建
virtualenv <venv_name>
# 激活 命令结束会发现命令行提示符前缀发生变更 后面就是pip之类的使用了 以下两个分别是windows和linux环境的激活命令
.\<venv_name>\Scripts\activate
source /<venv_name>/bin/activate
# 退出虚拟环境
deactivate
# 删除
rmdir /s /q <venv_name>
rm -rf xxx
```

虚拟环境新建结束，编译器配置一些项目的python解释器，选择新建的那个虚拟环境就可以切换了



## 包管理方式

```markdown
# demo
package1==1.0.0
package2>=2.1.0
```

```markdown
# 安装全部
pip install -r requirements.txt
# 安装全部并升级 但是好像没有生效
pip install -r requirements.txt --upgrade
# 能会使用缓存的包，而不是从远程仓库获取最新版本。可以尝试使用 --no-cache-dir 选项来禁用缓存
pip install -r requirements.txt --upgrade --no-cache-dir
# 要检查当前安装的库版本以及可用的最新版本
pip list --outdated
# 导出依赖列表
pip freeze > requirements.txt
# 卸载全部
pip uninstall -r requirements.txt -y
```

































