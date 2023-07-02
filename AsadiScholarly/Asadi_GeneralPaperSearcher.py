# System libs
import traceback
import timeit
import random
#####################################################################
# Third party libs# from builtins import None

import PyPaperBot.__main__ as pbot

#################################################################
import Asadi_PaperListHardCode
#################################################################
WARNING_LIST = []
KeywordIndex_HighLevel = 0
KeywordCount_HighLevel = 0
Level_1_Progress = 0.0
Level_2_Progress = 0.0
Level_3_Progress = 0.0
TOTAL_FOUNDED_PAPERS = 0
previouslyDownloaded_total = 0
GeneralPaperSearcher_VERBOSE_MODE = False
#################################################################
wb = None
sheet = None
fname = None
lastRow = 0



#########################################################################
def save_excel():
	global wb
	wb.save(str(fname)) 


#########################################################################
def temporal_save(i):
	global wb
	wb.save(str(fname) + "_temp" + str(i) + ".xls") 		


####################################################################
def print_warnings():
	i = 0
	for warning in WARNING_LIST:
		search_term = warning [0]
		searching_location = warning [1]
		start_date = warning [2]
		end_date = warning [3]
		print("WARNINGS[%s] due to len(search_term)=%s" % (i, len(search_term)))		
		print("search_term ", search_term)		
		print("-"*20)
		i += 1

#########################################################################

#################################################################
def download_single_paperUsingPaperBot(paperTitle,paper_year,proxy,dwn_dir):
	MIN_TITLE_LENGTH = 10 #dige vaghean az 10 kamtar 100% nist
	if(paperTitle == None or paperTitle == "None" or\
	 paperTitle == "" or (len(paperTitle) < MIN_TITLE_LENGTH)):
		if(GeneralPaperSearcher_VERBOSE_MODE):
			print("GeneralPaperSearcher_VERBOSE_MODE ")
		print("\n\n Nothing will have been downloaded:: Incorrect Paper Title ",paperTitle)
		return 0
	paperTitle = paperTitle.strip(".")
	paperTitle = paperTitle.strip()
	paperTitle = paperTitle.strip("\n")
	scholar_results= 1 #save the first results, only not 10 results by default
	start_page = 1
	end_page = 1
	scholar_pages= range(start_page, end_page + 1) #just first page of google scholar search		
	min_year= paper_year #note
	max_dwn= None
	max_dwn_type= None
	journal_filter= None
	restrict= 1 #0:Download only Bibtex - 1:Down load only papers PDF
	DOIs= None
	scihub_mirror= None
	pbot.start(paperTitle,scholar_results, scholar_pages, dwn_dir, proxy, min_date=None, num_limit=None, num_limit_type=None, filter_jurnal_file=None, restrict=None, DOIs=None, SciHub_URL=None)
#################################################################3


