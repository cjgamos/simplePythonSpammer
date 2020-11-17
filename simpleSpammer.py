import pyautogui
import time

print("=" * 20)
msg = ['Lorem','ipsum','dolor','sit','amet,','consectetur','adipiscing','elit,','sed','do','eiusmod','tempor','incididunt','ut','labore','et','dolore','magna','aliqua.','Metus','vulputate','eu','scelerisque','felis.','Tincidunt','arcu','non','sodales','neque','sodales','ut','etiam','sit.','Ut','sem','viverra','aliquet','eget.','Viverra','ipsum','nunc','aliquet','bibendum','enim','facilisis.','Volutpat','odio','facilisis','mauris','sit','amet','massa','vitae.','Leo','in','vitae','turpis','massa.','Pellentesque','habitant','morbi','tristique','senectus','et','netus','et.','Ligula','ullamcorper','malesuada','proin','libero','nunc.','Id','volutpat','lacus','laoreet','non.','Maecenas','ultricies','mi','eget','mauris.','Gravida','cum','sociis','natoque','penatibus','et','magnis','dis.','Sed','ullamcorper','morbi','tincidunt','ornare.','Lectus','urna','duis','convallis','convallis','tellus','id','interdum','velit.','Gravida','dictum','fusce','ut','placerat','orci','nulla','pellentesque','dignissim.','Mauris','pharetra','et','ultrices','neque','ornare','aenean.','Pharetra','sit','amet','aliquam','id','diam','maecenas.','Id','aliquet','lectus','proin','nibh','nisl.','Id','cursus','metus','aliquam','eleifend','mi','in','nulla','posuere.','Aliquet','enim','tortor','at','auctor','urna','nunc','id','cursus','metus.','Pellentesque','sit','amet','porttitor','eget','dolor','morbi','non','arcu','risus.','Facilisi','cras','fermentum','odio','eu','feugiat','pretium','nibh','ipsum.','Ut','aliquam','purus','sit','amet','luctus','venenatis.','Sagittis','orci','a','scelerisque','purus','semper.','Adipiscing','elit','pellentesque','habitant','morbi','tristique','senectus','et','netus','et.','Tempor','orci','dapibus','ultrices','in','iaculis','nunc','sed','augue.','Nibh','venenatis','cras','sed','felis','eget.','Auctor','neque','vitae','tempus','quam','pellentesque','nec','nam','aliquam.','Nisl','purus','in','mollis','nunc','sed.','Lorem','donec','massa','sapien','faucibus','et','molestie','ac','feugiat.','Fames','ac','turpis','egestas','integer','eget','aliquet','nibh','praesent.','Odio','morbi','quis','commodo','odio','aenean','sed','adipiscing','diam.','Sem','nulla','pharetra','diam','sit','amet','nisl.','Venenatis','a','condimentum','vitae','sapien.','Vitae','aliquet','nec','ullamcorper','sit','amet','risus','nullam','eget.','Diam','maecenas','sed','enim','ut','sem.','Mattis','molestie','a','iaculis','at','erat.','Risus','in','hendrerit','gravida','rutrum','quisque.','Ac','auctor','augue','mauris','augue','neque','gravida','in','fermentum.','Nibh','nisl','condimentum','id','venenatis','a','condimentum','vitae','sapien.','Imperdiet','dui','accumsan','sit','amet','nulla','facilisi','morbi','tempus.','Leo','vel','orci','porta','non','pulvinar.','Nibh','nisl','condimentum','id','venenatis','a','condimentum.','Amet','venenatis','urna','cursus','eget','nunc','scelerisque','viverra','mauris','in.','Vel','elit','scelerisque','mauris','pellentesque','pulvinar','pellentesque','habitant.','At','lectus','urna','duis','convallis','convallis','tellus','id.','Molestie','ac','feugiat','sed','lectus','vestibulum','mattis','ullamcorper','velit','sed.','Faucibus','in','ornare','quam','viverra','orci','sagittis','eu','volutpat','odio.','Augue','eget','arcu','dictum','varius','duis.']
n = input("How many time: ")
msgNum = len(msg)
print("=" * 20)


count= 5
while (count != 0):
	print("Countdown " + str(count))
	time.sleep(1)
	count -= 1

print('\n')
print("Ready!")
time.sleep(2)
print("GOGOGOGO!")

for x in range(0, int(n)):
	for y in range(msgNum):
		print("Word #" + str(y) + '\n')
		pyautogui.typewrite(msg[y] + '\n')
		time.sleep(4)