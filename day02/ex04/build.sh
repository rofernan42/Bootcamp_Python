PKG_DIR=.

mkdir $PKG_DIR/ai42
touch $PKG_DIR/ai42/__init__.py
cp loading.py $PKG_DIR/ai42
cp logger.py $PKG_DIR/ai42

python setup.py sdist bdist_wheel
