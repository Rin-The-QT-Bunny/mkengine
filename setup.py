from setuptools import setup, find_packages

setup(
    name="mkengine",
    version="1.0",
    author="Yiqi Sun (Zongjing Li)",
    author_email="ysun697@gatech.edu",
    description="Melkor of Iron Crown, the personal package for machine learning and more",

    # project main page
    url="http://jiayuanm.com/", 

    # the package that are prerequisites
    packages=find_packages(),
    package_data={
        '':['mkengine'],
        'bandwidth_reporter':['mkengine']
               },
)