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
pip show virtualenv
pip install virtualenv
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
# 导出依赖列表
pip freeze > requirements.txt
# 卸载全部
pip uninstall -r requirements.txt -y
```

