###########################################################3			
def DownloadAllPapers(List_of_PaperTitles,List_of_years,dwn_dir= "./ToDownloadPapers/"):

	global Level_1_Estimate
	global Level_2_Estimate
	global Level_3_Estimate
	global KeywordCount_HighLevel	
	global KeywordIndex_HighLevel
	global previouslyDownloaded_total
	start_time = timeit.default_timer()
	proxy = None	
	i = 0
	ConnectionError_SSLError_count = 0
	for papertitle in List_of_PaperTitles:
		paper_year = List_of_years[i]
		try:
			print("\n")
			print("~"*50)
			Level_2_Progress = Level_1_Progress * (i + 1) / len(List_of_PaperTitles)
			if(GeneralPaperSearcher_VERBOSE_MODE):
				print("GeneralPaperSearcher_VERBOSE_MODE ")
			print("\n DownloadPapers_AccordingToExcelList:start to download paper "+ str(i+1) + " out of " + str(len(List_of_PaperTitles)))
			print("papertitle = ",papertitle)
			print("paper_year = ",paper_year)
			print("DownloadPapers_AccordingToExcelList Level_1_Progress = %s , **level2=%s , level3=%s " % (Level_1_Progress, Level_2_Progress, Level_3_Progress))
			print("DownloadPapers_AccordingToExcelList previouslyDownloaded_total = ",previouslyDownloaded_total)
			print("\n")			
			# .....
			Level_1_Estimate = 0
			Level_2_Estimate = 0
			Level_3_Estimate = 0
			try:						
				previouslyDownloaded = download_single_paperUsingPaperBot(papertitle,paper_year,proxy,dwn_dir)
				previouslyDownloaded_total +=previouslyDownloaded
			except Exception as Cexptin:
				ConnectionError_SSLError_count +=1
				print("\n\n\n")
				if(GeneralPaperSearcher_VERBOSE_MODE):
					print("GeneralPaperSearcher_VERBOSE_MODE ")
				print("DownloadPapers_AccordingToExcelList-->ConnectionError_SSLError!!!!!!!!??????????",Cexptin)
				#Asadi_SoundUtility.play_Error_sound()
				traceback.print_tb(Cexptin.__traceback__)
				print("\n\n\n")
				if(ConnectionError_SSLError_count == 1):
					continue
				else:
					break
			current_time = timeit.default_timer()
			Elapsed_time_from_start = (current_time - start_time)/60
			if(GeneralPaperSearcher_VERBOSE_MODE):
				print("GeneralPaperSearcher_VERBOSE_MODE ")
			print("DownloadPapers_AccordingToExcelList Elapsed_time download_single_paperUsingPaperBot(minute) =%s, === %s hours " % (Elapsed_time_from_start, Elapsed_time_from_start / 60))		
			try:
				Level_1_Estimate = Elapsed_time_from_start / Level_1_Progress - Elapsed_time_from_start
				Level_2_Estimate = Elapsed_time_from_start / Level_2_Progress - Elapsed_time_from_start
				Level_3_Estimate = Elapsed_time_from_start / Level_3_Progress - Elapsed_time_from_start
			except Exception:
				pass
			print("\nDownloadPapers Estimated Remained Time to finish(minutes) based on Level_1_Progress = %s , **level2=%s , level3=%s " % (Level_1_Estimate, Level_2_Estimate, Level_3_Estimate))			
			print("\nDownloadPapers Estimated Remained Time to finish(hours) based on Level_1_Progress = %s , **level2=%s , level3=%s " % (Level_1_Estimate/60, Level_2_Estimate/60, Level_3_Estimate/60))
			print("~"*50)
		except Exception as exptin:
			print("\n\n\n")
			if(GeneralPaperSearcher_VERBOSE_MODE):
				print("GeneralPaperSearcher_VERBOSE_MODE ")
			print("DownloadPapers_AccordingToExcelList-->??????????",exptin)
			print("papertitle = ",papertitle)
			print("paper_year = ",paper_year)
			traceback.print_tb(exptin.__traceback__)
			print("\n\n\n")
		i+=1
	if (ConnectionError_SSLError_count > 1):
		if(GeneralPaperSearcher_VERBOSE_MODE):
				print("GeneralPaperSearcher_VERBOSE_MODE ")		
		raise Exception("GeneralPaperSearcher_VERBOSE_MODE ConnectionError_SSLError_count = "+str(ConnectionError_SSLError_count))

#.......................................................................................
#########################################################################
def DownloadPapers_AccordingToHardCodedlList(dwn_dir= "./ToDownloadPapers/"):
	
	List_of_PaperTitles,List_of_years = Asadi_PaperListHardCode.Get_list_of_Papers_FromHarcodedList()
	DownloadAllPapers(List_of_PaperTitles,List_of_years,dwn_dir)
	
##########################################################################

##########################################################################
def my_rotate_function(lis, n):
	return lis[n:] + lis[:n]
##################################################################
################################################################
def test_SSL():
	try:
		test1_SSL()
	except Exception as exptin:
		print("\n\n\n")
		print("exptin ", exptin)
		traceback.print_tb(exptin.__traceback__)
		print("\n\n\n")
	try:
		test2_SSL()
	except Exception as exptin:
		print("\n\n\n")
		print("exptin ", exptin)
		traceback.print_tb(exptin.__traceback__)
		print("\n\n\n")
def test1_SSL():
	from urllib.request import urlopen
	print("\n\n test 1")
	content = urlopen('https://www.howsmyssl.com/a/check').read()
	print("content ",content)
def test2_SSL():
	import ssl
	from urllib.request import urlopen
	print("\n\n test 2")
	content = urlopen('https://www.howsmyssl.com/a/check', context=ssl._create_unverified_context()).read()
	print("content ",content)
#################################################################
if __name__ == '__main__':
	start_time = timeit.default_timer()
	#test_SSL()
	current_time = timeit.default_timer()
	Elapsed_time_from_start = current_time - start_time 
	print("main function finished, \nElapsed_time_from_start(second) =%s, === %s minute " % (Elapsed_time_from_start, Elapsed_time_from_start / 60))
	
