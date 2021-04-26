echo "project name:"
read prjname
mkdir $prjname
cd src
cp RPG.py -t ../$prjname
cd ..
cd $prjname
touch $prjname.py
echo "import RPG as r" > $prjname.py
touch $prjname.sf
echo "this is a test StoryFile" > $prjname.sf
