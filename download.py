from pytube import YouTube
url=input("Enter url of the video to download\n")
try:
	yt = YouTube(url)
	needed={'360p':0,'480p':0,'720p':0,'1080p':0}
	#progressive include both video and audio
	for i in yt.streams.filter(file_extension='mp4',progressive=True):
	        k=str(i)[45:str(i).index('fps')-1][1:-1]
	        if k=='360p':
	            needed['360p']=i.itag
	        if k=='480p':
	            needed['480p']=i.itag
	        if k=='720p':
	            needed['720p']=i.itag
	        if k=='1080p':
	            needed['1080p']=i.itag   
	print('Avaliable quality')
	for i in needed:
	    if needed[i]==0:
	        pass
	    else:
	        print(i,'Type',needed[i])
	to_down=int(input())
	stream = yt.streams.get_by_itag(to_down)
	# The file is downloaded to the current directory
	stream.download()
	print('downloaded')
except:
	print('Can't download video)
	print('Try python -m pip install --upgrade pytube')
	
