echo "project name:"
read prjname
cd ..
mkdir $prjname
cd $prjname
touch $prjname.py
touch helloworld.sf
cd ..
cd 'Project Start'
cd src
cp RPG.py /home/cris/Desktop/EngineStart/$prjname
cd ..
cd ..
cd $prjname
echo "import RPG as r" > $prjname.py
echo "Hello World StoryFile test" > helloworld.sf
cd ..
