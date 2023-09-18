cur_date=$(date +%Y%m%d)
name="mrc0.2.1."$cur_date
echo $name
mkdir release
cp -r basic release/rime/
cp -r schema/. release/rime/
cp -r dict/. release/rime/
cp -r custom/. release/rime/
7zz a $name.zip release
rm -r release